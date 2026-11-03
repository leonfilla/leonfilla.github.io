#!/usr/bin/env python3
"""Bündelt ähnliche Rezept-Kandidaten über Chats und Quellen hinweg.

Aufruf:  python3 tools/dubletten.py kandidaten.json
Ergänzt jeden Kandidaten um:
  gruppe        Kennung der Ähnlichkeitsgruppe (nur bei Gruppen mit ≥ 2 Mitgliedern)
  gruppe_name   lesbarer Name (bei xBloom die Bohne)
  rolle         "neueste" oder "aelter"
  fast_gleich   True, wenn die Parameter kaum von der neuesten Fassung abweichen
  eckdaten      kurze Parameterzeile zum Vergleichen (xBloom: Mahlgrad, RPM, Temperaturen)
"""
import json, re, sys, unicodedata

# Bekannte Bohnen: Anzeigename → Suchmuster
BOHNEN = {
    "Kerinci": r"kerinci", "Joven Macario": r"joven\s+macario", "Gran Galope": r"gran\s+galope",
    "Kenya AA Githima": r"githima|kenya\s+aa", "Uraga Raro Boda": r"uraga", "Ruronzi Anaerobic": r"ruronzi",
    "Huye Mountain": r"huye", "24/sieben Decaf": r"24\s*/?\s*sieben|24/7", "Popayan Reserve Decaf": r"popay[aá]n",
    "Kijani Kiboko Decaf": r"kijani", "El Eucalipto": r"eucalipto", "El Paraíso": r"para[ií]so",
    "La Esperanza": r"esperanza", "Pink Bourbon Decaf": r"pink\s+bourbon", "Heilandt Sommer": r"heilandt\s+sommer|\bsommer\b.*heilandt",
    "Phoenix Omniroast Decaf": r"phoenix|omniroast\s+decaf", "Rubiac Decaf": r"rubiac", "La Flaca Decaf": r"la\s+flaca",
    "Johann Jacobs Haus": r"johann\s+jacobs", "Yirgacheffe (Äthiopien)": r"yirgacheffe|äthiop|ethiopi",
    "Pacamara": r"pacamara", "Sidra": r"\bsidra\b", "Reposado": r"reposado", "Field Coffee": r"field\s+coffee",
}
BOHNEN_RX = [(n, re.compile(p, re.I)) for n, p in BOHNEN.items()]
# Generische Überschriften, die nichts über das Rezept sagen
GENERISCH = re.compile(r"^(\d+\.\s*)?(gewichtungs-check|recherche-ergebnisse|analyse|persona|mahlwerk|zutaten|"
                       r"abweichung|ergebnis|eindeutige id|einleitung|berechnungsgrundlage|parameter|executive summary|"
                       r"zusammensetzung|teil \d)\b", re.I)


def titel_von(k):
    t = (k.get("titel") or "").strip("*: ")
    if GENERISCH.search(t) or len(t) < 6:
        for zeile in re.findall(r"^#{1,4}\s+\**(.+?)\**\s*$", k.get("text") or "", re.M):
            if not GENERISCH.search(zeile.strip("*: ")) and len(zeile) > 6:
                return zeile.strip("*: ")[:120]
        frage = re.search(r"Frage:\s*(.+)", k.get("text") or "")
        if frage:
            return frage.group(1)[:100]
    return t


STOP = {"und", "mit", "für", "der", "die", "das", "von", "rezept", "rezepte", "version", "variante", "optimiert",
        "neues", "neue", "schnelle", "schnell", "einfache", "aus", "dem", "den", "ein", "eine", "gemini", "frage"}


def woerter(t):
    t = unicodedata.normalize("NFKC", (t or "").lower())
    t = re.sub(r"\b[vV]\s?\d+(\.\d+)?\b", " ", t)
    return {w for w in re.findall(r"[a-zäöüß]{4,}", t) if w not in STOP}


def jaccard(a, b):
    return len(a & b) / len(a | b) if a and b else 0.0


def bohne(k):
    kopf = " ".join([k.get("titel") or "", k.get("chat_titel") or "", (k.get("text") or "")[:1200]])
    for name, rx in BOHNEN_RX:
        if rx.search(kopf):
            return name
    return None


MAHL_RX = re.compile(r"mahlgrad(?:\s*\([^)]*\))?\s*\**\s*[:=|]?\s*\**\s*(\d{1,2})\b", re.I)
RPM_RX = re.compile(r"(\d{2,3})\s*rpm\b|rpm(?:\s*\([^)]*\))?\s*\**\s*[:=|]?\s*\**\s*(\d{2,3})\b", re.I)
GUSS_RX = re.compile(r"\|\s*\**\s*(bloom|guss\s*\d|aufguss\s*\d|pour\s*\d|phase\s*\d)\s*\**\s*\|\s*(\d{2,3})\s*(?:g|ml)?\s*\|\s*(\d{2})", re.I)
TEMP_RX = re.compile(r"(\d{2})(?:[.,]\d)?\s?°\s?C")


def xb_zahlen(text):
    """Mahlgrad, RPM, Temperaturen und Güsse (Menge, Temperatur) aus Tabellen oder Fließtext."""
    t = text or ""
    mahl = MAHL_RX.findall(t)
    rpm = [a or b for a, b in RPM_RX.findall(t)]
    guesse = [(int(m), int(tp)) for _, m, tp in GUSS_RX.findall(t)]
    temps = [str(tp) for _, tp in guesse] or TEMP_RX.findall(t)
    return mahl, rpm, temps, guesse


def fingerabdruck(k):
    mahl, rpm, temps, guesse = xb_zahlen(k.get("text") or "")
    return {f"m{x}" for x in mahl} | {f"r{x}" for x in rpm} | {f"g{m}@{t}" for m, t in guesse} | \
        ({f"t{x}" for x in temps} if not guesse else set())


def eckdaten(k):
    mahl, rpm, temps, _ = xb_zahlen(k.get("text") or "")
    teile = []
    if mahl:
        teile.append("Mahlgrad " + "/".join(dict.fromkeys(mahl[:4])))
    if rpm:
        teile.append("RPM " + "/".join(dict.fromkeys(rpm[:3])))
    if temps:
        teile.append("°C " + "→".join(temps[:6]))
    _, _, _, guesse = xb_zahlen(k.get("text") or "")
    if guesse:
        teile.append("g " + "/".join(str(m) for m, _ in guesse[:6]))
    return " · ".join(teile)


class Gruppen:
    def __init__(self, n):
        self.p = list(range(n))
    def finde(self, i):
        while self.p[i] != i:
            self.p[i] = self.p[self.p[i]]; i = self.p[i]
        return i
    def vereine(self, a, b):
        self.p[self.finde(a)] = self.finde(b)


def main(pfad):
    K = json.load(open(pfad, encoding="utf-8"))
    for k in K:
        for f in ("gruppe", "gruppe_name", "rolle", "fast_gleich", "eckdaten"):
            k.pop(f, None)
    n = len(K)
    g = Gruppen(n)
    for k in K:
        k["titel"] = titel_von(k)
    w = [woerter(k.get("titel")) for k in K]
    z = [woerter(" ".join(k.get("zutaten") or [])) for k in K]
    b = [bohne(k) if k["bereich"] == "kaffee-xbloom" else None for k in K]

    for i in range(n):
        for j in range(i + 1, n):
            ki, kj = K[i], K[j]
            if ki["bereich"] != kj["bereich"]:
                continue
            if ki["bereich"] == "kaffee-xbloom":
                # xBloom: gleiche Bohne = gleiche Gruppe
                if b[i] and b[i] == b[j]:
                    g.vereine(i, j)
            elif jaccard(w[i], w[j]) >= 0.5 or (z[i] and z[j] and jaccard(z[i], z[j]) >= 0.7 and jaccard(w[i], w[j]) >= 0.25):
                g.vereine(i, j)

    gruppen = {}
    for i in range(n):
        gruppen.setdefault(g.finde(i), []).append(i)

    anzahl = 0
    for wurzel, glieder in gruppen.items():
        if len(glieder) < 2:
            continue
        anzahl += 1
        # neueste Fassung zuerst: Datum, dann Claude vor Gemini, dann Rezeptkarte/Datei vor Text
        glieder.sort(key=lambda i: (K[i]["datum"], K[i].get("quelle", "claude") == "claude",
                                    K[i]["art"] != "text"), reverse=True)
        kopf = K[glieder[0]]
        name = b[glieder[0]] or kopf["titel"]
        fp_kopf = fingerabdruck(kopf) if kopf["bereich"] == "kaffee-xbloom" else None
        for rang, i in enumerate(glieder):
            k = K[i]
            k["gruppe"] = f"g{wurzel}"
            k["gruppe_name"] = name
            k["rolle"] = "neueste" if rang == 0 else "aelter"
            if k["bereich"] == "kaffee-xbloom":
                k["eckdaten"] = eckdaten(k)
                if rang and fp_kopf:
                    fp = fingerabdruck(k)
                    k["fast_gleich"] = bool(fp and fp_kopf) and jaccard(fp, fp_kopf) >= 0.5
            elif rang:
                k["fast_gleich"] = jaccard(w[i], w[glieder[0]]) >= 0.8 and (not z[i] or jaccard(z[i], z[glieder[0]]) >= 0.85)

    json.dump(K, open(pfad, "w", encoding="utf-8"), ensure_ascii=False)
    mitglieder = sum(1 for k in K if k.get("gruppe"))
    xb = {k["gruppe_name"] for k in K if k.get("gruppe") and k["bereich"] == "kaffee-xbloom"}
    print(f"{anzahl} Gruppen mit {mitglieder} Kandidaten; davon xBloom-Bohnen: {len(xb)}")
    print("fast gleich:", sum(1 for k in K if k.get("fast_gleich")))
    print("xBloom ohne erkannte Bohne:", sum(1 for k, bb in zip(K, b) if k["bereich"] == "kaffee-xbloom" and not bb))


if __name__ == "__main__":
    main(sys.argv[1])
