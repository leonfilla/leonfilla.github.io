---
titel: Vollkorn-Sauerteigbrot V12 – Küchen-Arbeitsdokument
status: aktiv
datum: '2026-04-16'
quelle:
  typ: claude
  url: https://claude.ai/chat/732292ba-174b-4232-ba19-da295ddfc1a8
  hinweis: Evidenzbasierte Optimierung eines Vollkorn-Nährstoffbrots
importiert: true
linie: vollkorn-sauerteig
version: V12
variante: Küchen-Arbeitsdokument
fokus: "Nährstoff-Vollkornbrot aus sechs Mehlen mit Tangzhong, Psyllium-Gel und Lein-Hanf-Quellstück, Saltolyse statt Autolyse und Kneten ohne Handkontakt – Wilfa-Intervalle, Coil Folds mit der Teigkarte, Umkippen in den Gärkorb. Alle Zwischenprodukte sind auf 100 % Verbrauch kalibriert."
ergebnis: 1 Laib, ca. 720 g, ca. 20 Scheiben
zeit: {aktiv: 30, gesamt: 2400}
geraete: [instant-pot-pro-max, wilfa-probaker, bosch-hng978, apera-ph60f, kernthermometer]
tags: [Sauerteig, Vollkorn, High Protein]
changelog:
  - {version: "V12", text: "Hydration korrekt auf Gesamtmehl berechnet (82 %), transparente Wasserbilanz mit 105 g freiem Wasser"}
  - {version: "V12", text: "Saltolyse 30 min statt Autolyse/Fermentolyse"}
  - {version: "V12", text: "Kerntemperatur 98 statt 97 °C wegen der Psyllium-Setzzeit"}
  - {version: "V12", text: "Minimale Teigberührung: Intervallkneten, Coil Folds mit nasser Teigkarte, Umkippen statt Formen"}
  - {version: "V12", text: "Zwischenprodukte exakt auf 100 % Verbrauch kalibriert"}
brot:
  teiggewicht: 820
  kerntemperatur: 98
  gare:
    - {phase: "Anstellgut auffrischen (1:5:5)", temp: 24, zeit: "über Nacht"}
    - {phase: "Levain (Instant Pot, Sous Vide)", temp: 28, zeit: "6–8 h", ph: "4.1–4.3"}
    - {phase: "Saltolyse", temp: "24–26", zeit: "30 min"}
    - {phase: "Stockgare mit 2–3 Coil Folds", zeit: "ca. 6–6,5 h, +70–80 %", ph: "4.3–4.5"}
    - {phase: "Kaltgare im Gärkorb", temp: 4, zeit: "8–12 h"}
  backprofil:
    - {phase: "Vorheizen mit Pizzastein und leerer Wasserwanne", temp: 250, zeit: "mind. 45 min"}
    - {phase: "Ofentrieb", temp: 250, dampf: "voll", zeit: "12 min"}
    - {phase: "Krustenbildung", temp: 220, dampf: "aus, kurz lüften", zeit: "18 min"}
    - {phase: "Krumen-Setzphase", temp: 200, dampf: "aus", zeit: "bis 98 °C Kern, ca. 10–13 min"}
    - {phase: "Crisp Finish (optional)", temp: 210, dampf: "Heißluft", zeit: "5 min"}
zutaten:
  - {gruppe: "Levain", name: "Anstellgut, reif", menge: 42, einheit: "g", hinweis: "am Vorabend 4 g ASG + 20 g Mehl + 20 g Wasser auffrischen"}
  - {gruppe: "Levain", name: "Weizenvollkornmehl", menge: 105, einheit: "g", mehl: true}
  - {gruppe: "Levain", name: "Wasser, 28 °C", menge: 105, einheit: "g", wasser: 1}
  - {gruppe: "Saatenquellstück", name: "Leinsamen, geschrotet", menge: 30, einheit: "g"}
  - {gruppe: "Saatenquellstück", name: "Hanfsamen, ganz", menge: 35, einheit: "g"}
  - {gruppe: "Saatenquellstück", name: "Wasser", menge: 90, einheit: "g", wasser: 1}
  - {gruppe: "Tangzhong", name: "Weizenvollkornmehl", menge: 20, einheit: "g", mehl: true}
  - {gruppe: "Tangzhong", name: "Wasser", menge: 80, einheit: "g", wasser: 1}
  - {gruppe: "Psyllium-Gel", name: "Flohsamenschalen, ganz, hell", menge: 8, einheit: "g"}
  - {gruppe: "Psyllium-Gel", name: "Wasser", menge: 40, einheit: "g", wasser: 1}
  - {gruppe: "Saltolyse", name: "Weizenvollkornmehl", menge: 225, einheit: "g", mehl: true}
  - {gruppe: "Saltolyse", name: "Roggenvollkornmehl", menge: 110, einheit: "g", mehl: true}
  - {gruppe: "Saltolyse", name: "Linsenmehl, grün oder rot", menge: 72, einheit: "g", mehl: true}
  - {gruppe: "Saltolyse", name: "Kürbiskernmehl, entölt", menge: 24, einheit: "g", mehl: true}
  - {gruppe: "Saltolyse", name: "Einkornvollkornmehl", menge: 24, einheit: "g", mehl: true}
  - {gruppe: "Saltolyse", name: "Hafervollkornmehl", menge: 25, einheit: "g", mehl: true}
  - {gruppe: "Saltolyse", name: "Vitalkleber", menge: 12, einheit: "g", mehl: true}
  - {gruppe: "Saltolyse", name: "Wasser, frei", menge: 105, einheit: "g", wasser: 1}
  - {gruppe: "Saltolyse", name: "Salz", menge: 10, einheit: "g"}
  - {gruppe: "Finalmix", name: "Levain", menge: 210, einheit: "g", hinweis: "Rest ca. 50 g als neues Anstellgut"}
  - {gruppe: "Finalmix", name: "Tangzhong, Saatenquellstück, Psyllium-Gel", einheit: "", hinweis: "gesamte Mengen"}
schritte:
  - {titel: "Fr 21:00 – Anstellgut auffrischen", text: "4 g Anstellgut, 20 g Mehl und 20 g Wasser verrühren und bei 24 °C über Nacht stehen lassen."}
  - {titel: "Sa 08:00 – Levain ansetzen", text: "42 g Anstellgut, 105 g Weizenvollkornmehl und 105 g Wasser (28 °C) verrühren und im Instant Pot (Sous Vide, 28 °C) reifen lassen.", timer: 23400}
  - {titel: "Saatenquellstück", text: "30 g geschroteten Lein, 35 g Hanfsamen und 90 g Wasser verrühren und abgedeckt quellen lassen."}
  - {titel: "Tangzhong kochen", text: "20 g Weizenvollkornmehl und 80 g Wasser unter ständigem Rühren auf 72–75 °C erhitzen, bis eine deutliche Spur stehen bleibt; mit Folie direkt auf der Oberfläche bei Raumtemperatur abkühlen, nicht in den Kühlschrank."}
  - {titel: "14:30 – Levain prüfen", text: "Verdoppelt, Float-Test positiv, pH 4,1–4,3. 210 g für den Teig abwiegen, 50 g als neues Anstellgut kühl stellen."}
  - {titel: "Psyllium-Gel", text: "8 g Flohsamenschalen in 40 g Wasser einrieseln, sofort mit der Gabel verrühren und quellen lassen.", timer: 3600}
  - {titel: "15:00 – Saltolyse", text: "480 g Mehlmischung, 12 g Vitalkleber, 105 g Wasser und 10 g Salz im Wilfa 2–3 Minuten auf Stufe 1 mischen, abgedeckt bei 24–26 °C ruhen lassen.", timer: 1800}
  - {titel: "15:30 – Finalmix 1", text: "Levain, Tangzhong, Saatenquellstück und Psyllium-Gel zugeben, 3 Minuten Stufe 1, dann ruhen.", timer: 480}
  - {titel: "Finalmix 2", text: "3 Minuten Stufe 1–2, dann ruhen.", timer: 480}
  - {titel: "Finalmix 3", text: "3 Minuten Stufe 2. Teigtemperatur messen, Ziel 25–26 °C.", timer: 180}
  - {titel: "Umfüllen", text: "Mit befeuchteter Teigkarte in einen graduierten Behälter gleiten lassen und das Startvolumen markieren."}
  - {titel: "16:50 – Coil Fold 1", text: "Mit befeuchteter Teigkarte unter eine Seite fahren, anheben, auf sich selbst falten lassen, Vierteldrehung, wiederholen (ca. 20 Sekunden).", timer: 3600}
  - {titel: "18:20 – Coil Fold 2", text: "Wie Fold 1; ein dritter Fold um 19:50 nur, wenn der Teig noch schlaff ist.", timer: 5400}
  - {titel: "22:00 – Stockgare beenden", text: "Bei +70–80 % Volumen, pH 4,3–4,5 und langsam zurückfederndem Fingertest."}
  - {titel: "Umkippen", text: "Gärkorb mit Reismehl und Weizenvollkorn (1:1) bemehlen, Behälter darüber umdrehen und langsam absetzen – nicht nachformen."}
  - {titel: "Kaltgare", text: "Gärkorb im Beutel bei 4 °C in den Kühlschrank stellen.", timer: 39600}
  - {titel: "So 09:00 – Vorheizen", text: "Pizzastein und leere Wasserwanne mindestens 45 Minuten bei 250 °C vorheizen.", timer: 2700}
  - {titel: "Einschneiden", text: "Kalten Teig auf Backpapier stürzen und einmal ca. 1,5 cm tief im 45°-Winkel einschneiden."}
  - {titel: "Ofentrieb", text: "Einschießen und 12 Minuten bei 250 °C mit voller Dampfzufuhr backen.", timer: 720}
  - {titel: "Krustenbildung", text: "Dampf aus, Ofen kurz öffnen, 18 Minuten bei 220 °C; bräunt es zu früh, auf 210 °C.", timer: 1080}
  - {titel: "Krumen-Setzphase", text: "Auf 200 °C, Kernfühler setzen und bis 98 °C backen.", timer: 690}
  - {titel: "Crisp Finish", text: "Optional 5 Minuten bei 210 °C Heißluft, nur wenn die Kruste weich wirkt.", timer: 300}
  - {titel: "Auskühlen", text: "Mindestens 4, besser 6 Stunden auf dem Gitter auskühlen lassen, dann wiegen (Ziel 11–13 % Backverlust).", timer: 14400}
---

## Warum so

Bei 53 % Nicht-Weizen-Mehlen bringen Roggen und Linse eigene Proteasen und α-Amylase mit; Salz von Anfang an (Saltolyse) strafft das verdünnte Gluten und hemmt diese Enzyme. Tangzhong bindet Wasser in der Stärke, Psyllium außerhalb – zwei getrennte Wasserräume, die sich ergänzen; Lein ist eher aus Nährwertgründen dabei. Das Psyllium-Arabinoxylan wird erst um 98 °C stabil und setzt sich beim Abkühlen, daher höhere Kerntemperatur und mindestens 4 Stunden Auskühlen. Pro Laib ca. 9,5 g ALA aus Lein und Hanf.

## Stellschrauben

- Bräunt zu früh in Phase 2 → 210 statt 220 °C
- Backverlust unter 10 % → zu viel gebundenes Wasser, Tangzhong-Anteil prüfen
- Kruste weich → optionales Crisp Finish; über 70 % Hydration drohen dabei Trocknungsrisse

## Varianten

- **Ohne Coil Folds:** Saltolyse 45 Minuten, Intervallkneten 3 × 4 statt 3 × 3 Minuten, nur Umkippen – Krume tendenziell flacher.
- **Offene Tests für V13:** ein Lauf ohne Lein-Mucilage (ganze Leinsamen), ein Lauf mit 2,5 % Tangzhong und mehr freiem Wasser.
