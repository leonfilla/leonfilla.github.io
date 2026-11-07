---
titel: Vollkorn-Sauerteigbrot V16 mit ganzer Chia und Akazie
status: archiv
datum: '2026-06-19'
quelle:
  typ: claude
  url: https://claude.ai/chat/92d7e3a0-45a4-466a-9727-75fed036aa43
  hinweis: Brotrezept mit Chiasamen optimieren
importiert: true
linie: v16-vollstandiges-rezept-workflow-module-a-c-d-aka-6a59c
version: V16
fokus: 100 % Vollkorn-Sauerteigbrot, frei geschoben, mit gekeimtem Mehl, ganzer Chia und Akazienfaser. Ein 45-°C-Phytase-Soak im Instant Pot senkt das Phytat, Stockgare über pH, langer Kühlretard.
ergebnis: 1 Laib
zeit: {aktiv: 33, gesamt: 2280}
geraete: [wilfa-probaker, instant-pot-pro-max, apera-ph60f, kernthermometer, bosch-hng978]
tags: [Brot, Vollkorn, Sauerteig]
changelog:
  - {version: V16, text: "Chia 20 g geschrotet → 25 g ganz, Hanf 20 g → 0 g, Wasser im Hauptteig 380 g → 390 g."}
brot:
  kerntemperatur: 98
  gare:
    - {phase: Levain, temp: "~21", zeit: 10–14 h, ph: "4,1–4,3"}
    - {phase: Phytase-Soak, temp: 45, zeit: 45 min}
    - {phase: Saltolyse, temp: Raumtemperatur, zeit: 25 min}
    - {phase: Stockgare, temp: "~21", zeit: 5–8 h, ph: "4,55–4,65"}
    - {phase: Kühlretard, temp: 4, zeit: 12–16 h}
  backprofil:
    - {phase: Ofentrieb, temp: 250, dampf: voll (Stufe 3), zeit: 12–15 min}
    - {phase: Krustenbildung, temp: 220, dampf: aus, zeit: 18 min}
    - {phase: Krumensetzung, temp: 200, dampf: aus, zeit: bis Kern 98 °C}
    - {phase: Crisp Finish (optional), temp: 210, dampf: Heißluft, zeit: 5 min}
zutaten:
  - {gruppe: Levain, name: Anstellgut, menge: 15, einheit: g, hinweis: aus dem Kühlschrank}
  - {gruppe: Levain, name: Weizenvollkornmehl fein, menge: 75, einheit: g}
  - {gruppe: Levain, name: Wasser, menge: 75, einheit: g, hinweis: Raumtemperatur}
  - {gruppe: Soak, name: Weizenvollkornmehl fein, menge: 275, einheit: g, mehl: true, hinweis: backstark}
  - {gruppe: Soak, name: Gekeimtes Weizen- oder Dinkelvollkornmehl, menge: 50, einheit: g, mehl: true}
  - {gruppe: Soak, name: Roggenvollkornmehl fein, menge: 75, einheit: g, mehl: true}
  - {gruppe: Soak, name: Hafervollkornmehl fein, menge: 50, einheit: g, mehl: true}
  - {gruppe: Soak, name: Chiasamen ganz, menge: 25, einheit: g}
  - {gruppe: Soak, name: Akazienfaser, menge: 10, einheit: g}
  - {gruppe: Soak, name: Wasser, menge: 340, einheit: g, wasser: 1, hinweis: ca. 30 °C}
  - {gruppe: Saltolyse, name: Salz, menge: 10, einheit: g}
  - {gruppe: Saltolyse, name: Vitalkleber, menge: 25, einheit: g}
  - {gruppe: Saltolyse, name: Psylliumschalen fein, menge: 7, einheit: g}
  - {gruppe: Saltolyse, name: Wasser, menge: 50, einheit: g, wasser: 1}
  - {gruppe: Saltolyse, name: Ascorbinsäure, menge: 0.05, einheit: g, hinweis: optional}
  - {gruppe: Finalmix, name: Reifer Levain, menge: 100, einheit: g, hinweis: enthält je 50 g Mehl und Wasser}
schritte:
  - titel: Levain ansetzen
    text: Am Vorabend 15 g Anstellgut, 75 g Weizenvollkornmehl und 75 g Wasser klümpchenfrei verrühren, locker abdecken, Füllstand markieren und bei Raumtemperatur reifen lassen.
    timer: 43200
  - titel: Levain prüfen
    text: Reif, wenn gewölbt, Float-Test positiv und pH 4,1–4,3.
  - titel: Anstellgut zurückstellen
    text: 35 g reifen Levain in ein sauberes Glas füllen und in den Kühlschrank stellen.
  - titel: Soak mischen
    text: In der Instant-Pot-Schüssel alle Mehle, 25 g ganze Chia, 10 g Akazienfaser und 340 g Wasser (ca. 30 °C) homogen vermengen. Kein Salz, kein Vitalkleber, kein Psyllium, kein Levain.
  - titel: Phytase-Soak
    text: Abgedeckt im Instant Pot, Sous Vide 45 °C, 45 Minuten. Nicht verlängern.
    timer: 2700
  - titel: Abkühlen
    text: Schüssel herausnehmen und bei Raumtemperatur auf etwa 34 °C abkühlen lassen.
    timer: 1080
  - titel: Saltolyse mischen
    text: 10 g Salz, 25 g Vitalkleber, 7 g Psyllium, 50 g Wasser und gegebenenfalls die Ascorbinsäure zugeben, mit dem K-Haken 2 Minuten auf Stufe 1 mischen.
    timer: 120
  - titel: Saltolyse ruhen
    text: Abgedeckt bei Raumtemperatur ruhen lassen.
    timer: 1500
  - titel: Finalmix
    text: 100 g Levain zugeben. Spiralhaken 3 Minuten Stufe 1, 5 Minuten Ruhe, 3 Minuten Stufe 1–2, 5 Minuten Ruhe, 3 Minuten Stufe 2 bis zum dünnen Fenster.
    timer: 1140
  - titel: Teigtemperatur prüfen
    text: Ziel 26–27 °C. Teig mit nasser Teigkarte in einen graduierten Behälter geben, Startvolumen markieren.
  - titel: Erster Coil Fold
    text: Nach 60 Minuten Stockgare einmal mit nasser Teigkarte falten.
    timer: 3600
  - titel: Zweiter Coil Fold
    text: Nach weiteren 90 Minuten zweiter Fold, bei sehr schlaffem Teig später ein dritter.
    timer: 5400
  - titel: Stockgare beenden
    text: Bei pH 4,55–4,65 und 60–70 % Volumenzuwachs, Poke-Test federt langsam zurück.
  - titel: Minimalform
    text: Gärkorb mit Reismehl und Weizenvollkornmehl 1:1 bemehlen, Teig hineingleiten lassen, Naht oben.
  - titel: Kühlretard
    text: Gärkorb im Beutel bei 4 °C 16 Stunden in den Kühlschrank.
    timer: 57600
  - titel: Vorheizen
    text: Pizzastein auf mittlerer Schiene, 250 °C Ober-/Unterhitze mindestens 45 Minuten, Wassertank füllen.
    timer: 2700
  - titel: Einschneiden
    text: Teig kalt auf Backpapier stürzen, einmal etwa 1,5 cm tief im 45°-Winkel einschneiden.
  - titel: Ofentrieb
    text: Einschießen, 250 °C mit vollem Dampf (Stufe 3).
    timer: 720
  - titel: Kruste
    text: Kurz lüften, 220 °C ohne Dampf.
    timer: 1080
  - titel: Durchbacken
    text: 200 °C ohne Dampf bis 98 °C Kerntemperatur, optional 5 Minuten 210 °C Heißluft zum Abschluss.
  - titel: Auskühlen
    text: Auf dem Gitter mindestens 4 Stunden, besser 6, auskühlen lassen.
    timer: 14400
gesichtet: false
---

## Warum so

Die Getreidephytase arbeitet bei 45–55 °C nahe ihrem Optimum; der Soak ist deshalb der einzige warme Schritt und baut Phytat ab, länger würde die Amylase die Krume gummig machen. Gesamthydration etwa 88 % (440 g Wasser inklusive Levain auf 500 g Mehl) – getragen von Chia, Psyllium und Akazie. Ganze Chia bindet langsamer als geschrotete, der Teig ist am Mix schlaffer und festigt sich im 16-h-Retard. Die Gele müssen bei 98 °C Kern vollständig durchwärmt werden und beim Auskühlen setzen, sonst bleibt die Krume gummig.

## Stellschrauben

- Teig zu schlaff oder läuft breit → 10–15 g weniger Wasser, Retard 16 h, Stockgare bei pH 4,6 beenden
- Mehr Öffnung gewünscht → zuerst Chia auf 20 g, dann Hydration +2 % mit längerem Retard, dann Vitalkleber auf 6 %
- Krume gummig → länger auskühlen, Kern sicher 98 °C, Soak nicht über 45 Minuten
- Samen bleiben hart → vollen 16-h-Retard nutzen
- Zu sauer → Stockgare bei pH 4,65 beenden, jüngeren Levain (pH 4,3), Retard ≤ 12 h

## Varianten

- **Ohne Keimmehl:** 50 g mehr Weizenvollkornmehl, Soak auf 50 Minuten, Roggen optional 85 g.
- **Ohne Kühlschrank:** Statt Retard 1,5–2,5 h bei Raumtemperatur bis zum Poke-Test, dann sofort backen – flacherer Ofentrieb.
- **Seltenes Backen:** Bei mehr als 10 Tagen Abstand das zurückgestellte Anstellgut vor dem Kühlen einmal füttern (10 g + 20 g Mehl + 20 g Wasser, 2 h anspringen lassen).
