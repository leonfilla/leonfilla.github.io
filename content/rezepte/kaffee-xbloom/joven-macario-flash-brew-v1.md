---
titel: "Joven Macario – Flash Brew"
status: aktiv
datum: "2025-07-10"
quelle:
  typ: "gemini"
  url: "https://gemini.google.com/app/10c9fbe1c57e5cce"
  hinweis: "Nutze das Dokument im Anhang als Prompt für folgende Kaffeebohne: Joven Macario …"
importiert: true
linie: "joven-macario-heiss-c92f6"
variante: "Flash Brew V1"
bohne: "heilandt-joven-macario"
fokus: "Iced Pour Over auf 100 g Eis: drei kurze Güsse und Mahlgrad 42 extrahieren Orange und Traube schnell und klar."
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
  rpm: 70
  bruehzeit: "1:55"
  guesse:
    - {phase: "Bloom", menge: 40, temp: 94, fluss: 3.2, pause: 30, muster: "zentral", vib_vor: true, vib_nach: false}
    - {phase: "Guss 2", menge: 60, temp: 94, fluss: 3.5, pause: 20, muster: "spirale", vib_vor: false, vib_nach: false}
    - {phase: "Guss 3", menge: 60, temp: 92, fluss: 3.5, pause: 0, muster: "kreis", vib_vor: false, vib_nach: true}
---

## Warum so
Der feine Mahlgrad gleicht die geringe Wassermenge aus, 70 RPM schützen die Klarheit; die Absenkung auf 92 °C bremst den turbulenten letzten Guss. Laut Feedback-Loop wirkt die Tasse leicht eindimensional-säuerlich – dafür V2.
