#!/usr/bin/env python3
"""Findet Rezept-Kandidaten im Claude-Datenexport (conversations.json).

Aufruf:  python3 tools/import_claude.py conversations.json kandidaten.json
Die Ausgabe enthält Auszüge aus privaten Chats und gehört NICHT ins Repo.
"""
import json, re, sys, hashlib, unicodedata

MENGE = re.compile(r"\b\d+(?:[.,]\d+)?\s?(?:g|kg|ml|l|EL|TL|Stk|Prise|min|°C)\b")
BEREICH_REGELN = [
    ("kaffee-xbloom", re.compile(r"x\s?bloom", re.I)),
    ("kaffee-oracle-jet", re.compile(r"oracle jet|flat white|americano|siebträger|espresso", re.I)),
    ("kaffee-unterwegs", re.compile(r"pulsar|x-ultra|reisekit|unterwegs", re.I)),
    ("brot-automat", re.compile(r"sd-yr2540|brotbackautomat|backautomat|panasonic", re.I)),
    ("brot-sauerteig", re.compile(r"sauerteig|levain|vollkornbrot|\bbrot\b(?!.*banane)|krume|stückgare|stockgare", re.I)),
    ("smoothies", re.compile(r"smoothie|shake|vetain|kreatin|trinkjoghurt", re.I)),
    ("instant-pot", re.compile(r"instant pot|pressure cook|natural release|druckablass|hochdruck|\bnpr\b|\bhp\b", re.I)),
    ("backen", re.compile(r"kuchen|bananenbrot|muffin|zimtschnecke|brioche|cobbler|waffel|keks|käsekuchen|backofen|backform|kastenform|springform", re.I)),
]
# Chats ohne Rezepte, die nur wegen Mengenangaben auffallen (Training, Gesundheit, Technik, Reisen …)
AUSSCHLUSS = re.compile(r"trainingsplan|workout|heimtraining|health|gesundheit|tertial|aeg|reiseziel|urlaub|portasplit|"
                        r"schlafzimmer|jaz |riu |clear-protein|wasserenth|osmose|webpage|mixer-alternative|timemore|"
                        r"pale ale|bohnen-alternativen|kaufen|vergleich peruan|nährstoffprofil|lisdex|lernplan", re.I)
KOCHWORT = re.compile(r"zutat|zubereitung|bloom|mahlgrad|ofen|instant pot|teig|mehl|mixen|mixer|kochen|garen|backen|"
                      r"rezept|einweichen|pfanne|topf|brüh|espresso|smoothie|druck", re.I)
KAFFEE_TEXT = re.compile(r"(mahlgrad|grind).{0,400}(bloom|guss|pour)|(bloom|guss).{0,400}(mahlgrad|grind)", re.I | re.S)


REIHENFOLGE = ["kaffee-xbloom", "kaffee-oracle-jet", "kaffee-unterwegs", "brot-automat", "smoothies",
               "instant-pot", "backen", "brot-sauerteig"]
REGELN = dict(BEREICH_REGELN)


def bereich_von(titel, *texte):
    """Erst nach Titeln entscheiden, dann nach dem Text."""
    for t in (titel or "", " ".join(x or "" for x in texte)):
        for b in REIHENFOLGE:
            if REGELN[b].search(t):
                return b
    return "allgemein"


def norm_titel(t):
    t = unicodedata.normalize("NFKD", t.lower())
    t = re.sub(r"\b(v|version)\s?\d+(\.\d+)?\b", " ", t)
    return set(w for w in re.findall(r"[a-zäöüß]{3,}", t) if w not in {"und", "mit", "für", "der", "die", "das", "von"})


def aehnlich(a, b):
    if not a or not b:
        return False
    return len(a & b) / len(a | b) >= 0.5


def kid(*teile):
    return hashlib.sha1("|".join(teile).encode()).hexdigest()[:12]


def main(src, ziel):
    chats = json.load(open(src, encoding="utf-8"))
    kandidaten = []
    for c in chats:
        chat = {"chat_id": c["uuid"], "chat_titel": c.get("name") or "(ohne Titel)",
                "chat_url": f"https://claude.ai/chat/{c['uuid']}", "datum": (c.get("created_at") or "")[:10]}
        eigene = []
        if AUSSCHLUSS.search(chat["chat_titel"]):
            continue
        for m in c.get("chat_messages") or []:
            if m.get("sender") != "assistant":
                continue
            zeit = m.get("created_at", "")
            for i, b in enumerate(m.get("content") or []):
                typ = b.get("type")
                if typ == "tool_use" and "recipe_display" in (b.get("name") or ""):
                    inp = b.get("input") or {}
                    titel = inp.get("title") or "Rezept"
                    eigene.append({**chat, "id": kid(m["uuid"], str(i)), "art": "karte", "zeit": zeit,
                                   "titel": titel, "beschreibung": inp.get("description"),
                                   "portionen": inp.get("base_servings"), "zutaten": inp.get("ingredients") or [],
                                   "schritte": inp.get("steps") or [], "notizen": inp.get("notes"),
                                   "bereich": bereich_von(titel + " " + chat["chat_titel"], inp.get("description"), inp.get("notes"),
                                                          json.dumps(inp.get("steps") or [], ensure_ascii=False))})
                elif typ == "tool_use" and (b.get("name") in ("create_file", "Write") or b.get("name") == "artifacts"):
                    inp = b.get("input") or {}
                    text = inp.get("file_text") or inp.get("content") or ""
                    pfad = inp.get("path") or inp.get("file_path") or inp.get("title") or ""
                    if b.get("name") == "artifacts" and inp.get("command") not in ("create", "rewrite"):
                        continue
                    if len(MENGE.findall(text)) < 6 and not KAFFEE_TEXT.search(text):
                        continue
                    if re.search(r"\.(py|js|jsx|ts|css|json|sh)$", pfad) and not re.search(r"rezept|recipe|smoothie|xbloom", pfad + text[:400], re.I):
                        continue
                    titel = (re.search(r"^#\s+(.+)$", text, re.M) or re.search(r"(.*)", inp.get("title") or pfad.split("/")[-1])).group(1).strip()
                    eigene.append({**chat, "id": kid(m["uuid"], str(i)), "art": "datei", "zeit": zeit, "titel": titel[:120],
                                   "pfad": pfad, "text": text, "bereich": bereich_von(titel + " " + chat["chat_titel"], text[:3000])})
                elif typ == "text":
                    text = b.get("text") or ""
                    mengen = len(MENGE.findall(text))
                    kaffee = bool(KAFFEE_TEXT.search(text)) and re.search(r"\d+\s?°", text)
                    if len(text) < 300 or (mengen < 8 and not kaffee) or not KOCHWORT.search(text):
                        continue
                    titel = (re.search(r"^#{1,3}\s+(.+)$", text, re.M) or re.search(r"\*\*(.+?)\*\*", text) or re.search(r"(.{0,80})", text)).group(1).strip()
                    eigene.append({**chat, "id": kid(m["uuid"], str(i)), "art": "text", "zeit": zeit,
                                   "titel": titel[:120], "text": text,
                                   "bereich": bereich_von(titel + " " + chat["chat_titel"], text[:3000])})
        # Iterationen im selben Chat: ältere Fassung → Archiv vorschlagen
        for k in eigene:
            k["_n"] = norm_titel(k["titel"])
        for j, k in enumerate(eigene):
            spaeter = [x for x in eigene[j + 1:] if x["art"] == k["art"] and aehnlich(k["_n"], x["_n"])]
            k["ersetzt_durch"] = spaeter[-1]["id"] if spaeter else None
            mehrere = k["art"] == "text" and len(re.findall(r"^(?:#{1,3}\s|\*\*\d|\d+\.\s\*\*)", k.get("text", ""), re.M)) >= 3
            if k["ersetzt_durch"]:
                k["vorschlag"] = "archiv"
            elif mehrere:
                k["vorschlag"] = "idee"
            elif k["art"] == "text" and any(x["art"] in ("karte", "datei") for x in eigene):
                k["vorschlag"] = "verwerfen"   # Begleittext zu einer Karte oder Datei im selben Chat
            else:
                k["vorschlag"] = "aktiv"
        for k in eigene:
            k.pop("_n", None)
        kandidaten.extend(eigene)
    kandidaten.sort(key=lambda k: (k["datum"], k["zeit"]))
    json.dump(kandidaten, open(ziel, "w", encoding="utf-8"), ensure_ascii=False)
    from collections import Counter
    print(len(kandidaten), "Kandidaten aus", len({k["chat_id"] for k in kandidaten}), "Chats")
    print(Counter(k["art"] for k in kandidaten), Counter(k["vorschlag"] for k in kandidaten))
    print(Counter(k["bereich"] for k in kandidaten))


if __name__ == "__main__":
    main(*sys.argv[1:3])
