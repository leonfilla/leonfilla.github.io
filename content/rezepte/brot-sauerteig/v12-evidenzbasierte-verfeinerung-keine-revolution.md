---
titel: Vollkorn-Sauerteigbrot V12
status: aktiv
datum: '2026-04-16'
quelle: {typ: claude, url: 'https://claude.ai/chat/732292ba-174b-4232-ba19-da295ddfc1a8', hinweis: Evidenzbasierte Optimierung eines Vollkorn-Nährstoffbrots}
importiert: true
linie: vollkorn-sauerteig
version: V12
fokus: 'Prozessfeinschliff von V11 bei gleicher Formel: drei Coil Folds statt Dehnen und Falten, Fermentolyse bei höchstens 27 °C und ein drittes Backsegment, in dem die Krume setzt.'
ergebnis: 1 Laib, ca. 720 g (12 Scheiben à 60 g)
zeit: {aktiv: 40, gesamt: 1800}
geraete: [wilfa-probaker, bosch-hng978, apera-ph60f, kernthermometer]
tags: [Vollkorn, Sauerteig, High Protein]
brot:
  teiggewicht: 820
  kerntemperatur: 98
  gare:
  - {phase: Levain, temp: 28, zeit: 6 h, ph: 4.2}
  - {phase: Saltolyse, temp: 26–27, zeit: 45–60 min}
  - {phase: Stockgare, temp: 26, zeit: '4–4,5 h', ph: 4.6}
  - {phase: Anstückgare, temp: 22, zeit: 20–30 min}
  - {phase: Kaltgare, temp: 4, zeit: 14–16 h}
  backprofil:
  - {phase: Vorheizen (Topf), temp: 250, zeit: 45 min}
  - {phase: Spring, temp: 250, dampf: Deckel, zeit: 22 min}
  - {phase: Kruste, temp: 220, dampf: offen, zeit: 20 min}
  - {phase: Krume setzen, temp: 205, dampf: offen, zeit: 10–15 min}
zutaten:
- {gruppe: Levain, name: 'Anstellgut, reif', menge: 12, einheit: g}
- {gruppe: Levain, name: Weizenvollkornmehl, menge: 60, einheit: g, mehl: true}
- {gruppe: Levain, name: Roggenvollkornmehl, menge: 60, einheit: g, mehl: true}
- {gruppe: Levain, name: Wasser, menge: 120, einheit: g, wasser: 1, hinweis: 'lauwarm, ca. 30 °C'}
- {gruppe: Tangzhong, name: Weizenvollkornmehl, menge: 20, einheit: g, mehl: true}
- {gruppe: Tangzhong, name: Wasser, menge: 80, einheit: g, wasser: 1}
- {gruppe: Quellstück, name: 'Leinsamen, geschrotet', menge: 30, einheit: g}
- {gruppe: Quellstück, name: 'Hanfsamen, geschält', menge: 35, einheit: g}
- {gruppe: Quellstück, name: Wasser, menge: 100, einheit: g, wasser: 1}
- {gruppe: Hauptteig, name: Wasser, menge: 253, einheit: g, wasser: 1, hinweis: 29 °C bei 22 °C Küche}
- {gruppe: Hauptteig, name: Jod-Selen-Salz, menge: 9.5, einheit: g}
- {gruppe: Hauptteig, name: Weizenvollkornmehl, menge: 215, einheit: g, mehl: true}
- {gruppe: Hauptteig, name: Roggenvollkornmehl, menge: 50, einheit: g, mehl: true}
- {gruppe: Hauptteig, name: Einkornvollkornmehl, menge: 25, einheit: g, mehl: true}
- {gruppe: Hauptteig, name: Hafervollkornmehl, menge: 25, einheit: g, mehl: true}
- {gruppe: Hauptteig, name: Rotes Linsenmehl, menge: 75, einheit: g, mehl: true}
- {gruppe: Hauptteig, name: 'Kürbiskernmehl, entölt', menge: 25, einheit: g, mehl: true}
- {gruppe: Hauptteig, name: Vitalkleber, menge: 18, einheit: g, mehl: true}
- {gruppe: Hauptteig, name: 'Nährhefe, angereichert', menge: 10, einheit: g}
- {gruppe: Hauptteig, name: Zuckerrübenmelasse, menge: 5, einheit: g}
- {gruppe: Hauptteig, name: 'Flohsamenschalen, ganz', menge: 8, einheit: g}
schritte:
- {titel: Levain ansetzen, text: 'Morgens (ca. 06:00) 12 g Anstellgut, 60 g Weizen-, 60 g Roggenvollkornmehl und 120 g lauwarmes Wasser verrühren und bei 28 °C (Ofen mit Lampe) reifen lassen, bis pH 4,2 und deutlich aufgewölbt.', timer: 21600}
- {titel: Tangzhong kochen, text: '20 g Weizenvollkornmehl und 80 g Wasser unter Rühren auf 65–70 °C erhitzen, bis gelatinös; auf ≤ 30 °C abkühlen lassen.'}
- {titel: Quellstück ansetzen, text: '30 g geschrotete Leinsamen, 35 g Hanfsamen und 100 g Wasser 20 Minuten quellen lassen.', timer: 1200}
- {titel: Salz lösen, text: '253 g Wasser (29 °C) mit 9,5 g Salz vollständig auflösen.'}
- {titel: Saltolyse mischen, text: '215 g Weizen-, 50 g Roggen-, 25 g Einkorn-, 25 g Hafervollkornmehl, 75 g Linsenmehl, 25 g Kürbiskernmehl, 18 g Vitalkleber und 10 g Nährhefe zugeben und grob zu Klumpen mischen.'}
- {titel: Saltolyse ruhen, text: '45–60 Minuten bei 26–27 °C ruhen lassen, nie über 27 °C.', timer: 2700}
- {titel: Einarbeiten, text: 'Levain, 5 g Melasse, Tangzhong, Quellstück und 8 g ganze Flohsamenschalen zugeben.'}
- {titel: Intervallkneten, text: 'Dreimal 3 Minuten kneten, dazwischen insgesamt 5 Minuten Rubaud-Kneten im Behälter mit nasser Hand. Teigtemperatur 25 °C ± 0,5 messen.', timer: 900}
- {titel: Coil Fold 1, text: 'Nach 30 Minuten mit nassen Händen Teig mittig anheben, unterklappen, Behälter 90° drehen und wiederholen.', timer: 1800}
- {titel: Coil Fold 2, text: Nach weiteren 45 Minuten (t = 75 min) identisch wiederholen., timer: 2700}
- {titel: Coil Fold 3, text: 'Bei t = 150 min ein letztes Mal falten, danach ungestört lassen.', timer: 4500}
- {titel: Stockgare beenden, text: 'Bei 26 °C nach insgesamt 4–4,5 Stunden bei pH 4,6 und +70–75 % Volumen beenden.'}
- {titel: Formen, text: Mit einem finalen Coil im Behälter formen und in den bemehlten Gärkorb stürzen (Naht oben).}
- {titel: Anstückgare, text: 20–30 Minuten bei Raumtemperatur stehen lassen., timer: 1500}
- {titel: Kaltgare, text: 14–16 Stunden bei 4 °C kühlen., timer: 54000}
- {titel: Ofen vorheizen, text: Ofen mit Gusseisentopf 45 Minuten auf 250 °C vorheizen., timer: 2700}
- {titel: Einschneiden, text: 'Teigling direkt aus dem Kühlschrank auf Backpapier stürzen und kreuz- oder rautenförmig 0,5–0,7 cm tief mit senkrechter Klinge einschneiden.'}
- {titel: Backen mit Deckel, text: 22 Minuten bei 250 °C mit Deckel backen., timer: 1320}
- {titel: Backen offen, text: Deckel abnehmen und 20 Minuten bei 220 °C backen., timer: 1200}
- {titel: Krume setzen, text: 'Bei 205 °C 10–15 Minuten weiterbacken, bis 98 °C Kerntemperatur.', timer: 720}
- {titel: Auskühlen, text: Mindestens 4 Stunden auf dem Gitter auskühlen lassen. Ziel 715–730 g., timer: 14400}
changelog:
- {version: V12, text: Drei Coil Folds (30/75/150 min) statt Dehnen und Falten}
- {version: V12, text: Fermentolyse 26–27 °C statt 26–28 °C}
- {version: V12, text: Drittes Backsegment 205 °C bis Kern 98 °C; Phase 2 auf 20 min verkürzt}
- {version: V12, text: Leitungswasser ohne Filterung}
---

## Warum so

Coil Folds richten das Gluten in zwei Ebenen aus, verlieren weniger Gas und reißen die Kleie seltener als klassisches Falten. Die typische Sauerteighefe hat ihr Optimum bei etwa 27 °C, darüber legen Proteasen und Amylasen aus Roggen und Linsen zu – daher die Obergrenze. Salz von Anfang an bremst die Proteasen des glutenschwachen Mehlmixes. Die dritte Backphase bei 205 °C setzt die psylliumhaltige Krume vollständig, ohne die Kruste zu verbrennen; Ziel sind 11–13 % Backverlust. Pro 60-g-Scheibe ca. 150 kcal, 7,5 g Protein, 4,8 g Ballaststoffe.

## Stellschrauben

- Backverlust unter 8 % → Phase 1 auf 260 °C, Teigling auf 750 g
- Unterkrume kompakt → Gärkorb weniger bemehlen, Naht oben einsetzen
- Teig zu straff → Tangzhong weglassen, Flohsamen 30 Minuten vorquellen
- Ofentrieb schwach → Levain auf 144 g oder Teigtemperatur 26 °C
- Krume klebrig → Kaltgare auf 12 h verkürzen

## Varianten

- Zweistufiger Levain: 1:2:2 über Nacht bei 22–24 °C, dann 1:2:2 für 3–4 h bei 27–28 °C – mehr Hefe und Aroma
