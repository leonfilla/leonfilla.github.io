import React, { useState, useEffect } from 'react';

// Icons (angenommen, diese sind wie in der vorherigen Version definiert)
const ChevronDownIcon = () => (
  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6 transition-transform duration-300">
    <path strokeLinecap="round" strokeLinejoin="round" d="m19.5 8.25-7.5 7.5-7.5-7.5" />
  </svg>
);
const ChevronUpIcon = () => (
    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6 transition-transform duration-300">
      <path strokeLinecap="round" strokeLinejoin="round" d="m4.5 15.75 7.5-7.5 7.5 7.5" />
    </svg>
);
const CoffeeBeanIcon = () => (
    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="w-5 h-5 mr-2 text-yellow-700"> {/* Increased margin */}
        <path strokeLinecap="round" strokeLinejoin="round" d="M14.25 7.75a4.125 4.125 0 0 0-4.173-4.123A4.125 4.125 0 0 0 5.827 7.75c0 4.113 3.324 7.437 7.437 7.437 4.113 0 7.437-3.324 7.437-7.437 0-.134-.007-.266-.02-.398M14.25 7.75c-.013.132-.02.264-.02.398m0 0A4.11 4.11 0 0 1 10.08 11.873A4.11 4.11 0 0 1 5.827 7.75m8.423 0c0-2.28-1.846-4.125-4.125-4.125M5.827 7.75c0-2.28 1.846-4.125 4.125-4.125m0 0a4.125 4.125 0 0 1 4.125 4.125m-4.125-4.125V3.625m0 4.125c-1.036 0-1.99.403-2.725 1.138C6.403 9.71 6 10.665 6 11.75c0 1.035.403 1.99.902 2.725.502.734 1.168 1.275 1.923 1.625" />
    </svg>
);
const ExternalLinkIcon = () => (
  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-4 h-4 ml-1">
    <path strokeLinecap="round" strokeLinejoin="round" d="M13.5 6H5.25A2.25 2.25 0 0 0 3 8.25v10.5A2.25 2.25 0 0 0 5.25 21h10.5A2.25 2.25 0 0 0 18 18.75V10.5m-10.5 6L21 3m0 0h-5.25M21 3v5.25" />
  </svg>
);

// Überarbeitete Kaffeedaten mit Fokus auf Lesbarkeit, Wissenschaftlichkeit und Geschmacksprofil (Süße, Körper, Fruchtigkeit)
const coffeeData = [
  {
    id: 'uraga',
    name: 'Uraga Raro Boda Omniroast (Kaffeekirsche)',
    isDecaf: false,
    shortDescription: 'Äthiopien Natural: Intensive rote Beeren, floraler Jasmin, voller Körper & ausgeprägte Süße.',
    mainImage: 'https://placehold.co/600x400/A855F7/FFFFFF?text=Uraga+Raro',
    colorAccent: 'bg-purple-600',
    textColorAccent: 'text-purple-700',
    borderColorAccent: 'border-purple-500',
    bgColorAccentLight: 'bg-purple-50',
    details: {
      sorte: 'Äthiopien Natural Omniroast',
      menge: 16,
      verhaeltnis: '1:16.0',
      wasserGesamt: 256,
      mahlgrad: 59, // Eher mittel-grob für Klarheit bei Naturals
      rpm: 70, // Niedriger für weniger Fines, schont florale Noten
      aromaProfil: 'Äthiopischer Natural Omniroast, der durch seine ausgeprägte Süße, Noten von roten Beeren und Jasmin sowie einen vollen, klaren Körper besticht. Ziel ist es, die delikaten floralen Jasminnoten zu schützen, die intensive Fruchtigkeit roter Beeren und die Süße hervorzuheben und einen runden Körper zu entwickeln.',
      aufgussStrategieText: 'Eine gestaffelte Aufgussstrategie mit spezifischen Mustern und einem leicht fallenden Temperaturprofil wird verwendet. Moderate Flussraten und niedrige Mahlwerk-RPM (70) schützen die delikaten Aromen. Auf Vibration wird verzichtet, um Klarheit zu maximieren und die Süße und Fruchtigkeit zu fördern, was zu einem vollen Körper ohne Bitterkeit führt.',
      aufgussStrategiePunkte: [
        'Blooming (92°C, Spiralförmig): Sanftes Öffnen der Aromen, Vorbereitung für gleichmäßige Extraktion.',
        'Aufguss 2 (80ml, 93°C, Spiralförmig): Betont Fruchtigkeit (rote Beeren) und florale Noten (Jasmin) durch leicht erhöhte Temperatur.',
        'Aufguss 3 (80ml, 92°C, Kreisförmig): Entwickelt Süße und Körper durch sanftere Extraktion und leicht reduzierte Temperatur.',
        'Aufguss 4 (48ml, 90°C, Zentral): Rundet den Körper ab und fokussiert auf Balance, vermeidet Überextraktion durch geringeres Volumen und Temperatur.'
      ],
      brewSteps: [
        { phase: 'Blooming', menge: 48, temp: 92, durchfluss: 3.0, pause: 40, muster: 'Spiralförmig', vibVor: 'Nein', vibNach: 'Nein', dauer: 56 },
        { phase: 'Aufguss 2', menge: 80, temp: 93, durchfluss: 3.2, pause: 30, muster: 'Spiralförmig', vibVor: 'Nein', vibNach: 'Nein', dauer: 55 },
        { phase: 'Aufguss 3', menge: 80, temp: 92, durchfluss: 3.0, pause: 30, muster: 'Kreisförmig', vibVor: 'Nein', vibNach: 'Nein', dauer: 57 },
        { phase: 'Aufguss 4', menge: 48, temp: 90, durchfluss: 3.0, pause: 0, muster: 'Zentral', vibVor: 'Nein', vibNach: 'Nein', dauer: 16 },
      ],
      gesamtBruehzeit: '3:04',
      anmerkungenTabelle: "Fokus: Schutz der Jasminnote, Betonung von intensiver Frucht (rote Beeren) & ausgeprägter Süße, voller & klarer Körper. Keine Vibration für maximale Klarheit."
    }
  },
  {
    id: 'gran_galope',
    name: 'Gran Galope Filter (Kaffeekirsche)',
    isDecaf: false,
    shortDescription: 'Kolumbien Washed: Saftige Schwarzbeere, Melasse-Süße, Hauch Pampelmuse, voller Körper.',
    mainImage: 'https://placehold.co/600x400/16A34A/FFFFFF?text=Gran+Galope',
    colorAccent: 'bg-green-600',
    textColorAccent: 'text-green-700',
    borderColorAccent: 'border-green-500',
    bgColorAccentLight: 'bg-green-50',
    details: {
      sorte: 'Kolumbien Washed Filter',
      menge: 16,
      verhaeltnis: '1:15.5', // Etwas enger für mehr Körper und Süße
      wasserGesamt: 248,
      mahlgrad: 56, // Etwas feiner für Washed, um Süße und Körper zu fördern
      rpm: 80, // Mittel, guter Kompromiss für Washed
      aromaProfil: 'Kolumbianischer Washed Filter, charakterisiert durch Noten von Schwarzbeere und Pampelmuse, ergänzt durch eine tiefe Melasse-Süße und einen vollen Körper. Ziel ist es, eine saftige, klare Fruchtigkeit und lebendige Säure zu erzielen, die Melasse-Süße voll zu entwickeln und einen präsenten Körper mit guter Klarheit zu schaffen.',
      aufgussStrategieText: 'Initiale höhere Temperaturen und Flussraten zielen auf die Extraktion von Säure und Frucht. Darauf folgen gestaffelte Güsse mit spezifischen Mustern und leicht fallender Temperatur, um Süße und Körper auszubalancieren. Mittlere Mahlwerk-RPM (80) unterstützen eine gleichmäßige Extraktion. Eine kurze Vibration nach dem Blooming dient der Nivellierung des Kaffeebetts für eine homogenere Extraktion.',
      aufgussStrategiePunkte: [
        'Blooming (95°C, Spiralförmig): Hohe Temperatur für optimale Entgasung und Vorbereitung der Fruchtextraktion.',
        'Vibration nach Blooming: "Ja" zur einmaligen Nivellierung des Kaffeebetts für gleichmäßigere Folgeextraktionen.',
        'Aufguss 2 (70ml, 95°C, Spiralförmig): Betont Säure und Frucht (Schwarzbeere, Pampelmuse) durch hohe Temperatur und dynamisches Muster.',
        'Aufguss 3 (70ml, 94°C, Spiralförmig): Beginnt mit der Entwicklung von Süße (Melasse) und Körper bei leicht reduzierter Temperatur.',
        'Aufguss 4 (60ml, 93°C, Zentral): Finalisiert die Extraktion, fokussiert auf Körper und Balance bei weiter reduzierter Temperatur.'
      ],
      brewSteps: [
        { phase: 'Blooming', menge: 48, temp: 95, durchfluss: 3.2, pause: 30, muster: 'Spiralförmig', vibVor: 'Nein', vibNach: 'Ja', dauer: 45 },
        { phase: 'Aufguss 2', menge: 70, temp: 95, durchfluss: 3.4, pause: 25, muster: 'Spiralförmig', vibVor: 'Nein', vibNach: 'Nein', dauer: 46 },
        { phase: 'Aufguss 3', menge: 70, temp: 94, durchfluss: 3.4, pause: 25, muster: 'Spiralförmig', vibVor: 'Nein', vibNach: 'Nein', dauer: 46 },
        { phase: 'Aufguss 4', menge: 60, temp: 93, durchfluss: 3.2, pause: 0, muster: 'Zentral', vibVor: 'Nein', vibNach: 'Nein', dauer: 19 },
      ],
      gesamtBruehzeit: '2:36',
      anmerkungenTabelle: "Fokus: Saftige Säure (Pampelmuse) & Frucht (Schwarzbeere), ausgeprägte Melasse-Süße, voller Körper. Vibration nach Bloom zur Bett-Nivellierung."
    }
  },
  {
    id: 'kenya_aa',
    name: 'Kenya AA Top Githima Filter (Kaffeekirsche)',
    isDecaf: false,
    shortDescription: 'Kenia Washed Doppel-Fermentiert: Komplexer Schwarztee, Pflaume, Physalis, elegante Süße.',
    mainImage: 'https://placehold.co/600x400/3B82F6/FFFFFF?text=Kenya+AA',
    colorAccent: 'bg-blue-600',
    textColorAccent: 'text-blue-700',
    borderColorAccent: 'border-blue-500',
    bgColorAccentLight: 'bg-blue-50',
    details: {
      sorte: 'Kenia Washed Doppel-Fermentiert Filter/Omni',
      menge: 16,
      verhaeltnis: '1:16.0',
      wasserGesamt: 256,
      mahlgrad: 61, // Eher grob wegen Doppel-Fermentation (höhere Löslichkeit)
      rpm: 65, // Sehr niedrig, um Fines zu minimieren und Überextraktion vorzubeugen
      aromaProfil: 'Ein Kenia Washed Doppel-Fermentiert Filterkaffee mit komplexen Noten von Schwarztee, saftiger Pflaume und spritziger Physalis. Er zeichnet sich durch einen lang anhaltenden Körper, eine subtile, elegante Süße und eine lebendige, aber angenehme Säure aus. Ziel ist es, die subtile Süße und den komplexen Körper zu entwickeln, die spritzige Säure harmonisch einzubinden und eine teenähnliche Klarheit zu erreichen.',
      aufgussStrategieText: 'Aufgrund der hohen Löslichkeit durch die doppelte Fermentation werden sanfte Brühparameter gewählt: niedrigere Temperaturen, geringere Flussraten und eine niedrige Mahlwerk-RPM (65). Längere Pausen zwischen den Güssen unterstützen eine kontrollierte Extraktion. Auf Vibration wird verzichtet, um die Klarheit und die delikaten Aromen zu bewahren.',
      aufgussStrategiePunkte: [
        'Blooming (92°C, Kreisförmig): Sanftes Blooming zur schonenden Vorbereitung, wichtig bei hochlöslichen Kaffees.',
        'Aufguss 2 (70ml, 93°C, Spiralförmig): Sanfter Start zur Entfaltung von Säure (Physalis, Pflaume) und Klarheit.',
        'Aufguss 3 (70ml, 92°C, Spiralförmig): Kontrollierte Extraktion zur Entwicklung von Süße und Komplexität (Schwarztee).',
        'Aufguss 4 (68ml, 91°C, Zentral): Entwicklung des lang anhaltenden Körpers und Balance bei niedrigerer Temperatur.'
      ],
      brewSteps: [
        { phase: 'Blooming', menge: 48, temp: 92, durchfluss: 3.0, pause: 40, muster: 'Kreisförmig', vibVor: 'Nein', vibNach: 'Nein', dauer: 56 },
        { phase: 'Aufguss 2', menge: 70, temp: 93, durchfluss: 3.1, pause: 35, muster: 'Spiralförmig', vibVor: 'Nein', vibNach: 'Nein', dauer: 58 },
        { phase: 'Aufguss 3', menge: 70, temp: 92, durchfluss: 3.1, pause: 35, muster: 'Spiralförmig', vibVor: 'Nein', vibNach: 'Nein', dauer: 58 },
        { phase: 'Aufguss 4', menge: 68, temp: 91, durchfluss: 3.0, pause: 0, muster: 'Zentral', vibVor: 'Nein', vibNach: 'Nein', dauer: 23 },
      ],
      gesamtBruehzeit: '3:15',
      anmerkungenTabelle: "Fokus: Spritzige Säure (Pflaume/Physalis), subtile Süße, komplexer Schwarztee-Körper. Keine Vibration zur Wahrung der Klarheit bei diesem delikaten Kaffee."
    }
  },
  {
    id: 'popayan_decaf',
    name: 'Popayan Reserve Decaf (Kaffeekirsche)',
    isDecaf: true,
    shortDescription: 'Kolumbien E.A. Decaf: Süßes Zuckerrohr, Kakaonibs, Bergpfirsich, präsente Süße.',
    mainImage: 'https://placehold.co/600x400/EF4444/FFFFFF?text=Popayan+Decaf',
    colorAccent: 'bg-red-600',
    textColorAccent: 'text-red-700',
    borderColorAccent: 'border-red-500',
    bgColorAccentLight: 'bg-red-50',
    details: {
      sorte: 'Kolumbien E.A. Decaf Omniroast',
      menge: 16,
      verhaeltnis: '1:15.0', // Enger für mehr Süße und Körper bei Decafs
      wasserGesamt: 240,
      mahlgrad: 60, // Mittel, Decafs können fragiler sein
      rpm: 60, // Niedrigste RPM zur Minimierung von Fines und Schonung
      aromaProfil: 'Ein Kolumbien E.A. Decaf Omniroast, der mit Noten von süßem Zuckerrohr, feinen Kakaonibs und saftigem Bergpfirsich überzeugt. Er bietet einen fruchtbetonten Körper, eine sehr präsente Süße und eine milde, angenehme Säure. Ziel ist es, maximale Süße und klare Fruchtnoten zu extrahieren, einen angenehmen Körper zu formen und jegliche Bitterkeit durch sorgfältiges Fines-Management zu minimieren.',
      aufgussStrategieText: 'Die Strategie zielt auf maximale Schonung des Kaffees. Eine reduzierte Anzahl von Güssen (nur ein Hauptaufguss), ein sanftes Aufgussmuster, die niedrigste Mahlwerk-RPM (60) und eine konstante, moderate Temperatur (93°C) werden verwendet. Auf Vibration wird verzichtet, um die Migration von Feinstpartikeln zu verhindern und die Süße zu schützen.',
      aufgussStrategiePunkte: [
        'Blooming (93°C, Kreisförmig): Konstante, moderate Temperatur für sanfte Entgasung.',
        'Aufguss 2 (192ml, 93°C, Spiralförmig): Einziger, großer Hauptaufguss zur Minimierung der Agitation und zur gleichmäßigen Extraktion von Süße (Zuckerrohr, Bergpfirsich) und Körper (Kakaonibs).'
      ],
      brewSteps: [
        { phase: 'Blooming', menge: 48, temp: 93, durchfluss: 3.0, pause: 35, muster: 'Kreisförmig', vibVor: 'Nein', vibNach: 'Nein', dauer: 51 },
        { phase: 'Aufguss 2', menge: 192, temp: 93, durchfluss: 3.0, pause: 0, muster: 'Spiralförmig', vibVor: 'Nein', vibNach: 'Nein', dauer: 64 },
      ],
      gesamtBruehzeit: '1:55',
      anmerkungenTabelle: "Fokus: Maximale Süße (Zuckerrohr) & fruchtiger Körper (Bergpfirsich), minimale Bitterkeit. Ein Hauptaufguss für schonende Süße- und Körperentwicklung. Keine Vibration."
    }
  },
  {
    id: 'kijani_kiboko_decaf',
    name: 'Kijani Kiboko Decaf Filter', // Name angepasst für Konsistenz
    isDecaf: true,
    shortDescription: 'Kenia CO₂ Decaf: Johannisbeere, Grapefruit, dunkle Trauben, seidiges Mundgefühl.',
    mainImage: 'https://placehold.co/600x400/F59E0B/FFFFFF?text=Kijani+Kiboko', 
    colorAccent: 'bg-amber-500',
    textColorAccent: 'text-amber-700',
    borderColorAccent: 'border-amber-500',
    bgColorAccentLight: 'bg-amber-50',
    details: {
      sorte: 'Kenia CO₂ Decaf Filter',
      menge: 16, // Konsistent mit anderen Rezepten, falls "19grams" nicht spezifisch für dieses Rezept war
      verhaeltnis: '1:15.5', 
      wasserGesamt: 248, 
      mahlgrad: 58, // Mittel für CO2 Decaf
      rpm: 60, // Niedrigste RPM für schonende Extraktion
      aromaProfil: 'Ein Kenia CO₂ Decaf Filterkaffee, der mit typischen Kenia-Noten von schwarzer Johannisbeere und Grapefruit sowie süßen dunklen Trauben begeistert. Er besitzt ein besonders seidiges Mundgefühl. Ziel ist es, die delikaten Fruchtnoten und die Süße präzise herauszuarbeiten und ein geschmeidiges, seidiges Mundgefühl zu entwickeln.',
      aufgussStrategieText: 'Eine sanfte, vielschichtige Extraktion wird angestrebt. Spezifische Aufgussmuster, ein leicht fallendes Temperaturprofil und die niedrigste Mahlwerk-RPM (60) sorgen für eine schonende Behandlung. Auf Vibration wird verzichtet, um die feinen Aromen und die Klarheit zu bewahren. Die Gesamtwassermenge ist an die Rösterempfehlung angepasst, um das optimale Geschmacksprofil zu treffen.',
      aufgussStrategiePunkte: [
        'Blooming (92°C, Kreisförmig): Sanfte Vorbereitung zur Aktivierung der Aromen.',
        'Aufguss 2 (70ml, 93°C, Spiralförmig): Aktivierung der Fruchtnoten (Johannisbeere, Grapefruit).',
        'Aufguss 3 (70ml, 92°C, Spiralförmig): Entwicklung von Süße (dunkle Trauben) und des seidigen Mundgefühls.',
        'Aufguss 4 (60ml, 91°C, Zentral): Finalisierung der Extraktion, Betonung des Mundgefühls und der Balance.'
      ],
      brewSteps: [
        { phase: 'Blooming', menge: 48, temp: 92, durchfluss: 3.0, pause: 35, muster: 'Kreisförmig', vibVor: 'Nein', vibNach: 'Nein', dauer: 51 },
        { phase: 'Aufguss 2', menge: 70, temp: 93, durchfluss: 3.1, pause: 30, muster: 'Spiralförmig', vibVor: 'Nein', vibNach: 'Nein', dauer: 53 },
        { phase: 'Aufguss 3', menge: 70, temp: 92, durchfluss: 3.1, pause: 30, muster: 'Spiralförmig', vibVor: 'Nein', vibNach: 'Nein', dauer: 53 },
        { phase: 'Aufguss 4', menge: 60, temp: 91, durchfluss: 3.0, pause: 0, muster: 'Zentral', vibVor: 'Nein', vibNach: 'Nein', dauer: 20 },
      ],
      gesamtBruehzeit: '2:57',
      anmerkungenTabelle: "Fokus: Klare Kenia-Frucht (Johannisbeere, Grapefruit), Süße (dunkle Trauben) & seidiges Mundgefühl. Keine Vibration für maximale Delikatesse."
    }
  },
  {
    id: 'huye_mountain_elbgold',
    name: 'HUYE MOUNTAIN | Natural (elbgold)', // Name leicht angepasst für Klarheit
    isDecaf: false,
    shortDescription: 'Ruanda Natural: Weisse Nektarine, Kakaonibs, Preiselbeere, ausgeprägte Fruchtsüße.',
    mainImage: 'https://placehold.co/600x400/DD6B20/FFFFFF?text=Huye+Mountain', 
    colorAccent: 'bg-orange-600', 
    textColorAccent: 'text-orange-700',
    borderColorAccent: 'border-orange-500',
    bgColorAccentLight: 'bg-orange-50',
    details: {
      sorte: 'Ruanda Red Bourbon (Natural)',
      produzent: 'David Rubanzangabo',
      region: 'Ruanda | Huye | Gishamvu',
      menge: 16,
      verhaeltnis: '1:16.0', 
      wasserGesamt: 256,     
      mahlgrad: 57, // Mittel-grob für Natural
      rpm: 60, // Niedrig für weniger Fines und klare Frucht
      aromaProfil: 'Ein Natural Red Bourbon aus Ruanda von David Rubanzangabo, der durch Aromen von weißer Nektarine, subtilen Kakaonibs und einer lebendigen Preiselbeer-Fruchtigkeit besticht. Ziel ist es, die ausgeprägte Fruchtsüße und die komplexen Aromen des Natural-Prozesses hervorzuheben, eine klare Tasse zu erzielen und einen angenehmen, runden Körper zu entwickeln.',
      aufgussStrategieText: 'Die Strategie fokussiert auf eine sanfte Extraktion, um die delikaten Fruchtnoten (weiße Nektarine, Preiselbeere) zu bewahren und die Süße der Kakaonibs harmonisch zu integrieren. Niedrigere Temperaturen und Mahlwerk-RPMs (60) helfen, Überextraktion zu vermeiden und die Klarheit zu fördern. Auf Vibration wird verzichtet, um die feinen Geschmacksnuancen nicht zu überdecken.',
      aufgussStrategiePunkte: [
        'Blooming (91°C, Kreisförmig): Sanftes Öffnen der Aromen bei moderater Temperatur, ideal für Naturals.',
        'Aufguss 2 (70ml, 92°C, Spiralförmig): Entfaltung der Fruchtigkeit (Nektarine, Preiselbeere).',
        'Aufguss 3 (70ml, 90°C, Kreisförmig): Entwicklung der Süße (Kakaonibs) und des Körpers bei reduzierter Temperatur.',
        'Aufguss 4 (68ml, 88°C, Zentral): Finalisierung für einen sauberen, ausgewogenen Abgang bei nochmals gesenkter Temperatur, um Bitterkeit zu vermeiden.'
      ],
      brewSteps: [ 
        { phase: 'Blooming', menge: 48, temp: 91, durchfluss: 3.0, pause: 45, muster: 'Kreisförmig', vibVor: 'Nein', vibNach: 'Nein', dauer: 61 }, 
        { phase: 'Aufguss 2', menge: 70, temp: 92, durchfluss: 3.0, pause: 30, muster: 'Spiralförmig', vibVor: 'Nein', vibNach: 'Nein', dauer: 53 }, 
        { phase: 'Aufguss 3', menge: 70, temp: 90, durchfluss: 3.0, pause: 30, muster: 'Kreisförmig', vibVor: 'Nein', vibNach: 'Nein', dauer: 53 }, 
        { phase: 'Aufguss 4', menge: 68, temp: 88, durchfluss: 3.0, pause: 0, muster: 'Zentral', vibVor: 'Nein', vibNach: 'Nein', dauer: 23 },      
      ],
      gesamtBruehzeit: '3:10', 
      anmerkungenTabelle: "Fokus: Fruchtige Süße (Weisse Nektarine, Preiselbeere) und Kakaonibs-Noten. Klarheit trotz Natural-Aufbereitung. Mittlerer Körper. Keine Vibration."
    }
  }
];


// Die GeneralInfoSection Komponente mit überarbeiteten Texten und angepasster Überschriften-Hierarchie
const GeneralInfoSection = ({isInfoOpen, setIsInfoOpen}) => (
    <div className="mb-8 p-6 bg-white rounded-lg shadow-lg">
        <button
            onClick={() => setIsInfoOpen(!isInfoOpen)}
            className="flex items-center justify-between w-full text-left text-2xl font-semibold text-gray-800 py-3 focus:outline-none"
        >
            Allgemeine Informationen zum Brühvorgang & xBloom Studio
            {isInfoOpen ? <ChevronUpIcon /> : <ChevronDownIcon />}
        </button>
        {isInfoOpen && (
            <div className="mt-4 text-gray-700 space-y-6 prose max-w-none 
                            prose-headings:text-gray-700 
                            prose-h3:text-xl prose-h3:font-semibold 
                            prose-h4:text-lg prose-h4:font-semibold prose-h4:text-gray-600 
                            prose-h5:text-base prose-h5:font-medium prose-h5:text-gray-600"> {/* H5 angepasst */}
                <section>
                    <h3>1. Zielsetzung der Rezepte</h3>
                    <p>Diese Sammlung von Brührezepten wurde entwickelt, um das volle Geschmackspotenzial ausgewählter Kaffeesorten mit dem xBloom Studio Kaffeeautomaten optimal zu entfalten. Der Fokus liegt auf der Nutzung der spezifischen Einstellmöglichkeiten des Geräts, um gezielt die Geschmacksdimensionen <strong>Süße, Fruchtigkeit und Körper</strong> zu betonen und zu optimieren.</p>
                    <p>Ein zentrales Anliegen ist die Anwendung wissenschaftlich fundierter und rösterspezifischer Aufgussstrategien. Diese umfassen die Anzahl der Aufgüsse, die Verteilung des Wasservolumens, die Auswahl passender Aufgussmuster und die Steuerung der Mahlwerk-Drehzahl.</p>
                    
                    <h4>Bedeutung präzisierter Parameter und der Aufgussstrategie</h4>
                    <p>Die präzise Steuerung jedes Brühparameters ist entscheidend, um gewünschte Aromakomponenten bestmöglich zu extrahieren und eine hohe Reproduzierbarkeit zu sichern. Die hier bereitgestellten detaillierten Angaben sind für eine einfache Übertragung in die xBloom App aufbereitet.</p>
                    <p>Die Aufgussstrategie – die Abfolge von Anzahl, Volumen, Dauer, Flussrate und Muster jedes Aufgusses sowie der Pausen – ist der Schlüssel zur gezielten Geschmacksbeeinflussung. Unterschiedliche Aromastoffe lösen sich verschieden schnell. Eine intelligente Aufgusssequenz nutzt diese Dynamiken für ein "Flavor Layering": Geschmacksfacetten werden sukzessive und kontrolliert extrahiert und harmonisch vereint.</p>
                    <p>Spezifische xBloom-Funktionen, wie die binäre Vibration (an/aus), erfordern bewusste Nutzung. Da Intensität/Dauer nicht justierbar sind, ist der Zeitpunkt kritisch. Ein Vibrationsimpuls muss sorgfältig gegen Risiken (Fines-Migration, Überextraktion) abgewogen werden. Die Rezepte berücksichtigen dies.</p>
                    
                    <h4>Hinweis auf die Rolle der Mahlwerk-Drehzahl (RPM)</h4>
                    <p>Die benutzerdefinierte Einstellung der Mahlwerk-Drehzahl (60-120 RPM) im xBloom Studio erweitert die Kontrolle über den Mahlprozess signifikant. Die Drehzahl beeinflusst die Partikelgrößenverteilung und Feinstpartikel-Produktion. Langsamere Drehzahlen sind oft vorteilhaft für Filterkaffee (weniger Fines, klarere Tasse, mehr Süße). Die RPM-Anpassung ist somit ein wichtiger Aspekt zur Feinabstimmung.</p>
                </section>
                <hr className="my-6"/>
                <section>
                    <h3>2. Verständnis der xBloom Studio Programmiermöglichkeiten</h3>
                    <p>Ein detailliertes Verständnis der Parameter ist grundlegend. Dieser Abschnitt erläutert Kernparameter und deren strategische Nutzung. "Dauer (s)" in den Brühschritten fasst Aufgusszeit und Pause zusammen.</p>
                    
                    <h4>2.1. Temperatursteuerung (Blooming & Aufgüsse)</h4>
                    <p>Das xBloom Studio erlaubt Temperaturen bis 95°C pro Phase. Die Temperatur beeinflusst, welche Aromen wie schnell gelöst werden. Höhere Temperaturen extrahieren intensiver (Risiko: Bitterkeit, Verlust delikater Noten). Niedrigere Temperaturen extrahieren sanfter (Risiko: Unterextraktion).</p>
                    <p>Phasenweise Temperaturkontrolle ermöglicht differenzierte Steuerung: Höher initial (Blooming, erster Hauptaufguss) für Säuren/Frucht. Später niedriger, um unerwünschte Verbindungen zu minimieren und Süße zu entwickeln.</p>
                    
                    <h4>2.2. Wasserdurchflussmenge (Blooming & Aufgüsse)</h4>
                    <p>Die Flussrate (3.0-3.5 ml/s) beeinflusst Kontaktzeit, Agitation und Extraktionsgleichmäßigkeit. Höher = mehr Agitation, niedriger = sanftere Benetzung.</p>
                    
                    <h4>2.3. Pausenzeiten (Zwischen Blooming/Aufgüssen)</h4>
                    <p>Pausen (0-59s) lassen das Kaffeebett setzen ("Drain Time"), fördern gleichmäßige Extraktion, reduzieren Channeling und beeinflussen Temperaturstabilität.</p>
                    
                    <h4>2.4. Aufgussmuster und ihre Auswirkungen</h4>
                    <p>Die drei Muster – "zentral", "spiralförmig", "kreisförmig" – definieren die Wasserapplikation und beeinflussen Agitation, Benetzung und Extraktion:</p>
                    <ul className="list-disc pl-5 mt-2 space-y-1">
                        <li><strong>Zentral:</strong> Wasserfokus mittig. Kann Verteilung fördern, birgt Channeling-Gefahr. Nützlich für Temperaturstabilität im Kern. Geringere Agitation am Rand. Oft für späte Güsse zur Körperbetonung.</li>
                        <li><strong>Spiralförmig:</strong> Gleichmäßige Wasserverteilung über größere Fläche. Fördert homogene Benetzung/Extraktion. Gut für Blooming und Hauptextraktion (Frucht, Süße).</li>
                        <li><strong>Kreisförmig:</strong> Sanfte, breite Kreise für schonende Sättigung. Geeignet für Blooming empfindlicher Kaffees oder Hauptaufgüsse mit geringer Agitation.</li>
                    </ul>
                    <p className="mt-2">Angesichts des engen Flussratenbereichs ist das Muster primäres Mittel zur Steuerung der Wasser-Kaffee-Interaktion.</p>
                    
                    <h4>2.5. Kaffeefilter-Vibration (an/aus) – Empfehlungen</h4>
                    <p>Die Vibration ist ein An/Aus-Schalter; der Zeitpunkt ist kritisch.</p>
                        <p><strong>Potenzielle Vorteile:</strong> Nivellierung des Betts, CO₂-Freisetzung, Channeling-Reduktion.</p>
                        <p><strong>Risiken:</strong> Fines-Migration, Filterverstopfung, Überextraktion (v.a. bei feinem Mahlgut, Naturals, Decafs).</p>
                        <p><strong>Empfehlung:</strong> Bei Fines-anfälligen Kaffees vermeiden oder nur einmalig/gezielt einsetzen (z.B. nach Blooming zum Ebnen, falls nötig). Bei robusteren Kaffees experimentell nach Hauptaufguss zur leichten Extraktionsförderung denkbar. Generell Vibration zurückhaltend nutzen, um Klarheit, Süße, Frucht nicht zu gefährden (Ausnahme: Gran Galope zur Bett-Nivellierung).</p>
                    
                    <h4>2.6. Die Kunst der Aufgussstrategie für Süße, Fruchtigkeit & Körper</h4>
                    <p>Die gezielte Steuerung dieser drei Dimensionen erfordert ein Verständnis der Aufgussstrategie, v.a. Anzahl der Güsse und Volumenverteilung.</p>
                    <p><strong>Anzahl der Aufgüsse:</strong> Mehrere kleine Güsse (Blooming + 2-3 Hauptgüsse) sind oft besser als ein großer Guss für gleichmäßigere, kontrolliertere Extraktion und Temperaturerhaltung.</p>
                    <p><strong>Volumenverteilung:</strong></p>
                    <ul className="list-disc pl-5 mt-2 space-y-1">
                        <li><strong>Süße:</strong> Löst sich oft mittel bis spät. Strategien: Längere Kontaktzeit mittig/spät, leicht fallende Temperatur, mehrere kleine Güsse. Ziel: Maximale Süße ohne Bitterkeit. Rezepte nutzen Volumen/Temperatur in späten Güssen (3, 4) zur Süßemaximierung. Kreisförmige/zentrale Muster können sanft steuern.</li>
                        <li><strong>Fruchtigkeit/Säurebalance:</strong> Löst sich typischerweise früh. Ausreichendes Blooming und gezielte erste Hauptaufgüsse (Volumen, Temperatur, Muster) sind entscheidend. Mehr Wasser im ersten Hauptaufguss (Aufguss 2) kann Frucht betonen. Spiralförmige/kreisförmige Muster mit moderater Temperatur sind oft ideal.</li>
                        <li><strong>Körper/Mundgefühl:</strong> Wird durch gelöste Feststoffe beeinflusst (spätere Güsse wichtig). Strategien: Anzahl/Volumen späterer Güsse anpassen. Zentrales Muster im letzten Guss (Aufguss 4) kann Extraktion im Kern intensivieren und Körper fördern. Engeres Brühverhältnis unterstützt volleren Körper. Rezepte balancieren dies für runden Körper ohne Trübheit.</li>
                    </ul>
                </section>
                <hr className="my-6"/>
                <section>
                    <h3>3. Anleitung zur App-Eingabe und Feinabstimmung</h3>
                    <h4>3.1. Praktische Hinweise zur Übertragung der Rezepte</h4>
                    <p>Übertragen Sie die Rezepte sorgfältig in die xBloom App. Achten Sie auf exakte Übernahme aller Werte (Temperatur, Wassermenge, Flussrate, Muster, Pausen, Vibration). RPM wird im Grinder-Modul oder Rezept eingestellt. "Dauer (s)" = Phase inkl. Pause.</p>
                    
                    <h4>3.2. Systematische Feinabstimmung</h4>
                    <p>Rezepte sind optimierte Ausgangspunkte. Präferenzen/Bohnen können Anpassungen erfordern.</p>
                    <p><strong>Primärer Hebel Mahlgrad:</strong> Entscheidend. Sauer/wässrig &rarr; feiner. Bitter/scharf &rarr; gröber.</p>
                    <p><strong>Sekundäre Hebel:</strong></p>
                    <ul className="list-disc pl-5 mt-2 space-y-2">
                        <li>
                            <strong>Aufgussstrategie (Anzahl, Volumen, Muster):</strong>
                            <ul className="list-circle pl-5 mt-1 space-y-1">
                                <li><em>Mehr Süße:</em> Volumen mittlerer/später Güsse (3, 4) leicht erhöhen oder Temperatur dort leicht senken. Längere Pausen (ohne starkes Auskühlen). Mehrere kleine Güsse.</li>
                                <li><em>Mehr Fruchtigkeit:</em> Volumen des ersten Hauptaufgusses (Aufguss 2) anpassen. Mehr Wasser hier kann Frucht betonen. Temperatur Aufguss 2 ggf. leicht erhöhen (max. 95-96°C). Spiralförmige/kreisförmige Muster früh.</li>
                                <li><em>Mehr Körper:</em> Engeres Brühverhältnis. Volumen später Güsse (Aufguss 4) erhöhen oder zentrales Muster für letzten Guss. Längere Gesamtkontaktzeit.</li>
                            </ul>
                        </li>
                        <li><strong>Temperaturen einzelner Phasen:</strong> Bei Bitterkeit Temperatur in späten Güssen (3, 4) um 1-2°C senken. Bei unangenehmer Säure Temperatur Blooming/Aufguss 2 leicht erhöhen.</li>
                        <li><strong>Wasserdurchflussmenge:</strong> Nur feine Justierungen (3.0-3.5 ml/s).</li>
                        <li><strong>Kaffeefilter-Vibration (An/Aus):</strong> Äußerst vorsichtig. "An" nach Blooming kann Bett nivellieren. "An" nach Hauptaufguss kann Extraktion leicht erhöhen (Risiko: Fines). Bei Verstopfung/Bitterkeit &rarr; "Aus".</li>
                        <li><strong>Mahlwerk RPM:</strong> Bei Bitterkeit trotz gröberem Mahlgrad RPM weiter reduzieren (Richtung 60 RPM). Bei harten, hellen Bohnen ggf. leicht erhöhen (75-85 RPM).</li>
                    </ul>
                    <p className="mt-2"><strong>Systematisches Vorgehen:</strong> Nur eine Variable gleichzeitig ändern. Änderungen/Ergebnisse notieren. Parameter interagieren.</p>
                </section>
                <hr className="my-6"/>
                <section>
                    <h3>4. Abschließende Bemerkungen</h3>
                    <p>Das xBloom Studio eröffnet durch detaillierte Kontrolle (phasenweise Temperatur, Flussraten, Pausen, Muster, Vibration, RPM) neue Präzision. Diese Rezepte nutzen dies gezielt für Süße, Fruchtigkeit und Körper.</p>
                    <p>Rezepte sind fundierte Ausgangspunkte. Faktoren wie Bohnencharge, Wasser, Präferenzen beeinflussen das Ergebnis. Experimentierfreude und methodische Feinabstimmung sind Schlüssel zum Optimum. Hochwertiges Wasser und frische Bohnen bleiben unerlässlich.</p>
                </section>
            </div>
        )}
    </div>
  );


const App = () => {
  const [selectedCoffee, setSelectedCoffee] = useState(null);
  const [isGeminiModalOpen, setIsGeminiModalOpen] = useState(false);
  const [geminiContent, setGeminiContent] = useState('');
  const [geminiLoading, setGeminiLoading] = useState(false);
  const [geminiError, setGeminiError] = useState('');
  const [currentGeminiCoffeeName, setCurrentGeminiCoffeeName] = useState('');
  const [isInfoOpen, setIsInfoOpen] = useState(false); 
  const [isCaffeinatedOpen, setIsCaffeinatedOpen] = useState(true); 
  const [isDecafOpen, setIsDecafOpen] = useState(true);


  const caffeinatedCoffees = coffeeData.filter(coffee => !coffee.isDecaf);
  const decafCoffees = coffeeData.filter(coffee => coffee.isDecaf);

  const openRecipeModal = (coffee) => {
    setSelectedCoffee(coffee);
  };

  const closeRecipeModal = () => {
    setSelectedCoffee(null);
  };

  const openGeminiModal = async (coffee) => {
    setCurrentGeminiCoffeeName(coffee.name);
    setIsGeminiModalOpen(true);
    setGeminiLoading(true);
    setGeminiError('');
    setGeminiContent('');

    // Slightly refined prompt for clarity and focus
    const prompt = `Du bist ein erfahrener Kaffee-Sommelier und sprichst Deutsch. Basierend auf den folgenden Informationen zu einem Kaffee, erstelle bitte:
1.  **Detaillierte Verkostungsnotizen:** Beschreibe die Aromen (Geruch) und den Geschmack (Geschmack, Mundgefühl, Abgang) des Kaffees lebendig und ansprechend. Konzentriere dich auf die Aspekte Süße, Körper und Fruchtigkeit. (ca. 60-80 Wörter).
2.  **Food-Pairing Vorschläge:** Gib zwei konkrete Speisen oder Snacks an, die gut zu diesem Kaffee passen, mit einer kurzen Begründung, warum sie harmonieren (jeweils ca. 20-30 Wörter).
3.  **Kreative Empfehlung:** Verfasse eine kurze, einladende Beschreibung des Kaffees, als würdest du ihn einem Freund empfehlen, der Wert auf hohe Kaffeequalität legt (ca. 30-50 Wörter).

Formatiere deine Antwort klar und übersichtlich mit den Überschriften "**Detaillierte Verkostungsnotizen:**", "**Food-Pairing Vorschläge:**" und "**Kreative Empfehlung:**". Verwende Markdown für die Fettformatierung der Überschriften.

Hier sind die Kaffee-Informationen:
Kaffee-Name: ${coffee.name}
Herkunft/Region: ${coffee.details.region || 'Nicht spezifiziert'}
Produzent: ${coffee.details.produzent || 'Nicht spezifiziert'}
Varietät/Sorte: ${coffee.details.sorte} 
Aufbereitung: ${coffee.details.sorte.toLowerCase().includes("natural") ? "Natural" : (coffee.details.sorte.toLowerCase().includes("washed") ? "Washed" : (coffee.details.sorte.toLowerCase().includes("co₂") || coffee.details.sorte.toLowerCase().includes("e.a.") ? "Decaf (" + coffee.details.sorte + ")" : "Nicht spezifiziert"))}
Aromaprofil laut Rezeptentwickler: ${coffee.details.aromaProfil}
Zusammenfassung der Brühstrategie: ${coffee.details.aufgussStrategieText}`;

    let chatHistory = [];
    chatHistory.push({ role: "user", parts: [{ text: prompt }] });
    const payload = { contents: chatHistory };
    const apiKey = ""; // Wird zur Laufzeit von der Umgebung bereitgestellt
    const apiUrl = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=${apiKey}`;

    try {
      const response = await fetch(apiUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });

      if (!response.ok) {
        const errorData = await response.json();
        console.error('API Error Data:', errorData);
        throw new Error(`API-Fehler: ${response.status} ${response.statusText}. Details: ${errorData?.error?.message || 'Keine spezifischen Fehlerdetails vom API.'}`);
      }

      const result = await response.json();
      setGeminiLoading(false);

      if (result.candidates && result.candidates.length > 0 &&
          result.candidates[0].content && result.candidates[0].content.parts &&
          result.candidates[0].content.parts.length > 0) {
        let text = result.candidates[0].content.parts[0].text;
        // Markdown to HTML conversion (bold and newlines)
        text = text.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>'); 
        text = text.replace(/\n/g, '<br />'); 
        setGeminiContent(text);
      } else {
        console.error('Unerwartete API Antwortstruktur:', result);
        setGeminiError('Fehler: Die Antwort der KI hat ein unerwartetes Format oder ist leer.');
      }
    } catch (error) {
      console.error('Fehler beim Abrufen der Gemini-Details:', error);
      setGeminiLoading(false);
      setGeminiError(`Ein Fehler ist aufgetreten: ${error.message}. Bitte prüfen Sie die Browser-Konsole für Details.`);
    }
  };

  const closeGeminiModal = () => {
    setIsGeminiModalOpen(false);
  };

  // Komponente für zusammenklappbare Kaffee-Sektionen
  const CollapsibleCoffeeSection = ({ title, coffees, isOpen, onToggle, onSelect, onGemini }) => (
    <div className="mb-8">
        <button
            onClick={onToggle}
            className="flex items-center justify-between w-full text-left text-3xl font-semibold text-gray-700 py-4 px-6 bg-white rounded-lg shadow-md hover:bg-gray-50 transition-colors focus:outline-none focus:ring-2 focus:ring-purple-500"
        >
            {title}
            <span className={`transform transition-transform duration-300 ${isOpen ? 'rotate-180' : ''}`}>
                <ChevronDownIcon />
            </span>
        </button>
        {isOpen && (
            <div className="mt-6 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                {coffees.map((coffee) => (
                    <CoffeeCard key={coffee.id} coffee={coffee} onSelect={onSelect} onGemini={onGemini} />
                ))}
            </div>
        )}
    </div>
  );


  return (
    <div className="min-h-screen bg-gray-100 p-4 sm:p-8 font-sans"> {/* Ensure sans-serif font globally */}
      <header className="text-center mb-12">
        <h1 className="text-5xl font-bold text-gray-800">Kaffee-Rezepte für xBloom Studio</h1>
        <p className="text-xl text-gray-600 mt-2">Optimierte Brühstrategien für Süße, Körper & Fruchtigkeit</p>
      </header>

      <GeneralInfoSection isInfoOpen={isInfoOpen} setIsInfoOpen={setIsInfoOpen} />

      <CollapsibleCoffeeSection 
        title="Koffeinhaltige Kaffees" // Titel angepasst
        coffees={caffeinatedCoffees}
        isOpen={isCaffeinatedOpen}
        onToggle={() => setIsCaffeinatedOpen(!isCaffeinatedOpen)}
        onSelect={openRecipeModal}
        onGemini={openGeminiModal}
      />

      <CollapsibleCoffeeSection
        title="Entkoffeinierte Kaffees" // Titel angepasst
        coffees={decafCoffees}
        isOpen={isDecafOpen}
        onToggle={() => setIsDecafOpen(!isDecafOpen)}
        onSelect={openRecipeModal}
        onGemini={openGeminiModal}
      />
      
      {selectedCoffee && (
        <RecipeModal coffee={selectedCoffee} onClose={closeRecipeModal} onGemini={openGeminiModal} />
      )}

      {isGeminiModalOpen && (
        <GeminiModal
          isOpen={isGeminiModalOpen}
          onClose={closeGeminiModal}
          content={geminiContent}
          isLoading={geminiLoading}
          error={geminiError}
          coffeeName={currentGeminiCoffeeName}
        />
      )}
       <footer className="text-center mt-16 py-8 border-t border-gray-300">
            <p className="text-gray-600 text-sm">&copy; 2024 Coffee Excellence. Alle Rechte vorbehalten.</p>
            <p className="text-gray-500 text-xs mt-1">Kaffeerezepte optimiert für das xBloom Studio.</p>
            {/* Link zum neuen HTML-Dokument */}
            <a 
                href="hinweis_dokument_kaffeerezepte.html" 
                target="_blank" 
                rel="noopener noreferrer" 
                className="text-xs text-blue-500 hover:text-blue-700 mt-2 inline-flex items-center hover:underline"
            >
                Entwicklungshinweise zu den Rezepten <ExternalLinkIcon />
            </a>
        </footer>
    </div>
  );
};

const CoffeeCard = ({ coffee, onSelect, onGemini }) => {
  return (
    <div className={`bg-white rounded-xl shadow-xl hover:shadow-purple-300/50 transition-all duration-300 ease-in-out flex flex-col overflow-hidden border ${coffee.borderColorAccent} border-opacity-50`}>
      <img 
        src={coffee.mainImage} 
        alt={`[Bild von ${coffee.name}]`} 
        className="w-full h-52 object-cover" // Increased height
        onError={(e) => {
            e.target.onerror = null; 
            e.target.src='https://placehold.co/600x400/CCCCCC/FFFFFF?text=Bild+Ladefehler';
        }}
      />
      <div className="p-6 flex flex-col flex-grow">
        <h3 className={`text-2xl font-semibold ${coffee.textColorAccent} mb-2 flex items-center`}><CoffeeBeanIcon /> {coffee.name}</h3>
        <p className="text-gray-600 text-sm mb-4 flex-grow">{coffee.shortDescription}</p>
        <div className="mb-4 space-y-1 text-sm text-gray-700 border-t border-gray-200 pt-3"> {/* Added border and padding */}
            <p><strong>Sorte:</strong> {coffee.details.sorte}</p>
            <p><strong>Verhältnis:</strong> {coffee.details.verhaeltnis}</p>
            <p><strong>Mahlgrad (xBloom):</strong> {coffee.details.mahlgrad}</p>
            <p><strong>Mahlwerk RPM:</strong> {coffee.details.rpm}</p>
        </div>
        <div className="mt-auto space-y-3"> {/* Increased spacing */}
            <button
            onClick={() => onSelect(coffee)}
            className={`${coffee.colorAccent} text-white w-full py-2.5 px-4 rounded-lg hover:opacity-90 transition-opacity shadow-md hover:shadow-lg transform hover:-translate-y-0.5`}
            >
            Vollständiges Rezept ansehen
            </button>
            <button
            onClick={() => onGemini(coffee)}
            className="bg-purple-600 text-white w-full py-2.5 px-4 rounded-lg hover:bg-purple-700 transition-colors shadow-md hover:shadow-lg transform hover:-translate-y-0.5 flex items-center justify-center"
            >
            <span role="img" aria-label="sparkles" className="mr-2 text-lg">✨</span> Mehr von der KI erfahren
            </button>
        </div>
      </div>
    </div>
  );
};

const RecipeModal = ({ coffee, onClose, onGemini }) => {
  if (!coffee) return null;

  // Helper to prevent "Nein" from being displayed for vibration
  const getVibrationText = (step) => {
    let vibText = '';
    if (step.vibVor && String(step.vibVor).toLowerCase() !== 'nein') {
      vibText += `Vor (${step.vibVor})`;
    }
    if (step.vibNach && String(step.vibNach).toLowerCase() !== 'nein') {
      if (vibText) vibText += ', ';
      vibText += `Nach (${step.vibNach})`;
    }
    return vibText || 'Keine'; // Show 'Keine' if both are 'Nein' or undefined
  };


  return (
    <div className="fixed inset-0 bg-black bg-opacity-75 flex justify-center items-start py-8 sm:py-12 px-4 z-40 transition-opacity duration-300 ease-in-out overflow-y-auto"> {/* Allow scrolling for modal itself */}
      <div className="bg-white p-6 sm:p-8 rounded-xl shadow-2xl w-full max-w-3xl max-h-[95vh] sm:max-h-[90vh] overflow-y-auto relative"> {/* Inner scroll for content */}
        <button onClick={onClose} className="absolute top-3 right-3 sm:top-4 sm:right-4 text-gray-400 hover:text-gray-700 text-3xl sm:text-4xl font-light transition-colors">&times;</button>
        
        <h2 className={`text-3xl sm:text-4xl font-bold ${coffee.textColorAccent} mb-3 flex items-center`}><CoffeeBeanIcon/> {coffee.name}</h2>
        <div className="text-sm text-gray-500 mb-5 space-y-0.5"> {/* Grouped meta info */}
            <p><strong>Sorte:</strong> {coffee.details.sorte}</p>
            {coffee.details.produzent && <p><strong>Produzent:</strong> {coffee.details.produzent}</p>}
            {coffee.details.region && <p><strong>Region:</strong> {coffee.details.region}</p>}
        </div>


        <div className={`p-4 sm:p-5 rounded-lg mb-6 ${coffee.bgColorAccentLight} border-l-4 ${coffee.borderColorAccent}`}>
            <h4 className={`text-xl font-semibold ${coffee.textColorAccent} mb-2`}>Aromaprofil & Zielsetzung</h4>
            <p className="text-gray-700 text-sm sm:text-base">{coffee.details.aromaProfil}</p>
        </div>
        
        <div className="mb-6">
            <h4 className={`text-xl font-semibold ${coffee.textColorAccent} mb-3`}>Brühparameter (Übersicht)</h4>
            <div className="grid grid-cols-2 sm:grid-cols-3 gap-x-4 gap-y-2 text-sm sm:text-base text-gray-700">
                <p><strong>Kaffeemenge:</strong> {coffee.details.menge}g</p>
                <p><strong>Brühverhältnis:</strong> {coffee.details.verhaeltnis}</p>
                <p><strong>Gesamtwasser:</strong> {coffee.details.wasserGesamt}ml</p>
                <p><strong>Mahlgrad (xBloom):</strong> {coffee.details.mahlgrad}</p>
                <p><strong>Mahlwerk RPM:</strong> {coffee.details.rpm}</p>
                <p><strong>Gesamtbrühzeit:</strong> {coffee.details.gesamtBruehzeit}</p>
            </div>
        </div>

        <div className="mb-6">
            <h4 className={`text-xl font-semibold ${coffee.textColorAccent} mb-3`}>Brühschritte (xBloom App Eingabe)</h4>
            <div className="space-y-4">
            {coffee.details.brewSteps.map((step, index) => {
                const vibrationDisplay = getVibrationText(step);
                return (
                    <div key={index} className="p-3 sm:p-4 bg-gray-50 rounded-lg border border-gray-200 shadow-sm text-sm sm:text-base">
                        <p className="font-semibold text-gray-800 text-base sm:text-lg">{index + 1}. {step.phase}</p>
                        <div className="grid grid-cols-2 sm:grid-cols-3 gap-x-4 gap-y-1.5 mt-2 text-gray-600">
                            <p><strong>Menge:</strong> {step.menge}ml</p>
                            <p><strong>Temp:</strong> {step.temp}°C</p>
                            <p><strong>Fluss:</strong> {step.durchfluss}ml/s</p>
                            <p><strong>Pause:</strong> {step.pause}s</p>
                            <p><strong>Muster:</strong> {step.muster}</p>
                            <p><strong>Dauer (Phase):</strong> {step.dauer}s</p>
                            { (vibrationDisplay !== 'Keine') &&
                                <p className="col-span-2 sm:col-span-3"><strong>Vibration:</strong> {vibrationDisplay}</p>
                            }
                        </div>
                    </div>
                );
            })}
            </div>
        </div>
        
        <div className={`p-4 sm:p-5 rounded-lg mb-6 ${coffee.bgColorAccentLight} border-l-4 ${coffee.borderColorAccent}`}>
            <h4 className={`text-xl font-semibold ${coffee.textColorAccent} mb-2`}>Erläuterung der Aufgussstrategie</h4>
            <p className="text-gray-700 text-sm sm:text-base mb-2">{coffee.details.aufgussStrategieText}</p>
            {coffee.details.aufgussStrategiePunkte && coffee.details.aufgussStrategiePunkte.length > 0 && (
                <ul className="list-disc list-inside text-sm sm:text-base text-gray-700 space-y-1 pl-1">
                    {coffee.details.aufgussStrategiePunkte.map((punkt, i) => <li key={i}>{punkt}</li>)}
                </ul>
            )}
        </div>
         <p className="text-xs text-gray-500 mt-4 mb-6 italic">Anmerkung zur Tabelle/Ziel: {coffee.details.anmerkungenTabelle}</p>


        <div className="mt-8 pt-6 border-t border-gray-200 flex flex-col sm:flex-row gap-3">
          <button
            onClick={() => {
                onClose(); // Close current modal first
                // Timeout to ensure RecipeModal is closed before GeminiModal opens, preventing z-index issues
                setTimeout(() => onGemini(coffee), 50); 
            }}
            className="bg-purple-600 text-white py-2.5 px-5 rounded-lg hover:bg-purple-700 transition-colors w-full sm:w-auto flex items-center justify-center shadow-md hover:shadow-lg transform hover:-translate-y-0.5"
          >
           <span role="img" aria-label="sparkles" className="mr-2 text-lg">✨</span> Mehr von der KI erfahren
          </button>
          <button
            onClick={onClose}
            className="bg-gray-200 text-gray-700 py-2.5 px-5 rounded-lg hover:bg-gray-300 transition-colors w-full sm:w-auto shadow-sm hover:shadow-md"
          >
            Schließen
          </button>
        </div>
      </div>
    </div>
  );
};

const GeminiModal = ({ isOpen, onClose, content, isLoading, error, coffeeName }) => {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 bg-black bg-opacity-75 flex justify-center items-start py-8 sm:py-12 px-4 z-50 transition-opacity duration-300 ease-in-out overflow-y-auto"> {/* Allow scrolling for modal itself */}
      <div className="bg-white p-6 sm:p-8 rounded-xl shadow-2xl w-full max-w-lg max-h-[95vh] sm:max-h-[90vh] overflow-y-auto"> {/* Inner scroll for content */}
        <h3 className="text-2xl sm:text-3xl font-semibold text-purple-700 mb-1">KI Kaffee-Sommelier Notizen</h3>
        <p className="text-sm text-gray-500 mb-6">für: <strong>{coffeeName}</strong></p>
        {isLoading && (
          <div className="flex justify-center items-center h-40"> {/* Increased height */}
            <div className="animate-spin rounded-full h-16 w-16 border-t-4 border-b-4 border-purple-500"></div> {/* Larger spinner */}
          </div>
        )}
        {error && <div className="text-red-600 bg-red-100 p-4 rounded-lg border border-red-300 text-sm sm:text-base">{error}</div>}
        {content && !isLoading && (
          // Using prose for better typography for AI generated content
          <div className="prose prose-sm sm:prose-base max-w-none text-gray-700" dangerouslySetInnerHTML={{ __html: content }} />
        )}
        <button
          onClick={onClose}
          className="mt-8 bg-red-500 text-white py-2.5 px-5 rounded-lg hover:bg-red-600 transition-colors w-full shadow-md hover:shadow-lg"
        >
          Schließen
        </button>
      </div>
    </div>
  );
};

export default App;
