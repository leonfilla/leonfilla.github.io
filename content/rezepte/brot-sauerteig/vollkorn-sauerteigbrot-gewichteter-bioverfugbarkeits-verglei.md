---
titel: Vollkorn-Sauerteigbrot V13
status: aktiv
datum: '2026-05-21'
quelle:
  typ: claude
  url: https://claude.ai/chat/1f1baaf8-2a5f-4084-89e7-3cc6e33c3012
  hinweis: Neues Brotrezept nach Anforderungen
importiert: true
linie: vollkorn-sauerteig
version: V13
fokus: "Synthese aus V9 und V12, gewichtet auf Mineral-Bioverfügbarkeit: Weizen, gekeimter Weizen, Roggen und Hafer, salzfreies Phytase-Soak bei 45–48 °C, danach Salzruhe und Intervallkneten. Linsen, Kürbiskernmehl, Lein, Psyllium und Tangzhong sind gestrichen."
ergebnis: 1 Laib, ca. 960 g Teig
zeit: {aktiv: 25, gesamt: 1560}
geraete: [instant-pot-pro-max, wilfa-probaker, bosch-hng978, apera-ph60f, kernthermometer]
tags: [Sauerteig, Vollkorn]
changelog:
  - {version: "V13", text: "Neu: 10 % gekeimtes Weizenvollkorn, optional ca. 100 ppm Ascorbinsäure"}
  - {version: "V13", text: "Gestrichen gegenüber V8/V12: Linsenmehl, Kürbiskernmehl, Lein, Psyllium, Tangzhong, Einkorn, Melasse, Hefeflocken"}
  - {version: "V13", text: "Roggen von 23 auf 15 %, Vitalkleber von 2,34 auf 4 %, Hanf 5 %"}
  - {version: "V13", text: "Phytase-Soak bei 45–48 °C vor kurzer Salzruhe statt Saltolyse allein; Kerntemperatur 97 statt 98 °C"}
brot:
  teiggewicht: 960
  kerntemperatur: 97
  gare:
    - {phase: "Levain", temp: 28, zeit: "bis Float-Test", ph: "4.1–4.3"}
    - {phase: "Phytase-Soak (salzfrei, Instant Pot)", temp: "45–48", zeit: "35–40 min", ph: "ca. 6"}
    - {phase: "Salzruhe", temp: "Raumtemperatur", zeit: "20 min"}
    - {phase: "Stockgare mit 2 Coil Folds", temp: 28, zeit: "3,5–4,5 h, +60–70 %", ph: "4.55–4.65"}
    - {phase: "Kaltgare im Gärkorb", temp: 4, zeit: "12–16 h"}
  backprofil:
    - {phase: "Vorheizen mit Pizzastein", temp: 250, zeit: "mind. 45 min"}
    - {phase: "Ofentrieb", temp: 250, dampf: "Stufe 3", zeit: "12–15 min"}
    - {phase: "Kruste", temp: 220, dampf: "aus, kurz lüften", zeit: "18 min"}
    - {phase: "Krumensetzung", temp: 200, dampf: "aus", zeit: "bis 97 °C Kern"}
    - {phase: "Crisp Finish (optional)", temp: 210, dampf: "Heißluft", zeit: "5 min"}
zutaten:
  - {gruppe: "Levain", name: "Anstellgut", menge: 10, einheit: "g"}
  - {gruppe: "Levain", name: "Weizenvollkornmehl", menge: 50, einheit: "g", mehl: true, hinweis: "+ Puffer, insgesamt ca. 30 g mehr Levain ansetzen"}
  - {gruppe: "Levain", name: "Wasser, 28 °C", menge: 50, einheit: "g", wasser: 1}
  - {gruppe: "Phytase-Soak", name: "Weizenvollkornmehl, backstark, fein", menge: 325, einheit: "g", mehl: true}
  - {gruppe: "Phytase-Soak", name: "Gekeimtes Weizenvollkornmehl", menge: 50, einheit: "g", mehl: true}
  - {gruppe: "Phytase-Soak", name: "Roggenvollkornmehl, fein", menge: 75, einheit: "g", mehl: true}
  - {gruppe: "Phytase-Soak", name: "Hafervollkornmehl, fein", menge: 50, einheit: "g", mehl: true}
  - {gruppe: "Phytase-Soak", name: "Wasser", menge: 300, einheit: "g", wasser: 1}
  - {gruppe: "Salzruhe", name: "Salz", menge: 10, einheit: "g"}
  - {gruppe: "Salzruhe", name: "Ascorbinsäure", menge: 0.05, einheit: "g", hinweis: "optional, ca. 100 ppm"}
  - {gruppe: "Salzruhe", name: "Vitalkleber", menge: 20, einheit: "g"}
  - {gruppe: "Salzruhe", name: "Wasser, kühl", menge: 30, einheit: "g", wasser: 1}
  - {gruppe: "Finalmix", name: "Levain, kalt", menge: 100, einheit: "g"}
  - {gruppe: "Finalmix", name: "Hanfsamen, geschält", menge: 25, einheit: "g"}
  - {gruppe: "Finalmix", name: "Wasser", menge: 10, einheit: "g", wasser: 1}
schritte:
  - {titel: "Levain ansetzen", text: "10 g Anstellgut, 50 g Weizenvollkornmehl und 50 g Wasser (28 °C) plus ca. 30 g Puffer ansetzen und bei 28 °C bis pH 4,1–4,3 bzw. Float-Test reifen lassen. 100 g verwenden, Rest als neues Anstellgut."}
  - {titel: "Soak mischen", text: "325 g Weizenvollkorn, 50 g Keimmehl, 75 g Roggen, 50 g Hafer und 300 g Wasser mit dem K-Haken 90 Sekunden homogenisieren – ohne Salz, Vitalkleber, Levain und Hanf."}
  - {titel: "Phytase-Soak", text: "Im Instant Pot bei 45–48 °C halten.", timer: 2250}
  - {titel: "Salzruhe", text: "10 g Salz, optional Ascorbinsäure, 20 g Vitalkleber und 30 g kühles Wasser zugeben, 2 Minuten Stufe 1, abgedeckt ruhen lassen.", timer: 1200}
  - {titel: "Finalmix 1", text: "100 g kalten Levain, 25 g Hanf und 10 g Wasser zugeben, mit dem Spiralhaken 3 Minuten Stufe 1, dann ruhen.", timer: 480}
  - {titel: "Finalmix 2", text: "3 Minuten Stufe 1–2, dann ruhen.", timer: 480}
  - {titel: "Finalmix 3", text: "3 Minuten Stufe 2 bis zum Fenstertest. Teigendtemperatur 27–28 °C.", timer: 180}
  - {titel: "Stockgare", text: "Bei 28 °C im Instant Pot gehen lassen.", timer: 3600}
  - {titel: "Coil Fold 1", text: "Nach 60 Minuten Coil Fold mit befeuchteter Teigkarte (ca. 20 Sekunden).", timer: 5400}
  - {titel: "Coil Fold 2", text: "Nach 150 Minuten zweiter Coil Fold; dann bis pH 4,55–4,65 und +60–70 % Volumen weitergehen lassen.", timer: 3600}
  - {titel: "Umkippen", text: "Behälter über dem bemehlten Gärkorb umkippen, Naht oben, nicht nachformen."}
  - {titel: "Kaltgare", text: "Im Beutel bei 4 °C 12–16 Stunden kühlen.", timer: 50400}
  - {titel: "Vorheizen", text: "Pizzastein mindestens 45 Minuten bei 250 °C vorheizen.", timer: 2700}
  - {titel: "Einschneiden", text: "Teig kalt stürzen und einmal einschneiden."}
  - {titel: "Ofentrieb", text: "250 °C mit Dampf Stufe 3.", timer: 780}
  - {titel: "Kruste", text: "Dampf aus, kurz lüften, 18 Minuten bei 220 °C.", timer: 1080}
  - {titel: "Krumensetzung", text: "Bei 200 °C bis 97 °C Kerntemperatur; optional 5 Minuten Crisp Finish bei 210 °C Heißluft."}
  - {titel: "Auskühlen", text: "Mindestens 3 Stunden auf dem Rost auskühlen lassen.", timer: 10800}
---

## Warum so

Beim nativen pH um 6 und 45–48 °C ist die Getreidephytase hoch aktiv, während die Roggen-Aspartatproteasen (Optimum pH 3,5) ruhen – so gibt es V9s Phytatabbau ohne V12s Glutenrisiko. Gekeimtes Weizenvollkorn baut Phytat vorab ab und hebt die Phytaseaktivität der ganzen Charge. Die Stockgare endet bei pH 4,6: mild und noch über der Schwelle, ab der Proteasen das Gluten angreifen. Linsen, Kürbiskernmehl und Lein bringen viel eigenes Phytat und verdünnen das Gluten; Hafer-β-Glucan übernimmt die Rolle der löslichen Faser. Erwartet: ca. 88–92 % Phytatabbau, GI um 52–54.

## Stellschrauben

- Teig zu fest (Hafer und Keimmehl binden) → 10–15 g Wasser mehr
- Teigtemperatur zu hoch → kühleres Wasser, kalter Levain
- Mehr Eisenaufnahme → Vitamin-C-reicher Belag (Paprika, Tomate, Zitrone), nicht Ascorbinsäure im Teig
