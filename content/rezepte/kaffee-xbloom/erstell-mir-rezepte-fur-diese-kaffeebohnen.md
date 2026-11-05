---
titel: Erstell mir Rezepte für diese Kaffeebohnen
status: aktiv
datum: '2025-09-27'
quelle:
  typ: gemini
  url: https://gemini.google.com/app/20bcdd449a5fbb1a
  hinweis: Erstell mir Rezepte für diese Kaffeebohnen
importiert: true
---

> **Frage im Chat:** Erstell mir Rezepte für diese Kaffeebohnen

[START DER REZEPTERSTELLUNG]

#### Recherche-Ergebnisse

Basierend auf den Informationen auf der Kaffeeverpackung wurde eine Recherche durchgeführt.

- **Kaffee**: Lérida

- **Rösterei**: LF (Identifiziert durch das Logo, eine spezifische Rösterei konnte online nicht eindeutig zugeordnet werden, daher wird "LF Roasters" als Platzhalter verwendet)

- **Herkunft**: Panama, Boquete

- **Farm**: Finca Lérida

- **Produzentin**: Maria Antonella Amoruso

- **Varietät(en)**: Catuai

- **Anbauhöhe**: 1990 - 2000m

- **Aufbereitung**: Natural Anaerobic Slow Dried

- **Geschmacksnoten (Röster)**: Watermelon, Starfruit, White Currant

#### EAS-Berechnung

Die Berechnung des "Extraction Aggressiveness Score" (EAS) basiert auf den recherchierten Bohneneigenschaften und der vorgegebenen Wasserchemie.

- **Attribut-Modifikatoren**:

  - Aufbereitung (Natural Anaerobic): -0.60

  - Röstgrad (Hell): +0.25 (Annahme basierend auf den fruchtigen Noten)

  - Anbauhöhe (>2000 m): +0.20 (Da die Spanne bis 2000m reicht, wird der höhere Modifikator für maximale Dichte angesetzt)

- **EAS (Bohne)**: -0.60 + 0.25 + 0.20 = -0.15

- **Wasser-Modifikator**: -0.15 (Festgelegt aufgrund von KH = 3-4 °dKH und TDS > 175 ppm)

- **EAS (Final)**: -0.15 + (-0.15) = -0.30

#### Rezept 1: Ausgewogenes Rezept passend zur Kaffeebohne

**Allgemeine Einstellungen:**

- **Kaffee**: 16 g

- **Brühverhältnis**: 1:16.5

- **Gesamtwasser**: 264 g

- **Mahlgrad (xbloom Skala 1-80)**: 52

- **Mahlwerk-RPM**: 70 RPM

- **Gesamtbrühzeit (geschätzt)**: 03:10

**Brühschritte:**

|Phase |Wassermenge (g) |Temp. (°C) |Flussrate (ml/s) |Pause (s) |Gießmuster |Vibration |
|**Bloom** |48 |88 |3.0 |40 |Zentral |- |
|**Guss 2** |108 |90 |3.2 |35 |Spirale |- |
|**Guss 3** |108 |89 |3.3 |0 |Kreis |- |

**Anmerkungen/Begründung:**
*

- **Intention des Rezepts**: Das Ziel ist, die durch die anaerobe Aufbereitung extrem hohe Löslichkeit zu kontrollieren. Die delikaten und flüchtigen Noten von Wassermelone und Sternfrucht sollen präzise extrahiert werden, ohne die weinigen, potenziell überfermentierten Noten in den Vordergrund zu stellen.

- **Allgemeine Begründung**: Der relativ grobe Mahlgrad (52) und die niedrige RPM (70) reduzieren die Oberfläche und die Menge an Feinpartikeln, was einer Überextraktion entgegenwirkt. Das Brühverhältnis von 1:16.5 sorgt für einen vollen Körper, ohne die feinen Säuren zu überdecken. Die lange Bloom-Phase von 40s bei niedriger Temperatur erlaubt ein sanftes Entgasen, ohne die fragilen Aromastoffe zu verbrennen.

- **Temperaturprofil-Begründung**: Die Starttemperatur von 88°C ist bewusst niedrig gewählt, um die empfindlichen Aromen zu schützen. Der leichte Anstieg auf 90°C im zweiten Guss erhöht die Extraktionsenergie gezielt, um die Süße (White Currant) und den Körper zu entwickeln. Die finale Absenkung auf 89°C minimiert die Extraktion von Bitterstoffen am Ende des Brühvorgangs.

---

#### Rezept 2: Kreatives Signatur-Rezept: "Aromatic Cascade"

**Version 1: Layered Infusion**

**Allgemeine Einstellungen:**

- **Kaffee**: 16 g

- **Brühverhältnis**: 1:17.0

- **Gesamtwasser**: 272 g

- **Mahlgrad (xbloom Skala 1-80)**: 54

- **Mahlwerk-RPM**: 60 RPM

- **Gesamtbrühzeit (geschätzt)**: 03:30

**Brühschritte:**

|Phase |Wassermenge (g) |Temp. (°C) |Flussrate (ml/s) |Pause (s) |Gießmuster |Vibration |
|**Bloom** |40 |86 |3.0 |45 |Zentral |Davor |
|**Guss 2** |60 |88 |3.2 |35 |Spirale |- |
|**Guss 3** |60 |91 |3.2 |35 |Spirale |- |
|**Guss 4** |60 |91 |3.4 |35 |Kreis |- |
|**Guss 5** |52 |88 |3.4 |0 |Zentral |- |

**Anmerkungen/Begründung (Version 1):**

- , indem es die Extraktion durch ein ansteigendes Temperaturprofil in Schichten aufteilt.     Ziel ist es, die Aromen von Wassermelone und Sternfrucht noch explosiver und getrennter darzustellen als im ausgewogenen Rezept.

- **Temperaturprofil-Begründung**: Das progressive Profil (86°C -> 88°C -> 91°C -> 88°C) ist der Kern der Methode. Der ultra-sanfte Start bei 86°C extrahiert nur die flüchtigsten Aromen. Der Peak bei 91°C löst gezielt die komplexen Zucker und Säuren. Die finale Absenkung schont das Kaffeebett und sorgt für einen sauberen Abgang.

**Hypothetischer Feedback-Loop & Korrektur:**
*

- Zusätzlich wird der Mahlgrad leicht feiner justiert.

**Version 2: Layered Infusion - Body Boost**

**Allgemeine Einstellungen:**

- **Kaffee**: 16 g

- **Brühverhältnis**: 1:17.0

- **Gesamtwasser**: 272 g

- **Mahlgrad (xbloom Skala 1-80)**: **51** (von 54)

- **Mahlwerk-RPM**: 60 RPM

- **Gesamtbrühzeit (geschätzt)**: 03:40

**Brühschritte:**

|Phase |Wassermenge (g) |Temp. (°C) |Flussrate (ml/s) |Pause (s) |Gießmuster |Vibration |
|**Bloom** |40 |86 |3.0 |45 |Zentral |Davor |
|**Guss 2** |60 |88 |3.2 |35 |Spirale |- |
|**Guss 3** |60 |91 |3.2 |35 |Spirale |**Danach** |
|**Guss 4** |60 |91 |3.4 |35 |Kreis |- |
|**Guss 5** |52 |88 |3.4 |0 |Zentral |- |

**Anmerkungen/Begründung (Version 2):**

- **Begründung der Korrektur**: Der feinere Mahlgrad (51) vergrößert die Partikeloberfläche und erhöht die Extraktion.   Dies erhöht den Körper und das Mundgefühl, während die defensive Grundstruktur des Rezepts die empfindlichen Aromen weiterhin schützt.

---

#### Rezept 3: Kreatives Iced Brew Rezept: "Tropical Chill"

**Version 1: Shock Infusion**

**Allgemeine Einstellungen:**

- **Kaffee**: 16 g

- 

- **Brühverhältnis**: 1:10.5

- **Gesamtwasser**: 168 g

- **Mahlgrad (xbloom Skala 1-80)**: 45

- **Mahlwerk-RPM**: 80 RPM

- **Gesamtbrühzeit (geschätzt)**: 02:20

**Brühschritte:**

|Phase |Wassermenge (g) |Temp. (°C) |Flussrate (ml/s) |Pause (s) |Gießmuster |Vibration |
|**Bloom** |40 |92 |3.0 |35 |Zentral |Davor |
|**Guss 2** |64 |94 |3.4 |30 |Spirale |Danach |
|**Guss 3** |64 |90 |3.4 |0 |Kreis |- |

**Anmerkungen/Begründung (Version 1):**

- 
  extrahieren schnell die notwendigen Säuren und Zucker, bevor das Konzentrat auf das Eis trifft und die Extraktion abrupt stoppt ("Schockextraktion"). Dies bewahrt die frischen Noten von Sternfrucht und Wassermelone in einer kalten Anwendung.

**Hypothetischer Feedback-Loop & Korrektur:**

- **Identifizierte Schwäche (V1)**: Die konzentrierte Extraktion könnte, obwohl schnell, zu einer gewissen Schärfe oder Adstringenz führen, insbesondere durch die Kombination aus feinerem Mahlgrad und Agitation.

- **Korrekturmaßnahme (V2)**: Um die Extraktion zu glätten, wird die Agitation reduziert (keine Vibration), aber die Kontaktzeit durch einen zusätzlichen, kleinen Guss erhöht. Die Temperatur wird leicht gesenkt, um die Extraktion sanfter zu gestalten.

**Version 2: Smooth Chill**

**Allgemeine Einstellungen:**

- **Kaffee**: 16 g

- 

- **Brühverhältnis**: 1:10.5

- **Gesamtwasser**: 168 g

- **Mahlgrad (xbloom Skala 1-80)**: **46** (von 45)

- **Mahlwerk-RPM**: 80 RPM

- **Gesamtbrühzeit (geschätzt)**: 02:35

**Brühschritte:**

|Phase |Wassermenge (g) |Temp. (°C) |Flussrate (ml/s) |Pause (s) |Gießmuster |Vibration |
|**Bloom** |40 |**91** |3.0 |35 |Zentral |Davor |
|**Guss 2** |**50** |**93** |3.4 |30 |Spirale |- |
|**Guss 3** |**50** |93 |3.4 |30 |Spirale |- |
|**Guss 4** |**28** |**89** |3.2 |0 |Kreis |- |

**Anmerkungen/Begründung (Version 2):**

- **Begründung der Korrektur**: Die Entfernung der "Vibration Danach" ist die größte Veränderung, um die Agitation und damit das Risiko von Adstringenz zu senken. Die Aufteilung des Hauptgusses in zwei Puls-Güsse (Guss 2 & 3) bei konstanter Temperatur erhöht die Kontaktzeit und fördert eine gleichmäßigere Extraktion. Der leicht gröbere Mahlgrad (46) und die insgesamt etwas niedrigere Temperaturkurve sorgen für eine sanftere Extraktion, die zu einem runderen und süßeren Kaltgetränk führt.

---

#### Umgang mit Datenlücken

- **Röstgrad**: Der Röstgrad war auf der Verpackung nicht explizit angegeben. Basierend auf den hellen, fruchtigen und säurebetonten Geschmacksnoten ("Watermelon, Starfruit, White Currant") wurde mit hoher Sicherheit auf einen "Hellen / Light" Röstgrad geschlossen. Dies ist eine Standardannahme für moderne Spezialitätenkaffees mit diesem Profil.

- **Rösterei**: Das Logo "LF" konnte keiner spezifischen, bekannten Rösterei eindeutig zugeordnet werden. Die Analyse und Rezeptentwicklung basieren ausschließlich auf den vom Produzenten und auf der Verpackung bereitgestellten Informationen zur Bohne selbst.

---

#### Selbst-Konsistenz-Prüfung

- 

  - **Aufbereitung**: Beide Kaffees sind **"Anaerobic Natural"**.

  - **Varietät**: Der Lérida ist ein Catuai, der El Paraiso ein Castillo. Beide sind Hochertragsvarietäten, die für ihre Robustheit bekannt sind, was sie in ihrem Extraktionsverhalten ähnlicher macht als beispielsweise im Vergleich zu einer fragilen Geisha.

  - **Herkunft**: Panama vs. Kolumbien. Beide sind renommierte zentral-/südamerikanische Anbauländer, die für hochwertige Kaffees mit ausgeprägter Säure bekannt sind.

**Parameter-Vergleich:** (Rezept 1 vs. Gardelli Beispiel)

|Parameter |Aktuelles Rezept (Lérida) |Vorheriges Rezept (Finca El Paraiso) |Abweichung & Begründung (>5% Abweichung) |
|**Mahlgrad** |"52" |"55" |**-5.5%**: Die Abweichung ist minimal. Der leicht feinere Mahlgrad für den Lérida ist gerechtfertigt durch seine höhere Anbauhöhe (1990-2000m vs. 1900m), die auf eine höhere Bohnendichte hindeutet und eine etwas intensivere Extraktion erfordert, um das volle Potenzial zu erschließen. |
|**Peak-Temp.** |"90 °C" |"88 °C" |**+2.3%**: Keine signifikante Abweichung. Die etwas höhere Peak-Temperatur unterstützt die Extraktion der dichteren Lérida-Bohne. |
|**RPM** |"70" |"70" |**0%**: Keine Abweichung. Für beide hochlöslichen anaeroben Kaffees wird eine identische, defensive RPM gewählt, um die Fines-Produktion zu kontrollieren. |

[ENDE DER REZEPTERSTELLUNG]

[START DER REZEPTERSTELLUNG]

#### Recherche-Ergebnisse

- **Kaffee**: Los Pirineos Black Honey

- **Rösterei**: La Finca (LF)

- **Herkunft**: El Salvador, Usulután

- **Varietät(en)**: Elite Bourbon

- **Anbauhöhe**: 1400 - 1550 m

- **Aufbereitung**: Black Honey

- **Geschmacksnoten (Röster)**: Strawberry, Milk Chocolate, Apricot

- **Quelle**: Die Informationen wurden direkt vom Etikett des Kaffeepakets entnommen (Primärquelle).

#### EAS-Berechnung

- **Attribut-Modifikatoren**:
*

*

*

*

- **EAS (Bohne)**: -0.30 + 0.25 + 0.00 + 0.00 = **-0.05**

- 

- **EAS (Final)**: -0.05 + (-0.15) = **-0.20**

---

#### Rezept 1: Ausgewogenes Rezept: "Schokoladen-Frucht-Balance"

**Allgemeine Einstellungen:**

- **Kaffee**: 16 g

- 

- **Gesamtwasser**: 264 g

- **Mahlgrad (xbloom Skala 1-80)**: 53

- **Mahlwerk-RPM**: 75 RPM

- **Gesamtbrühzeit (geschätzt)**: 03:10

**Brühschritte:**

|Phase |Wassermenge (g) |Temp. (°C) |Flussrate (ml/s) |Pause (s) |Gießmuster |Vibration |
|Bloom |48 |88 |3.2 |40 | | |
|Guss 2 |108 |89 |3.3 |35 | |- |
|Guss 3 |108 |88 |3.3 |0 | |- |

**Anmerkungen/Begründung:**
*

- **Intention des Rezepts**: Das Ziel ist eine harmonische Balance zwischen der Süße der Milchschokolade und den delikaten Fruchtnoten von Erdbeere und Aprikose. Das Rezept ist so konzipiert, dass es die hohe Löslichkeit des Black Honey Kaffees kontrolliert, um ein süßes, klares und komplexes Tassenprofil zu erzeugen.

- 
  Die lange Bloom-Phase von 40s erlaubt ein vollständiges Entgasen, ohne flüchtige Aromen durch zu hohe Temperaturen zu verlieren.

- **Temperaturprofil-Begründung**: Die moderate Peak-Temperatur von 89°C ist ein Kernaspekt der defensiven Strategie. Sie ist hoch genug, um die Süße und die komplexen Zucker des Black Honey Prozesses zu extrahieren, aber niedrig genug, um die feinen Erdbeer- und Aprikosenaromen zu schützen und die Extraktion von bitteren oder überfermentierten Noten zu verhindern.

---

#### Rezept 2: Kreatives Signatur-Rezept: "Layered Fruit Infusion"

#### Version 1: Temperatur-Stufen-Extraktion

**Allgemeine Einstellungen:**

- **Kaffee**: 16 g

- 

- **Gesamtwasser**: 272 g

- **Mahlgrad (xbloom Skala 1-80)**: 55

- **Mahlwerk-RPM**:  RPM

- **Gesamtbrühzeit (geschätzt)**: 03:25

**Brühschritte:**

|Phase |Wassermenge (g) |Temp. (°C) |Flussrate (ml/s) |Pause (s) |Gießmuster |Vibration |
|Bloom |40 |86 |3.0 | | |- |
|Guss 2 |80 |87 |3.2 |40 | |- |
|Guss 3 |80 |90 |3.4 |40 | |- |
|Guss 4 |72 |88 |3.4 |0 | |- |

**Anmerkungen/Begründung (Version 1):**

- **Intention & Überlegenheit**: Dieses Rezept zielt darauf ab, die Aromen gezielt zu schichten, indem es die Temperaturempfindlichkeit verschiedener chemischer Verbindungen ausnutzt. Es ist dem ausgewogenen Ansatz überlegen, weil es die "Erdbeere" (extrahiert bei niedrigeren Temperaturen) von der "Milchschokolade" (benötigt etwas mehr Energie) trennt.

- **Temperaturprofil-Begründung**: Die sehr niedrige Starttemperatur von 86°C dient der maximalen Schonung der flüchtigen Fruchtester (Erdbeere). Der Sprung auf 90°C im dritten Guss liefert die nötige Energie, um Maillard-Produkte und Zuckerkomplexe (Milchschokolade) zu lösen. Der letzte Guss mit 88°C spült die verbleibenden Zucker aus, ohne Bitterkeit zu erzeugen.

**Hypothetischer Feedback-Loop & Korrektur:**

- **Identifizierte Schwäche (V1)**: Die Komplexität könnte zu Lasten des Körpers gehen. Das Ergebnis ist möglicherweise aromatisch, aber im Mundgefühl zu dünn oder "teetartig".

- **Korrekturmaßnahme (V2)**: Um den Körper zu stärken (d.h. die Total Dissolved Solids, TDS, zu erhöhen), wird eine gezielte Agitation hinzugefügt und das Brühverhältnis leicht konzentriert.

#### Version 2: "Layered Fruit Infusion" - Body-Boost

**Allgemeine Einstellungen:**

- **Kaffee**: 16 g

- 

- **Gesamtwasser**: **264 g** (geändert)

- **Mahlgrad (xbloom Skala 1-80)**: 55

- **Mahlwerk-RPM**:  RPM

- **Gesamtbrühzeit (geschätzt)**: 03:15

**Brühschritte:**

|Phase |Wassermenge (g) |Temp. (°C) |Flussrate (ml/s) |Pause (s) |Gießmuster |Vibration |
|Bloom |40 |86 |3.0 | | |- |
|Guss 2 |80 |87 |3.2 |40 | |- |
|Guss 3 |80 |90 |3.4 |40 | | |
|Guss 4 |**64 g** (geändert) |88 |3.4 |0 | |- |

**Anmerkungen/Begründung (Version 2):**

- Die Konzentration des Brühverhältnisses auf 1:16.5 erhöht die finale Stärke (TDS) des Getränks weiter und sorgt für ein volleres, runderes Mundgefühl, das die aromatische Komplexität unterstützt.

---

#### Rezept 3: Kreatives Iced Brew Rezept: "Apricot Shock"

#### Version 1: High-Energy Konzentrat

**Allgemeine Einstellungen:**

- **Kaffee**: 16 g

- 

- 

- **Gesamtwasser**: 160 g

- **Mahlgrad (xbloom Skala 1-80)**: 44

- **Mahlwerk-RPM**: 90 RPM

- **Gesamtbrühzeit (geschätzt)**: 02:10

**Brühschritte:**

|Phase |Wassermenge (g) |Temp. (°C) |Flussrate (ml/s) |Pause (s) |Gießmuster |Vibration |
|Bloom |40 |93 |3.0 |30 | | |
|Guss 2 |60 |94 |3.5 |25 | |- |
|Guss 3 |60 |92 |3.5 |0 | |- |

**Anmerkungen/Begründung (Version 1):**

- **Intention & Überlegenheit**: Dieses Rezept erzeugt ein intensives Konzentrat, das durch das sofortige Abkühlen auf Eis ("Flash Chilling") seine flüchtigen Fruchtaromen (insbesondere Aprikose) behält.

**Hypothetischer Feedback-Loop & Korrektur:**

- **Identifizierte Schwäche (V1)**: Trotz der aggressiven Parameter könnte das Ergebnis leicht unterextrahiert schmecken und eine gewisse "Leere" im Geschmack aufweisen, sobald das gesamte Eis geschmolzen ist.

- **Korrekturmaßnahme (V2)**: Um die Extraktionstiefe weiter zu erhöhen und dem Getränk mehr Komplexität und Süße zu verleihen, wird die Wassermenge leicht erhöht und ein Bypass mit heißem Wasser hinzugefügt.

#### Version 2: "Apricot Shock" - Sweetness-Finish

**Allgemeine Einstellungen:**

- **Kaffee**: 16 g

- 

- 

- **Gesamtwasser**: **168 g** (geändert)

- **Mahlgrad (xbloom Skala 1-80)**: 44

- **Mahlwerk-RPM**: 90 RPM

- **Gesamtbrühzeit (geschätzt)**: 02:20

**Brühschritte:**

|Phase |Wassermenge (g) |Temp. (°C) |Flussrate (ml/s) |Pause (s) |Gießmuster |Vibration |
|Bloom |40 |93 |3.0 |30 | | |
|Guss 2 |64 |94 |3.5 |25 | |- |
|Guss 3 |64 |92 |3.5 |0 | |- |
|**Bypass** |**15 g** (hinzugefügt) |**** |- |- |- |- |

**Anmerkungen/Begründung (Version 2):**

- **Begründung der Korrektur**: Die Erhöhung des Brühwassers auf 168 g (1:10.5) treibt die Extraktion weiter voran. Der entscheidende Schritt ist der 15g Bypass mit °C heißem Wasser. Anstatt das Konzentrat nur mit dem Schmelzwasser zu verdünnen, fügt der Bypass eine kontrollierte Menge warmen Wassers hinzu. Dies hebt die finale Temperatur des Getränks leicht an, was die Wahrnehmung von Süße und Komplexität verbessert, ohne die erfrischende Kühle zu opfern. Es ist eine Technik, um die "Schock"-Aromatik beizubehalten, aber die finale Tasse runder und vollständiger zu gestalten.

---

#### Umgang mit Datenlücken

- **Röstgrad**: Das Etikett gibt "FILTER" an. Für einen Spezialitätenkaffee mit den Noten "Strawberry" und "Apricot" wurde ein heller Röstgrad ("Hell / Light") angenommen, da diese Noten typischerweise bei schonenden, hellen Röstungen am besten zur Geltung kommen. Dies ist eine Annahme mit hohem Konfidenzlevel.

---

#### Selbst-Konsistenz-Prüfung

- 

- **Die Wahl basiert auf der folgenden Priorität**:
*

  - **Varietät**: Der Los Pirineos ist eine "Elite Bourbon", der Joven Macario ist eine Mischung aus "Typica, Bourbon".

  - **Herkunft**: El Salvador und Mexiko sind beides mittelamerikanische Länder, deren Kaffees oft ähnliche Grundprofile aufweisen können, auch wenn sie unterschiedlich sind.

**Parameter-Vergleich:**

|Parameter |Aktuelles Rezept (Rezept 1) |Vorheriges Rezept (Joven Macario) |Abweichung & Begründung (>5% Abweichung) |
|Mahlgrad |53 | |**+17.8%**: Mein Rezept verwendet einen deutlich gröberen Mahlgrad. Begründung: Ein "Black Honey" ist typischerweise der intensivste und löslichste der Honey-Prozesse. Um eine Überextraktion der leicht fermentierten Noten zu vermeiden und die Klarheit zu erhöhen, ist ein gröberer Mahlgrad eine logische defensive Anpassung im Vergleich zum Red Honey. |
|Peak-Temp. |89 °C | |**-3.3%**: Kein signifikanter Unterschied. Die leicht niedrigere Temperatur in meinem Rezept ist konsistent mit der defensiveren Herangehensweise, die für einen Black Honey im Vergleich zu einem Red Honey erforderlich ist, um die delikaten Fruchtnoten zu schützen. |
|RPM |75 | |**+7.1%**: Die leicht höhere RPM in meinem Rezept kompensiert den gröberen Mahlgrad, indem sie eine gleichmäßigere Partikelverteilung anstrebt, ohne die Fines-Produktion drastisch zu erhöhen. Es ist eine Feinabstimmung, um die Extraktion trotz des gröberen Mahlgrads effizient zu halten. |

[ENDE DER REZEPTERSTELLUNG]
