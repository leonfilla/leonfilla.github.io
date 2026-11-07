---
titel: Rungeto – Flash Brew mit Bypass
status: aktiv
datum: '2025-07-31'
quelle:
  typ: gemini
  url: https://gemini.google.com/app/91881ffb847c50a9
  hinweis: Erstell mir für diese Bohne von Coffee Circle Rezepte
importiert: true
linie: coffee-circle-rungeto-2025-07-31
variante: Flash Brew
fokus: Hochextrahiertes Konzentrat für Eiskaffee; statt den letzten Teil durchs Bett zu pressen, kommen 20 g als 85-°C-Bypass dazu – sauberer Abgang ohne Kratzen.
ergebnis: 1 Glas über Eis
geraete:
- xbloom-studio
zutaten:
- {name: Eis, einheit: g, hinweis: Menge im Chat nicht erhalten}
schritte:
- {titel: Eis vorlegen, text: Eis in Karaffe oder Glas unter den Brühkorb geben.}
xbloom:
  dosis: 16
  wasser: 140
  mahlgrad: 35
  rpm: 100
  bruehzeit: '2:10'
  bypass: {menge: 20, temp: 85}
  guesse:
  - {phase: Bloom, menge: 40, temp: 96, fluss: 3.0, pause: 35, muster: zentral, vib_vor: true, vib_nach: false}
  - {phase: Guss 2, menge: 50, temp: 96, fluss: 3.5, pause: 30, muster: spirale, vib_vor: false, vib_nach: true}
  - {phase: Guss 3, menge: 50, temp: 96, fluss: 3.5, pause: 0, muster: kreis, vib_vor: false, vib_nach: true}
bohne: coffee-circle-rungeto
gesichtet: false
---

## Warum so

Die geringe Wassermenge wird durch maximale Parameter kompensiert (96 °C, feiner Mahlgrad, 100 RPM, Vibration danach). Der Bypass stoppt die Extraktion, bevor späte Bitterstoffe kommen, und stellt das Gesamtverhältnis 1:10 (160 g) ein.

## Varianten

- Version 1 ohne Bypass: 40/60/60 g, Mahlgrad 34 – Risiko kratziger Bitterkeit.
