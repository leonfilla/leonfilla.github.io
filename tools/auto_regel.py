#!/usr/bin/env python3
"""Berechnet automatische Status-Vorschläge für die Rezept-Sichtung.

Aufruf:
  python3 tools/auto_regel.py SICHTUNG.json ENTSCHEIDUNGEN_DIR CHATS_DIR CLAUDE_EXPORT.json GEMINI_EXPORT.json KANDIDATEN_CLAUDE.json KANDIDATEN_GEMINI.json

Schreibt in SICHTUNG.json pro Kandidat ein Feld `auto`:
  {status, grund, linie, linie_name, basis, eigen}
  basis = Status, von dem die Regel ausging (eigene Entscheidung, sonst Vorschlag)
  eigen = True, wenn basis eine eigene Entscheidung war (Klick oder geprüfter Chat)

Regel (pro Rezeptlinie = gleiches Gericht/gleiche Bohne UND gleiche Zubereitungsart):
  1 × Aktiv:  eigenes Aktiv/Unfertig (neuestes) > im Chat gelobt > Fassung nach Korrektur
              > Claude vor Gemini > neuestes > Karte/Datei vor Text. Eigenes Unfertig bleibt Unfertig.
              Eigenes Verwerfen wird nie hochgestuft.
  1 × Archiv: die Fassung, die sich am stärksten vom aktiven unterscheidet (nur wenn deutlich anders).
  Rest:       Verwerfen. Ideen bleiben unberührt.
Einzelstücke: eigene Entscheidung bleibt; sonst Vorschlag, wobei Aktiv → Unfertig (außer gelobt).
"""
import collections, glob, hashlib, json, re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from dubletten import fingerabdruck, woerter, jaccard  # noqa: E402

POS = re.compile(r"gefällt mir|gefiel|lecker|perfekt|super|sehr gut|richtig gut|go-?to|favorit|hat geschmeckt|"
                 r"schmeckt (mir )?(gut|toll|super)|genau so", re.I)
NEG = re.compile(r"zu (bitter|sauer|trocken|süß|dünn|flach|wässrig|fest|nass|klebrig|dunkel|hell|weich|hart)|"
                 r"nicht so gut|schmeckt nicht|misslungen|zusammengefallen|fließt|angebrannt|leider", re.I)

ZUBEREITUNG = [
    ("Flash Brew", re.compile(r"flash[\s-]?brew|iced|japanese|japanisch|auf eis\b|eiskaffee|eiswürfel|\beis\b(?!en)", re.I)),
    ("Bypass", re.compile(r"\bbypass\b", re.I)),
    ("8 g", re.compile(r"\b8\s?g\b(?!\s*(salz|zucker))|8-g|halbe portion", re.I)),
]


def kid(*t):
    return hashlib.sha1("|".join(t).encode()).hexdigest()[:12]


def zubereitung(k):
    kopf = (k.get("titel") or "") + " " + (k.get("text") or "")[:600]
    for name, rx in ZUBEREITUNG:
        if rx.search(kopf):
            return name
    return "heiß"


def inhalt_fp(k):
    if k["bereich"] == "kaffee-xbloom":
        return fingerabdruck(k)
    zut = " ".join(k.get("zutaten") or [])
    text = zut or (k.get("text") or "")[:3000]
    mengen = set(re.findall(r"\d+(?:[.,]\d+)?\s?(?:g|ml|min|°C)\b", text))
    return mengen | woerter(text)


VERSIONSWORT = re.compile(r"\b(v\d+(\.\d+)?|version|optimiert|überarbeitet|korrigiert|final|neu|verbessert|angepasst)\b", re.I)


def kern_titel(t):
    """Titel ohne Nummerierung, Versionsangaben und Zahlen – zwei gleiche Kerne = Iteration desselben Rezepts."""
    t = VERSIONSWORT.sub(" ", ohne_nummer(t or "").lower())
    t = re.sub(r"\d+([.,]\d+)?", " ", t)
    return frozenset(re.findall(r"[a-zäöüß]{3,}", t))


MENGE_RX = re.compile(r"\b\d+(?:[.,]\d+)?\s?(?:g|kg|ml|l|EL|TL|min|°C)\b")


def rezeptartig(k):
    """Echtes Rezept statt Analyse/Recherche: genug Mengen, Rezeptkarte/Datei oder xBloom-Güsse."""
    if k["art"] in ("karte", "datei"):
        return True
    if k["bereich"] == "kaffee-xbloom" and " g " in (k.get("eckdaten") or "") + " ":
        return True
    return len(MENGE_RX.findall(k.get("text") or "")) >= 8


def ohne_nummer(t):
    return re.sub(r"^(rezept|variante|gericht|frühstück|getränk|profil)\s*\d+\s*[:.)–-]\s*", "", (t or "").strip(), flags=re.I)


def feedback_claude(export, ids):
    sig = {}
    for c in json.load(open(export, encoding="utf-8")):
        msgs = c.get("chat_messages") or []
        for mi, m in enumerate(msgs):
            if m.get("sender") != "assistant":
                continue
            for i, _ in enumerate(m.get("content") or []):
                cid = kid(m["uuid"], str(i))
                if cid not in ids:
                    continue
                nxt = next((x for x in msgs[mi + 1:] if x.get("sender") == "human"), None)
                t = ((nxt or {}).get("text") or "")[:600]
                if POS.search(t):
                    sig[cid] = "pos"
                elif NEG.search(t):
                    sig[cid] = "neg"
    return sig


def feedback_gemini(export, kand):
    prompts = collections.defaultdict(list)
    for e in json.load(open(export, encoding="utf-8")):
        if not e.get("title", "").startswith("Eingegebener Prompt:"):
            continue
        url = next((d.get("url") for d in e.get("details") or [] if "gemini.google.com" in (d.get("url") or "")), None)
        if url:
            prompts["g-" + url.rsplit("/", 1)[-1]].append((e["time"], e["title"].split(":", 1)[1]))
    sig = {}
    for k in kand:
        ps = sorted(prompts.get(k["chat_id"], []))
        nxt = next((p for t, p in ps if t > k["zeit"]), "")
        if POS.search(nxt[:600]):
            sig[k["id"]] = "pos"
        elif NEG.search(nxt[:600]):
            sig[k["id"]] = "neg"
    return sig


def main(sichtung, edir, cdir, claude_export, gemini_export, kc, kg):
    K = json.load(open(sichtung, encoding="utf-8"))
    def lies(f):
        d = json.load(open(f))
        return d.get("data", d) if isinstance(d, dict) else {}
    E = {Path(f).stem: lies(f) for f in glob.glob(edir + "/*.json")}
    G = {Path(f).stem for f in glob.glob(cdir + "/*.json") if lies(f).get("geprueft")}
    zeit = {}
    for p in (kc, kg):
        for x in json.load(open(p, encoding="utf-8")):
            zeit[x["id"]] = x.get("zeit") or x.get("datum")
    for k in K:
        k["_zeit"] = zeit.get(k["id"]) or k["datum"]
        if k["id"] in E:
            k["_basis"], k["_eigen"] = E[k["id"]].get("status"), True
            k["_bereich"] = E[k["id"]].get("bereich") or k["bereich"]
        else:
            k["_basis"] = k["vorschlag"]
            k["_eigen"] = k["chat_id"] in G      # im geprüften Chat zählt der Vorschlag als deine Entscheidung
            k["_bereich"] = k["bereich"]

    ids = {k["id"] for k in K}
    sig = feedback_claude(claude_export, ids)
    sig.update(feedback_gemini(gemini_export, [dict(k, zeit=k["_zeit"]) for k in K if k.get("quelle") == "gemini"]))
    # Fassung direkt nach einer Korrektur im selben Chat
    nach_korrektur = set()
    pro_chat = collections.defaultdict(list)
    for k in K:
        pro_chat[k["chat_id"]].append(k)
    for xs in pro_chat.values():
        xs.sort(key=lambda k: k["_zeit"])
        for a, b in zip(xs, xs[1:]):
            if sig.get(a["id"]) == "neg":
                nach_korrektur.add(b["id"])

    # Linien bilden: Dublettengruppe × Zubereitungsart; Nicht-xBloom zusätzlich Titelnähe zum Gruppenkopf
    linien = collections.defaultdict(list)
    for k in K:
        if k["_basis"] == "idee":
            continue
        if not k.get("gruppe") or k["_bereich"] != k["bereich"]:
            continue
        key = (k["gruppe"], zubereitung(k) if k["bereich"] == "kaffee-xbloom" else "")
        linien[key].append(k)
    for key, xs in list(linien.items()):
        if xs[0]["bereich"] == "kaffee-xbloom" or len(xs) < 2:
            continue
        kopf = max(xs, key=lambda k: k["_zeit"])
        wk = woerter(ohne_nummer(kopf["titel"]))
        behalten = [k for k in xs if k is kopf or jaccard(woerter(ohne_nummer(k["titel"])), wk) >= 0.34
                    or jaccard(inhalt_fp(k), inhalt_fp(kopf)) >= 0.5]
        linien[key] = behalten
    getrennt = {}
    for key, xs in linien.items():
        koepfe = {}
        for k in sorted(xs, key=lambda k: k["_zeit"], reverse=True):
            if k["_eigen"] and k["_basis"] in ("aktiv", "unfertig"):
                kern = kern_titel(k["titel"])
                if not any(jaccard(kern, c) >= 0.8 for c in koepfe):
                    koepfe[kern] = k
        if len(koepfe) <= 1 or xs[0]["bereich"] == "kaffee-xbloom":
            getrennt[key] = xs
            continue
        # Du hast mehrere verschiedene Rezepte bewusst aktiv gesetzt: jedes bekommt eine eigene Linie
        teile = {c: [] for c in koepfe}
        for k in xs:
            kern = kern_titel(k["titel"])
            ziel = max(koepfe, key=lambda c: jaccard(kern, c))
            teile[ziel].append(k)
        for i, (c, ts) in enumerate(teile.items()):
            getrennt[(key[0] + f"-{i}", key[1])] = ts
    linien = {k: v for k, v in getrennt.items() if len(v) >= 2}
    in_linie = {}

    def rang(k):
        eigen_aktiv = k["_eigen"] and k["_basis"] in ("aktiv", "unfertig")
        return (eigen_aktiv, sig.get(k["id"]) == "pos", k["id"] in nach_korrektur,
                k.get("quelle", "claude") == "claude", k["_zeit"], k["art"] != "text")

    stat = collections.Counter()
    for (gid, zub), xs in linien.items():
        name = xs[0].get("gruppe_name") or xs[0]["titel"]
        if zub:
            name = f"{name} · {zub}"
        lid = f"{gid}-{zub or 'x'}"
        waehlbar = [k for k in xs if not (k["_eigen"] and k["_basis"] in ("verwerfen", "archiv"))]
        if not waehlbar:
            for k in xs:
                in_linie[k["id"]] = (k["_basis"], "alle Fassungen von dir archiviert oder verworfen", lid, name)
            continue
        aktiv = max(waehlbar, key=rang)
        st_aktiv = "unfertig" if (aktiv["_eigen"] and aktiv["_basis"] == "unfertig") else "aktiv"
        if aktiv["_eigen"] and aktiv["_basis"] in ("aktiv", "unfertig"):
            grund = "von dir gewählt"
        elif sig.get(aktiv["id"]) == "pos":
            grund = "im Chat gelobt"
        elif aktiv["id"] in nach_korrektur:
            grund = "Fassung nach deiner Korrektur"
        else:
            grund = "neueste Fassung" + (" (Claude)" if aktiv.get("quelle", "claude") == "claude" else "")
        in_linie[aktiv["id"]] = (st_aktiv, grund, lid, name)
        fa = inhalt_fp(aktiv)
        rest = [k for k in xs if k is not aktiv]
        # Deine eigenen Archiv-/Verwerfen-Entscheidungen bleiben, wie sie sind
        fest = [k for k in rest if k["_eigen"] and k["_basis"] in ("archiv", "verwerfen")]
        for k in fest:
            in_linie[k["id"]] = (k["_basis"], "deine Entscheidung bleibt", lid, name)
        rest = [k for k in rest if k not in fest]
        abst = sorted(((1 - jaccard(inhalt_fp(k), fa) if fa and inhalt_fp(k) else 0.0, k) for k in rest),
                      key=lambda t: t[0], reverse=True)
        schon_archiv = any(k["_basis"] == "archiv" for k in fest)
        kandidaten_archiv = [(d, k) for d, k in abst if rezeptartig(k) and d >= 0.5]
        archiv = kandidaten_archiv[0][1] if kandidaten_archiv and not schon_archiv else None
        for d, k in abst:
            if k is archiv:
                in_linie[k["id"]] = ("archiv", f"stärkste Alternative ({round(d * 100)} % anders)", lid, name)
            else:
                in_linie[k["id"]] = ("verwerfen", "ältere oder ähnliche Fassung" + (" (fast gleich)" if d < 0.3 else ""), lid, name)

    for k in K:
        if k["id"] in in_linie:
            st, grund, lid, name = in_linie[k["id"]]
        elif k["_basis"] == "idee":
            st, grund, lid, name = "idee", "Idee bleibt unberührt", None, None
        elif k["_eigen"]:
            st, grund, lid, name = k["_basis"], "deine Entscheidung bleibt", None, None
        elif k["_basis"] == "aktiv":
            if sig.get(k["id"]) == "pos":
                st, grund = "aktiv", "Einzelstück, im Chat gelobt"
            else:
                st, grund = "unfertig", "Einzelstück, noch nicht erprobt"
            lid = name = None
        else:
            st, grund, lid, name = k["_basis"], "Vorschlag übernommen", None, None
        k["auto"] = {"status": st, "grund": grund, "linie": lid, "linie_name": name,
                     "basis": k["_basis"], "eigen": k["_eigen"]}
        stat[(k["_eigen"], k["_basis"] != st)] += 1
        for f in ("_zeit", "_basis", "_eigen", "_bereich"):
            k.pop(f, None)

    json.dump(K, open(sichtung, "w", encoding="utf-8"), ensure_ascii=False)
    ae = [k for k in K if k["auto"]["eigen"] and k["auto"]["basis"] != k["auto"]["status"]]
    ao = [k for k in K if not k["auto"]["eigen"] and k["auto"]["basis"] != k["auto"]["status"]]
    print(f"Linien: {len(linien)} mit {sum(len(v) for v in linien.values())} Kandidaten")
    print("Feedback-Signale:", collections.Counter(sig.values()), "nach Korrektur:", len(nach_korrektur))
    print("Ergebnis gesamt:", collections.Counter(k["auto"]["status"] for k in K))
    print(f"Änderungen an deinen Entscheidungen: {len(ae)}", collections.Counter((k['auto']['basis'], k['auto']['status']) for k in ae))
    print(f"Änderungen an offenen Vorschlägen: {len(ao)}", collections.Counter((k['auto']['basis'], k['auto']['status']) for k in ao))


if __name__ == "__main__":
    main(*sys.argv[1:8])
