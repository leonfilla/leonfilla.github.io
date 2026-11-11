---
titel: Bosch-Ofen – Gären, Sensor, Kernthermometer
bereich: brot-sauerteig
kurz: Was der HNG978NB1 als Gärraum, mit PerfectBake und mit dem Kernthermometer fürs Brot leistet – und wo nicht
reihenfolge: 3
---

Die Menüpfade auf dieser Seite stammen aus Recherchen, nicht aus dem Handbuch, und sind am Gerät noch zu bestätigen. Eine der Quellen nennt das Modell HNG987NB1 – ein Zahlendreher, gemeint ist der HNG978NB1.

## Gärstufe

Die Gärstufe beginnt bei **30 °C**; tiefer lässt sie sich nicht regeln. Für Hefeteige aus hellem Mehl oder Dinkel ist das unproblematisch, die Rezepte dafür nutzen 35–40 °C. Für Weizenvollkorn-Sauerteig sind 30 °C dagegen die Obergrenze; sein Wohlfühlbereich liegt bei 26–28 °C.

Das Problem ist weniger der Sollwert als die Regelung. Um im Mittel 30 °C zu halten, heizt ein Haushaltsofen kurz über den Sollwert (eine Quelle nennt 35–40 °C) und schaltet dann ab; während der Heizphasen trifft zusätzlich Strahlungswärme die Teigoberfläche. Nachgemessen ist das nicht – ein Thermometer im Garraum klärt es. Bei hochhydriertem Vollkorn steigt die Proteaseaktivität ab etwa 30 °C stark an, und schon 30 min Überhitzung können das Gerüst irreversibel schwächen.

### Ofen als passive Thermobox

Ohne Zubehör lässt sich der Garraum als isolierte Kiste nutzen:

1. Gärstufe 3–5 min einschalten, Thermometer in den Garraum legen.
2. Sobald die Luft 30 °C hat, den Ofen **komplett ausschalten**.
3. Teig hinein, Tür zu. Die LED-Beleuchtung heizt nicht; nur die Isolierung hält die Wärme.
4. Nach 60 min messen. Unter 24 °C: 1 min Gärstufe, dann sofort wieder aus.

Der Tipp „Ofen nur mit eingeschalteter Lampe“, der in einigen Quellen und älteren Rezepten steht, funktioniert bei diesem Ofen also nicht. Gradgenaue 25–28 °C liefert erst die Lösung mit externem Regler und Heizmatte aus der [Gärraum-Notiz](/rezept/brot-sauerteig/gaerraum-steuerung-backofen-inkbird/).

### Aktive Gärstufe

Wenn doch aktiv gegärt wird:

- **Wassertank** bis zur Markierung „Max“ füllen, die Gärstufe arbeitet nur mit Wasser.
- **Einschubhöhe 2.**
- **Heizarten → Gärstufe → 30 °C.**
- Trockene Alternative: **Ober-/Unterhitze auf 30 °C** ohne Dampf, den Teig dann abdecken.

Die feuchte Luft der Gärstufe überträgt Wärme besser als trockene; der Teigkern erreicht 30 °C entsprechend schneller.

| Phase bei 30 °C | Regel |
|---|---|
| Stockgare | 30–50 % kürzer als bei 20–22 °C; Timer auf die Hälfte der Rezeptzeit, ab 2–3 h prüfen; Endpunkt nach Volumen (siehe [Fermentation](/wissen/sauerteig-fermentation/)) |
| Stückgare | nur 30–60 min, sonst flach und sauer ohne Ofentrieb |
| junger oder instabiler Sauerteig | nicht bei 30 °C führen – die Säurebildner sind sehr produktiv, das Vollkorngerüst leidet |

## PerfectBake-Sensor

Der Sensor misst die Feuchte der Abluft. Aus dem Verlauf der Feuchteabgabe regelt der Ofen Temperatur, Dauer und Dampfstoß selbst und schaltet ab, wenn der Kern durchgebacken ist.

**Assist → Brot → Brot → „Brot, ungesüßt“ → Form „Laib“ → PerfectBake aktivieren → Start**

„Brot, ungesüßt“ ist das Profil für Teige ohne nennenswerten Zucker und Fett; für Rosinen- oder Gewürzbrote passt es nicht. Einschub auf Ebene 2 oder wie im Display angegeben.

- **Tür während des Programms nicht öffnen.** Ein Öffnen zerstört die Messkurve und führt zu Abbruch oder Fehlsteuerung.
- **Kalter Teig** direkt aus dem Kühlschrank kann ohne Vorheizen hinein; der Sensor misst ab der ersten Minute. Verlangt die Software Vorheizen, erst nach dem Signal einschieben und dann starten.

Die Tür-Regel macht den Sensorweg unverträglich mit allem, was die manuellen Profile im Bestand tun: Dampf nach 10 min ablassen, Thermometer nachträglich stecken, am Ende ausdünsten. Es ist eine Entweder-oder-Entscheidung – Automatik ohne Eingriff oder manuelles Profil. Ob der Sensor mit einem vorgeheizten Pizzastein sinnvoll regelt, ist offen; bisher wird im Bestand ausschließlich manuell gebacken.

## Kernthermometer

Das eingebaute Bratenthermometer (PerfectRoast Plus) wird in die Buchse im Garraum gesteckt und automatisch erkannt.

- **Messbereich:** Die Anzeige beginnt erst bei etwa 30 °C. Für die Gärüberwachung bei 24–28 °C ist es damit unbrauchbar, höchstens als Alarm gegen Überhitzung.
- **Drei Messpunkte**, der Ofen wertet den niedrigsten. Alle drei müssen im Teig stecken, sonst misst einer die Ofenluft. Waagerecht in die dickste Stelle stecken.
- **Einstellung:** Heizart wählen (z. B. Ober-/Unterhitze oder 4D-Heißluft) → Thermometer-Symbol im Touchdisplay → Kerntemperatur **96–98 °C** → Start. Der Ofen schaltet bei Erreichen ab oder meldet sich, je nach Einstellung. 97 °C ergibt eine weichere, 98 °C eine stabilere Krume.

Wann stecken? Eine Quelle rät, die Sonde erst nach etwa 20 min einzustecken, wenn die Kruste trägt, weil sie im weichen Rohteig rutscht und die Struktur beschädigt. Im Rezept [Hanf-Vollkorn mit Brühstück](/rezept/brot-sauerteig/bewertung-der-ofenfunktionen-bosch-hng978nb1/) wird sie dagegen vor dem Einschießen in den kalten Teigling gesteckt. Beides ist richtig für seinen Fall: Ein kalt gegarter Teigling ist fest genug, und vorher zu stecken erspart das Öffnen in der Dampfphase. Warm gegarte, weiche Teige bekommen die Sonde erst nach der Dampfphase – dann, wenn die Tür zum Dampfablassen ohnehin aufgeht.
