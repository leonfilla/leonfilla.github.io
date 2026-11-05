---
titel: weekly_smoothie_plan.jsx
status: aktiv
datum: '2026-04-24'
quelle:
  typ: claude
  url: https://claude.ai/chat/e243ac2d-4628-41b9-ae87-39b4cf14f878
  hinweis: Protein-Smoothies für Frühstück und Muskelaufbau
importiert: true
---

<details><summary>Ursprüngliche Datei</summary><pre><code>import { useState } from &quot;react&quot;;

const week = [
  {
    day: &quot;Mo&quot;, label: &quot;Montag&quot;, training: &quot;Lauftag&quot;, trainingColor: &quot;#1a7a4a&quot;,
    name: &quot;Beet Blueberry Banana Spinach&quot;,
    focus: &quot;NO-Boost + Anthocyane + Vit. K&quot;,
    focusColor: &quot;#7c2d8a&quot;,
    rationale: &quot;Rote Beete (roh) liefert maximales Nitrat für NO-Synthese — ideal 2–3 h vor dem Laufen. Blaubeeren + Spinat decken Vitamin K und Folat. Banane für schnelle KH.&quot;,
    macros: { kcal: 748, p: 49, f: 22, kh: 83, bal: 14 },
    banana: true,
    ingredients: [
      { name: &quot;Vollmilch 3,8 %&quot;, amt: &quot;260 ml&quot;, tag: null },
      { name: &quot;TK Blaubeeren&quot;, amt: &quot;130 g&quot;, tag: &quot;Anthocyane&quot; },
      { name: &quot;TK Banane&quot;, amt: &quot;90 g&quot;, tag: &quot;KH + Bindung&quot; },
      { name: &quot;Rohe Rote Beete, gerieben&quot;, amt: &quot;65 g&quot;, tag: &quot;Nitrat roh ↑↑&quot; },
      { name: &quot;TK Blattspinat&quot;, amt: &quot;55 g&quot;, tag: &quot;Vit. K + Folat&quot; },
      { name: &quot;Haferflocken, fein&quot;, amt: &quot;35 g&quot;, tag: null },
      { name: &quot;Leinsamen, gemahlen&quot;, amt: &quot;12 g&quot;, tag: &quot;ALA&quot; },
      { name: &quot;Meersalz&quot;, amt: &quot;1 Prise&quot;, tag: &quot;Elektrolyt&quot; },
    ],
    fills: [&quot;Vit. K ~280 %&quot;, &quot;Folat ~60 %&quot;, &quot;Nitrat ↑↑&quot;, &quot;Anthocyane&quot;],
    note: &quot;Farbe: tief violett · Rote Beete zuletzt einfüllen · vor dem Laufen trinken&quot;,
  },
  {
    day: &quot;Di&quot;, label: &quot;Dienstag&quot;, training: &quot;Gymtag&quot;, trainingColor: &quot;#1a5a8a&quot;,
    name: &quot;Cherry Cacao Zucchini Walnut&quot;,
    focus: &quot;DOMS + Recovery + Mg&quot;,
    focusColor: &quot;#8a2a1a&quot;,
    rationale: &quot;Sauerkirsche hemmt COX-1/2 und reduziert DOMS nachweislich. Kakao-Flavanole + Walnuss-ALA synergistisch anti-inflammatorisch. Zucchini erhöht Volumen ohne Kalorien. Kein Nussmus — ganze Walnüsse.&quot;,
    macros: { kcal: 762, p: 50, f: 31, kh: 72, bal: 13 },
    banana: false,
    ingredients: [
      { name: &quot;Vollmilch 3,8 %&quot;, amt: &quot;270 ml&quot;, tag: null },
      { name: &quot;TK Sauerkirschen&quot;, amt: &quot;150 g&quot;, tag: &quot;COX-Hemmer · DOMS↓&quot; },
      { name: &quot;TK Zucchini, roh&quot;, amt: &quot;100 g&quot;, tag: &quot;Volumen · geschmacksneutral&quot; },
      { name: &quot;Rohkakao-Pulver, ungesüßt&quot;, amt: &quot;15 g&quot;, tag: &quot;Flavanole · Mg&quot; },
      { name: &quot;Walnüsse, ganz&quot;, amt: &quot;20 g&quot;, tag: &quot;ALA Omega-3&quot; },
      { name: &quot;Haferflocken, fein&quot;, amt: &quot;35 g&quot;, tag: null },
      { name: &quot;Medjool-Dattel, entkernt&quot;, amt: &quot;1 Stk. (~18 g)&quot;, tag: &quot;Süße + KH&quot; },
    ],
    fills: [&quot;DOMS↓&quot;, &quot;Mg ~85 %&quot;, &quot;ALA Omega-3&quot;, &quot;Flavanole&quot;],
    note: &quot;Farbe: dunkelbraun · dessertartig · post-workout ideal&quot;,
  },
  {
    day: &quot;Mi&quot;, label: &quot;Mittwoch&quot;, training: &quot;Ruhetag&quot;, trainingColor: &quot;#555&quot;,
    name: &quot;Mango Spinach Pea Flax&quot;,
    focus: &quot;Folat + Vit. K + ALA · leicht&quot;,
    focusColor: &quot;#1a6b3a&quot;,
    rationale: &quot;Ruhetag: weniger KH, mehr Mikronährstoffe. Erbsen sind die folatreichste Gemüseoption. Spinat für Vitamin K. Mango überdeckt beides. Leinsamen für ALA ohne zusätzliche Kaloriendichte.&quot;,
    macros: { kcal: 682, p: 50, f: 22, kh: 67, bal: 15 },
    banana: false,
    ingredients: [
      { name: &quot;Vollmilch 3,8 %&quot;, amt: &quot;260 ml&quot;, tag: null },
      { name: &quot;TK Mango&quot;, amt: &quot;160 g&quot;, tag: &quot;Vit. C + Cremigkeit&quot; },
      { name: &quot;TK Blattspinat&quot;, amt: &quot;65 g&quot;, tag: &quot;Vit. K &gt;250 % AI&quot; },
      { name: &quot;TK Erbsen, aufgetaut&quot;, amt: &quot;80 g&quot;, tag: &quot;Folat ~75 % RDA&quot; },
      { name: &quot;Haferflocken, fein&quot;, amt: &quot;30 g&quot;, tag: null },
      { name: &quot;Leinsamen, gemahlen&quot;, amt: &quot;12 g&quot;, tag: &quot;ALA 3,2 g&quot; },
      { name: &quot;Hanfsamen, geschält&quot;, amt: &quot;15 g&quot;, tag: &quot;vollst. Aminosäuren&quot; },
    ],
    fills: [&quot;Folat ~75 %&quot;, &quot;Vit. K &gt;250 %&quot;, &quot;ALA 3,2 g&quot;, &quot;niedrigste kcal&quot;],
    note: &quot;Farbe: sattgrün · niedrigstes Fett + kcal der Woche · ideal Ruhetag&quot;,
  },
  {
    day: &quot;Do&quot;, label: &quot;Donnerstag&quot;, training: &quot;Lauftag&quot;, trainingColor: &quot;#1a7a4a&quot;,
    name: &quot;Pineapple Broccoli Carrot Hemp&quot;,
    focus: &quot;Bromelain + Sulforaphan + Beta-Carotin&quot;,
    focusColor: &quot;#1a6b8a&quot;,
    rationale: &quot;Drei bioaktive Substanzen: Bromelain (Ananas, anti-inflammatorisch), Sulforaphan (Brokkoli, Nrf2-Aktivierung), Beta-Carotin (Karotte, Vitamin A &gt;100 % RDA). Ananas überdeckt Brokkoli und Karotte vollständig.&quot;,
    macros: { kcal: 748, p: 52, f: 24, kh: 78, bal: 15 },
    banana: false,
    ingredients: [
      { name: &quot;Vollmilch 3,8 %&quot;, amt: &quot;255 ml&quot;, tag: null },
      { name: &quot;TK Ananas&quot;, amt: &quot;150 g&quot;, tag: &quot;Bromelain · Vit. C&quot; },
      { name: &quot;TK Brokkoli&quot;, amt: &quot;80 g&quot;, tag: &quot;Sulforaphan · Nrf2↑&quot; },
      { name: &quot;TK Karotte, gegart&quot;, amt: &quot;100 g&quot;, tag: &quot;Beta-Carotin · Vit. A&quot; },
      { name: &quot;Hanfsamen, geschält&quot;, amt: &quot;20 g&quot;, tag: &quot;Mg · vollst. AS&quot; },
      { name: &quot;Haferflocken, fein&quot;, amt: &quot;28 g&quot;, tag: null },
      { name: &quot;Bio-Limette, ½ mit Schale&quot;, amt: &quot;~30 ml&quot;, tag: &quot;Flavonoide&quot; },
    ],
    fills: [&quot;Vit. A ~110 %&quot;, &quot;Sulforaphan&quot;, &quot;Bromelain&quot;, &quot;Vit. C ~90 %&quot;],
    note: &quot;Farbe: hellgelb-grün · Limette mit Schale da Bio · höchstes Protein der Woche&quot;,
  },
  {
    day: &quot;Fr&quot;, label: &quot;Freitag&quot;, training: &quot;Gymtag&quot;, trainingColor: &quot;#1a5a8a&quot;,
    name: &quot;Blackberry Beet Spinach Almond&quot;,
    focus: &quot;Anthocyane + NO + Vit. E + Vit. K&quot;,
    focusColor: &quot;#5a1a8a&quot;,
    rationale: &quot;Brombeeren + Rote Beete = höchste Anthocyan + Nitrat-Kombination der Woche. Mandeln für Vitamin E (Muskelschutz post-workout). Spinat ergänzt Vitamin K und Eisen.&quot;,
    macros: { kcal: 756, p: 50, f: 28, kh: 75, bal: 16 },
    banana: true,
    ingredients: [
      { name: &quot;Vollmilch 3,8 %&quot;, amt: &quot;255 ml&quot;, tag: null },
      { name: &quot;TK Brombeeren&quot;, amt: &quot;140 g&quot;, tag: &quot;Anthocyane · Vit. K&quot; },
      { name: &quot;TK Banane&quot;, amt: &quot;80 g&quot;, tag: &quot;KH + Bindung&quot; },
      { name: &quot;Rohe Rote Beete, gerieben&quot;, amt: &quot;65 g&quot;, tag: &quot;Nitrat ↑↑&quot; },
      { name: &quot;TK Blattspinat&quot;, amt: &quot;50 g&quot;, tag: &quot;Vit. K · Eisen&quot; },
      { name: &quot;Mandeln, ganz&quot;, amt: &quot;22 g&quot;, tag: &quot;Vit. E · Calcium&quot; },
      { name: &quot;Chiasamen&quot;, amt: &quot;12 g&quot;, tag: &quot;Omega-3&quot; },
    ],
    fills: [&quot;Anthocyane ↑↑&quot;, &quot;Vit. E ~60 %&quot;, &quot;Eisen ~90 %&quot;, &quot;Vit. K &gt;300 %&quot;],
    note: &quot;Farbe: tief violett-schwarz · stärkste Antioxidantienkombination der Woche&quot;,
  },
  {
    day: &quot;Sa&quot;, label: &quot;Samstag&quot;, training: &quot;Ruhetag&quot;, trainingColor: &quot;#555&quot;,
    name: &quot;Peach Raspberry Spinach Chia&quot;,
    focus: &quot;Vit. C + Selen + Omega-3 · leichtester&quot;,
    focusColor: &quot;#8a4a1a&quot;,
    rationale: &quot;Paranüsse (2 Stk.) decken 100 % des Selen-Tagesbedarfs — die größte strukturelle Mikronährstofflücke der Gesamternährung. Pfirsich + Himbeere für Vitamin C und sanfte Frische. Ruhetag: niedrigstes KH.&quot;,
    macros: { kcal: 671, p: 47, f: 20, kh: 64, bal: 14 },
    banana: false,
    ingredients: [
      { name: &quot;Vollmilch 3,8 %&quot;, amt: &quot;265 ml&quot;, tag: null },
      { name: &quot;TK Pfirsich&quot;, amt: &quot;150 g&quot;, tag: &quot;Kalium · mild-süß&quot; },
      { name: &quot;TK Himbeeren&quot;, amt: &quot;100 g&quot;, tag: &quot;Vit. C · Prebiotikum&quot; },
      { name: &quot;TK Blattspinat&quot;, amt: &quot;55 g&quot;, tag: &quot;Vit. K · Folat&quot; },
      { name: &quot;Paranüsse, ganz&quot;, amt: &quot;2 Stk. (~14 g)&quot;, tag: &quot;Selen 100 % RDA&quot; },
      { name: &quot;Chiasamen&quot;, amt: &quot;14 g&quot;, tag: &quot;ALA · Ballaststoffe&quot; },
      { name: &quot;Haferflocken, fein&quot;, amt: &quot;25 g&quot;, tag: null },
    ],
    fills: [&quot;Selen ~100 %&quot;, &quot;Vit. C ~65 %&quot;, &quot;Vit. K ~200 %&quot;, &quot;niedrigste kcal&quot;],
    note: &quot;Paranüsse: max. 2 Stk./Tag — mehr kann zu Selenose führen · niedrigste kcal der Woche&quot;,
  },
  {
    day: &quot;So&quot;, label: &quot;Sonntag&quot;, training: &quot;Flex&quot;, trainingColor: &quot;#6a4a1a&quot;,
    name: &quot;Triple Green Cherry Mango&quot;,
    focus: &quot;Sulforaphan + Folat + DOMS · max. Mikros&quot;,
    focusColor: &quot;#1a6b3a&quot;,
    rationale: &quot;Drei Gemüse: Brokkoli (Sulforaphan), Spinat (Vit. K + Folat), Erbsen (Folat). Sauerkirsche für DOMS-Prävention. Mango überdeckt alle drei Gemüse vollständig. Mikronährstoffdichtester Shake der Woche.&quot;,
    macros: { kcal: 724, p: 52, f: 21, kh: 79, bal: 17 },
    banana: false,
    ingredients: [
      { name: &quot;Vollmilch 3,8 %&quot;, amt: &quot;260 ml&quot;, tag: null },
      { name: &quot;TK Mango&quot;, amt: &quot;150 g&quot;, tag: &quot;Gemüse überdecken · Vit. C&quot; },
      { name: &quot;TK Sauerkirschen&quot;, amt: &quot;100 g&quot;, tag: &quot;COX-Hemmer · DOMS↓&quot; },
      { name: &quot;TK Brokkoli&quot;, amt: &quot;70 g&quot;, tag: &quot;Sulforaphan · Nrf2↑&quot; },
      { name: &quot;TK Blattspinat&quot;, amt: &quot;55 g&quot;, tag: &quot;Vit. K · Eisen&quot; },
      { name: &quot;TK Erbsen, aufgetaut&quot;, amt: &quot;60 g&quot;, tag: &quot;Folat ~60 %&quot; },
      { name: &quot;Hanfsamen, geschält&quot;, amt: &quot;18 g&quot;, tag: &quot;vollst. AS · Mg&quot; },
      { name: &quot;Bio-Limette, ½ mit Schale&quot;, amt: &quot;~30 ml&quot;, tag: &quot;Flavonoide&quot; },
    ],
    fills: [&quot;Folat ~90 %&quot;, &quot;Vit. K &gt;350 %&quot;, &quot;Sulforaphan&quot;, &quot;höchste Ballaststoffe&quot;],
    note: &quot;Farbe: tiefgrün · Mango-Menge unverzichtbar · mikronährstoffdichtester Shake der Woche&quot;,
  },
];

const trainingIcon = { &quot;Lauftag&quot;: &quot;↗&quot;, &quot;Gymtag&quot;: &quot;◈&quot;, &quot;Ruhetag&quot;: &quot;○&quot;, &quot;Flex&quot;: &quot;◇&quot; };

export default function App() {
  const [selected, setSelected] = useState(0);
  const s = week[selected];

  return (
    &lt;div style={{
      fontFamily: &quot;&#x27;Georgia&#x27;, serif&quot;,
      background: &quot;#f9f7f3&quot;,
      minHeight: &quot;100vh&quot;,
      maxWidth: 480,
      margin: &quot;0 auto&quot;,
    }}&gt;

      {/* Week strip */}
      &lt;div style={{
        display: &quot;grid&quot;, gridTemplateColumns: &quot;repeat(7,1fr)&quot;,
        background: &quot;#fff&quot;,
        borderBottom: &quot;0.5px solid #e5e0d8&quot;,
        position: &quot;sticky&quot;, top: 0, zIndex: 10,
      }}&gt;
        {week.map((w, i) =&gt; (
          &lt;button
            key={i}
            onClick={() =&gt; setSelected(i)}
            style={{
              background: selected === i ? &quot;#1a1a1a&quot; : &quot;none&quot;,
              border: &quot;none&quot;,
              padding: &quot;10px 4px&quot;,
              cursor: &quot;pointer&quot;,
              display: &quot;flex&quot;,
              flexDirection: &quot;column&quot;,
              alignItems: &quot;center&quot;,
              gap: 3,
              transition: &quot;background .15s&quot;,
            }}
          &gt;
            &lt;span style={{
              fontSize: 10,
              fontFamily: &quot;monospace&quot;,
              color: selected === i ? &quot;#999&quot; : &quot;#bbb&quot;,
              letterSpacing: &quot;.05em&quot;,
            }}&gt;{w.day}&lt;/span&gt;
            &lt;span style={{
              fontSize: 13,
              fontWeight: 500,
              color: selected === i ? &quot;#fff&quot; : &quot;#333&quot;,
            }}&gt;{trainingIcon[w.training]}&lt;/span&gt;
            &lt;span style={{
              width: 4, height: 4,
              borderRadius: &quot;50%&quot;,
              background: selected === i ? w.trainingColor : &quot;transparent&quot;,
              border: `1px solid ${w.trainingColor}`,
            }}&gt;&lt;/span&gt;
          &lt;/button&gt;
        ))}
      &lt;/div&gt;

      {/* Main content */}
      &lt;div style={{ padding: &quot;1.25rem 1rem 3rem&quot; }}&gt;

        {/* Day header */}
        &lt;div style={{ marginBottom: &quot;1rem&quot; }}&gt;
          &lt;div style={{ display: &quot;flex&quot;, alignItems: &quot;center&quot;, gap: 8, marginBottom: 4 }}&gt;
            &lt;span style={{
              fontSize: 10, fontFamily: &quot;monospace&quot;, fontWeight: 700,
              padding: &quot;2px 8px&quot;, borderRadius: 20,
              background: s.trainingColor + &quot;18&quot;, color: s.trainingColor,
              letterSpacing: &quot;.08em&quot;,
            }}&gt;{s.training}&lt;/span&gt;
            &lt;span style={{ fontSize: 12, color: &quot;#aaa&quot; }}&gt;{s.label}&lt;/span&gt;
          &lt;/div&gt;
          &lt;h2 style={{ fontSize: 20, fontWeight: 700, margin: &quot;0 0 3px&quot;, color: &quot;#1a1a1a&quot;, lineHeight: 1.2 }}&gt;
            {s.name}
          &lt;/h2&gt;
          &lt;div style={{
            display: &quot;inline-flex&quot;, alignItems: &quot;center&quot;, gap: 5,
            background: s.focusColor + &quot;12&quot;,
            border: `0.5px solid ${s.focusColor}30`,
            borderRadius: 8, padding: &quot;3px 9px&quot;, marginTop: 4,
          }}&gt;
            &lt;span style={{ fontSize: 11, color: s.focusColor, fontWeight: 500 }}&gt;{s.focus}&lt;/span&gt;
          &lt;/div&gt;
        &lt;/div&gt;

        {/* Rationale */}
        &lt;p style={{
          fontSize: 13, color: &quot;#666&quot;, lineHeight: 1.6,
          margin: &quot;0 0 1rem&quot;,
          padding: &quot;10px 12px&quot;,
          background: &quot;#fff&quot;,
          borderRadius: 10,
          border: &quot;0.5px solid #e5e0d8&quot;,
        }}&gt;
          {s.rationale}
        &lt;/p&gt;

        {/* Macros */}
        &lt;div style={{ display: &quot;grid&quot;, gridTemplateColumns: &quot;repeat(5,minmax(0,1fr))&quot;, gap: 6, marginBottom: 12 }}&gt;
          {[
            { label: &quot;kcal&quot;, val: s.macros.kcal, unit: &quot;&quot;, color: &quot;#1a1a1a&quot; },
            { label: &quot;Protein&quot;, val: s.macros.p, unit: &quot;g&quot;, color: &quot;#7c3aed&quot; },
            { label: &quot;Fett&quot;, val: s.macros.f, unit: &quot;g&quot;, color: &quot;#d4860a&quot; },
            { label: &quot;KH&quot;, val: s.macros.kh, unit: &quot;g&quot;, color: &quot;#1a7a4a&quot; },
            { label: &quot;Ballaststoffe&quot;, val: s.macros.bal, unit: &quot;g&quot;, color: &quot;#1a6b8a&quot; },
          ].map((m, i) =&gt; (
            &lt;div key={i} style={{
              background: &quot;#fff&quot;, borderRadius: 8, padding: &quot;8px 4px&quot;, textAlign: &quot;center&quot;,
              border: &quot;0.5px solid #e5e0d8&quot;,
            }}&gt;
              &lt;div style={{ fontSize: 9, color: &quot;#bbb&quot;, marginBottom: 2, fontFamily: &quot;monospace&quot; }}&gt;{m.label}&lt;/div&gt;
              &lt;div style={{ fontSize: 13, fontWeight: 700, color: m.color }}&gt;{m.val}{m.unit}&lt;/div&gt;
            &lt;/div&gt;
          ))}
        &lt;/div&gt;

        {/* Fills */}
        &lt;div style={{ display: &quot;flex&quot;, gap: 5, flexWrap: &quot;wrap&quot;, marginBottom: 14 }}&gt;
          {s.fills.map((f, i) =&gt; (
            &lt;span key={i} style={{
              fontSize: 11, padding: &quot;3px 9px&quot;, borderRadius: 20,
              background: s.focusColor + &quot;10&quot;,
              color: s.focusColor,
              border: `0.5px solid ${s.focusColor}25`,
              fontWeight: 500,
            }}&gt;{f}&lt;/span&gt;
          ))}
        &lt;/div&gt;

        {/* Ingredients */}
        &lt;div style={{
          background: &quot;#fff&quot;, borderRadius: 12, border: &quot;0.5px solid #e5e0d8&quot;,
          overflow: &quot;hidden&quot;, marginBottom: 10,
        }}&gt;
          &lt;div style={{
            padding: &quot;8px 14px&quot;, borderBottom: &quot;0.5px solid #f0ece4&quot;,
            display: &quot;flex&quot;, justifyContent: &quot;space-between&quot;, alignItems: &quot;center&quot;,
          }}&gt;
            &lt;span style={{ fontSize: 10, fontFamily: &quot;monospace&quot;, fontWeight: 700, color: &quot;#bbb&quot;, letterSpacing: &quot;.1em&quot; }}&gt;
              ZUTATEN · 620 ml vor dem Mixen
            &lt;/span&gt;
            &lt;span style={{ fontSize: 10, color: &quot;#bbb&quot; }}&gt;+ 35 g Pulver · 5 g Kreatin&lt;/span&gt;
          &lt;/div&gt;
          {s.ingredients.map((ing, i) =&gt; (
            &lt;div key={i} style={{
              display: &quot;flex&quot;, justifyContent: &quot;space-between&quot;, alignItems: &quot;flex-start&quot;,
              padding: &quot;7px 14px&quot;,
              borderBottom: i &lt; s.ingredients.length - 1 ? &quot;0.5px solid #f5f2ee&quot; : &quot;none&quot;,
              background: i % 2 === 0 ? &quot;#fff&quot; : &quot;#fdfcfa&quot;,
            }}&gt;
              &lt;div style={{ flex: 1 }}&gt;
                &lt;span style={{ fontSize: 13, color: &quot;#333&quot; }}&gt;{ing.name}&lt;/span&gt;
                {ing.tag &amp;&amp; (
                  &lt;span style={{
                    fontSize: 10, marginLeft: 6,
                    color: s.focusColor, fontFamily: &quot;monospace&quot;,
                  }}&gt;· {ing.tag}&lt;/span&gt;
                )}
              &lt;/div&gt;
              &lt;span style={{ fontSize: 12, fontWeight: 700, color: &quot;#999&quot;, whiteSpace: &quot;nowrap&quot;, marginLeft: 10 }}&gt;
                {ing.amt}
              &lt;/span&gt;
            &lt;/div&gt;
          ))}
        &lt;/div&gt;

        {/* Note */}
        &lt;div style={{
          fontSize: 12, color: &quot;#888&quot;, fontStyle: &quot;italic&quot;,
          padding: &quot;8px 12px&quot;,
          borderLeft: `3px solid ${s.focusColor}40`,
          background: s.focusColor + &quot;06&quot;,
          borderRadius: &quot;0 8px 8px 0&quot;,
        }}&gt;
          {s.note}
        &lt;/div&gt;

        {/* Weekly micro overview */}
        &lt;div style={{
          marginTop: 16,
          background: &quot;#fff&quot;, borderRadius: 12,
          border: &quot;0.5px solid #e5e0d8&quot;,
          padding: &quot;10px 14px&quot;,
        }}&gt;
          &lt;p style={{ fontSize: 10, fontFamily: &quot;monospace&quot;, fontWeight: 700, color: &quot;#bbb&quot;, letterSpacing: &quot;.1em&quot;, margin: &quot;0 0 8px&quot; }}&gt;
            WÖCHENTLICHE MIKRONÄHRSTOFFVERTEILUNG
          &lt;/p&gt;
          {[
            { label: &quot;Vit. K&quot;, days: [1,1,1,0,1,1,1], color: &quot;#1a7a4a&quot; },
            { label: &quot;Folat&quot;, days: [1,0,1,0,1,1,1], color: &quot;#1a6b8a&quot; },
            { label: &quot;ALA Omega-3&quot;, days: [1,1,1,0,1,1,0], color: &quot;#d4860a&quot; },
            { label: &quot;Nitrat/NO&quot;, days: [1,0,0,0,1,0,0], color: &quot;#8a2a1a&quot; },
            { label: &quot;Sulforaphan&quot;, days: [0,0,0,1,0,0,1], color: &quot;#1a5a2a&quot; },
            { label: &quot;Selen&quot;, days: [0,0,0,0,0,1,0], color: &quot;#6a4a1a&quot; },
            { label: &quot;Anthocyane&quot;, days: [1,1,0,0,1,1,0], color: &quot;#5a1a8a&quot; },
          ].map((row, i) =&gt; (
            &lt;div key={i} style={{ display: &quot;flex&quot;, alignItems: &quot;center&quot;, gap: 6, marginBottom: 5 }}&gt;
              &lt;span style={{ fontSize: 11, color: &quot;#666&quot;, minWidth: 90 }}&gt;{row.label}&lt;/span&gt;
              &lt;div style={{ display: &quot;flex&quot;, gap: 3 }}&gt;
                {row.days.map((on, j) =&gt; (
                  &lt;div key={j} style={{
                    width: 24, height: 16, borderRadius: 4,
                    background: on ? row.color + &quot;20&quot; : &quot;#f5f2ee&quot;,
                    border: `0.5px solid ${on ? row.color + &quot;50&quot; : &quot;#e5e0d8&quot;}`,
                    display: &quot;flex&quot;, alignItems: &quot;center&quot;, justifyContent: &quot;center&quot;,
                  }}&gt;
                    &lt;span style={{ fontSize: 9, color: on ? row.color : &quot;#ccc&quot;, fontFamily: &quot;monospace&quot;, fontWeight: 700 }}&gt;
                      {week[j].day}
                    &lt;/span&gt;
                  &lt;/div&gt;
                ))}
              &lt;/div&gt;
            &lt;/div&gt;
          ))}
        &lt;/div&gt;

      &lt;/div&gt;
    &lt;/div&gt;
  );
}
</code></pre></details>
