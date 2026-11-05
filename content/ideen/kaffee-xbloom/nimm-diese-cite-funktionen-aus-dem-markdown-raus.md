---
titel: Nimm diese cite funktionen aus dem markdown raus
datum: '2026-02-26'
quelle:
  typ: gemini
  url: https://gemini.google.com/app/9fc9b057fcebc45b
  hinweis: verändere diesen Markdown, dass für Gemini klar wird, dass pro Pour folgendes ve…
importiert: true
---

> **Frage im Chat:** nimm diese cite funktionen aus dem markdown raus

### Globale Parameter (Gelten für das gesamte Rezept)

|Parameter |Range / Schritte |Auswirkung |
|**Kaffeemenge (Dose)** |5 g – 18 g (1 g Schritte) |Definiert die Basis für das Brühverhältnis. |
|**Brühverhältnis (Ratio)** |Variabel (0.5 Schritte) |Berechnet Gesamtwassermenge. Bestimmt Viskosität und Endkonzentration (TDS). |
|**Mahlgrad (Grind Size)** |1 – 80 Klicks (18,75 µm/Stufe) |Gröber: Kürzere Durchlaufzeit, geringere Extraktionsausbeute (EY). Feiner: Längere Kontaktzeit, höhere EY. |
|**Mühlen-Geschwindigkeit (Grinder RPM)** |60 – 120 RPM (10er Schritte) |Niedrige RPM: Weniger Fines, mehr Textur. Hohe RPM: Mehr Klarheit und ausgeprägtere Süße. |
|**Anzahl der Aufgüsse (Pours)** |1 – 5 Pours |Definiert die Anzahl der nachfolgenden Extraktionsphasen. |

### Individuelle Parameter pro Pour (Für jeden Aufguss separat definierbar)

|Parameter (pro Pour) |Range / Schritte |Auswirkung für diesen spezifischen Pour |
|**Wasservolumen (ml)** |Variabel (in ml) |Bestimmt die exakte Wassermenge für den aktuellen Aufguss. |
|**Wassertemperatur** |40 °C – 96 °C / BP (1 °C Schritte) |Steuert Lösungsgeschwindigkeit in dieser Phase. |
|**Durchflussmenge (Flow Rate)** |3.0 – 3.5 ml/s (0.1 Schritte) |Bestimmt Gießgeschwindigkeit und Stärke der mechanischen Agitation pro Sekunde. |
|**Pausenzeiten** |0 – 360 Sekunden |Legt die Wartezeit nach diesem Pour fest (inkl. Blooming bei Pour 1). Steuert das Absinken des Kaffeebetts. |
|**Gießmuster (Pour Pattern)** |Zentriert, Spirale, Kreise |Steuert mechanische Agitation und Bypass-Verhalten am Filterrand. |
|**Vibration** |Ein/Aus |Vorab: Ebnung des Kaffeebetts. Danach: Erhöhung der Agitation, Aufbrechen von Channeling. |
