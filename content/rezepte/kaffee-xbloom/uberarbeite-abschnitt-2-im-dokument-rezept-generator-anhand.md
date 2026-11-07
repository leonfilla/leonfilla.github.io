---
titel: Rezept-Generator – EAS auf xBloom-Parameter abbilden
status: archiv
datum: '2025-07-14'
quelle:
  typ: gemini
  url: https://gemini.google.com/app/46f08616d0df3077
  hinweis: Überarbeite Abschnitt 2 im Dokument Rezept-Generator anhand der anderen Datei
importiert: true
fokus: Kein Rezept – Formeltabelle, die einen Extraktions-Score (EAS, −1 bis +1) auf Temperatur, Mahlgrad, RPM, Vibration und Pausen der xBloom abbildet.
geraete: [xbloom-studio]
tags: [Rezept-Generator, Formeln]
gesichtet: false
---

## Notizen

- Peak-Temperatur = 90 + EAS × 6 (84–96 °C).
- Mahlgrad = 50 − EAS × 20 (70 grob bis 30 fein).
- RPM = 80 + EAS × 20 (60–100).
- Pausen = 35 − EAS × 10 s (45–25 s).
- Vibration „danach“ beim letzten Guss nur, wenn EAS > 0,7.
