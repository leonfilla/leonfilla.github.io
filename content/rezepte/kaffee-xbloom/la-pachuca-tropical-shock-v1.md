---
titel: "La Pachuca – Tropical Shock (Iced)"
status: aktiv
datum: "2025-08-29"
quelle:
  typ: "gemini"
  url: "https://gemini.google.com/app/2773758b39af7ed3"
  hinweis: "erstell mir rezepte für la pachuca juicy honey fermentation von elbgold"
importiert: true
linie: "la-pachuca-2025-08-29"
variante: "Tropical Shock V1"
fokus: "Iced Brew auf 100 g Eis mit aggressiverer Strategie: Mahlgrad 42, 90 RPM und 94 °C für ein starkes Konzentrat."
ergebnis: "1 Glas über Eis, 260 g"
geraete: [xbloom-studio]
zutaten:
  - {name: "Eis", menge: 100, einheit: "g"}
schritte:
  - {titel: "Eis vorlegen", text: "100 g Eis in den Server geben."}
xbloom:
  dosis: 16
  verhaeltnis: 10
  wasser: 160
  mahlgrad: 42
  rpm: 90
  bruehzeit: "2:10"
  guesse:
    - {phase: "Bloom", menge: 40, temp: 94, fluss: 3.0, pause: 35, muster: "zentral", vib_vor: true, vib_nach: false}
    - {phase: "Guss 2", menge: 60, temp: 94, fluss: 3.3, pause: 30, muster: "spirale", vib_vor: false, vib_nach: false}
    - {phase: "Guss 3", menge: 60, temp: 92, fluss: 3.5, pause: 0, muster: "kreis", vib_vor: false, vib_nach: true}
bohne: elbgold-la-pachuca
---

## Warum so
Feiner Mahlgrad, mehr Fines und hohe Starttemperatur extrahieren ein Konzentrat, das das Schmelzwasser trägt. Laut Feedback-Loop kann die Intensität eine adstringierende Teenote bringen – dafür V2 mit Bypass.
