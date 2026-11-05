---
titel: Überarbeite Abschnitt 2 im Dokument Rezept-Generator anhand der anderen Datei …
status: aktiv
datum: '2025-07-14'
quelle:
  typ: gemini
  url: https://gemini.google.com/app/46f08616d0df3077
  hinweis: Überarbeite Abschnitt 2 im Dokument Rezept-Generator anhand der anderen Datei (d…
importiert: true
---

> **Frage im Chat:** Überarbeite Abschnitt 2 im Dokument Rezept-Generator anhand der anderen Datei (dort Abschnitt 7 genannt)

Absolut. Hier ist der überarbeitete Abschnitt 2 des Dokuments "Rezept-Generator", aktualisiert mit den Informationen aus dem von dir bereitgestellten Analysedokument.

---

#### **Abschnitt 2: Systemausgabe: Abbildung des EAS auf Maschinenparameter**

|Parameter |Basiswert (bei EAS=0.0) |EAS-Multiplikator |Formel |Ergebnis bei EAS = -1.0 |Ergebnis bei EAS = +1.0 |
|**Peak-Temp. (°C)** |90 |6 |90 + (EAS × 6) |84°C |96°C |
|**Mahlgrad (1-80)** |50 |-20 |50 - (EAS × 20) |70 (grob) |30 (fein) |
|**Mahlwerk-RPM** |80 |20 |80 + (EAS × 20) |60 RPM |100 RPM |
|**Vibration** |N/A |N/A |WENN EAS > 0.7, DANN 'Danach' beim letzten Guss |- |'Danach' |
|**Pausenzeiten (s)** |35 |-10 |35 - (EAS × 10) |45 s (lang) |25 s (kurz) |
