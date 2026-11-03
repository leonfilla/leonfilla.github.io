# Leons Rezepte

Statische Rezeptseite unter **https://xbloom.leonfilla.de**. Jedes Rezept ist eine Markdown-Datei mit YAML-Kopf. Ein kleines Python-Skript baut daraus die Seite und prüft dabei jedes Rezept gegen die Gerätegrenzen in `content/profil/equipment.yaml`.

## Aufbau

```
content/
  bereiche.yaml            Bereiche und ihre Reihenfolge auf der Startseite
  rezepte/<bereich>/*.md   ein Rezept pro Datei, Ordnername = Bereich
  bohnen/*.yaml            Kaffeebohnen, auf die xBloom-Rezepte verweisen
  profil/                  equipment, vorlieben, prozess, vorrat
  wissen/*.md              Grundlagen und validierte Prinzipien
  seiten/*.md              Impressum, Datenschutz
templates/                 Jinja2-Vorlagen
static/                    CSS, JavaScript, Favicon
public/                    wird unverändert ins Wurzelverzeichnis kopiert (CNAME)
build.py                   Bauen und Prüfen
```

Bereiche: `kaffee-xbloom`, `kaffee-oracle-jet`, `kaffee-unterwegs`, `brot-sauerteig`, `brot-automat`, `instant-pot`, `smoothies`, `backen`, `allgemein`.

## Lokal bauen

```sh
pip install -r requirements.txt
python3 build.py          # baut nach _site/
python3 build.py --check  # nur prüfen
```

Bei jedem Push auf `main` baut GitHub Actions die Seite und veröffentlicht sie. Pull Requests werden nur geprüft.

## Rezeptformat

Alle Felder außer `titel` sind optional. Der Text unter dem YAML-Kopf ist Markdown und erscheint als Notizen.

```yaml
---
titel: El Eucalipto – Go-to heiß
linie: heilandt-el-eucalipto   # fasst Versionen und Varianten zusammen (Standard: Dateiname)
version: v2                    # z. B. v5, V18.1 – sortiert numerisch
variante: Go-to heiß
status: aktiv                  # aktiv | entwurf | archiv
favorit: true                  # erscheint unter „Go-to“
bewertung: 8                   # 0–10
datum: 2026-07-27
quelle: {typ: chat, url: https://claude.ai/chat/…, hinweis: Chat-Titel}
geraete: [xbloom-studio]       # IDs aus equipment.yaml
bohne: heilandt-el-eucalipto   # Datei in content/bohnen/
tags: [Beilage]
fokus: Ein Satz, worum es geht.
portionen: 4                   # aktiviert den Portionsrechner
zutaten:
  - {name: Jasminreis, menge: 300}                 # Einheit Standard g
  - {name: Vollkornmehl, menge: 400, mehl: true, gruppe: Hauptteig}
  - {name: Milch, menge: 50, wasser: 0.87, hinweis: 3,8 %}
schritte:
  - {titel: Druckgaren, text: "Pressure Cook, **High**, 4 Minuten.", timer: 240}
changelog:
  - {version: v2, datum: 2026-08-01, text: Bloom auf 48 g}
---
```

### Bereichsblöcke

```yaml
xbloom:     {dosis: 16, verhaeltnis: 16, wasser: 256, mahlgrad: 58, rpm: 60, bruehzeit: "2:50",
             bypass: {menge: 60, temp: 85},
             guesse: [{phase: Bloom, menge: 48, temp: 92, fluss: 3.0, pause: 35,
                       muster: zentral, vib_vor: true, vib_nach: false}]}
espresso:   {getraenk: Flat White, dosis: 22, ausbeute: 39, zeit: 26, temperatur: 92,
             mahlgrad: 29, preinfusion: 7, milch: {menge: 140, temp: 58}}
instantpot: {programm: Pressure Cook, druck: High, zeit: 4, ablass: Natural Release,
             ablass_min: 10, pot_in_pot: false, temperatur: 42}
brot:       {programm: "Menü 3", kerntemperatur: 97, hydration: 84, spender_g: 130}
smoothie:   {volumen_ml: 560, protein: 45, kcal: 700}
parameter:  {Frei: Wert}   # beliebige weitere Kacheln
```

## Prüfungen beim Bauen

- **xBloom:** Dosis 16 oder 8 g, Mahlgrad 1–80, RPM 60–120, Temperatur ≤ 96 °C, Fluss 3,0–3,5 ml/s, Verhältnis in 0,5er-Schritten, Summe der Güsse = Wasser, Dosis × Verhältnis ≈ Wasser
- **Oracle Jet:** Dosis ≥ 22 g
- **Instant Pot:** Druck Low, High oder Max
- **Brot:** angegebene `hydration` muss zur Wasserbilanz der Zutaten passen (`mehl: true`, `wasser: Anteil`); Spender ≤ 150 g
- **Smoothies:** Volumen ≤ 600 ml
- Geräte und Bohnen müssen existieren

Bei aktiven Rezepten und Entwürfen bricht der Build ab, bei archivierten Rezepten erscheint nur ein Hinweis auf der Seite.

## Maschinenlesbar

`/katalog.json` enthält alle Rezepte, Bohnen und das Profil – damit Claude vor dem Erstellen neuer Rezepte den aktuellen Stand lesen kann.
