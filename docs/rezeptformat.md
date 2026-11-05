# Rezeptformat

Jedes Rezept ist eine Datei `content/rezepte/<bereich>/<slug>.md`: YAML-Kopf mit allen Daten, darunter kurze Notizen in Markdown. **Eine Datei = ein Rezept.** Mehrere Rezepte aus einem Chat werden zu mehreren Dateien mit gemeinsamer `linie` (bei Varianten) bzw. eigener Linie (bei verschiedenen Gerichten).

Die Seite stellt jedes Rezept in derselben Reihenfolge dar:

1. **Titel und Kurzbeschreibung** – was es ist, in einem Satz, warum so, in einem zweiten
2. **Eckdaten** – Kacheln mit den Werten, die man vor dem Start braucht (je Bereich verschieden)
3. **Zutaten** – gruppiert, in Gramm, in Verarbeitungsreihenfolge
4. **Zubereitung** – nummerierte Schritte, ein Handgriff pro Schritt, Timer wo gewartet wird
5. **Notizen** – höchstens drei feste Abschnitte: *Warum so*, *Stellschrauben*, *Varianten*
6. **Änderungen und Quelle**

## Gemeinsamer Kopf (alle Bereiche)

```yaml
titel: Kurzer Name des Gerichts, ohne „Rezept 1:“, höchstens ~60 Zeichen
status: aktiv | unfertig | archiv
datum: 2026-07-29
quelle: {typ: claude | gemini, url: …, hinweis: Chat-Titel}
linie: gemeinsamer Schlüssel aller Fassungen/Varianten
variante: z. B. „Körper“, „Klarheit“, „8 g“ – nur wenn es Geschwister gibt
fokus: 1–2 Sätze. Was ist das, und was ist das Besondere daran?
ergebnis: 4 Portionen | 1 Laib, ca. 950 g | 1 Tasse, 256 ml
portionen: 4                # nur wenn skalierbar; aktiviert den Portionsrechner
zeit: {aktiv: 15, gesamt: 45}   # Minuten
geraete: [instant-pot-pro-max]  # IDs aus profil/equipment.yaml
tags: [Frühstück, vegetarisch]
zutaten:
  - {gruppe: Hauptteig, name: Weizenvollkornmehl, menge: 400, einheit: g, mehl: true}
  - {name: Wasser, menge: 320, einheit: g, wasser: 1}
  - {name: Ei, menge: 1, einheit: "", hinweis: Größe M}
schritte:
  - {titel: Kurz und imperativ, text: Ein Handgriff, Mengen ausgeschrieben., timer: 600}
```

Regeln: Mengen in Gramm (auch Flüssigkeiten, Gewürze, Eier, wo sinnvoll mit Stück als Hinweis). Schritte ohne Begründungen – die gehören in *Warum so*. Recherche, Quellenlisten, Produktvergleiche und lange Herleitungen entfallen.

## Eckdaten je Bereich

| Bereich | Block | Felder |
|---|---|---|
| xBloom Studio | `xbloom` | dosis (16/8), verhaeltnis, wasser, mahlgrad, rpm, bruehzeit, bypass {menge, temp}, guesse [{phase, menge, temp, fluss, pause, muster, vib_vor, vib_nach}] · `bohne` |
| Oracle Jet | `espresso` | getraenk, dosis, ausbeute, zeit, temperatur, mahlgrad, preinfusion, milch {menge, temp, textur}, sieb |
| Unterwegs | `handbrew` | methode, dosis, wasser, mahlgrad, temperatur, bloom {menge, zeit}, gesamtzeit; Schritte mit Uhrzeit im Titel („0:40 – Hauptguss“) |
| Sauerteig | `brot` | teiggewicht, hydration, gare [{phase, temp, zeit, ph}], backprofil [{phase, temp, dampf, zeit}], kerntemperatur · Zutaten mit `mehl: true` / `wasser: Anteil` für Bäckerprozente |
| Brotbackautomat | `brot` | programm, groesse, braeunung, spender_g, hydration · Zutaten in Einfüllreihenfolge |
| Instant Pot | `instantpot` | programm, druck (Low/High/Max), zeit, ablass, ablass_min, temperatur, pot_in_pot |
| Smoothies | `smoothie` | volumen_ml (≤ 600), kcal, protein · Zutaten in Mixreihenfolge |
| Backen | `ofen` | modus, temp, dampf, zeit, kerntemperatur, form |
| Allgemein | `ofen` (optional) | wie Backen, wenn ein Ofen im Spiel ist |

## Notizen

```markdown
## Warum so
Höchstens 5 Sätze zum Mechanismus.

## Stellschrauben
- Zu sauer → 1–2 Stufen feiner
- Krume zu dicht → 10 g mehr Wasser

## Varianten
- Für 8 g: …
```
