---
titel: mango_five.jsx
status: aktiv
datum: '2026-04-24'
quelle:
  typ: claude
  url: https://claude.ai/chat/e243ac2d-4628-41b9-ae87-39b4cf14f878
  hinweis: Protein-Smoothies für Frühstück und Muskelaufbau
importiert: true
linie: mango-five-jsx-cc59c
---

<details><summary>Ursprüngliche Datei</summary><pre><code>import { useState } from &quot;react&quot;;

const smoothies = [
  {
    id: 1,
    name: &quot;Mango Spinach Banana Flax&quot;,
    badge: &quot;Vit. K · Folat · ALA&quot;,
    color: &quot;#1a7a4a&quot;,
    desc: &quot;Spinat schließt Vit. K + Folat · Banane für schnelle post-run KH · Leinsamen für ALA · ausgewogenste Variante&quot;,
    macros: { kcal: 600, p: 43, f: 18, kh: 68, bal: 12 },
    ingredients: [
      { name: &quot;Vollmilch 3,8 %&quot;,           amt: &quot;220 ml&quot;, vol: 220 },
      { name: &quot;TK Mango&quot;,                  amt: &quot;140 g&quot;,  vol: 133, tag: &quot;Vit. C · Cremigkeit&quot;, tc: &quot;#e67e22&quot; },
      { name: &quot;TK Banane&quot;,                 amt: &quot;75 g&quot;,   vol: 71,  tag: &quot;schnelle KH&quot;, tc: &quot;#1a7a4a&quot; },
      { name: &quot;TK Blattspinat&quot;,            amt: &quot;55 g&quot;,   vol: 52,  tag: &quot;Vit. K + Folat&quot;, tc: &quot;#1a7a4a&quot; },
      { name: &quot;Leinsamen, gemahlen&quot;,       amt: &quot;12 g&quot;,   vol: 12,  tag: &quot;ALA 3,2 g&quot;, tc: &quot;#d4860a&quot; },
      { name: &quot;Haferflocken, fein&quot;,        amt: &quot;22 g&quot;,   vol: 35 },
      { name: &quot;35 g Pulver + 5 g Kreatin&quot;,amt: &quot;fix&quot;,    vol: 50, fixed: true },
    ],
    totalVol: 573,
    note: &quot;Farbe: sattgrün · einfachste Zubereitung · Spinat hinter Mango komplett unsichtbar&quot;,
  },
  {
    id: 2,
    name: &quot;Mango Beet Banana Hemp&quot;,
    badge: &quot;NO-Boost · höchste KH&quot;,
    color: &quot;#c0392b&quot;,
    desc: &quot;Rote Beete roh + Mango = Nitrat + Vit. C synergistisch · höchste KH der fünf · Hanfsamen für Mg + vollständige AS · Meersalz für Elektrolyte&quot;,
    macros: { kcal: 640, p: 46, f: 26, kh: 71, bal: 11 },
    ingredients: [
      { name: &quot;Vollmilch 3,8 %&quot;,           amt: &quot;225 ml&quot;, vol: 225 },
      { name: &quot;TK Mango&quot;,                  amt: &quot;130 g&quot;,  vol: 123, tag: &quot;Vit. C · KH&quot;, tc: &quot;#e67e22&quot; },
      { name: &quot;Rohe Rote Beete, gerieben&quot;, amt: &quot;60 g&quot;,   vol: 57,  tag: &quot;Nitrat roh ↑↑&quot;, tc: &quot;#c0392b&quot; },
      { name: &quot;TK Banane&quot;,                 amt: &quot;70 g&quot;,   vol: 66,  tag: &quot;schnelle KH + Bindung&quot;, tc: &quot;#1a7a4a&quot; },
      { name: &quot;Hanfsamen, geschält&quot;,       amt: &quot;18 g&quot;,   vol: 20,  tag: &quot;Mg · vollst. AS&quot;, tc: &quot;#1a6b8a&quot; },
      { name: &quot;Haferflocken, fein&quot;,        amt: &quot;25 g&quot;,   vol: 40 },
      { name: &quot;Meersalz&quot;,                  amt: &quot;1 Prise&quot;,vol: 0,   tag: &quot;Na-Ausgleich&quot;, tc: &quot;#1a6b8a&quot; },
      { name: &quot;35 g Pulver + 5 g Kreatin&quot;,amt: &quot;fix&quot;,    vol: 50, fixed: true },
    ],
    totalVol: 581,
    note: &quot;Rote Beete zuletzt einfüllen · stärkste post-run Variante · Farbe: violett-orange&quot;,
  },
  {
    id: 3,
    name: &quot;Mango Cherry Broccoli Chia&quot;,
    badge: &quot;DOMS · Sulforaphan&quot;,
    color: &quot;#1a5a8a&quot;,
    desc: &quot;Mango überdeckt Brokkoli vollständig · Sauerkirsche für DOMS-Reduktion · Sulforaphan aktiviert Nrf2 · dreifache anti-inflammatorische Wirkung&quot;,
    macros: { kcal: 593, p: 42, f: 17, kh: 70, bal: 13 },
    ingredients: [
      { name: &quot;Vollmilch 3,8 %&quot;,           amt: &quot;195 ml&quot;, vol: 195 },
      { name: &quot;TK Mango&quot;,                  amt: &quot;130 g&quot;,  vol: 123, tag: &quot;Brokkoli überdecken&quot;, tc: &quot;#e67e22&quot; },
      { name: &quot;TK Sauerkirschen&quot;,          amt: &quot;70 g&quot;,   vol: 66,  tag: &quot;DOMS↓ · COX-Hemmer&quot;, tc: &quot;#c0392b&quot; },
      { name: &quot;TK Brokkoli&quot;,              amt: &quot;65 g&quot;,   vol: 62,  tag: &quot;Sulforaphan · nie auftauen&quot;, tc: &quot;#1a7a4a&quot; },
      { name: &quot;TK Banane&quot;,                 amt: &quot;60 g&quot;,   vol: 57,  tag: &quot;KH + Bindung&quot;, tc: &quot;#1a7a4a&quot; },
      { name: &quot;Chiasamen&quot;,                 amt: &quot;12 g&quot;,   vol: 12,  tag: &quot;Omega-3&quot;, tc: &quot;#7c3aed&quot; },
      { name: &quot;Haferflocken, fein&quot;,        amt: &quot;22 g&quot;,   vol: 35 },
      { name: &quot;35 g Pulver + 5 g Kreatin&quot;,amt: &quot;fix&quot;,    vol: 50, fixed: true },
    ],
    totalVol: 600,
    note: &quot;Brokkoli direkt aus TK — nicht auftauen · Mango-Menge unverzichtbar für vollständige Abdeckung&quot;,
  },
  {
    id: 4,
    name: &quot;Mango Pineapple Carrot Walnut&quot;,
    badge: &quot;Beta-Carotin · Bromelain&quot;,
    color: &quot;#d4860a&quot;,
    desc: &quot;Mango + Ananas + Karotte = dreifaches Beta-Carotin · Bromelain aus Ananas anti-inflammatorisch · Walnüsse für ALA · tropischste Variante&quot;,
    macros: { kcal: 575, p: 38, f: 22, kh: 62, bal: 11 },
    ingredients: [
      { name: &quot;Vollmilch 3,8 %&quot;,           amt: &quot;215 ml&quot;, vol: 215 },
      { name: &quot;TK Mango&quot;,                  amt: &quot;130 g&quot;,  vol: 123, tag: &quot;Beta-Carotin · Vit. C&quot;, tc: &quot;#e67e22&quot; },
      { name: &quot;TK Ananas&quot;,                 amt: &quot;100 g&quot;,  vol: 95,  tag: &quot;Bromelain · Vit. C&quot;, tc: &quot;#d4860a&quot; },
      { name: &quot;TK Karotte, gegart&quot;,        amt: &quot;70 g&quot;,   vol: 66,  tag: &quot;Beta-Carotin · Vit. A&quot;, tc: &quot;#d4860a&quot; },
      { name: &quot;Walnüsse, ganz&quot;,            amt: &quot;15 g&quot;,   vol: 17,  tag: &quot;ALA Omega-3&quot;, tc: &quot;#7a5a1a&quot; },
      { name: &quot;Medjool-Dattel, entkernt&quot;,  amt: &quot;1 Stk. (~18 g)&quot;, vol: 15, tag: &quot;KH + Bindung&quot; },
      { name: &quot;Leinsamen, gemahlen&quot;,       amt: &quot;12 g&quot;,   vol: 12,  tag: &quot;ALA&quot;, tc: &quot;#7a5a1a&quot; },
      { name: &quot;35 g Pulver + 5 g Kreatin&quot;,amt: &quot;fix&quot;,    vol: 50, fixed: true },
    ],
    totalVol: 593,
    note: &quot;Farbe: leuchtendes Orange · Vit.-A-Tagesbedarf vollständig gedeckt · süßeste der fünf&quot;,
  },
  {
    id: 5,
    name: &quot;Mango Blackberry Spinach Almond&quot;,
    badge: &quot;Anthocyane · Vit. E · Vit. K&quot;,
    color: &quot;#7c3aed&quot;,
    desc: &quot;Mango + Brombeere = tropisch-beerige KH-Basis · Spinat für Vit. K · Mandeln für Vit. E · höchste Ballaststoffe der fünf&quot;,
    macros: { kcal: 604, p: 43, f: 21, kh: 65, bal: 13 },
    ingredients: [
      { name: &quot;Vollmilch 3,8 %&quot;,           amt: &quot;175 ml&quot;, vol: 175 },
      { name: &quot;TK Mango&quot;,                  amt: &quot;120 g&quot;,  vol: 114, tag: &quot;Vit. C · KH&quot;, tc: &quot;#e67e22&quot; },
      { name: &quot;TK Brombeeren&quot;,             amt: &quot;110 g&quot;,  vol: 104, tag: &quot;Anthocyane · Vit. K&quot;, tc: &quot;#7c3aed&quot; },
      { name: &quot;TK Blattspinat&quot;,            amt: &quot;55 g&quot;,   vol: 52,  tag: &quot;Vit. K + Folat&quot;, tc: &quot;#1a7a4a&quot; },
      { name: &quot;TK Banane&quot;,                 amt: &quot;60 g&quot;,   vol: 57,  tag: &quot;KH + Bindung&quot;, tc: &quot;#1a7a4a&quot; },
      { name: &quot;Mandeln, ganz&quot;,             amt: &quot;18 g&quot;,   vol: 20,  tag: &quot;Vit. E · Calcium&quot;, tc: &quot;#d4860a&quot; },
      { name: &quot;Haferflocken, fein&quot;,        amt: &quot;18 g&quot;,   vol: 29 },
      { name: &quot;35 g Pulver + 5 g Kreatin&quot;,amt: &quot;fix&quot;,    vol: 50, fixed: true },
    ],
    totalVol: 601,
    note: &quot;Farbe: dunkelviolett · Mango + Brombeere harmonieren sehr gut · niedrigste Milchmenge der fünf&quot;,
  },
];

const mcols = [
  { key:&quot;kcal&quot;, l:&quot;kcal&quot;, c:&quot;#1a1a1a&quot;, u:&quot;&quot; },
  { key:&quot;p&quot;,   l:&quot;Protein&quot;, c:&quot;#7c3aed&quot;, u:&quot;g&quot; },
  { key:&quot;f&quot;,   l:&quot;Fett&quot;, c:&quot;#d4860a&quot;, u:&quot;g&quot; },
  { key:&quot;kh&quot;,  l:&quot;KH&quot;, c:null, u:&quot;g&quot; },
  { key:&quot;bal&quot;, l:&quot;Ballaststoffe&quot;, c:&quot;#1a6b8a&quot;, u:&quot;g&quot; },
];

export default function App() {
  const [open, setOpen] = useState(null);
  return (
    &lt;div style={{ fontFamily:&quot;Georgia,serif&quot;, background:&quot;#f9f7f3&quot;, minHeight:&quot;100vh&quot;, padding:&quot;1rem 1rem 3rem&quot;, maxWidth:480, margin:&quot;0 auto&quot; }}&gt;

      &lt;div style={{ marginBottom:&quot;1rem&quot; }}&gt;
        &lt;p style={{ fontSize:10, color:&quot;#bbb&quot;, letterSpacing:&quot;.12em&quot;, margin:&quot;0 0 3px&quot;, fontFamily:&quot;monospace&quot; }}&gt;
          POST ZONE 2 / GYM · TK MANGO · MAX. 600 ML
        &lt;/p&gt;
        &lt;h1 style={{ fontSize:19, fontWeight:700, color:&quot;#1a1a1a&quot;, margin:&quot;0 0 3px&quot; }}&gt;5 Mango-Smoothies&lt;/h1&gt;
        &lt;p style={{ fontSize:12, color:&quot;#999&quot;, margin:0 }}&gt;35 g Vetain Neutral · 5 g Kreatin · Vollmilch · Gemüse in allen fünf&lt;/p&gt;
      &lt;/div&gt;

      {smoothies.map((s) =&gt; (
        &lt;div key={s.id} style={{
          background:&quot;#fff&quot;, borderRadius:12,
          border:`0.5px solid ${open===s.id ? s.color+&quot;55&quot;:&quot;#e5e0d8&quot;}`,
          marginBottom:10, overflow:&quot;hidden&quot;,
        }}&gt;
          &lt;button onClick={() =&gt; setOpen(open===s.id ? null : s.id)}
            style={{ width:&quot;100%&quot;, background:&quot;none&quot;, border:&quot;none&quot;, padding:&quot;12px 13px 10px&quot;, textAlign:&quot;left&quot;, cursor:&quot;pointer&quot; }}&gt;

            &lt;div style={{ display:&quot;flex&quot;, alignItems:&quot;flex-start&quot;, gap:10 }}&gt;
              &lt;span style={{ fontSize:22, fontWeight:800, color:s.color+&quot;28&quot;, fontFamily:&quot;monospace&quot;, lineHeight:1, flexShrink:0 }}&gt;0{s.id}&lt;/span&gt;
              &lt;div style={{ flex:1 }}&gt;
                &lt;div style={{ display:&quot;flex&quot;, alignItems:&quot;center&quot;, gap:6, flexWrap:&quot;wrap&quot;, marginBottom:3 }}&gt;
                  &lt;span style={{ fontSize:10, fontWeight:700, padding:&quot;2px 8px&quot;, borderRadius:20, background:s.color+&quot;14&quot;, color:s.color, fontFamily:&quot;monospace&quot; }}&gt;{s.badge}&lt;/span&gt;
                &lt;/div&gt;
                &lt;div style={{ fontSize:14, fontWeight:700, color:&quot;#1a1a1a&quot; }}&gt;{s.name}&lt;/div&gt;
                &lt;p style={{ fontSize:11, color:&quot;#888&quot;, margin:&quot;3px 0 0&quot;, lineHeight:1.5 }}&gt;{s.desc}&lt;/p&gt;
              &lt;/div&gt;
              &lt;span style={{ color:&quot;#ccc&quot;, fontSize:13, flexShrink:0, marginTop:2 }}&gt;{open===s.id?&quot;▲&quot;:&quot;▼&quot;}&lt;/span&gt;
            &lt;/div&gt;

            &lt;div style={{ display:&quot;grid&quot;, gridTemplateColumns:&quot;repeat(5,1fr)&quot;, gap:5, marginTop:9 }}&gt;
              {mcols.map((m) =&gt; (
                &lt;div key={m.key} style={{
                  background:&quot;#f9f7f3&quot;, borderRadius:7, padding:&quot;5px 3px&quot;, textAlign:&quot;center&quot;,
                  border: m.key===&quot;kh&quot; ? `0.5px solid ${s.color}45`:&quot;0.5px solid transparent&quot;,
                }}&gt;
                  &lt;div style={{ fontSize:9, color:&quot;#ccc&quot;, marginBottom:1 }}&gt;{m.l}&lt;/div&gt;
                  &lt;div style={{ fontSize:12, fontWeight:700, color: m.key===&quot;kh&quot; ? s.color : m.c }}&gt;{s.macros[m.key]}{m.u}&lt;/div&gt;
                &lt;/div&gt;
              ))}
            &lt;/div&gt;
            &lt;div style={{ marginTop:6, fontSize:11, color:s.color, fontFamily:&quot;monospace&quot; }}&gt;≈ {s.totalVol} ml ✓&lt;/div&gt;
          &lt;/button&gt;

          {open===s.id &amp;&amp; (
            &lt;div style={{ borderTop:&quot;0.5px solid #f0ece4&quot;, padding:&quot;8px 13px 12px&quot; }}&gt;
              &lt;p style={{ fontSize:9, fontWeight:700, color:&quot;#ccc&quot;, letterSpacing:&quot;.12em&quot;, margin:&quot;0 0 6px&quot;, fontFamily:&quot;monospace&quot; }}&gt;ZUTATEN&lt;/p&gt;
              &lt;div style={{ display:&quot;flex&quot;, gap:1, height:5, borderRadius:3, overflow:&quot;hidden&quot;, marginBottom:8 }}&gt;
                {s.ingredients.map((ing,i) =&gt; {
                  const cols=[&quot;#d4860a&quot;,&quot;#e67e22&quot;,&quot;#c0392b&quot;,&quot;#1a7a4a&quot;,&quot;#7c3aed&quot;,&quot;#7a5a1a&quot;,&quot;#888&quot;,&quot;#7c3aed&quot;];
                  return &lt;div key={i} style={{ flexBasis:`${Math.max((ing.vol/s.totalVol)*100,0.5)}%`, background:cols[i%cols.length], opacity:ing.fixed?0.3:0.55 }}/&gt;;
                })}
              &lt;/div&gt;
              {s.ingredients.map((ing,i) =&gt; (
                &lt;div key={i} style={{
                  display:&quot;flex&quot;, justifyContent:&quot;space-between&quot;, alignItems:&quot;flex-start&quot;,
                  padding:&quot;4px 0&quot;, borderBottom: i&lt;s.ingredients.length-1?&quot;0.5px solid #f5f2ee&quot;:&quot;none&quot;,
                  background:ing.fixed?&quot;#f5f3ff&quot;:&quot;transparent&quot;, borderRadius:ing.fixed?4:0, paddingLeft:ing.fixed?4:0,
                }}&gt;
                  &lt;div&gt;
                    &lt;span style={{ fontSize:13, color:ing.fixed?&quot;#7c3aed&quot;:&quot;#333&quot; }}&gt;{ing.name}&lt;/span&gt;
                    {ing.tag &amp;&amp; &lt;span style={{ fontSize:10, color:ing.tc||s.color, marginLeft:5, fontFamily:&quot;monospace&quot; }}&gt;· {ing.tag}&lt;/span&gt;}
                  &lt;/div&gt;
                  &lt;div style={{ textAlign:&quot;right&quot;, marginLeft:8, flexShrink:0 }}&gt;
                    &lt;div style={{ fontSize:11, fontWeight:700, color:&quot;#bbb&quot; }}&gt;{ing.amt}&lt;/div&gt;
                    {!ing.fixed &amp;&amp; ing.vol&gt;2 &amp;&amp; &lt;div style={{ fontSize:9, color:&quot;#ddd&quot; }}&gt;≈ {ing.vol} ml&lt;/div&gt;}
                  &lt;/div&gt;
                &lt;/div&gt;
              ))}
              &lt;div style={{ marginTop:8, fontSize:11, color:&quot;#999&quot;, fontStyle:&quot;italic&quot;, borderLeft:`3px solid ${s.color}35`, paddingLeft:8, lineHeight:1.5 }}&gt;{s.note}&lt;/div&gt;
            &lt;/div&gt;
          )}
        &lt;/div&gt;
      ))}
      &lt;p style={{ fontSize:10, color:&quot;#ddd&quot;, textAlign:&quot;center&quot;, fontFamily:&quot;monospace&quot;, marginTop:4 }}&gt;TIPPE FÜR ZUTATEN&lt;/p&gt;
    &lt;/div&gt;
  );
}
</code></pre></details>
