#!/usr/bin/env python3
"""Baut die Rezeptseite aus content/ nach _site/.

Aufruf:
    python3 build.py            # bauen, bei Fehlern abbrechen
    python3 build.py --check    # nur prüfen, nichts schreiben

Abhängigkeiten: PyYAML, Markdown, Jinja2 (siehe requirements.txt).
"""
from __future__ import annotations

import datetime as dt
import html
import json
import re
import shutil
import sys
from pathlib import Path

import markdown
import yaml
from zoneinfo import ZoneInfo
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).parent
CONTENT = ROOT / "content"
OUT = ROOT / "_site"
SITE_URL = "https://rezepte.leonfilla.de"

STATUS = {"aktiv": "Aktiv", "unfertig": "Unfertig", "archiv": "Archiv"}
STATUS_ALIAS = {"entwurf": "unfertig"}
STATUS_RANG = {"aktiv": 0, "unfertig": 1, "archiv": 2}
MUSTER = {"spirale": "Spirale", "kreis": "Kreis", "zentral": "Zentral"}


# ---------------------------------------------------------------- Laden

def read_yaml(path: Path):
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def read_md(path: Path):
    text = path.read_text(encoding="utf-8")
    meta, body = {}, text
    if text.startswith("---"):
        parts = text.split("\n---", 1)
        meta = yaml.safe_load(parts[0][3:]) or {}
        body = parts[1].lstrip("-").lstrip("\n") if len(parts) > 1 else ""
    return meta, body


def md(text: str, breaks: bool = False) -> str:
    exts = ["tables", "sane_lists", "attr_list", "fenced_code"] + (["nl2br"] if breaks else [])
    return markdown.markdown(text or "", extensions=exts)


def md_inline(text: str) -> str:
    out = md(text)
    return re.sub(r"^<p>(.*)</p>$", r"\1", out.strip(), flags=re.S)


def version_key(v) -> tuple:
    nums = re.findall(r"\d+", str(v or ""))
    return tuple(int(n) for n in nums) or (0,)


# ---------------------------------------------------------------- Prüfung

class Report:
    def __init__(self):
        self.fehler: list[str] = []
        self.warnungen: list[str] = []

    def add(self, rezept, level: str, text: str):
        rezept["hinweise"].append({"level": level, "text": text})
        line = f"{rezept['quelle_datei']}: {text}"
        (self.fehler if level == "fehler" else self.warnungen).append(line)


def in_range(value, spec) -> bool:
    if value is None or spec is None:
        return True
    if isinstance(spec, list):
        return value in spec
    lo, hi = spec.get("min"), spec.get("max")
    return (lo is None or value >= lo) and (hi is None or value <= hi)


def spec_text(spec) -> str:
    if isinstance(spec, list):
        return " oder ".join(fmt(s) for s in spec)
    lo, hi = spec.get("min"), spec.get("max")
    if lo is not None and hi is not None:
        return f"{fmt(lo)}–{fmt(hi)}"
    return f"≥ {fmt(lo)}" if lo is not None else f"≤ {fmt(hi)}"


PHANTOM_OK = {"hinweis", "einheit", "gruppe", "timer", "menge", "text", "ph", "dampf", "temp", "zeit", "phase"}


def pruefe(r, ctx, report: Report):
    # Nur aktive Rezepte müssen alle Grenzen einhalten; unfertige und archivierte bekommen Hinweise.
    # Aus Chats übernommene Rezepte: Verstöße als sichtbarer Hinweis, nicht als Build-Abbruch
    hart = "fehler" if r["status"] == "aktiv" and not r.get("importiert") else "warnung"
    def add(level, text):
        report.add(r, level, text)

    if not r.get("titel"):
        add("fehler", "Titel fehlt")
    # Ungequotete Kommas in einzeiligen {…}-Einträgen erzeugen leere Phantom-Schlüssel
    brot = r.get("brot") if isinstance(r.get("brot"), dict) else {}
    for feld, liste in (("zutaten", r.get("zutaten")), ("schritte", r.get("schritte")),
                        ("gare", brot.get("gare")), ("backprofil", brot.get("backprofil"))):
        for e in liste or []:
            if isinstance(e, dict):
                kaputt = [str(k) for k, v in e.items() if v is None and str(k) not in PHANTOM_OK]
                if kaputt:
                    add("fehler", f"{feld}: Komma ohne Anführungszeichen – „{', '.join(kaputt)}“ abgetrennt")
    if r["status"] not in STATUS:
        add("fehler", f"Unbekannter Status „{r['status']}“")
    for g in r.get("geraete") or []:
        if g not in ctx["geraete"]:
            add("fehler", f"Unbekanntes Gerät „{g}“ – in content/profil/equipment.yaml anlegen")
    if r.get("bohne") and r["bohne"] not in ctx["bohnen"]:
        add("fehler", f"Unbekannte Bohne „{r['bohne']}“ – in content/bohnen/ anlegen")

    typ = r["bereich_info"]["typ"]

    xb = r.get("xbloom")
    if typ == "xbloom" and not xb:
        if r.get("importiert") or r.get("body_html"):
            add("warnung", "Parameter stehen nur im Text – noch nicht als xBloom-Block erfasst")
        else:
            add("fehler", "xbloom-Block fehlt")
    if xb:
        g = ctx["geraete"]["xbloom-studio"].get("grenzen", {})
        if not in_range(xb.get("dosis"), g.get("dosis")):
            add(hart, f"Dosis {fmt(xb.get('dosis'))} g – erlaubt sind {spec_text(g['dosis'])} g")
        if not in_range(xb.get("mahlgrad"), g.get("mahlgrad")):
            add(hart, f"Mahlgrad {xb.get('mahlgrad')} außerhalb {spec_text(g['mahlgrad'])}")
        if not in_range(xb.get("rpm"), g.get("rpm")):
            add(hart, f"RPM {xb.get('rpm')} außerhalb {spec_text(g['rpm'])}")
        schritt = g.get("verhaeltnis_schritt")
        v = xb.get("verhaeltnis")
        if v and schritt and abs(v / schritt - round(v / schritt)) > 1e-6:
            add(hart, f"Verhältnis 1:{fmt(v)} ist in der App nicht einstellbar (Schritte von {fmt(schritt)})")
        guesse = xb.get("guesse") or []
        for i, s in enumerate(guesse, 1):
            if not in_range(s.get("temp"), g.get("temp")):
                add(hart, f"Guss {i}: {s.get('temp')} °C über dem Maximum von {g['temp']['max']} °C")
            if not in_range(s.get("fluss"), g.get("fluss")):
                add(hart, f"Guss {i}: Fluss {fmt(s.get('fluss'))} ml/s außerhalb {spec_text(g['fluss'])}")
            if s.get("muster") and s["muster"] not in MUSTER:
                add("fehler", f"Guss {i}: unbekanntes Muster „{s['muster']}“")
        summe = sum(s.get("menge", 0) for s in guesse)
        if guesse and xb.get("wasser") and abs(summe - xb["wasser"]) > 1:
            add(hart, f"Güsse ergeben {summe} g, angegeben sind {xb['wasser']} g Wasser")
        if xb.get("dosis") and v and xb.get("wasser"):
            soll = xb["dosis"] * v
            if abs(soll - xb["wasser"]) > 2.5:
                add("warnung", f"{fmt(xb['dosis'])} g × 1:{fmt(v)} = {soll:.0f} g, angegeben sind {xb['wasser']} g")
        by = xb.get("bypass")
        if by and not in_range(by.get("temp"), g.get("temp")):
            add(hart, f"Bypass-Temperatur {by.get('temp')} °C über dem Maximum")

    es = r.get("espresso")
    if es:
        g = ctx["geraete"]["oracle-jet"].get("grenzen", {})
        if not in_range(es.get("dosis"), g.get("dosis")):
            add(hart, f"Dosis {fmt(es.get('dosis'))} g – das IMS-Sieb braucht {spec_text(g['dosis'])} g")

    ip = r.get("instantpot")
    if ip:
        g = ctx["geraete"]["instant-pot-pro-max"].get("grenzen", {})
        if ip.get("druck") and not in_range(str(ip["druck"]).lower(), g.get("druck")):
            add(hart, f"Druckstufe „{ip['druck']}“ gibt es nicht (Low, High, Max)")

    br = r.get("brot") or {}
    calc = r.get("berechnet", {})
    if br.get("hydration") is not None and calc.get("hydration") is not None:
        if abs(br["hydration"] - calc["hydration"]) > 1.0:
            add(hart, f"Angegebene Hydration {fmt(br['hydration'])} % passt nicht zur Wasserbilanz "
                      f"der Zutaten ({fmt(round(calc['hydration'], 1))} %)")
    if br.get("spender_g"):
        g = ctx["geraete"]["panasonic-sd-yr2540"].get("grenzen", {})
        if br["spender_g"] > g.get("spender_max_g", 1e9):
            add(hart, f"{br['spender_g']} g im Spender – maximal {g['spender_max_g']} g")

    sm = r.get("smoothie") or {}
    limit = r["bereich_info"].get("max_volumen_ml")
    if limit and sm.get("volumen_ml") and sm["volumen_ml"] > limit:
        add(hart, f"Volumen {sm['volumen_ml']} ml über der Grenze von {limit} ml")


# ---------------------------------------------------------------- Berechnungen

def fmt(x) -> str:
    if x is None:
        return "–"
    if isinstance(x, float):
        s = f"{x:.1f}".rstrip("0").rstrip(".")
        return s.replace(".", ",")
    return str(x)


WASSERANTEILE = [
    (re.compile(r"(?i)^(kaltes |warmes |lauwarmes )?wasser\b"), 1.0),
    (re.compile(r"(?i)^buttermilch\b"), 0.9),
    (re.compile(r"(?i)^(voll|fettarme |frische |h-)?milch\b(?!pulver)"), 0.87),
    (re.compile(r"(?i)^(ei|eier|vollei)\b"), 0.75),
    (re.compile(r"(?i)^eiweiß|^eiklar"), 0.88),
]


def berechne(r):
    calc = {}
    zut = r.get("zutaten") or []
    mehl = sum(z.get("menge", 0) for z in zut if z.get("mehl") and isinstance(z.get("menge"), (int, float)))
    if mehl:
        # Unmarkierte Flüssigkeiten mit Standard-Wasseranteil mitzählen (Milch 0,87, Ei 0,75 …)
        for z in zut:
            if "wasser" in z or z.get("einheit", "g") not in ("g", "ml") or "optional" in str(z.get("hinweis", "")).lower():
                continue
            for muster, anteil in WASSERANTEILE:
                if muster.match(str(z.get("name", ""))):
                    z["wasser"] = anteil
                    z["wasser_geschaetzt"] = True
                    break
        wasser = sum(z.get("menge", 0) * float(z.get("wasser", 0)) for z in zut
                     if isinstance(z.get("menge"), (int, float)) and z.get("wasser"))
        calc["mehl"] = mehl
        calc["wasser"] = wasser
        calc["hydration"] = wasser / mehl * 100 if wasser else None
        for z in zut:
            if isinstance(z.get("menge"), (int, float)) and z.get("einheit", "g") in ("g", "ml"):
                z["bp"] = z["menge"] / mehl * 100
    xb = r.get("xbloom")
    if xb and xb.get("guesse"):
        calc["guss_summe"] = sum(s.get("menge", 0) for s in xb["guesse"])
    r["berechnet"] = calc


def temp_svg(serien, height=150) -> str:
    """Kleines Liniendiagramm der Gusstemperaturen. serien = [(label, [temps], css_var)]."""
    alle = [t for _, ts, _ in serien for t in ts if t is not None]
    if not alle:
        return ""
    lo, hi = min(alle) - 1, max(alle) + 1
    n = max(len(ts) for _, ts, _ in serien)
    w, pad_l, pad_r, pad_t, pad_b = 320, 34, 12, 12, 26
    def x(i):
        return pad_l + (i * (w - pad_l - pad_r) / max(n - 1, 1))
    def y(t):
        return pad_t + (hi - t) * (height - pad_t - pad_b) / (hi - lo)
    parts = [f'<svg class="tempkurve" viewBox="0 0 {w} {height}" role="img" '
             f'aria-label="Temperaturverlauf über die Güsse">']
    for t in sorted({round(lo + 1), round((lo + hi) / 2), round(hi - 1)}):
        parts.append(f'<line x1="{pad_l}" x2="{w - pad_r}" y1="{y(t):.1f}" y2="{y(t):.1f}" class="gitter"/>')
        parts.append(f'<text x="{pad_l - 6}" y="{y(t) + 4:.1f}" text-anchor="end" class="achse">{t}°</text>')
    for i in range(n):
        label = "B" if i == 0 else str(i + 1)
        parts.append(f'<text x="{x(i):.1f}" y="{height - 8}" text-anchor="middle" class="achse">{label}</text>')
    for label, ts, var in serien:
        pts = " ".join(f"{x(i):.1f},{y(t):.1f}" for i, t in enumerate(ts) if t is not None)
        parts.append(f'<polyline points="{pts}" fill="none" stroke="var({var})" stroke-width="2.5" '
                     f'stroke-linejoin="round" stroke-linecap="round"><title>{html.escape(label)}</title></polyline>')
        for i, t in enumerate(ts):
            if t is not None:
                parts.append(f'<circle cx="{x(i):.1f}" cy="{y(t):.1f}" r="3.5" fill="var({var})">'
                             f'<title>{html.escape(label)}: {t} °C</title></circle>')
    parts.append("</svg>")
    return "".join(parts)


def xbloom_text(r) -> str:
    """Rezept als Text zum Abtippen in die xBloom-App."""
    xb = r["xbloom"]
    zeilen = [r["titel"],
              f"Dosis {fmt(xb.get('dosis'))} g · 1:{fmt(xb.get('verhaeltnis'))} · {xb.get('wasser')} g Wasser",
              f"Mahlgrad {xb.get('mahlgrad')} · RPM {xb.get('rpm')}"]
    for s in xb.get("guesse") or []:
        vib = [v for v, k in (("Vib. vor", "vib_vor"), ("Vib. nach", "vib_nach")) if s.get(k)]
        zeilen.append(f"{s.get('phase')}: {s.get('menge')} g · {s.get('temp')} °C · {fmt(s.get('fluss'))} ml/s · "
                      f"Pause {s.get('pause')} s · {MUSTER.get(s.get('muster'), s.get('muster'))}"
                      + (f" · {', '.join(vib)}" if vib else ""))
    if xb.get("bypass"):
        b = xb["bypass"]
        zeilen.append(f"Bypass: {b.get('menge')} g · {b.get('temp')} °C")
    return "\n".join(zeilen)


# ---------------------------------------------------------------- Hauptablauf

def lade():
    cfg = read_yaml(CONTENT / "bereiche.yaml")
    bereiche = {}
    for gruppe in cfg["gruppen"]:
        for b in gruppe["bereiche"]:
            b["gruppe"] = gruppe["name"]
            bereiche[b["id"]] = b

    equipment = read_yaml(CONTENT / "profil/equipment.yaml")
    geraete = {g["id"]: g for g in equipment["geraete"]}

    bohnen = {}
    for p in sorted((CONTENT / "bohnen").glob("*.yaml")):
        b = read_yaml(p)
        b["id"] = p.stem
        b["url"] = f"/bohnen/{p.stem}/"
        b["rezepte"] = []
        bohnen[p.stem] = b

    rezepte = []
    for p in sorted((CONTENT / "rezepte").glob("*/*.md")):
        meta, body = read_md(p)
        bereich = p.parent.name
        if bereich not in bereiche:
            sys.exit(f"Unbekannter Bereich-Ordner: {p.parent}")
        r = dict(meta)
        r.update({
            "slug": p.stem,
            "bereich": bereich,
            "bereich_info": bereiche[bereich],
            "url": f"/rezept/{bereich}/{p.stem}/",
            "quelle_datei": str(p.relative_to(ROOT)),
            "status": STATUS_ALIAS.get(r.get("status", "aktiv"), r.get("status", "aktiv")),
            "linie": r.get("linie", p.stem),
            "linie_explizit": "linie" in r,
            "hinweise": [],
            "body_html": md(body),
        })
        if isinstance(r.get("datum"), (dt.date, dt.datetime)):
            r["datum"] = r["datum"].isoformat()[:10]
        berechne(r)
        rezepte.append(r)

    wissen = []
    for p in sorted((CONTENT / "wissen").glob("*.md")):
        meta, body = read_md(p)
        meta.update({"id": p.stem, "url": f"/wissen/{p.stem}/", "body_html": md(body)})
        wissen.append(meta)
    wissen.sort(key=lambda w: (w.get("bereich", ""), w.get("reihenfolge", 99)))

    ideen = []
    for p in sorted((CONTENT / "ideen").glob("*/*.md")):
        meta, body = read_md(p)
        bereich = p.parent.name
        if bereich not in bereiche:
            continue
        if isinstance(meta.get("datum"), (dt.date, dt.datetime)):
            meta["datum"] = meta["datum"].isoformat()[:10]
        meta.update({"slug": p.stem, "bereich": bereich, "bereich_info": bereiche[bereich],
                     "url": f"/idee/{bereich}/{p.stem}/", "body_html": md(body), "quelle_datei": str(p.relative_to(ROOT))})
        ideen.append(meta)
    ideen.sort(key=lambda i: str(i.get("datum") or ""), reverse=True)

    seiten = {}
    for p in sorted((CONTENT / "seiten").glob("*.md")):
        meta, body = read_md(p)
        meta.update({"id": p.stem, "body_html": md(body, breaks=True)})
        seiten[p.stem] = meta

    profil = {name: read_yaml(CONTENT / f"profil/{name}.yaml")
              for name in ("vorlieben", "prozess", "vorrat")}
    profil["equipment"] = equipment
    return {"cfg": cfg, "bereiche": bereiche, "geraete": geraete, "bohnen": bohnen,
            "rezepte": rezepte, "wissen": wissen, "seiten": seiten, "profil": profil, "ideen": ideen}


def verknuepfe(ctx):
    linien = {}
    for r in ctx["rezepte"]:
        # Explizite Linien gelten bereichsübergreifend (verschobene Geschwister bleiben verknüpft)
        schluessel = r["linie"] if r.get("linie_explizit") else (r["bereich"], r["linie"])
        linien.setdefault(schluessel, []).append(r)
        if r.get("bohne") in ctx["bohnen"]:
            ctx["bohnen"][r["bohne"]]["rezepte"].append(r)
    for rs in linien.values():
        rs.sort(key=lambda r: (version_key(r.get("version")), str(r.get("datum") or ""), r.get("variante") or ""))
        for r in rs:
            r["geschwister"] = [x for x in rs if x is not r]
        # Ältere Versionen einer Linie gelten als überholt, sobald es eine neuere nicht archivierte gibt
        lebend = [x for x in rs if x["status"] != "archiv"]
        kopf = lebend[-1] if lebend else None
        for r in rs:
            r["veraltet"] = bool(kopf and r is not kopf and r.get("version") and kopf.get("version")
                                 and r["status"] != "archiv")
    for b in ctx["bohnen"].values():
        reihenfolge = {"Ausgewogen": 0, "Original": 1}
        b["status"] = sorted({r["status"] for r in b["rezepte"]}, key=lambda s: STATUS_RANG.get(s, 9))
        b["rezepte"].sort(key=lambda r: (STATUS_RANG.get(r["status"], 9), reihenfolge.get(r.get("variante"), 2),
                                         r.get("variante") or ""))
    for r in ctx["rezepte"]:
        if r.get("xbloom"):
            r["kopiertext"] = xbloom_text(r)
            r["tempkurve"] = temp_svg([(r["titel"], [s.get("temp") for s in r["xbloom"].get("guesse") or []],
                                        "--akzent")])
    farben = ["--serie-1", "--serie-2", "--serie-3", "--serie-4"]
    for b in ctx["bohnen"].values():
        # Höchstens 4 Kurven, damit jede Farbe eindeutig bleibt: aktive/unfertige zuerst, sonst die neuesten
        mit_xb = [r for r in b["rezepte"] if r.get("xbloom") and r["xbloom"].get("guesse")]
        lebend = [r for r in mit_xb if r["status"] != "archiv"]
        auswahl = (lebend or sorted(mit_xb, key=lambda r: str(r.get("datum") or ""), reverse=True))[:4]
        serien = [(r.get("variante") or r["titel"].split(" – ", 1)[-1], [s.get("temp") for s in r["xbloom"]["guesse"]],
                   farben[i % 4]) for i, r in enumerate(auswahl)]
        b["tempkurve"] = temp_svg(serien) if serien else ""
        b["serien"] = [(label, farben[i % 4]) for i, (label, _, _) in enumerate(serien)]


def suchindex(ctx):
    eintraege = []
    for r in ctx["rezepte"]:
        bohne = ctx["bohnen"].get(r.get("bohne"), {})
        text = " ".join(filter(None, [
            r.get("titel"), r.get("variante"), r["bereich_info"]["name"], bohne.get("name"),
            bohne.get("roesterei"), bohne.get("herkunft"), bohne.get("aufbereitung"),
            " ".join(r.get("tags") or []), " ".join(z.get("name", "") for z in r.get("zutaten") or [])]))
        eintraege.append({"t": r["titel"], "u": r["url"], "b": r["bereich_info"]["name"], "bid": r["bereich"],
                          "s": r["status"], "v": r.get("veraltet", False), "q": text.lower()})
    for i in ctx["ideen"]:
        eintraege.append({"t": i["titel"], "u": i["url"], "b": i["bereich_info"]["name"] + " · Idee", "bid": i["bereich"],
                          "s": "idee", "q": (i["titel"] + " " + i["bereich_info"]["name"]).lower()})
    for b in ctx["bohnen"].values():
        eintraege.append({"t": b["name"] + " (Bohne)", "u": b["url"], "b": b.get("roesterei", ""), "bid": "kaffee-xbloom",
                          "s": (b.get("status") or ["aktiv"])[0], "bohne": True, "q": " ".join(str(b.get(k, "")) for k in
                                                       ("name", "roesterei", "herkunft", "aufbereitung", "geschmack")).lower()})
    return eintraege


def katalog(ctx):
    """Maschinenlesbare Gesamtsicht – für Claude und andere Werkzeuge."""
    weg = {"bereich_info", "hinweise", "body_html", "geschwister", "kopiertext", "tempkurve", "quelle_datei"}
    return {
        "erzeugt": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        "bereiche": ctx["cfg"]["gruppen"],
        "profil": ctx["profil"],
        "bohnen": [{k: v for k, v in b.items() if k not in {"rezepte", "tempkurve", "serien"}}
                   for b in ctx["bohnen"].values()],
        "rezepte": [{**{k: v for k, v in r.items() if k not in weg}, "datei": r["quelle_datei"],
                     "url": SITE_URL + r["url"]} for r in ctx["rezepte"]],
    }


def schreibe(ctx):
    env = Environment(loader=FileSystemLoader(ROOT / "templates"),
                      autoescape=select_autoescape(["html"]), trim_blocks=True, lstrip_blocks=True)
    env.filters["fmt"] = fmt
    env.filters["md_inline"] = md_inline
    env.filters["datum"] = lambda d: ".".join(reversed(str(d)[:10].split("-"))) if d else ""
    env.globals.update(ctx=ctx, STATUS=STATUS, MUSTER=MUSTER, jahr=dt.date.today().year,
                       stand=dt.datetime.now(ZoneInfo("Europe/Berlin")).strftime("%d.%m.%Y, %H:%M"),
                       repo_edit="https://github.com/leonfilla/leonfilla.github.io/edit/main/")

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    shutil.copytree(ROOT / "static", OUT / "static")
    for p in (ROOT / "public").iterdir():
        shutil.copy(p, OUT / p.name)

    def seite(pfad: str, template: str, **kw):
        ziel = OUT / pfad.strip("/") / "index.html" if not pfad.endswith(".html") else OUT / pfad.strip("/")
        ziel.parent.mkdir(parents=True, exist_ok=True)
        ziel.write_text(env.get_template(template).render(pfad=pfad, **kw), encoding="utf-8")

    sichtbar = [r for r in ctx["rezepte"]]
    zaehler = {b: {s: sum(1 for r in sichtbar if r["bereich"] == b and r["status"] == s) for s in STATUS}
               for b in ctx["bereiche"]}
    favoriten = [r for r in sichtbar if r.get("favorit")]
    neueste = sorted([r for r in sichtbar if r.get("datum")], key=lambda r: r["datum"], reverse=True)[:6]

    seite("/", "index.html", zaehler=zaehler, favoriten=favoriten, neueste=neueste,
          index_json=json.dumps(suchindex(ctx), ensure_ascii=False))

    for bid, b in ctx["bereiche"].items():
        rs = [r for r in sichtbar if r["bereich"] == bid]
        gruppen = []
        if b["typ"] == "xbloom":
            bohnen = sorted({r.get("bohne") for r in rs if r.get("bohne")},
                            key=lambda x: ctx["bohnen"][x]["name"])
            nach_aufb = {}
            for x in bohnen:
                bb = ctx["bohnen"][x]
                key = "Decaf" if bb.get("decaf") else (bb.get("aufbereitung") or "Weitere Bohnen")
                nach_aufb.setdefault(key, []).append(bb)
            ordnung = ["Gewaschen", "Natural", "Anaerob / fermentiert"]
            gruppen = sorted(nach_aufb.items(), key=lambda kv: (kv[0] == "Decaf",
                             ordnung.index(kv[0]) if kv[0] in ordnung else 9, kv[0]))
        liste = sorted(rs, key=lambda r: (STATUS_RANG.get(r["status"], 9) + (1.5 if r.get("veraltet") else 0),
                                          not r.get("favorit"), r["titel"].lower(), version_key(r.get("version"))))
        anzahl = {s: sum(1 for r in rs if r["status"] == s) for s in STATUS}
        anzahl["ungesichtet"] = sum(1 for r in rs if r.get("gesichtet") is False)
        wissen = [w for w in ctx["wissen"] if w.get("bereich") == bid]
        ohne_bohne = [r for r in liste if b["typ"] == "xbloom" and not r.get("bohne")]
        ideen_n = sum(1 for i in ctx["ideen"] if i["bereich"] == bid)
        seite(f"/{bid}/", "bereich.html", bereich=b, gruppen=gruppen, wissen=wissen, liste=liste, anzahl=anzahl,
              ohne_bohne=ohne_bohne, ideen_n=ideen_n)

    for r in sichtbar:
        seite(r["url"], "rezept.html", r=r, bohne=ctx["bohnen"].get(r.get("bohne")))

    seite("/bohnen/", "bohnen.html")
    for b in ctx["bohnen"].values():
        seite(b["url"], "bohne.html", b=b)

    seite("/profil/", "profil.html", p=ctx["profil"])
    seite("/ideen/", "ideen.html")
    for i in ctx["ideen"]:
        seite(i["url"], "idee.html", i=i)
    seite("/wissen/", "wissen_liste.html")
    for w in ctx["wissen"]:
        seite(w["url"], "wissen.html", w=w)
    for s in ctx["seiten"].values():
        seite(f"/{s['id']}/", "seite.html", s=s)
    seite("/404.html", "seite.html", s={"titel": "Nicht gefunden",
                                       "body_html": "<p>Diese Seite gibt es nicht. <a href=\"/\">Zur Startseite</a></p>"})

    (OUT / "katalog.json").write_text(json.dumps(katalog(ctx), ensure_ascii=False, indent=1, default=str),
                                     encoding="utf-8")


def main():
    nur_pruefen = "--check" in sys.argv
    ctx = lade()
    report = Report()
    for r in ctx["rezepte"]:
        pruefe(r, ctx, report)
    verknuepfe(ctx)

    print(f"{len(ctx['rezepte'])} Rezepte, {len(ctx['bohnen'])} Bohnen, {len(ctx['wissen'])} Wissensseiten")
    if report.warnungen:
        print(f"\n{len(report.warnungen)} Warnungen (Archiv oder weich):")
        for w in report.warnungen:
            print("  ·", w)
    if report.fehler:
        print(f"\n{len(report.fehler)} FEHLER:")
        for f in report.fehler:
            print("  ✗", f)
        sys.exit(1)
    if not nur_pruefen:
        schreibe(ctx)
        print(f"\nGebaut nach {OUT.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
