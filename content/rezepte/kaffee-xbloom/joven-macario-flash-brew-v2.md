---
titel: "Joven Macario – Flash Brew Süße-Boost"
status: aktiv
datum: "2025-07-10"
quelle:
  typ: "gemini"
  url: "https://gemini.google.com/app/10c9fbe1c57e5cce"
  hinweis: "Nutze das Dokument im Anhang als Prompt für folgende Kaffeebohne: Joven Macario …"
importiert: true
linie: "joven-macario-heiss-c92f6"
variante: "Flash Brew V2"
bohne: "heilandt-joven-macario"
fokus: "Korrektur: durchgehend 95 °C und Vibration nach Guss 2 statt nach Guss 3 für mehr Traubensüße und Rückgrat auf Eis."
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
    - {phase: "Bloom", menge: 40, temp: 95, fluss: 3.2, pause: 30, muster: "zentral", vib_vor: true, vib_nach: false}
    - {phase: "Guss 2", menge: 60, temp: 95, fluss: 3.5, pause: 20, muster: "spirale", vib_vor: false, vib_nach: true}
    - {phase: "Guss 3", menge: 60, temp: 95, fluss: 3.5, pause: 0, muster: "kreis", vib_vor: false, vib_nach: false}
---

## Warum so
Mehr Temperatur und Agitation in der Hauptphase lösen mehr Zucker, die die Säure ausbalancieren und auch nach der Verdünnung tragen.
