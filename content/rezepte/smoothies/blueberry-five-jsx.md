---
titel: blueberry_five.jsx
status: archiv
datum: '2026-04-24'
quelle:
  typ: claude
  url: https://claude.ai/chat/e243ac2d-4628-41b9-ae87-39b4cf14f878
  hinweis: Protein-Smoothies für Frühstück und Muskelaufbau
importiert: true
---

<details><summary>Ursprüngliche Datei</summary><pre><code>import { useState } from &quot;react&quot;;

const smoothies = [
  {
    id: 1,
    name: &quot;Blueberry Spinach Walnut Oat&quot;,
    badge: &quot;Vit. K + Folat + ALA&quot;,
    badgeColor: &quot;#1a7a4a&quot;,
    banana: true,
    desc: &quot;Spinat schließt Vitamin K und Folat. Walnüsse für ALA Omega-3. Klassischste Kombination mit maximaler Mikronährstoffdichte.&quot;,
    macros: { kcal: 738, p: 49, f: 30, kh: 70, bal: 13 },
    ingredients: [
      { name: &quot;TK Blaubeeren&quot;, amt: &quot;140 g&quot;, tag: &quot;Anthocyane&quot;, tc: &quot;#7c3aed&quot; },
      { name: &quot;TK Banane&quot;, amt: &quot;80 g&quot;, tag: null },
      { name: &quot;TK Blattspinat&quot;, amt: &quot;65 g&quot;, tag: &quot;Vit. K &gt;250 %&quot;, tc: &quot;#1a7a4a&quot; },
      { name: &quot;Walnüsse, ganz&quot;, amt: &quot;22 g&quot;, tag: &quot;ALA Omega-3&quot;, tc: &quot;#d4860a&quot; },
      { name: &quot;Haferflocken, fein&quot;, amt: &quot;35 g&quot;, tag: null },
      { name: &quot;Leinsamen, gemahlen&quot;, amt: &quot;12 g&quot;, tag: &quot;ALA&quot;, tc: &quot;#d4860a&quot; },
    ],
    fills: [&quot;Vit. K &gt;250 %&quot;, &quot;Folat ~60 %&quot;, &quot;ALA ~3,5 g&quot;],
    note: &quot;Farbe: tiefviolett · einfachste Zubereitung · ideal als Basisrezept&quot;,
  },
  {
    id: 2,
    name: &quot;Blueberry Beet Carrot Hemp&quot;,
    badge: &quot;NO + Beta-Carotin&quot;,
    badgeColor: &quot;#c0392b&quot;,
    banana: true,
    desc: &quot;Rohe Rote Beete + Blaubeeren = Nitrat + Anthocyane synergistisch. Karotte deckt Vitamin A &gt;100 %. Hanfsamen für Magnesium.&quot;,
    macros: { kcal: 724, p: 50, f: 24, kh: 79, bal: 13 },
    ingredients: [
      { name: &quot;TK Blaubeeren&quot;, amt: &quot;140 g&quot;, tag: &quot;Anthocyane&quot;, tc: &quot;#7c3aed&quot; },
      { name: &quot;Rohe Rote Beete, gerieben&quot;, amt: &quot;70 g&quot;, tag: &quot;Nitrat roh ↑↑&quot;, tc: &quot;#c0392b&quot; },
      { name: &quot;TK Karotte, gegart&quot;, amt: &quot;100 g&quot;, tag: &quot;Vit. A &gt;100 %&quot;, tc: &quot;#e67e22&quot; },
      { name: &quot;TK Banane&quot;, amt: &quot;80 g&quot;, tag: null },
      { name: &quot;Hanfsamen, geschält&quot;, amt: &quot;20 g&quot;, tag: &quot;Mg · vollst. AS&quot;, tc: &quot;#1a6b8a&quot; },
      { name: &quot;Haferflocken, fein&quot;, amt: &quot;28 g&quot;, tag: null },
      { name: &quot;Meersalz&quot;, amt: &quot;1 Prise&quot;, tag: &quot;Elektrolyt&quot;, tc: &quot;#1a6b8a&quot; },
    ],
    fills: [&quot;Vit. A &gt;100 %&quot;, &quot;Nitrat ↑↑&quot;, &quot;Mg ~70 %&quot;],
    note: &quot;Farbe: tief violett-rot · Rote Beete zuletzt einfüllen · beste post-run Variante&quot;,
  },
  {
    id: 3,
    name: &quot;Blueberry Pineapple Broccoli Chia&quot;,
    badge: &quot;Sulforaphan + Bromelain&quot;,
    badgeColor: &quot;#1a6b8a&quot;,
    banana: false,
    desc: &quot;Ananas überdeckt Brokkoli vollständig. Bromelain + Sulforaphan beide Nrf2-aktiv. Höchste Vitamin-C-Dichte. Ohne Banane.&quot;,
    macros: { kcal: 707, p: 49, f: 19, kh: 80, bal: 14 },
    ingredients: [
      { name: &quot;TK Blaubeeren&quot;, amt: &quot;130 g&quot;, tag: &quot;Anthocyane&quot;, tc: &quot;#7c3aed&quot; },
      { name: &quot;TK Ananas&quot;, amt: &quot;130 g&quot;, tag: &quot;Bromelain · Vit. C&quot;, tc: &quot;#e67e22&quot; },
      { name: &quot;TK Brokkoli&quot;, amt: &quot;80 g&quot;, tag: &quot;Sulforaphan · Nrf2↑&quot;, tc: &quot;#1a7a4a&quot; },
      { name: &quot;Chiasamen&quot;, amt: &quot;15 g&quot;, tag: &quot;Omega-3&quot;, tc: &quot;#d4860a&quot; },
      { name: &quot;Haferflocken, fein&quot;, amt: &quot;30 g&quot;, tag: null },
      { name: &quot;Medjool-Dattel, entkernt&quot;, amt: &quot;1 Stk. (~18 g)&quot;, tag: &quot;Süße + KH&quot;, tc: &quot;#888&quot; },
      { name: &quot;Bio-Limette, ½ mit Schale&quot;, amt: &quot;~30 ml&quot;, tag: &quot;Flavonoide&quot;, tc: &quot;#1a7a4a&quot; },
    ],
    fills: [&quot;Vit. C ~90 %&quot;, &quot;Sulforaphan&quot;, &quot;niedrigstes Fett&quot;],
    note: &quot;Farbe: hellblau-gelb · Ananas-Menge nicht reduzieren — überdeckt Brokkoli vollständig&quot;,
  },
  {
    id: 4,
    name: &quot;Blueberry Cherry Cacao Zucchini&quot;,
    badge: &quot;DOMS + Flavanole&quot;,
    badgeColor: &quot;#8b5cf6&quot;,
    banana: false,
    desc: &quot;Sauerkirsche + Blaubeeren = doppelte Anthocyan-Dosis. Kakao-Flavanole ergänzen COX-Hemmung. Zucchini erhöht Volumen ohne Geschmack. Ohne Banane.&quot;,
    macros: { kcal: 712, p: 50, f: 22, kh: 72, bal: 12 },
    ingredients: [
      { name: &quot;TK Blaubeeren&quot;, amt: &quot;120 g&quot;, tag: &quot;Anthocyane&quot;, tc: &quot;#7c3aed&quot; },
      { name: &quot;TK Sauerkirschen&quot;, amt: &quot;120 g&quot;, tag: &quot;COX · DOMS↓&quot;, tc: &quot;#c0392b&quot; },
      { name: &quot;TK Zucchini, roh gewürfelt&quot;, amt: &quot;100 g&quot;, tag: &quot;Volumen · neutral&quot;, tc: &quot;#1a7a4a&quot; },
      { name: &quot;Rohkakao-Pulver, ungesüßt&quot;, amt: &quot;14 g&quot;, tag: &quot;Flavanole · Mg&quot;, tc: &quot;#8b5cf6&quot; },
      { name: &quot;Mandeln, ganz&quot;, amt: &quot;20 g&quot;, tag: &quot;Vit. E&quot;, tc: &quot;#d4860a&quot; },
      { name: &quot;Haferflocken, fein&quot;, amt: &quot;30 g&quot;, tag: null },
      { name: &quot;Medjool-Dattel, entkernt&quot;, amt: &quot;1 Stk. (~18 g)&quot;, tag: &quot;Süße&quot;, tc: &quot;#888&quot; },
    ],
    fills: [&quot;DOMS↓&quot;, &quot;Mg ~80 %&quot;, &quot;Flavanole ↑↑&quot;],
    note: &quot;Farbe: dunkelbraun-violett · stärkste anti-inflammatorische Kombination · post-workout ideal&quot;,
  },
  {
    id: 5,
    name: &quot;Blueberry Peach Spinach Brazil&quot;,
    badge: &quot;Selen + Kalium&quot;,
    badgeColor: &quot;#7a5a1a&quot;,
    banana: false,
    desc: &quot;Paranüsse (2 Stk.) decken 100 % Selen-Tagesbedarf. Pfirsich für Kalium und Cremigkeit. Spinat für Vitamin K. Niedrigste Kaloriendichte.&quot;,
    macros: { kcal: 668, p: 47, f: 19, kh: 71, bal: 12 },
    ingredients: [
      { name: &quot;TK Blaubeeren&quot;, amt: &quot;130 g&quot;, tag: &quot;Anthocyane&quot;, tc: &quot;#7c3aed&quot; },
      { name: &quot;TK Pfirsich&quot;, amt: &quot;130 g&quot;, tag: &quot;Kalium · mild-cremig&quot;, tc: &quot;#e67e22&quot; },
      { name: &quot;TK Blattspinat&quot;, amt: &quot;55 g&quot;, tag: &quot;Vit. K · Folat&quot;, tc: &quot;#1a7a4a&quot; },
      { name: &quot;Paranüsse, ganz&quot;, amt: &quot;2 Stk. (~14 g)&quot;, tag: &quot;Selen 100 % RDA&quot;, tc: &quot;#7a5a1a&quot; },
      { name: &quot;Chiasamen&quot;, amt: &quot;14 g&quot;, tag: &quot;Omega-3&quot;, tc: &quot;#d4860a&quot; },
      { name: &quot;Haferflocken, fein&quot;, amt: &quot;28 g&quot;, tag: null },
    ],
    fills: [&quot;Selen ~100 %&quot;, &quot;Vit. K &gt;200 %&quot;, &quot;niedrigste kcal&quot;],
    note: &quot;Paranüsse: max. 2 Stk./Tag, nicht täglich · niedrigste kcal der Serie&quot;,
  },
];

const macroLabels = [
  { key: &quot;kcal&quot;, label: &quot;kcal&quot;, color: &quot;#1a1a1a&quot;, unit: &quot;&quot; },
  { key: &quot;p&quot;, label: &quot;Protein&quot;, color: &quot;#7c3aed&quot;, unit: &quot;g&quot; },
  { key: &quot;f&quot;, label: &quot;Fett&quot;, color: &quot;#d4860a&quot;, unit: &quot;g&quot; },
  { key: &quot;kh&quot;, label: &quot;KH&quot;, color: &quot;#1a7a4a&quot;, unit: &quot;g&quot; },
  { key: &quot;bal&quot;, label: &quot;Ballaststoffe&quot;, color: &quot;#1a6b8a&quot;, unit: &quot;g&quot; },
];

export default function App() {
  const [open, setOpen] = useState(null);

  return (
    &lt;div style={{
      fontFamily: &quot;Georgia, serif&quot;,
      background: &quot;#f9f7f3&quot;,
      minHeight: &quot;100vh&quot;,
      padding: &quot;1rem 1rem 3rem&quot;,
      maxWidth: 480,
      margin: &quot;0 auto&quot;,
    }}&gt;
      {/* Header */}
      &lt;div style={{ marginBottom: &quot;1rem&quot; }}&gt;
        &lt;p style={{ fontSize: 10, color: &quot;#bbb&quot;, letterSpacing: &quot;.12em&quot;, margin: &quot;0 0 3px&quot;, fontFamily: &quot;monospace&quot; }}&gt;
          TK BLAUBEEREN · 5 VARIANTEN
        &lt;/p&gt;
        &lt;h1 style={{ fontSize: 20, fontWeight: 700, color: &quot;#1a1a1a&quot;, margin: &quot;0 0 3px&quot; }}&gt;
          Blaubeeren-Smoothies
        &lt;/h1&gt;
        &lt;p style={{ fontSize: 12, color: &quot;#999&quot;, margin: 0 }}&gt;
          250 ml Vollmilch · 35 g Proteinpulver · 5 g Kreatin · immer Gemüse
        &lt;/p&gt;
      &lt;/div&gt;

      {/* Base info */}
      &lt;div style={{
        background: &quot;#fff&quot;, borderRadius: 10, border: &quot;0.5px solid #e5e0d8&quot;,
        padding: &quot;8px 12px&quot;, marginBottom: 14,
        display: &quot;flex&quot;, gap: 10, flexWrap: &quot;wrap&quot;,
      }}&gt;
        {[
          { label: &quot;Basis-kcal&quot;, val: &quot;~375&quot;, color: &quot;#1a1a1a&quot; },
          { label: &quot;Basis-Protein&quot;, val: &quot;~40 g&quot;, color: &quot;#7c3aed&quot; },
          { label: &quot;Basis-Fett&quot;, val: &quot;~16 g&quot;, color: &quot;#d4860a&quot; },
          { label: &quot;Basis-KH&quot;, val: &quot;~14 g&quot;, color: &quot;#1a7a4a&quot; },
        ].map((b, i) =&gt; (
          &lt;div key={i} style={{ textAlign: &quot;center&quot;, flex: 1 }}&gt;
            &lt;div style={{ fontSize: 9, color: &quot;#ccc&quot;, fontFamily: &quot;monospace&quot; }}&gt;{b.label}&lt;/div&gt;
            &lt;div style={{ fontSize: 12, fontWeight: 700, color: b.color }}&gt;{b.val}&lt;/div&gt;
          &lt;/div&gt;
        ))}
      &lt;/div&gt;

      {/* Cards */}
      {smoothies.map((s, idx) =&gt; (
        &lt;div key={s.id} style={{
          background: &quot;#fff&quot;,
          borderRadius: 12,
          border: `0.5px solid ${open === s.id ? s.badgeColor + &quot;55&quot; : &quot;#e5e0d8&quot;}`,
          marginBottom: 10,
          overflow: &quot;hidden&quot;,
          transition: &quot;border-color .2s&quot;,
        }}&gt;
          &lt;button
            onClick={() =&gt; setOpen(open === s.id ? null : s.id)}
            style={{ width: &quot;100%&quot;, background: &quot;none&quot;, border: &quot;none&quot;, padding: &quot;12px 13px 10px&quot;, textAlign: &quot;left&quot;, cursor: &quot;pointer&quot; }}
          &gt;
            {/* Number + badge + name */}
            &lt;div style={{ display: &quot;flex&quot;, alignItems: &quot;flex-start&quot;, gap: 10 }}&gt;
              &lt;span style={{
                fontSize: 22, fontWeight: 800, color: s.badgeColor + &quot;30&quot;,
                lineHeight: 1, fontFamily: &quot;monospace&quot;, flexShrink: 0,
              }}&gt;0{idx + 1}&lt;/span&gt;
              &lt;div style={{ flex: 1 }}&gt;
                &lt;div style={{ display: &quot;flex&quot;, alignItems: &quot;center&quot;, gap: 6, flexWrap: &quot;wrap&quot;, marginBottom: 3 }}&gt;
                  &lt;span style={{
                    fontSize: 10, fontWeight: 700, padding: &quot;2px 8px&quot;, borderRadius: 20,
                    background: s.badgeColor + &quot;15&quot;, color: s.badgeColor,
                    letterSpacing: &quot;.04em&quot;, fontFamily: &quot;monospace&quot;,
                  }}&gt;{s.badge}&lt;/span&gt;
                  {s.banana &amp;&amp; (
                    &lt;span style={{ fontSize: 10, color: &quot;#ccc&quot; }}&gt;🍌&lt;/span&gt;
                  )}
                &lt;/div&gt;
                &lt;div style={{ fontSize: 14, fontWeight: 700, color: &quot;#1a1a1a&quot; }}&gt;{s.name}&lt;/div&gt;
                &lt;p style={{ fontSize: 12, color: &quot;#888&quot;, margin: &quot;3px 0 0&quot;, lineHeight: 1.5 }}&gt;{s.desc}&lt;/p&gt;
              &lt;/div&gt;
              &lt;span style={{ color: &quot;#ccc&quot;, fontSize: 13, marginTop: 2, flexShrink: 0 }}&gt;
                {open === s.id ? &quot;▲&quot; : &quot;▼&quot;}
              &lt;/span&gt;
            &lt;/div&gt;

            {/* Macros */}
            &lt;div style={{ display: &quot;grid&quot;, gridTemplateColumns: &quot;repeat(5,1fr)&quot;, gap: 5, marginTop: 10 }}&gt;
              {macroLabels.map((m) =&gt; (
                &lt;div key={m.key} style={{
                  background: &quot;#f9f7f3&quot;, borderRadius: 7, padding: &quot;5px 3px&quot;, textAlign: &quot;center&quot;,
                  border: m.key === &quot;kh&quot; ? `0.5px solid ${s.badgeColor}40` : &quot;0.5px solid transparent&quot;,
                }}&gt;
                  &lt;div style={{ fontSize: 9, color: &quot;#bbb&quot;, marginBottom: 1 }}&gt;{m.label}&lt;/div&gt;
                  &lt;div style={{ fontSize: 12, fontWeight: 700, color: m.key === &quot;kh&quot; ? s.badgeColor : m.color }}&gt;
                    {s.macros[m.key]}{m.unit}
                  &lt;/div&gt;
                &lt;/div&gt;
              ))}
            &lt;/div&gt;

            {/* Fills */}
            &lt;div style={{ display: &quot;flex&quot;, gap: 4, flexWrap: &quot;wrap&quot;, marginTop: 7 }}&gt;
              {s.fills.map((f, i) =&gt; (
                &lt;span key={i} style={{
                  fontSize: 10, padding: &quot;2px 7px&quot;, borderRadius: 20,
                  background: s.badgeColor + &quot;10&quot;, color: s.badgeColor,
                  border: `0.5px solid ${s.badgeColor}25`,
                }}&gt;{f}&lt;/span&gt;
              ))}
            &lt;/div&gt;
          &lt;/button&gt;

          {/* Ingredients */}
          {open === s.id &amp;&amp; (
            &lt;div style={{ borderTop: &quot;0.5px solid #f0ece4&quot;, padding: &quot;8px 13px 12px&quot; }}&gt;
              &lt;p style={{ fontSize: 9, fontWeight: 700, color: &quot;#ccc&quot;, letterSpacing: &quot;.12em&quot;, margin: &quot;0 0 6px&quot;, fontFamily: &quot;monospace&quot; }}&gt;
                ZUTATEN · + 250 ml Milch + 35 g Pulver + 5 g Kreatin
              &lt;/p&gt;
              {s.ingredients.map((ing, i) =&gt; (
                &lt;div key={i} style={{
                  display: &quot;flex&quot;, justifyContent: &quot;space-between&quot;, alignItems: &quot;flex-start&quot;,
                  padding: &quot;4px 0&quot;,
                  borderBottom: i &lt; s.ingredients.length - 1 ? &quot;0.5px solid #f5f2ee&quot; : &quot;none&quot;,
                }}&gt;
                  &lt;div&gt;
                    &lt;span style={{ fontSize: 13, color: &quot;#333&quot; }}&gt;{ing.name}&lt;/span&gt;
                    {ing.tag &amp;&amp; (
                      &lt;span style={{ fontSize: 10, color: ing.tc || &quot;#aaa&quot;, marginLeft: 5, fontFamily: &quot;monospace&quot; }}&gt;
                        · {ing.tag}
                      &lt;/span&gt;
                    )}
                  &lt;/div&gt;
                  &lt;span style={{ fontSize: 11, fontWeight: 700, color: &quot;#bbb&quot;, whiteSpace: &quot;nowrap&quot;, marginLeft: 10 }}&gt;
                    {ing.amt}
                  &lt;/span&gt;
                &lt;/div&gt;
              ))}
              &lt;div style={{
                marginTop: 8, fontSize: 11, color: &quot;#999&quot;, fontStyle: &quot;italic&quot;,
                paddingTop: 7, borderTop: `2px solid ${s.badgeColor}20`,
                borderLeft: `3px solid ${s.badgeColor}40`,
                paddingLeft: 8, lineHeight: 1.5,
              }}&gt;
                {s.note}
              &lt;/div&gt;
            &lt;/div&gt;
          )}
        &lt;/div&gt;
      ))}

      &lt;p style={{ fontSize: 10, color: &quot;#ddd&quot;, textAlign: &quot;center&quot;, fontFamily: &quot;monospace&quot;, marginTop: 4 }}&gt;
        TIPPE FÜR ZUTATEN
      &lt;/p&gt;
    &lt;/div&gt;
  );
}
</code></pre></details>
