---
titel: Vollkorn-Sauerteigbrot V9
status: aktiv
datum: '2026-04-16'
quelle: {typ: claude, url: 'https://claude.ai/chat/732292ba-174b-4232-ba19-da295ddfc1a8', hinweis: Evidenzbasierte Optimierung eines Vollkorn-Nährstoffbrots}
importiert: true
linie: vollkorn-sauerteig
version: V9
fokus: 'Korrigierte V8: mehr Vitalkleber, weniger Linsenmehl, Tangzhong ohne Salz bei 72–75 °C und Psyllium als Gel. Stockgare auf den realistisch erreichbaren pH 3,9–4,0, danach 18 h Kaltgare.'
ergebnis: 1 freigeschobener Laib, ca. 950 g Teig
zeit: {aktiv: 40, gesamt: 2520}
geraete: [wilfa-probaker, instant-pot-pro-max, bosch-hng978, apera-ph60f, kernthermometer]
tags: [Vollkorn, Sauerteig, High Protein]
brot:
  kerntemperatur: 96–97
  gare:
  - {phase: Levain, temp: 28, zeit: 6 h, ph: '4,2–4,3'}
  - {phase: Levain kalt, temp: 4, zeit: 10–14 h}
  - {phase: Autolyse, temp: 22, zeit: 60 min}
  - {phase: Stockgare, temp: 28, zeit: '3,5–4 h', ph: '3,9–4,0'}
  - {phase: Kaltgare, temp: 4, zeit: 18 h}
  backprofil:
  - {phase: Vorheizen (Stein), temp: 250, zeit: 60 min}
  - {phase: Ofentrieb, temp: 240, dampf: Stufe 3, zeit: 15 min}
  - {phase: Hauptphase, temp: 210, dampf: aus, zeit: 30 min}
  - {phase: Finish (optional), temp: 200, dampf: Tür 1 cm offen, zeit: 5 min}
zutaten:
- {gruppe: Levain, name: 'Anstellgut, reif', menge: 12, einheit: g}
- {gruppe: Levain, name: Weizenvollkornmehl, menge: 60, einheit: g, mehl: true}
- {gruppe: Levain, name: Roggenvollkornmehl, menge: 60, einheit: g, mehl: true}
- {gruppe: Levain, name: Wasser, menge: 120, einheit: g, wasser: 1, hinweis: '210 g Levain in den Teig, 50 g als neues Anstellgut'}
- {gruppe: Tangzhong, name: Weizenvollkornmehl, menge: 35, einheit: g, mehl: true}
- {gruppe: Tangzhong, name: Wasser, menge: 140, einheit: g, wasser: 1, hinweis: ohne Salz}
- {gruppe: Quellstück, name: 'Leinsamen, gemahlen', menge: 30, einheit: g}
- {gruppe: Quellstück, name: 'Hanfsamen, geschält', menge: 25, einheit: g}
- {gruppe: Quellstück, name: Wasser, menge: 85, einheit: g, wasser: 1}
- {gruppe: Quellstück, name: 'Flohsamenschalen, gemahlen', menge: 8, einheit: g, hinweis: Psyllium-Gel}
- {gruppe: Quellstück, name: Wasser, menge: 40, einheit: g, wasser: 1, hinweis: für das Psyllium-Gel}
- {gruppe: Hauptteig, name: Weizenvollkornmehl, menge: 275, einheit: g, mehl: true}
- {gruppe: Hauptteig, name: Roggenvollkornmehl, menge: 50, einheit: g, mehl: true}
- {gruppe: Hauptteig, name: Einkornvollkornmehl, menge: 25, einheit: g, mehl: true}
- {gruppe: Hauptteig, name: Hafervollkornmehl, menge: 25, einheit: g, mehl: true}
- {gruppe: Hauptteig, name: 'Rotes Linsenmehl, grob (>200 µm)', menge: 60, einheit: g, mehl: true}
- {gruppe: Hauptteig, name: Kürbiskernmehl, menge: 25, einheit: g, mehl: true}
- {gruppe: Hauptteig, name: Vitalkleber, menge: 20, einheit: g, mehl: true}
- {gruppe: Hauptteig, name: Amaranth-Vollkornmehl, menge: 3, einheit: g, mehl: true, hinweis: optional}
- {gruppe: Hauptteig, name: Wasser, menge: 35, einheit: g, wasser: 1}
- {gruppe: Hauptteig, name: Salz, menge: 10.5, einheit: g}
- {gruppe: Hauptteig, name: 'Nährhefe, angereichert', menge: 10, einheit: g}
- {gruppe: Hauptteig, name: Blackstrap-Melasse, menge: 10, einheit: g}
schritte:
- {titel: Tangzhong kochen, text: 'Vortag 17:00: 35 g Weizenvollkornmehl in 140 g Wasser unter Rühren auf 72–75 °C erhitzen, bis die Masse puddingartig-transluzent ist.', timer: 180}
- {titel: Tangzhong abkühlen, text: Auf handwarm (≤ 30 °C) abkühlen lassen.}
- {titel: Quellstück ansetzen, text: '30 g gemahlene Leinsamen, 25 g Hanfsamen und 85 g Wasser mischen und abgedeckt mindestens 1 Stunde quellen lassen.', timer: 3600}
- {titel: Levain ansetzen, text: '12 g Anstellgut, 60 g Weizenvollkornmehl, 60 g Roggenvollkornmehl und 120 g Wasser verrühren und im Instant Pot bei 28 °C reifen lassen.', timer: 21600}
- {titel: Levain prüfen und kühlen, text: 'Gegen 23:00 pH messen. Bei 4,2–4,3 in den Kühlschrank stellen, über 4,4 noch 30–60 Minuten warm lassen.'}
- {titel: Anstellgut abzweigen, text: 'Backtag 08:00: 50 g Levain als neues Anstellgut abfüllen und kühlen.'}
- {titel: Psyllium-Gel ansetzen, text: 8 g gemahlene Flohsamenschalen mit 40 g Wasser anrühren und 10 Minuten quellen lassen., timer: 600}
- {titel: Autolyse mischen, text: '275 g Weizen-, 50 g Roggen-, 25 g Einkorn-, 25 g Hafervollkornmehl, 60 g Linsenmehl, 25 g Kürbiskernmehl, 20 g Vitalkleber und 3 g Amaranthmehl in der Wilfa-Schüssel mischen. Tangzhong, Quellstück, Psyllium-Gel und 35 g Wasser zugeben, ohne Salz und Levain 3 Minuten auf Stufe 1 mischen.', timer: 180}
- {titel: Autolyse ruhen, text: Abgedeckt 60 Minuten bei Raumtemperatur stehen lassen., timer: 3600}
- {titel: Einarbeiten, text: '210 g Levain, 10,5 g Salz, 10 g Nährhefe und 10 g Melasse zugeben und 4 Minuten auf Stufe 1 kneten.', timer: 240}
- {titel: Auskneten, text: '6 Minuten auf Stufe 2 kneten, bis der Fenstertest annähernd gelingt. Teigtemperatur 26–28 °C.', timer: 360}
- {titel: Stockgare, text: 'Teig in einen geölten Behälter geben und im Instant Pot bei 28 °C etwa 4 Stunden gehen lassen – bis +50–70 % Volumen, pH 3,9–4,0 und Delle federt langsam zurück.', timer: 14400}
- {titel: Coil Fold (optional), text: 'Nach etwa 45 Minuten einmal einen Coil Fold geben, nur wenn der Teig sehr schlaff wirkt.'}
- {titel: Einschlagen, text: 'Teig mit nasser Teigkarte in den mit Reismehl bemehlten Gärkorb einschlagen – viermal falten (N, S, W, O), umdrehen, Naht unten.'}
- {titel: Kaltgare, text: Gärkorb 18 Stunden bei 4 °C in den Kühlschrank stellen., timer: 64800}
- {titel: Ofen vorheizen, text: Pizzastein einlegen und den Ofen 60 Minuten auf 250 °C aufheizen., timer: 3600}
- {titel: Einschießen, text: 'Teigling direkt aus dem Kühlschrank auf den Schieber stürzen, einmal tief einschneiden und einschießen. Ofen auf 240 °C stellen, Dampf Stufe 3.'}
- {titel: Ofentrieb, text: 15 Minuten bei 240 °C mit Dampf backen., timer: 900}
- {titel: Hauptphase, text: Dampf ablassen und 30 Minuten bei 210 °C backen., timer: 1800}
- {titel: Finish, text: 'Ist die Kruste noch hell, 5 Minuten bei 200 °C mit 1 cm geöffneter Tür nachbacken. Fertig bei 96–97 °C Kerntemperatur.', timer: 300}
- {titel: Auskühlen, text: Mindestens 2 Stunden auf einem Gitter auskühlen lassen., timer: 7200}
changelog:
- {version: V9, text: 'Rotes Linsenmehl 75 → 60 g, Vitalkleber 12 → 20 g'}
- {version: V9, text: 'Hafervollkorn 25 g neu, Amaranth 3 g optional'}
- {version: V9, text: Flohsamen 5 g ganz → 8 g gemahlen als Gel}
- {version: V9, text: Hydratation 85 → 82 % (420 g Wasser)}
- {version: V9, text: 'Tangzhong ohne Salz, 72–75 °C statt 65 °C; Salz erst nach der Autolyse'}
- {version: V9, text: 'Levain in einer Portion; Stockgare-Ziel pH 3,9–4,0 statt 4,5–4,8'}
- {version: V9, text: 'Stein 60 min bei 250 °C, Hauptphase 30 min, Kern 96–97 °C'}
---

## Warum so

Ein Hauptteig, der mit pH ~4,1 startet, kann nicht auf pH 4,5 enden – deshalb liegt der Stockgare-Endpunkt bei 3,9–4,0. Salz hebt die Verkleisterungstemperatur der Stärke, und erst über ~72 °C verkleistert Weizenstärke weitgehend; daher Tangzhong salzfrei und heißer. 4 % Vitalkleber gleichen die rund 26 % glutenfreien Mehle aus, gemahlenes Psyllium quillt im Gel vollständig und stützt den freigeschobenen Laib. Ohne Formgebung läuft ein Laib auf dem Stein breit – die 30-Sekunden-Faltung gibt die nötige Oberflächenspannung. Gargrad zusätzlich über 11–13 % Gewichtsverlust prüfen.

## Stellschrauben

- Teig sehr schlaff → ein Coil Fold nach 45 Minuten
- Kruste dunkel, Kern erreicht → Finish weglassen
- Mehr Phytatabbau gewünscht → Stockgare auf 5 Stunden verlängern
- Krume zu dicht → Wasser hälftig durch sehr weiches Mineralwasser ersetzen
