---
titel: Vollkorn-Sauerteigbrot V14 – Nährstoff-maximiert
status: archiv
datum: '2026-05-21'
quelle:
  typ: claude
  url: https://claude.ai/chat/1f1baaf8-2a5f-4084-89e7-3cc6e33c3012
  hinweis: Neues Brotrezept nach Anforderungen
importiert: true
linie: vollkorn-sauerteig
version: V14
variante: Nährstoff-maximiert
fokus: "V13 mit maximalen Ballaststoffen, Präbiotika, Omega-3 und Polyphenolen – Geschmack zählt nicht, Krume, Kruste und Biss schon. Chia, wenig Lein, Psyllium und Inulin kommen dazu, die Hydration steigt auf ca. 84 %."
ergebnis: 1 Laib
geraete: [instant-pot-pro-max, wilfa-probaker, bosch-hng978, apera-ph60f, kernthermometer]
tags: [Sauerteig, Vollkorn]
changelog:
  - {version: "V14", text: "Neu: 20 g Chia und 15 g Lein (geschrotet), 12 g Psyllium, 10 g Inulin oder Akazienfaser, optional 8–10 g Nährhefe und bis 15 g Kakao"}
  - {version: "V14", text: "Weizenvollkorn 325 → 315 g, Roggen 75 → 85 g, Vitalkleber 20 → 24 g, Hanf 25 → 20 g"}
  - {version: "V14", text: "Wasser ca. 420 statt 390 g; Soak 45 statt 35–40 min; Kerntemperatur wieder 98 °C, Auskühlen mindestens 4 h"}
brot:
  kerntemperatur: 98
  gare:
    - {phase: "Levain", temp: 28, ph: "4.1–4.3"}
    - {phase: "Phytase-Soak (salzfrei)", temp: "45–48", zeit: "45 min"}
    - {phase: "Salzruhe", zeit: "20 min"}
    - {phase: "Stockgare mit 2 Coil Folds", temp: 28, zeit: "+60–70 %", ph: "4.55–4.65"}
    - {phase: "Kaltgare im Gärkorb", temp: 4, zeit: "12–16 h"}
  backprofil:
    - {phase: "Vorheizen mit Pizzastein", temp: 250, zeit: "mind. 45 min"}
    - {phase: "Ofentrieb", temp: 250, dampf: "Stufe 3", zeit: "12–15 min"}
    - {phase: "Kruste", temp: 220, dampf: "aus", zeit: "18 min"}
    - {phase: "Krumensetzung", temp: 200, dampf: "aus", zeit: "bis 98 °C Kern"}
    - {phase: "Crisp Finish (optional)", temp: 210, dampf: "Heißluft", zeit: "5 min"}
zutaten:
  - {gruppe: "Levain", name: "Anstellgut", menge: 10, einheit: "g"}
  - {gruppe: "Levain", name: "Weizenvollkornmehl", menge: 50, einheit: "g", mehl: true}
  - {gruppe: "Levain", name: "Wasser, 28 °C", menge: 50, einheit: "g", wasser: 1}
  - {gruppe: "Phytase-Soak", name: "Weizenvollkornmehl, backstark, fein", menge: 315, einheit: "g", mehl: true}
  - {gruppe: "Phytase-Soak", name: "Gekeimtes Weizenvollkornmehl", menge: 50, einheit: "g", mehl: true}
  - {gruppe: "Phytase-Soak", name: "Roggenvollkornmehl, fein", menge: 85, einheit: "g", mehl: true}
  - {gruppe: "Phytase-Soak", name: "Hafervollkornmehl, fein", menge: 50, einheit: "g", mehl: true}
  - {gruppe: "Phytase-Soak", name: "Psylliumschalen", menge: 12, einheit: "g"}
  - {gruppe: "Phytase-Soak", name: "Inulin oder Akazienfaser", menge: 10, einheit: "g"}
  - {gruppe: "Phytase-Soak", name: "Kakao, entölt, cadmiumarm", menge: 15, einheit: "g", hinweis: "optional, 0–15 g"}
  - {gruppe: "Phytase-Soak", name: "Wasser", menge: 370, einheit: "g", wasser: 1, hinweis: "gesamt ohne Levain; Aufteilung wie V13 auf Soak, Salzruhe und Finalmix"}
  - {gruppe: "Salzruhe", name: "Salz", menge: 10, einheit: "g"}
  - {gruppe: "Salzruhe", name: "Vitalkleber", menge: 24, einheit: "g"}
  - {gruppe: "Salzruhe", name: "Ascorbinsäure", menge: 0.05, einheit: "g", hinweis: "optional"}
  - {gruppe: "Finalmix", name: "Levain", menge: 100, einheit: "g"}
  - {gruppe: "Finalmix", name: "Hanfsamen, geschält", menge: 20, einheit: "g"}
  - {gruppe: "Finalmix", name: "Chia, geschrotet", menge: 20, einheit: "g"}
  - {gruppe: "Finalmix", name: "Leinsamen, geschrotet", menge: 15, einheit: "g"}
  - {gruppe: "Finalmix", name: "Nährhefe, B12-angereichert", menge: 10, einheit: "g", hinweis: "optional, höchstens 10 g"}
schritte:
  - {titel: "Levain ansetzen", text: "10 g Anstellgut, 50 g Weizenvollkornmehl und 50 g Wasser (28 °C) bis pH 4,1–4,3 reifen lassen."}
  - {titel: "Soak mischen", text: "Getreidemehle, 12 g Psyllium, 10 g Inulin und ggf. Kakao trocken mischen, dann das Soak-Wasser einrühren – ohne Salz, Vitalkleber und Levain."}
  - {titel: "Phytase-Soak", text: "Im Instant Pot bei 45–48 °C halten.", timer: 2700}
  - {titel: "Salzruhe", text: "10 g Salz, 24 g Vitalkleber und ggf. Ascorbinsäure zugeben, kurz mischen, ruhen lassen.", timer: 1200}
  - {titel: "Finalmix", text: "100 g Levain, 20 g Hanf, 20 g Chia, 15 g Lein und ggf. Nährhefe zugeben und im Intervall bis zum Fenstertest kneten (3 Min Stufe 1 – 5 Min Pause – 3 Min Stufe 1–2 – 5 Min Pause – 3 Min Stufe 2). Teigendtemperatur 27–28 °C."}
  - {titel: "Stockgare", text: "Bei 28 °C, Coil Folds mit befeuchteter Teigkarte nach 60 und 150 Minuten, bis pH 4,55–4,65 und +60–70 % Volumen."}
  - {titel: "Umkippen", text: "In den bemehlten Gärkorb umkippen, nicht nachformen."}
  - {titel: "Kaltgare", text: "Bei 4 °C 12–16 Stunden.", timer: 50400}
  - {titel: "Backen", text: "Wie V13: 250 °C mit Dampf Stufe 3 12–15 Minuten, 220 °C ohne Dampf 18 Minuten, dann 200 °C bis 98 °C Kern; optional Crisp Finish."}
  - {titel: "Auskühlen", text: "Mindestens 4 Stunden auskühlen lassen.", timer: 14400}
---

## Warum so

Chia ist der bessere Omega-3-Träger – etwa ein Drittel des Phytats von Lein; Lein bleibt klein dosiert nur für die Lignane. Psyllium wird hier tragend: Es bindet die höhere Faser- und Wasserlast, sodass 84 % freigeschoben stehen. Mehr Roggen und 45 Minuten Soak puffern das zusätzliche Saatenphytat (Abbau weiter ca. 88 %). Die Gele aus Psyllium, Chia und Lein sind thermoreversibel, daher 98 °C Kern und lange Auskühlzeit. Kakao ist der stärkste Eisenhemmer – nur mit Vitamin-C-Belag oder ganz weglassen.

## Stellschrauben

- Krume gummig → länger auskühlen, dann Inulin und Lein reduzieren
- Laib läuft breit → Hydration um 4–6 % senken, Kaltgare verlängern
- Krume zu dicht → Vitalkleber 5,5 %, Psyllium als vorgequollenes Gel statt trocken
- Nährhefe nicht über 10 g – das Produkt ist stark mit Zink und B6 angereichert

## Varianten

- **Gestaffelt einführen:** 1. V13 + Psyllium + 84 % · 2. + Chia und Lein, Soak 45 min · 3. + Inulin (und Nährhefe) · 4. optional Kakao 3 %.
