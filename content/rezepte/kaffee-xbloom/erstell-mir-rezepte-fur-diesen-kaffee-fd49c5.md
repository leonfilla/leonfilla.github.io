---
titel: Erstell mir Rezepte für diesen Kaffee
status: aktiv
datum: '2025-07-28'
quelle:
  typ: gemini
  url: https://gemini.google.com/app/88da98afbcb78324
  hinweis: Erstell mir Rezepte für diesen Kaffee
importiert: true
---

> **Frage im Chat:** Erstell mir Rezepte für diesen Kaffee

[START DER REZEPTERSTELLUNG]

#### Recherche-Ergebnisse

**Kaffee**: Traumzeit
**Rösterei**: Kaffeehimmel Bio-Manufaktur
**Herkunft**: Brasilien, Cerrado, Minas Gerais
**Varietät(en)**: Catucai, Mundo Novo, Bourbon, Icatu (Abweichung zur Verpackung, die Webseite nennt mehr Varietäten)
**Anbauhöhe**: 950 m
**Aufbereitung**: Natural
**Geschmacksnoten (Röster)**: Weiches Mundgefühl, milde Nuss-Aromen
**Röstung (Röster)**: Medium (Abweichung zur Verpackung, die "medium-light" angibt)

#### EAS-Berechnung

**Attribut-Modifikatoren**:
*

- (Die Webseite des Rösters gibt "medium" an, was als verlässlicher eingestuft wird als das Label "medium-light" auf der Verpackung. Daher wird der neutrale Wert gewählt.)

- **Anbauhöhe (950 m)**: +0.00 (Kein Modifikator anwendbar, da unter 1800m)

- **Varietät (Catucai, Mundo Novo, Bourbon, Icatu)**: +0.00 (Kein Modifikator anwendbar)

**EAS (Bohne)**: -0.40 + 0.00 + 0.00 + 0.00 = **-0.40**

**EAS (Final)**: -0.40 + (-0.15) = **-0.55**

---

#### Rezept 1: Ausgewogenes Rezept: "Nussige Milde"

**Allgemeine Einstellungen:**

- **Kaffee**: 16 g

- **Brühverhältnis**: 1:16.0

- **Gesamtwasser**: 256 g

- **Mahlgrad (xbloom Skala 1-80)**: 56

- **Mahlwerk-RPM**: 72 RPM

- **Gesamtbrühzeit (geschätzt)**: 02:50

**Brühschritte:**

|Phase |Wassermenge (g) |Temp. (°C) |Flussrate (ml/s) |Pause (s) |Gießmuster |Vibration |
|Bloom |48 |88 |3.0 |40 | |- |
|Guss 2 |104 |89 |3.2 |30 | |- |
|Guss 3 |104 |88 |3.2 |0 | |- |

**Anmerkungen/Begründung:**

- . Der negative Score signalisiert, dass der Kaffee aufgrund der Natural-Aufbereitung eine hohe Löslichkeit aufweist und eine sanfte Extraktion benötigt, um Bitterkeit zu vermeiden und die milden Noten zu betonen.

- **Intention des Rezepts**: Das Ziel ist es, die vom Röster beschriebenen Noten – **weiches Mundgefühl und milde Nuss-Aromen** – klar und ausbalanciert zu extrahieren.

- und moderate Temperaturen umgesetzt. Das 1:16.0 Brühverhältnis sorgt für einen ausgewogenen Körper. Die lange Bloom-Phase von 40s bei niedriger Temperatur lässt den Kaffee sanft aufquellen und entgasen, was die Extraktion der nussigen Aromen begünstigt.

- **Temperaturprofil-Begründung**: Die niedrige Starttemperatur von 88°C und die leicht ansteigende dann fallende Temperatur (88°C -> 89°C -> 88°C) sind bewusst defensiv gewählt. Dies verhindert die Überextraktion der leicht löslichen Partikel aus dem Natural-Prozess und fördert die Entwicklung der süßen, nussigen Aromen anstelle von fermentartigen oder bitteren Noten.

---

#### Rezept 2: Kreatives Signatur-Rezept: "Samtkörper & Süße"

#### Version 1: Maximale Textur

**Allgemeine Einstellungen:**

- **Kaffee**: 16 g

- **Brühverhältnis**: 1:15.5

- **Gesamtwasser**: 248 g

- **Mahlgrad (xbloom Skala 1-80)**: 58

- **Mahlwerk-RPM**: 65 RPM

- **Gesamtbrühzeit (geschätzt)**: 03:05

**Brühschritte:**

|Phase |Wassermenge (g) |Temp. (°C) |Flussrate (ml/s) |Pause (s) |Gießmuster |Vibration |
|Bloom |40 |87 |3.0 |45 | | |
|Guss 2 |68 |88 |3.1 |35 | | |
|Guss 3 |70 |88 |3.2 |35 | |- |
|Guss 4 |70 |87 |3.2 |0 | |- |

**Anmerkungen/Begründung (Version 1):**

- , zielt dieses Rezept darauf ab, die vorgeschlagene defensive Haltung bewusst zu nutzen, um nicht nur die Nussigkeit, sondern vor allem ein maximal **weiches und samtiges Mundgefühl** zu erzeugen. Die Methode ist Rezept 1 überlegen, indem sie durch gezielte Agitation und ein konzentrierteres Brühverhältnis den Körper (TDS) erhöht, ohne die defensiven Grundparameter (Temperatur, Mahlgrad) zu verlassen.

- **Allgemeine Begründung**: Ein noch gröberer Mahlgrad (58) und langsamere RPM (65) schaffen eine sehr geringe Fines-Basis. . . Das engere 1:15.5 Verhältnis verstärkt diesen Effekt.

#### Hypothetischer Feedback-Loop & Korrektur:

- **Identifizierte Schwäche (V1)**: Die Kombination aus sehr grobem Mahlgrad, niedriger Temperatur und der Agitation nach dem zweiten Guss könnte zwar den Körper verbessern, aber die nussige Süße leicht unterentwickelt lassen und zu einer gewissen "Leere" im Geschmack führen.

- **Korrekturmaßnahme (V2)**: Um die Süße gezielt zu fördern, wird der Mahlgrad leicht feiner justiert, das Brühverhältnis minimal erweitert und die Temperatur im entscheidenden zweiten Guss leicht erhöht, um die Extraktion von Zuckern zu intensivieren. Die Agitation wird entfernt, um die Extraktion kontrollierter zu gestalten.

#### Version 2: Süßefokus-Korrektur

**Allgemeine Einstellungen:**

- **Kaffee**: 16 g

- **Brühverhältnis**: 1:16.0

- **Gesamtwasser**: 256 g

- **Mahlgrad (xbloom Skala 1-80)**: **55** (statt 58)

- **Mahlwerk-RPM**: 65 RPM

- **Gesamtbrühzeit (geschätzt)**: 03:00

**Brühschritte:**

|Phase |Wassermenge (g) |Temp. (°C) |Flussrate (ml/s) |Pause (s) |Gießmuster |Vibration |
|Bloom |48 |87 |3.0 |45 | | |
|Guss 2 |**104** |**90** |3.2 |35 | |**-** |
|Guss 3 |**104** |88 |3.2 |0 | |- |

**Anmerkungen/Begründung (Version 2):**

- **Begründung der Korrektur**: Die Reduzierung des Mahlgrades von 58 auf 55 vergrößert die Oberfläche des Kaffeemehls und fördert eine effizientere Extraktion. Die Erhöhung der Temperatur im zweiten, wichtigsten Extraktionsguss auf 90°C liefert gezielt mehr thermische Energie, um die für die Süße verantwortlichen Zuckerverbindungen (insbesondere Saccharose) zu lösen. Das Entfernen der Agitation und die Rückkehr zu einem 1:16.0 Verhältnis balancieren diese aggressiveren Änderungen aus, um eine Überextraktion gemäß der defensiven Gesamtstrategie zu vermeiden und ein süßeres, runderes Geschmacksprofil zu erzeugen.

---

#### Rezept 3: Kreatives Iced Brew Rezept: "Nuss-Praliné on the Rocks"

#### Version 1: Schock-Infusion

**Allgemeine Einstellungen:**

- **Kaffee**: 16 g

- **Brühverhältnis**: 1:10.0 (Konzentrat)

- **Gesamtwasser**: 160 g

- 

- **Mahlgrad (xbloom Skala 1-80)**: 45

- **Mahlwerk-RPM**: 75 RPM

- **Gesamtbrühzeit (geschätzt)**: 02:10

**Brühschritte:**

|Phase |Wassermenge (g) |Temp. (°C) |Flussrate (ml/s) |Pause (s) |Gießmuster |Vibration |
|Bloom |40 |92 |3.0 |35 | |- |
|Guss 2 |60 |93 |3.3 |25 | |- |
|Guss 3 |60 |91 |3.3 |0 | |- |

**Anmerkungen/Begründung (Version 1):**

- , passt ihn aber für einen Iced Brew an. Das Ziel ist ein erfrischendes Getränk, das die Nuss-Aromen in eine schokoladige, pralinéartige Richtung entwickelt. . Diese Methode ist einem einfachen Herunterkühlen überlegen, da sie gezielt die Aromen extrahiert, die sich bei Kälte gut halten, und durch den "Schock" auf dem Eis eine besondere Textur und Klarheit erzeugt.

- **Temperaturprofil-Begründung**: Die hohe Starttemperatur von 92°C ist notwendig, um trotz der kurzen Kontaktzeit eine ausreichende Extraktion zu gewährleisten. Der Peak bei 93°C maximiert die Extraktion von Körper und Süße im Hauptguss. Das Absenken auf 91°C am Ende verhindert die Extraktion von Bitterstoffen, die bei gekühlten Getränken besonders unangenehm hervortreten.

#### Hypothetischer Feedback-Loop & Korrektur:

- **Identifizierte Schwäche (V1)**: Das Konzentrat könnte durch die hohe Temperatur und den feinen Mahlgrad trotz der defensiven Absicht eine leichte, unerwünschte Bitterkeit oder Adstringenz aufweisen, die im kalten Zustand als "trocken" wahrgenommen wird.

- **Korrekturmaßnahme (V2)**: Um die Bitterkeit zu reduzieren und die Süße zu betonen, wird die Peak-Temperatur gesenkt und ein kleiner Bypass mit kühlerem Wasser hinzugefügt. Der Bypass verdünnt das Konzentrat leicht, bevor es auf das Eis trifft, senkt die Gesamtextraktion und sorgt für ein runderes, süßeres Endergebnis.

#### Version 2: Sweetness-Bypass-Korrektur

**Allgemeine Einstellungen:**

- **Kaffee**: 16 g

- **Brühverhältnis**: 1:9.5 (Konzentrat)

- **Gesamtwasser**: 152 g

- 

- 

- **Mahlgrad (xbloom Skala 1-80)**: 45

- **Mahlwerk-RPM**: 75 RPM

- **Gesamtbrühzeit (geschätzt)**: 02:05

**Brühschritte:**

|Phase |Wassermenge (g) |Temp. (°C) |Flussrate (ml/s) |Pause (s) |Gießmuster |Vibration |
|Bloom |40 |92 |3.0 |35 | |- |
|Guss 2 |60 |**91** |3.3 |25 | |- |
|Guss 3 |52 |**90** |3.3 |0 | |- |
|Bypass |8 |**80** |- |- |Direkt |- |

**Anmerkungen/Begründung (Version 2):**

- **Begründung der Korrektur**: Die Reduzierung der Brühtemperaturen (Peak von 93°C auf 91°C) verringert die Extraktionsaggressivität. Die entscheidende Änderung ist der 8g-Bypass mit 80°C Wasser.  Das kühlere Bypass-Wasser reduziert die gefühlte Bitterkeit und hebt die Süße und die nussigen Noten hervor, was zu einem ausgewogeneren und erfrischenderen Iced Coffee führt.

#### Umgang mit Datenlücken

- **Röstgrad**: Auf der Verpackung steht "medium-light", auf der Webseite des Rösters "medium". Da die Webseite in der Regel detailliertere und aktuellere Informationen enthält, wurde "medium" als Grundlage für die EAS-Berechnung verwendet. Dies führt zu einem konservativeren EAS-Score, was für einen Natural-Kaffee eine sichere Annahme ist.

#### Selbst-Konsistenz-Prüfung

Die Wahl basiert auf der folgenden Priorität:

- , der Traumzeit ein "Natural". Beide Methoden belassen Teile der Frucht an der Bohne, was zu einer erhöhten Löslichkeit im Vergleich zu einem gewaschenen Kaffee führt.

- 

- 

**Parameter-Vergleich:**

|Parameter |Aktuelles Rezept (Rezept 1) |"Vorheriges Rezept (Joven Macario)" |Abweichung & Begründung (>5% Abweichung) |
|Mahlgrad |"56" | |**+24.4%**: Die Abweichung ist signifikant. Mein Rezept nutzt einen viel gröberen Mahlgrad. Begründung: Der EASfinal meines Kaffees (-0.55) ist deutlich defensiver als der des Joven Macario (implizit weniger defensiv, da es kein Decaf/Anaerob ist). , und erfordert daher einen gröberen Mahlgrad zur Kontrolle der Extraktion. |
|Peak-Temp. |"89 °C" | |**-3.3%**: Keine signifikante Abweichung. Beide Temperaturen sind im defensiven bis moderaten Bereich, was zu den Aufbereitungsmethoden passt. |
|RPM |"72" | |**+2.9%**: Keine signifikante Abweichung. Beide Drehzahlen sind im unteren Bereich, um die Fines-Produktion bei diesen potenziell "klebrigen" Kaffees zu minimieren. |

[ENDE DER REZEPTERSTELLUNG]
