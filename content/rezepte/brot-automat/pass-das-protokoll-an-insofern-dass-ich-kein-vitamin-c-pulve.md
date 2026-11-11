---
titel: Weizen-Vollkorn-Sauerteigbrot mit Zitronensaft
status: archiv
datum: '2026-02-02'
quelle:
  typ: gemini
  url: https://gemini.google.com/app/ff35960758945a73
  hinweis: Bewerte die reine Knetfunktion von Sauerteigen des Panasonic SD-YR2540
importiert: true
linie: protokoll-weizen-vollkorn-sauerteigbrot-high-hydra-4224d
variante: Zitronensaft statt Vitamin C
fokus: Weizenmischbrot mit sehr hohem Vollkornanteil, im Automaten geknetet und frei auf dem Pizzastein gebacken. Zitronensaft ersetzt Vitamin-C-Pulver, 80 g Type 550 sind das Minimum für eine stabile Krume.
ergebnis: 1 Laib
geraete: [panasonic-sd-yr2540, bosch-hng978]
tags: [Sauerteig, Vollkorn]
brot:
  programm: Menü 21 – Vollkorn (Teig), nur zum Kneten
  gare:
    - {phase: "Vorteig", temp: "Raumtemperatur", zeit: "4–6 h, bis verdoppelt"}
    - {phase: "Autolyse", zeit: "45–60 min"}
    - {phase: "Stockgare mit 3 Coil Folds", zeit: "ca. 4 h ab Knetende"}
    - {phase: "Kaltgare im Gärkorb", temp: 5, zeit: "12–18 h"}
  backprofil:
    - {phase: "Vorheizen mit Pizzastein", temp: 250, zeit: "mind. 45 min"}
    - {phase: "Anbacken", temp: 250, dampf: "Dampfstoß intensiv", zeit: "0–10 min"}
    - {phase: "Ausbacken", temp: 210, dampf: "kein", zeit: "10–40 min"}
    - {phase: "Rösche", temp: 210, dampf: "aktive Entfeuchtung", zeit: "40–50 min"}
zutaten:
  - {gruppe: "Vorteig", name: "Anstellgut", menge: 30, einheit: "g", hinweis: "aus dem Kühlschrank"}
  - {gruppe: "Vorteig", name: "Weizenvollkornmehl", menge: 35, einheit: "g", mehl: true}
  - {gruppe: "Vorteig", name: "Wasser", menge: 35, einheit: "g", wasser: 1, hinweis: "lauwarm"}
  - {gruppe: "Hauptteig", name: "Weizenvollkornmehl", menge: 370, einheit: "g", mehl: true}
  - {gruppe: "Hauptteig", name: "Weizenmehl 550", menge: 80, einheit: "g", mehl: true}
  - {gruppe: "Hauptteig", name: "Wasser", menge: 305, einheit: "g", wasser: 1, hinweis: "kalt"}
  - {gruppe: "Hauptteig", name: "Zitronensaft", menge: 15, einheit: "g", wasser: 0.9, hinweis: "frisch gepresst"}
  - {gruppe: "Hauptteig", name: "Salz", menge: 10, einheit: "g"}
schritte:
  - {titel: "Vorteig ansetzen", text: "30 g Anstellgut, 35 g Weizenvollkornmehl und 35 g lauwarmes Wasser im Glas mischen."}
  - {titel: "Vorteig reifen lassen", text: "Bei Raumtemperatur stehen lassen, bis er sich verdoppelt hat.", timer: 18000}
  - {titel: "Autolyse mischen", text: "Roggen-Knethaken einsetzen. 370 g Weizenvollkornmehl, 80 g Weizenmehl 550, 305 g kaltes Wasser und 15 g Zitronensaft in den Behälter geben, Menü 21 starten und 2 Minuten mischen.", timer: 120}
  - {titel: "Quellen lassen", text: "Maschine stoppen und mit geschlossenem Deckel ruhen lassen.", timer: 3000}
  - {titel: "Kneten", text: "Vorteig und 10 g Salz zugeben, Menü 21 starten und nach 8 Minuten stoppen. Löst sich der Teig noch nicht vom Rand, max. 2 Minuten verlängern – insgesamt höchstens 12 Minuten.", timer: 480}
  - {titel: "Entnehmen", text: "Teig sofort in eine leicht geölte, eckige Wanne geben."}
  - {titel: "Coil Folds", text: "Dreimal im Abstand von 45 Minuten falten: Teig mittig anheben, Enden unterklappen lassen.", timer: 2700}
  - {titel: "Stockgare beenden", text: "Ruhen lassen, bis der Teig luftig ist und deutlich an Volumen zugenommen hat (ca. 4 Stunden ab Knetende)."}
  - {titel: "Formen", text: "Teig auf eine bemehlte Fläche kippen und straff zu einem Laib wirken."}
  - {titel: "Kaltgare", text: "Mit dem Schluss nach oben in den Gärkorb legen, luftdicht verpacken und bei 5 °C 12–18 Stunden kühlen.", timer: 43200}
  - {titel: "Ofen vorheizen", text: "Pizzastein auf Ebene 2, Ofen mindestens 45 Minuten auf 250 °C Ober-/Unterhitze vorheizen.", timer: 2700}
  - {titel: "Einschießen", text: "Teig direkt aus dem Kühlschrank auf Backpapier stürzen, tief einschneiden und auf den Stein ziehen."}
  - {titel: "Anbacken", text: "Sofort Dampfstoß (intensiv) auslösen und 10 Minuten bei 250 °C backen.", timer: 600}
  - {titel: "Ausbacken", text: "Auf 210 °C reduzieren und ohne weiteren Dampf 30 Minuten backen.", timer: 1800}
  - {titel: "Rösche", text: "Aktive Entfeuchtung einschalten (oder Holzlöffel in die Tür klemmen) und 10 Minuten fertig backen.", timer: 600}
  - {titel: "Auskühlen", text: "Klopfprobe (hohl) und auf dem Rost auskühlen lassen."}
---

## Warum so

Die Ascorbinsäure im Zitronensaft stärkt das Klebereiweiß, der niedrige pH hemmt die eiweißabbauenden Enzyme des Vollkorns. 80 g Type 550 (ca. 18 % des Hauptteigs) sind das funktionale Minimum gegen einen zerfließenden Teig; darunter leidet die Krumenstabilität deutlich. Der Dampfstoß am Anfang hält die Haut dehnbar für den Ofentrieb, die Entfeuchtung am Ende lässt die Kruste rösch werden.

## Stellschrauben

- Teig nach 8 Minuten noch nass → max. 2 Minuten nachkneten, nie über 12 Minuten (Überhitzung)
