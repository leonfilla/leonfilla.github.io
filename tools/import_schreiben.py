#!/usr/bin/env python3
"""Schreibt die gesichteten Rezepte als Dateien ins Repo.

Aufruf:
  python3 tools/import_schreiben.py SICHTUNG.json ENTSCHEIDUNGEN_DIR KANDIDATEN_CLAUDE.json KANDIDATEN_GEMINI.json

- Aktiv, Unfertig, Archiv → content/rezepte/<bereich>/<slug>.md
- Idee                    → content/ideen/<bereich>/<slug>.md
- Verwerfen               → nicht übernommen
Persönliche Gesundheits- und Wohnortangaben werden absatzweise entfernt, reine Gesundheitsberichte ganz ausgelassen.
"""
import collections, glob, hashlib, html, json, re, sys, unicodedata
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"

PRIVAT = re.compile(r"lisdexamfetamin|elvanse|\badhs\b|umweltallergie|allergien \(|heuschnupfen|31-jährig|medizinstudent|"
                    r"serum-|vorerkrank|stellingen|jütländer|blutbild|laborwerte? (von|des)", re.I)
GANZ_PRIVAT = re.compile(r"ernährungsoptimierung und supplementier", re.I)
GENERISCH = re.compile(r"^(\d+[.)]\s|basis|schritt|teil|kategorie|option|variante|profil|rezept)\b|"
                       r"vorbereitung|konzept|zeitplan|warum|upgrade|zutatenliste|parameter|analyse|berechnung", re.I)
EINHEIT = {"g": "g", "kg": "kg", "ml": "ml", "l": "l", "tsp": "TL", "tbsp": "EL", "cup": "Tasse", "fl_oz": "fl oz",
           "oz": "oz", "lb": "lb", "pinch": "Prise", None: ""}
BOHNEN_ROESTEREI = {"El Paraíso": "Heilandt", "Pink Bourbon Decaf": "Coffee Circle", "Heilandt Sommer": "Heilandt",
                    "Yirgacheffe (Äthiopien)": "Wildkaffee", "Field Coffee": "Field Coffee",
                    "Phoenix Omniroast Decaf": "Phoenix Coffee Roasters", "Johann Jacobs Haus": "Johann Jacobs Haus"}


def slug(t, n=60):
    t = unicodedata.normalize("NFKD", (t or "").lower().replace("ß", "ss"))
    t = "".join(c for c in t if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")[:n].strip("-") or "rezept"


class D(yaml.SafeDumper):
    pass


D.add_representer(type(None), lambda d, _: d.represent_scalar("tag:yaml.org,2002:null", ""))


def dump(o):
    return yaml.dump(o, Dumper=D, sort_keys=False, allow_unicode=True, width=1000)


def schwaerzen(text):
    """Entfernt Absätze mit persönlichen Gesundheits- oder Wohnortangaben."""
    if not text:
        return text, 0
    teile = re.split(r"(\n\s*\n)", text)
    raus = 0
    for i in range(0, len(teile), 2):
        if PRIVAT.search(teile[i]):
            teile[i] = ""
            raus += 1
    return re.sub(r"\n{3,}", "\n\n", "".join(teile)).strip(), raus


def jsx_zu_markdown(code):
    """Smoothie-Komponenten: Namen und Mengen aus den Datenobjekten lesen."""
    zeilen, aktuell = [], None
    for m in re.finditer(r'name:\s*"([^"]+)"[^\n]*?(?:amt:\s*"([^"]+)")?', code):
        name, amt = m.group(1), m.group(2)
        if amt:
            zeilen.append(f"- {amt} {name}")
        elif name != aktuell:
            aktuell = name
            zeilen.append(f"\n### {name}\n")
    md = "\n".join(zeilen).strip()
    roh = f"<details><summary>Ursprüngliche Datei</summary><pre><code>{html.escape(code)}</code></pre></details>"
    return (md + "\n\n" if md.count("- ") >= 3 else "") + roh


def guter_titel(k, o):
    t = (k.get("titel") or "").strip().strip("*: ")
    if not GENERISCH.search(t) and len(t) > 6:
        return t
    frage = (o.get("prompt") or "").strip()
    if not frage and k.get("chat_titel"):
        frage = re.sub(r"^Gemini · ", "", k["chat_titel"])
    frage = re.sub(r"\s+", " ", frage)
    if frage:
        frage = frage[0].upper() + frage[1:]
        return (frage[:80].rsplit(" ", 1)[0] + " …") if len(frage) > 80 else frage
    return t


def main(sichtung, edir, kc, kg):
    def lies(f):
        d = json.load(open(f))
        return d.get("data", d)
    E = {Path(f).stem: lies(f) for f in glob.glob(edir + "/*.json")}
    K = json.load(open(sichtung, encoding="utf-8"))
    orig = {x["id"]: x for p in (kc, kg) for x in json.load(open(p, encoding="utf-8"))}

    vorhanden = {p.stem for p in (CONTENT / "bohnen").glob("*.yaml")}
    bohnen_name = {yaml.safe_load(open(p))["name"]: p.stem for p in (CONTENT / "bohnen").glob("*.yaml")}
    bohnen_name.update({"Kenya AA Githima": "kaffeekirsche-kenya-aa-githima", "Gran Galope": "kaffeekirsche-gran-galope"})
    bestehende_titel = {yaml.safe_load(p.read_text().split("---")[1]).get("titel", "").lower()
                        for p in (CONTENT / "rezepte").glob("*/*.md")}

    stat = collections.Counter()
    belegt = set()
    neue_bohnen = {}
    for k in K:
        e = E.get(k["id"])
        status = e["status"] if e else k["vorschlag"]
        bereich = (e or {}).get("bereich") or k["bereich"]
        if status == "verwerfen":
            continue
        o = orig[k["id"]]
        voll = " ".join(str(o.get(f) or "") for f in ("text", "notizen", "prompt", "beschreibung"))
        if GANZ_PRIVAT.search(voll):
            stat["ausgelassen (privat)"] += 1
            continue
        titel = guter_titel(k, o)
        if titel.lower() in bestehende_titel:
            stat["übersprungen (schon vorhanden)"] += 1
            continue

        quelle = {"typ": k.get("quelle", "claude"), "url": k.get("chat_url") or None,
                  "hinweis": re.sub(r"^Gemini · ", "", k.get("chat_titel") or "")[:120]}
        fm = {"titel": titel, "status": status, "datum": k["datum"], "quelle": quelle, "importiert": True}
        auto = k.get("auto") or {}
        if auto.get("linie"):
            fm["linie"] = slug(auto.get("linie_name") or titel, 50) + "-" + hashlib.sha1(auto["linie"].encode()).hexdigest()[:5]

        if bereich == "kaffee-xbloom" and k.get("gruppe_name"):
            name = k["gruppe_name"]
            bid = bohnen_name.get(name) or neue_bohnen.get(name)
            if not bid:
                bid = slug(name)
                neue_bohnen[name] = bid
            fm["bohne"] = bid

        body, geschwaerzt = "", 0
        if k["art"] == "karte":
            if o.get("beschreibung"):
                fm["fokus"], g = schwaerzen(o["beschreibung"]); geschwaerzt += g
            if o.get("portionen"):
                fm["portionen"] = o["portionen"]
            zutaten, nach_id = [], {}
            for z in o.get("zutaten") or []:
                einheit = EINHEIT.get(z.get("unit"), z.get("unit") or "")
                eintrag = {"name": z.get("name", "")}
                if isinstance(z.get("amount"), (int, float)):
                    eintrag["menge"] = z["amount"]
                eintrag["einheit"] = einheit
                zutaten.append(eintrag)
                nach_id[z.get("id")] = f"{z.get('amount', '')} {einheit} {z.get('name', '')}".replace("  ", " ").strip()
            fm["zutaten"] = zutaten
            schritte = []
            for s in o.get("schritte") or []:
                text = re.sub(r"\{(\d{4})\}", lambda m: nach_id.get(m.group(1), m.group(0)), s.get("content") or "")
                text, g = schwaerzen(text); geschwaerzt += g
                eintrag = {"titel": s.get("title") or None, "text": text}
                if s.get("timer_seconds"):
                    eintrag["timer"] = int(s["timer_seconds"])
                schritte.append({k2: v for k2, v in eintrag.items() if v is not None})
            fm["schritte"] = schritte
            body, g = schwaerzen(o.get("notizen") or ""); geschwaerzt += g
        else:
            text = o.get("text") or ""
            pfad = o.get("pfad") or ""
            if re.search(r"\.(jsx|tsx|js)$", pfad):
                body = jsx_zu_markdown(text)
            else:
                body, g = schwaerzen(text); geschwaerzt += g
                # Doppelte Titelzeile oben entfernen
                body = re.sub(r"^#{1,4}\s+.*\n+", "", body, count=1) if body.startswith("#") else body
            if o.get("prompt"):
                frage, g = schwaerzen(o["prompt"]); geschwaerzt += g
                if frage:
                    body = "> **Frage im Chat:** " + re.sub(r"\s+", " ", frage)[:500] + "\n\n" + body

        if geschwaerzt:
            stat["Absätze entfernt (privat)"] += geschwaerzt
        ordner = CONTENT / ("ideen" if status == "idee" else "rezepte") / bereich
        ordner.mkdir(parents=True, exist_ok=True)
        name = slug(titel)
        while name in belegt or (ordner / f"{name}.md").exists():
            name = f"{slug(titel, 52)}-{k['id'][-6:]}"
            if name in belegt:
                name += "-2"
        belegt.add(name)
        if status == "idee":
            fm.pop("status")
        (ordner / f"{name}.md").write_text("---\n" + dump(fm) + "---\n\n" + body.strip() + "\n", encoding="utf-8")
        stat[status] += 1

    for name, bid in neue_bohnen.items():
        if bid in vorhanden:
            continue
        (CONTENT / "bohnen" / f"{bid}.yaml").write_text(dump({
            "name": name, "roesterei": BOHNEN_ROESTEREI.get(name, "Ohne Angabe"), "herkunft": None,
            "aufbereitung": None, "decaf": "decaf" in name.lower(), "geschmack": None,
            "quelle": "Import aus Chats – Angaben ergänzen"}), encoding="utf-8")
        stat["neue Bohnen"] += 1
    print(dict(stat))


if __name__ == "__main__":
    main(*sys.argv[1:5])
