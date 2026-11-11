---
titel: Weizen-Vollkorn-Sauerteigbrot V4.0
status: archiv
datum: '2026-02-02'
quelle:
  typ: gemini
  url: https://gemini.google.com/app/ff35960758945a73
  hinweis: Bewerte die reine Knetfunktion von Sauerteigen des Panasonic SD-YR2540
importiert: true
linie: protokoll-weizen-vollkorn-sauerteigbrot-high-hydra-4224d
version: V4.0
fokus: Weizen-Vollkorn-Sauerteigbrot mit Levain und Kneten im Automaten (Menü 29/31) und Backen frei auf dem Pizzastein. Neu sind die Anstellgut-Rücklage, ein Kochstück und Uhrzeiten von 12 bis 20 Uhr.
ergebnis: 1 Laib
zeit: {gesamt: 1560}
geraete: [panasonic-sd-yr2540, bosch-hng978]
tags: [Sauerteig, Vollkorn]
brot:
  programm: Menü 29 (Levain) · Menü 31 (Kneten)
  gare:
    - {phase: "Levain im Sauerteigbecher", zeit: "3 h 15 min"}
    - {phase: "Autolyse", zeit: "30 min"}
    - {phase: "Stockgare mit 3 Coil Folds", zeit: "ca. 4 h, bis +50–75 % Volumen"}
    - {phase: "Kaltgare im Gärkorb", temp: 5, zeit: "12–20 h"}
  backprofil:
    - {phase: "Vorheizen mit Pizzastein", temp: 275, zeit: "mind. 45 min"}
    - {phase: "Dampf-Phase", temp: 250, dampf: "Dampfstoß an", zeit: "0–10 min"}
    - {phase: "Gar-Phase", temp: 210, dampf: "aus, Schwaden ablassen", zeit: "10–40 min"}
    - {phase: "Crisp Finish", temp: 210, dampf: "Entfeuchtung", zeit: "40–50 min"}
changelog:
  - {version: "V4.0", text: "Levain vergrößert (45 g + 45 g), 80–90 g davon als Anstellgut-Rücklage"}
  - {version: "V4.0", text: "Kochstück aus 30 g Vollkornmehl und 150 g Wasser"}
  - {version: "V4.0", text: "Beispiel-Uhrzeiten zwischen 12 und 20 Uhr"}
  - {version: "V4.0", text: "Coil Folds genauer beschrieben"}
  - {version: "V4.0", text: "Dampfstoß als Ein/Aus, Crisp Finish statt Kochlöffeltrick"}
  - {version: "V4.0", datum: "2026-02-02", text: "Levain-Menge korrigiert: Ansatz 40 g Anstellgut + 55 g Weizenvollkorn + 55 g Wasser (150 g), davon 50 g Rücklage und ca. 100 g in den Teig statt nur 30–35 g"}
zutaten:
  - {gruppe: "Levain", name: "Anstellgut", menge: 40, einheit: "g", hinweis: "kalt"}
  - {gruppe: "Levain", name: "Weizenvollkornmehl", menge: 55, einheit: "g", hinweis: "vom fertigen Levain 50 g zurück ins Vorratsglas"}
  - {gruppe: "Levain", name: "Wasser", menge: 55, einheit: "g", hinweis: "35–40 °C"}
  - {gruppe: "Kochstück", name: "Weizenvollkornmehl", menge: 30, einheit: "g", mehl: true}
  - {gruppe: "Kochstück", name: "Wasser", menge: 150, einheit: "g", wasser: 1}
  - {gruppe: "Hauptteig", name: "Wasser", menge: 135, einheit: "g", wasser: 1, hinweis: "kalt"}
  - {gruppe: "Hauptteig", name: "Zitronensaft", menge: 15, einheit: "g", wasser: 0.9, hinweis: "frisch"}
  - {gruppe: "Hauptteig", name: "Weizenvollkornmehl", menge: 340, einheit: "g", mehl: true}
  - {gruppe: "Hauptteig", name: "Weizenmehl 550", menge: 80, einheit: "g", mehl: true}
  - {gruppe: "Hauptteig", name: "Levain", menge: 100, einheit: "g", hinweis: "Rest aus dem Becher, ca. 100 g"}
  - {gruppe: "Hauptteig", name: "Salz", menge: 12, einheit: "g"}
  - {gruppe: "Reserve", name: "Wasser", menge: 20, einheit: "g", hinweis: "optional, für Bassinage"}
schritte:
  - {titel: "12:00 – Levain ansetzen", text: "Knethaken entfernen. 40 g kaltes Anstellgut, 55 g Weizenvollkornmehl und 55 g warmes Wasser im Sauerteigbecher mischen, Becher in den Backbehälter stellen, Menü 29 starten.", timer: 11700}
  - {titel: "Kochstück kochen", text: "30 g Weizenvollkornmehl und 150 g Wasser klumpenfrei verrühren und bis puddingartig (65 °C) aufkochen."}
  - {titel: "Kochstück abkühlen", text: "In eine Schale umfüllen und mit Deckel auf Raumtemperatur abkühlen lassen."}
  - {titel: "15:15 – Anstellgut sichern", text: "Menü 29 stoppen. Vom verdoppelten Levain (ca. 150 g) 50 g zurück ins Vorratsglas und in den Kühlschrank; ca. 100 g bleiben im Becher."}
  - {titel: "Befüllen", text: "Roggen-Knethaken einsetzen. Kochstück, 135 g kaltes Wasser, 15 g Zitronensaft, 340 g Weizenvollkornmehl und 80 g Weizenmehl 550 in den Behälter geben."}
  - {titel: "Mischen", text: "Menü 31 für 2 Minuten laufen lassen.", timer: 120}
  - {titel: "Quellen lassen", text: "Maschine aus, Deckel zu.", timer: 1800}
  - {titel: "15:45 – Kneten", text: "Ca. 100 g Levain und 12 g Salz zugeben, Menü 31 auf 10 Minuten stellen.", timer: 600}
  - {titel: "Bassinage", text: "Bei Minute 8: Löst sich der Teig gut, die 20 g Reservewasser schluckweise zugeben; ist er noch klebrig, weglassen."}
  - {titel: "Entnehmen", text: "Teig sofort entnehmen (unter 26 °C) und abgedeckt in eine leicht geölte, eckige Wanne geben."}
  - {titel: "16:45 – Coil Fold 1", text: "Mit nassen Händen mittig unter den Teig greifen, anheben, bis sich das untere Ende löst, und so ablegen, dass es sich unterfaltet. Wanne um 90° drehen, viermal wiederholen.", timer: 2700}
  - {titel: "17:30 – Coil Fold 2", text: "Wie Fold 1.", timer: 2700}
  - {titel: "18:15 – Coil Fold 3", text: "Wie Fold 1, danach ungestört gehen lassen, bis das Volumen um 50–75 % zugenommen hat.", timer: 6300}
  - {titel: "20:00 – Formen", text: "Teig straff rund oder oval wirken und mit dem Schluss nach oben in den bemehlten Gärkorb legen."}
  - {titel: "Kaltgare", text: "Deckel auflegen und bei 5 °C 12–20 Stunden in den Kühlschrank stellen.", timer: 43200}
  - {titel: "Ofen vorheizen", text: "Pizzastein auf Ebene 2, mindestens 45 Minuten auf 275 °C Ober-/Unterhitze vorheizen.", timer: 2700}
  - {titel: "Einschießen", text: "Teig auf den Stein stürzen und einschneiden."}
  - {titel: "Dampf-Phase", text: "Temperatur sofort auf 250 °C senken und Dampfstoß aktivieren.", timer: 600}
  - {titel: "Gar-Phase", text: "Dampfstoß deaktivieren, Tür kurz ganz öffnen, auf 210 °C reduzieren.", timer: 1800}
  - {titel: "Crisp Finish", text: "Crisp Finish aktivieren und bis zur gewünschten Bräunung backen (Klopfprobe hohl).", timer: 600}
  - {titel: "Auskühlen", text: "Auf dem Rost vollständig auskühlen lassen."}
---

## Warum so

Das Kochstück bindet über verkleisterte Stärke zusätzliches Wasser und hält die Krume länger frisch. Coil Folds statt Dehnen und Falten: Der Teig faltet sich beim Anheben durch sein Eigengewicht unter sich – das schont das leicht reißende Vollkorn-Glutengerüst und erhält die Gasblasen. Crisp Finish saugt die Feuchte aktiv aus dem Garraum, wirksamer als ein Kochlöffel in der Tür.

## Stellschrauben

- Teig nach 8 Minuten Kneten noch klebrig → Reservewasser weglassen
