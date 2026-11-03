#!/usr/bin/env python3
"""Findet Rezept-Kandidaten im Gemini-Export (Google Takeout, „Meine Aktivitäten“ als JSON).

Aufruf:  python3 tools/import_gemini.py MeineAktivitäten.json kandidaten_gemini.json
Gruppiert Einträge über die Chat-URL zu Chats. Die Ausgabe enthält private Inhalte
und gehört NICHT ins Repo.
"""
import json, re, sys
from html.parser import HTMLParser
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from import_claude import MENGE, KAFFEE_TEXT, KOCHWORT, AUSSCHLUSS, bereich_von, norm_titel, aehnlich, kid  # noqa: E402


# Zusätzliche Nicht-Rezept-Themen, die nur in Gemini vorkommen (Produktvergleiche, Gesundheit)
GEMINI_AUSSCHLUSS = re.compile(r"munddusch|trinkflasch|supplement|polyphenol|lumbar|aeron|gosch|maxomixx|ballaststoff", re.I)


class ZuText(HTMLParser):
    """Wandelt Geminis Antwort-HTML in lesbares Markdown um."""
    def __init__(self):
        super().__init__()
        self.out, self.liste = [], []
    def handle_starttag(self, tag, attrs):
        if tag in ("h1", "h2", "h3", "h4"):
            self.out.append("\n\n" + "#" * min(int(tag[1]) + 1, 4) + " ")
        elif tag == "p":
            self.out.append("\n\n")
        elif tag in ("ul", "ol"):
            self.liste.append([tag, 0])
        elif tag == "li":
            art = self.liste[-1] if self.liste else ["ul", 0]
            art[1] += 1
            self.out.append("\n" + "  " * (len(self.liste) - 1) + ("- " if art[0] == "ul" else f"{art[1]}. "))
        elif tag in ("strong", "b"):
            self.out.append("**")
        elif tag == "br":
            self.out.append("\n")
        elif tag == "tr":
            self.out.append("\n|")
        elif tag == "hr":
            self.out.append("\n\n---")
    def handle_endtag(self, tag):
        if tag in ("ul", "ol") and self.liste:
            self.liste.pop(); self.out.append("\n")
        elif tag in ("strong", "b"):
            self.out.append("**")
        elif tag in ("td", "th"):
            self.out.append(" |")
    def handle_data(self, data):
        self.out.append(data)
    def text(self):
        return re.sub(r"\n{3,}", "\n\n", "".join(self.out)).strip()


def html_zu_text(h):
    p = ZuText(); p.feed(h); return p.text()


def main(src, ziel):
    eintraege = json.load(open(src, encoding="utf-8"))
    chats = {}
    for e in eintraege:
        if not e.get("title", "").startswith("Eingegebener Prompt:"):
            continue
        url = next((d.get("url") for d in e.get("details") or [] if "gemini.google.com" in (d.get("url") or "")), None)
        cid = url.rsplit("/", 1)[-1] if url else "ohne-chat-" + e["time"][:10]
        prompt = e["title"].split(":", 1)[1].strip()
        antwort = "\n\n".join(html_zu_text(h.get("html", "")) for h in e.get("safeHtmlItem") or [])
        chats.setdefault(cid, {"url": url, "eintraege": []})["eintraege"].append((e["time"], prompt, antwort))

    kandidaten = []
    for cid, c in chats.items():
        es = sorted(c["eintraege"])
        erster = es[0][1]
        titel_chat = "Gemini · " + (erster[:80] + ("…" if len(erster) > 80 else ""))
        if AUSSCHLUSS.search(erster) or GEMINI_AUSSCHLUSS.search(erster):
            continue
        chat = {"chat_id": "g-" + cid, "chat_titel": titel_chat, "chat_url": c["url"] or "", "datum": es[0][0][:10],
                "quelle": "gemini"}
        eigene = []
        for zeit, prompt, text in es:
            mengen = len(MENGE.findall(text))
            kaffee = bool(KAFFEE_TEXT.search(text)) and re.search(r"\d+\s?°", text)
            if len(text) < 300 or (mengen < 8 and not kaffee) or not KOCHWORT.search(text):
                continue
            m = re.search(r"^#{1,4}\s+(.+)$", text, re.M) or re.search(r"\*\*(.+?)\*\*", text) or re.search(r"(.{0,80})", text)
            titel = re.sub(r"^(Rezept|Recipe)\s*:\s*", "", m.group(1).strip().strip("*"))[:120]
            eigene.append({**chat, "id": "g" + kid(cid, zeit), "art": "text", "zeit": zeit, "titel": titel,
                           "prompt": prompt[:600], "text": text,
                           "bereich": bereich_von(titel + " " + erster, text[:3000])})
        for k in eigene:
            k["_n"] = norm_titel(k["titel"])
        for j, k in enumerate(eigene):
            spaeter = [x for x in eigene[j + 1:] if aehnlich(k["_n"], x["_n"])]
            k["ersetzt_durch"] = spaeter[-1]["id"] if spaeter else None
            mehrere = len(re.findall(r"^(?:#{1,4}\s|\*\*\d|\d+\.\s\*\*)", k["text"], re.M)) >= 3 and \
                len(re.findall(r"^#{1,4}\s*Zutaten", k["text"], re.M | re.I)) < 2
            k["vorschlag"] = "archiv" if k["ersetzt_durch"] else ("idee" if mehrere and len(MENGE.findall(k["text"])) < 12 else "aktiv")
            k.pop("_n")
        kandidaten.extend(eigene)
    kandidaten.sort(key=lambda k: (k["datum"], k["zeit"]))
    json.dump(kandidaten, open(ziel, "w", encoding="utf-8"), ensure_ascii=False)
    from collections import Counter
    print(len(chats), "Gemini-Chats,", len(kandidaten), "Kandidaten aus", len({k["chat_id"] for k in kandidaten}), "Chats")
    print(Counter(k["vorschlag"] for k in kandidaten), Counter(k["bereich"] for k in kandidaten))


if __name__ == "__main__":
    main(*sys.argv[1:3])
