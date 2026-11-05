---
titel: Nenn mir Rezepte für 1 und 3
status: aktiv
datum: '2026-03-01'
quelle:
  typ: gemini
  url: https://gemini.google.com/app/ba616feecd072e82
  hinweis: Nenn mir 5 Produkte, die ich mit frischer Vollmilch herstellen kann
importiert: true
---

> **Frage im Chat:** Nenn mir Rezepte für 1 und 3

#### 1. Gewichtungs-Check

- **Priorität 1 (Geschmack):** Maximale Viskosität und Cremigkeit durch gezielte Denaturierung von β-Lactoglobulin vor der Fermentation.

- **Priorität 2 (Gesundheit):** Hohe Dichte an aktiven probiotischen Kulturen, intaktes Fettsäurespektrum.

- **Priorität 3 (Aufwand):** Mittlere Aktivzeit für die thermische Vorbehandlung, dominierender Passiv-Anteil während der Gärung.

#### 2. Zutaten, Wasserwahl & Hardware-Mapping

|Komponente |Spezifikation / Menge |Hardware / Wasserwahl |
|Vollmilch |1000 g |Timemore Basic 2 Waage |
|Joghurt-Starter |50 g (aktiver thermophiler Joghurt, z. B. L. bulgaricus / S. thermophilus) |Timemore Basic 2 Waage |
|Sterilisationswasser |ca. 500 g. **Ungefiltert (Option A)**. |BLANCO EVOL-S Pro. Begründung: Dient ausschließlich dem Auskochen der Fermentationsgefäße. Da keine chemische Interaktion mit dem Endprodukt stattfindet, ist der Einsatz des Filters unwirtschaftlich. |
|Hitzequelle (Vorbereitung) |- |Berbel BKA 83 DLP E07 |
|Inkubation |Ziel: 43 °C |Bosch HNG978NB1 (Gärstufe/Dampf) |
|Temperatur-/pH-Messung |Ziel: 90 °C / pH 4,5 - 4,6 |CIRYCASE Thermometer / Apera Instruments PH60F |
|Kühlung |Ziel: 4 °C |Bosch KIF86PFE0 |

#### 3. Q/A-Analyse

- **Metrik:** Aktivzeit: 15 Min. Passivzeit: 8–10 Stunden.

- **Berechnung:** Die thermische Vorbehandlung (Aufrechterhaltung von 90 °C für 10 Minuten) skaliert linear mit der Viskosität (Qualität). Der Aufwand ist gering, erfordert jedoch Präsenz.

- **Bedingung für Alternativszenarien:** Erfüllt. Die manuelle Temperaturführung bindet Arbeitszeit. Ein Low-Effort-Szenario wird generiert.

#### 4. Prozess (Maximal-Qualität)

1. Glasgefäße mit kochendem Wasser (Option A) sterilisieren.

2. 1000 g Vollmilch in einem induktionsfähigen Edelstahltopf auf der Berbel BKA 83 DLP E07 unter Rühren auf 90 °C erhitzen (Messung via CIRYCASE).

3. Temperatur für exakt 10 Minuten bei 90 °C halten, um Molkenproteine zu denaturieren (erhöht die Wasserbindungskapazität des Endprodukts).

4. Topf in ein kaltes Wasserbad setzen und zügig auf 43 °C herunterkühlen.

5. 50 g Joghurt-Starter mit einem Schneebesen homogen einrühren.

6. Mischung in die Glasgefäße füllen und verschließen.

7. Im Bosch HNG978NB1 bei der spezifischen Gärstufe (oder manuell auf 43 °C) für 8 bis 10 Stunden inkubieren.

8. Nach 8 Stunden den pH-Wert mit dem Apera PH60F prüfen. Bei Erreichen von pH 4,5 bis 4,6 die Fermentation abbrechen.

9. Gefäße zur Stabilisierung des Koagels mindestens 12 Stunden im Bosch KIF86PFE0 (4 °C) kühlen.

#### 5. Prozess (Low-Effort-Alternative)

1. 1000 g Vollmilch in den Edelstahltopf des Instant Pot Pro Wifi geben.

2. Funktion Yogurt anwählen, Modus auf Boil setzen.

3. Nach automatischem Abschluss den Innentopf entnehmen und abkühlen lassen, bis das Display (oder das CIRYCASE Thermometer) ca. 43 °C anzeigt.

4. 50 g Joghurt-Starter einrühren.

5. Topf zurück in den Instant Pot setzen, Funktion Yogurt anwählen und Zeit auf 8 Stunden setzen.

6. Nach Ablauf direkt in den Kühlschrank überführen.
Resultat: Nahezu vollständige Automatisierung. Geringfügiger Viskositätsverlust durch die fehlende 10-minütige Haltephase bei 90 °C.

---

#### Rezept 3: Ricotta (Hitze-Säure-Präzipitation)

#### 1. Gewichtungs-Check

- **Priorität 1 (Geschmack):** Sehr feine, süßliche Textur durch optimale Aggregation der Molkenproteine und Rest-Caseine.

- **Priorität 2 (Gesundheit):** Höchste biologische Wertigkeit durch Extraktion der hitzeempfindlichen Molkenproteine.

- **Priorität 3 (Aufwand):** Kontinuierliche Überwachung am Induktionsfeld zwingend erforderlich für die Maximal-Qualität.

#### 2. Zutaten, Wasserwahl & Hardware-Mapping

|Komponente |Spezifikation / Menge |Hardware / Wasserwahl |
|Süßmolke (frisch) |2000 g (z. B. Nebenprodukt der Paneer-Produktion) |Timemore Basic 2 Waage |
|Vollmilch |200 g |Timemore Basic 2 Waage |
|Zitronensäure (kristallin) |6 g |Timemore Basic 2 Waage |
|Lösungswasser |40 g. **Gefiltert (Option B)**. |BLANCO EVOL-S Pro. Begründung: Wie beim Paneer verhindert das gefilterte Wasser mit reduzierter Karbonathärte eine Pufferung der Zitronensäure. Dies erlaubt ein millimetergenaues Aussteuern des isoelektrischen Punktes. |
|Hitzequelle |- |Berbel BKA 83 DLP E07 |
|Temperatur-/pH-Messung |Ziel: 85–90 °C / pH 5,9 - 6,0 |CIRYCASE Thermometer / Apera Instruments PH60F |

#### 3. Q/A-Analyse

- **Metrik:** Aktivzeit: 20 Min. Passivzeit: 20 Min.

- **Berechnung:** Der Aufwand skaliert linear. Die exakte Erfassung des Temperaturfensters (85–90 °C) in Kombination mit einem spezifischen pH-Wert verhindert gummiartige, körnige Texturen.

- **Bedingung für Alternativszenarien:** Erfüllt. Die feinen Flocken erfordern präzises, ruhiges Erhitzen ohne Turbulenzen. Eine alternative Automatisierung wird abgebildet.

#### 4. Prozess (Maximal-Qualität)

1. 2000 g Molke und 200 g Vollmilch in einem induktionsfähigen Topf mischen.

2. Auf der Berbel BKA 83 DLP E07 bei mittlerer Leistung langsam auf 85 bis 90 °C erhitzen. Kontinuierlich mit dem CIRYCASE Thermometer überwachen. Starke Konvektion (Sprudeln) zwingend vermeiden, da dies die fragilen Proteinnetzwerke zerstört.

3. Bei Erreichen der Zieltemperatur die Induktionszone deaktivieren.

4. Zitronensäure im Lösungswasser (Option B) auflösen.

5. Die Säurelösung tröpfchenweise zugeben. Dabei mit dem Apera PH60F den pH-Wert messen. Zielwert ist exakt pH 5,9 bis 6,0.

6. Sobald die Proteine ausflocken und an die Oberfläche steigen, jegliche mechanische Bewegung einstellen.

7. 20 Minuten ruhen lassen, damit die Flocken aggregieren und aushärten.

8. Die flotierende Ricotta-Masse mit einer Schaumkelle vorsichtig abheben und in einem feinen Sieb abtropfen lassen.

#### 5. Prozess (Low-Effort-Alternative)

1. Molke und Vollmilch in den Edelstahl-Innentopf des Instant Pot Pro Wifi füllen.

2. Sous-Vide-Funktion (falls bei diesem spezifischen Pro-Modell vorhanden, alternativ Slow Cook auf High) nutzen und Zieltemperatur auf 90 °C einstellen.

3. Nach Erreichen der Zieltemperatur (akustisches Signal) den Deckel öffnen.

4. Zitronensäurelösung auf einmal zugeben und einmalig leicht umrühren.

5. Gerät ausschalten, 20 Minuten ruhen lassen.

6. Masse abseihen.
Resultat: Eliminiert die Überwachungszeit am Herd. Die stärkere Konvektion im Instant Pot (aufgrund der Bodenheizung) kann jedoch zu einer feineren Fragmentierung der Flocken und damit zu einer etwas grieseligeren Textur sowie leicht verminderter Ausbeute führen.
