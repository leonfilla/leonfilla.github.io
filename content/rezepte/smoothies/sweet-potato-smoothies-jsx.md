---
titel: sweet_potato_smoothies.jsx
status: aktiv
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
    name: &quot;Süßkartoffel Mango Spinach Hemp&quot;,
    badge: &quot;Beta-Carotin · Vit. K · Mg&quot;,
    color: &quot;#1a7a4a&quot;,
    desc: &quot;Süßkartoffel + Mango = doppeltes Beta-Carotin · Spinat für Vit. K + Folat · Hanfsamen für Mg · cremigste der drei&quot;,
    macros: { kcal: 630, p: 46, f: 22, kh: 64, bal: 10 },
    ingredients: [
      { name: &quot;Vollmilch 3,8 %&quot;,           amt: &quot;265 ml&quot;, vol: 265 },
      { name: &quot;Süßkartoffel, gegart + abgekühlt&quot;, amt: &quot;80 g&quot;, vol: 72, tag: &quot;Beta-Carotin · Kalium · cremig&quot;, tc: &quot;#e67e22&quot; },
      { name: &quot;TK Mango&quot;,                  amt: &quot;120 g&quot;,  vol: 114, tag: &quot;Vit. C · KH&quot;, tc: &quot;#e67e22&quot; },
      { name: &quot;TK Blattspinat&quot;,            amt: &quot;50 g&quot;,   vol: 47,  tag: &quot;Vit. K + Folat&quot;, tc: &quot;#1a7a4a&quot; },
      { name: &quot;Hanfsamen, geschält&quot;,       amt: &quot;15 g&quot;,   vol: 17,  tag: &quot;Mg · vollst. AS&quot;, tc: &quot;#1a6b8a&quot; },
      { name: &quot;Haferflocken, fein&quot;,        amt: &quot;22 g&quot;,   vol: 35 },
      { name: &quot;35 g Pulver + 5 g Kreatin&quot;,amt: &quot;fix&quot;,    vol: 50, fixed: true },
    ],
    totalVol: 600,
    note: &quot;Farbe: warmes Gelb-Grün · Süßkartoffel gibt natürliche Süße und samtige Textur · Spinat geschmacklich nicht wahrnehmbar&quot;,
    spices: null,
  },
  {
    id: 2,
    name: &quot;Süßkartoffel Ananas Broccoli Chia&quot;,
    badge: &quot;Sulforaphan · Bromelain · leicht&quot;,
    color: &quot;#1a5a8a&quot;,
    desc: &quot;Ananas überdeckt Brokkoli vollständig · Sulforaphan + Bromelain + Süßkartoffel-Ballaststoffe · niedrigstes Fett + niedrigste kcal · ideal Ruhetag&quot;,
    macros: { kcal: 582, p: 42, f: 18, kh: 63, bal: 11 },
    ingredients: [
      { name: &quot;Vollmilch 3,8 %&quot;,           amt: &quot;239 ml&quot;, vol: 239 },
      { name: &quot;Süßkartoffel, gegart + abgekühlt&quot;, amt: &quot;80 g&quot;, vol: 72, tag: &quot;Beta-Carotin · Bindung&quot;, tc: &quot;#e67e22&quot; },
      { name: &quot;TK Ananas&quot;,                 amt: &quot;130 g&quot;,  vol: 123, tag: &quot;Bromelain · Vit. C&quot;, tc: &quot;#d4860a&quot; },
      { name: &quot;TK Brokkoli&quot;,              amt: &quot;65 g&quot;,   vol: 62,  tag: &quot;Sulforaphan · nie auftauen&quot;, tc: &quot;#1a7a4a&quot; },
      { name: &quot;Chiasamen&quot;,                 amt: &quot;12 g&quot;,   vol: 12,  tag: &quot;ALA · Ballaststoffe&quot;, tc: &quot;#7c3aed&quot; },
      { name: &quot;Haferflocken, fein&quot;,        amt: &quot;20 g&quot;,   vol: 32 },
      { name: &quot;Ingwer, frisch gerieben&quot;,   amt: &quot;1 TL&quot;,   vol: 4,   tag: &quot;anti-inflammatorisch&quot;, tc: &quot;#888&quot; },
      { name: &quot;35 g Pulver + 5 g Kreatin&quot;,amt: &quot;fix&quot;,    vol: 50, fixed: true },
    ],
    totalVol: 594,
    note: &quot;Farbe: hellgelb-orange · Ananas-Menge unverzichtbar · Brokkoli direkt aus TK → Sulforaphan bleibt intakt&quot;,
    spices: null,
  },
  {
    id: 3,
    name: &quot;Süßkartoffel Mango Carrot Walnut&quot;,
    badge: &quot;Vit. A &gt;150% · Chai-Spice&quot;,
    color: &quot;#d4860a&quot;,
    desc: &quot;Dreifaches Beta-Carotin: Süßkartoffel + Mango + Karotte · Walnüsse für ALA · Zimt + Kurkuma für Insulinsensitivität · wärmste Variante&quot;,
    macros: { kcal: 632, p: 46, f: 23, kh: 66, bal: 11 },
    ingredients: [
      { name: &quot;Vollmilch 3,8 %&quot;,           amt: &quot;239 ml&quot;, vol: 239 },
      { name: &quot;Süßkartoffel, gegart + abgekühlt&quot;, amt: &quot;80 g&quot;, vol: 72, tag: &quot;Beta-Carotin · Kalium&quot;, tc: &quot;#e67e22&quot; },
      { name: &quot;TK Mango&quot;,                  amt: &quot;120 g&quot;,  vol: 114, tag: &quot;Beta-Carotin · Vit. C&quot;, tc: &quot;#e67e22&quot; },
      { name: &quot;TK Karotte, gegart&quot;,        amt: &quot;80 g&quot;,   vol: 76,  tag: &quot;Beta-Carotin · Vit. A &gt;150 %&quot;, tc: &quot;#d4860a&quot; },
      { name: &quot;Walnüsse, ganz&quot;,            amt: &quot;15 g&quot;,   vol: 17,  tag: &quot;ALA Omega-3&quot;, tc: &quot;#7a5a1a&quot; },
      { name: &quot;Haferflocken, fein&quot;,        amt: &quot;20 g&quot;,   vol: 32 },
      { name: &quot;Ceylon-Zimt&quot;,              amt: &quot;½ TL&quot;,   vol: 1,   tag: &quot;Insulinsensitivität&quot;, tc: &quot;#888&quot; },
      { name: &quot;Kurkuma + Pfeffer&quot;,        amt: &quot;¼ TL / 1 Msp.&quot;, vol: 1, tag: &quot;Curcumin-Bioverfügbarkeit ↑&quot;, tc: &quot;#888&quot; },
      { name: &quot;35 g Pulver + 5 g Kreatin&quot;,amt: &quot;fix&quot;,    vol: 50, fixed: true },
    ],
    totalVol: 602,
    note: &quot;Farbe: leuchtendes Orange · wärmste + süßlichste Variante · Pfeffer nicht weglassen — aktiviert Curcumin um Faktor 20&quot;,
    spices: [&quot;Zimt&quot;, &quot;Kurkuma&quot;],
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
          REST-DAY · GEGARTE SÜSSKARTOFFEL · MAX. 600 ML
        &lt;/p&gt;
        &lt;h1 style={{ fontSize:19, fontWeight:700, color:&quot;#1a1a1a&quot;, margin:&quot;0 0 3px&quot; }}&gt;3 Süßkartoffel-Smoothies&lt;/h1&gt;
        &lt;p style={{ fontSize:12, color:&quot;#999&quot;, margin:0 }}&gt;35 g Vetain Neutral · 5 g Kreatin · Vollmilch · Ruhetag&lt;/p&gt;
      &lt;/div&gt;

      &lt;div style={{ background:&quot;#fff8f0&quot;, borderRadius:8, padding:&quot;8px 11px&quot;, marginBottom:12, border:&quot;0.5px solid #e67e2240&quot; }}&gt;
        &lt;p style={{ fontSize:11, color:&quot;#7a3a00&quot;, margin:0, lineHeight:1.5 }}&gt;
          &lt;strong&gt;Süßkartoffel:&lt;/strong&gt; gegart + auf Raumtemperatur oder kälter abgekühlt verwenden. Heißt die Kartoffel erhöht die Flüssigkeitstemperatur und verhindert eine cremige Textur. Schale entfernen. 80 g entsprechen etwa ⅓ einer mittelgroßen Süßkartoffel.
        &lt;/p&gt;
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
              &lt;span style={{ fontSize:22, fontWeight:800, color:s.color+&quot;28&quot;, fontFamily:&quot;monospace&quot;, lineHeight:1, flexShrink:0 }}&gt;
                0{s.id}
              &lt;/span&gt;
              &lt;div style={{ flex:1 }}&gt;
                &lt;div style={{ display:&quot;flex&quot;, alignItems:&quot;center&quot;, gap:6, flexWrap:&quot;wrap&quot;, marginBottom:3 }}&gt;
                  &lt;span style={{ fontSize:10, fontWeight:700, padding:&quot;2px 8px&quot;, borderRadius:20, background:s.color+&quot;14&quot;, color:s.color, fontFamily:&quot;monospace&quot; }}&gt;
                    {s.badge}
                  &lt;/span&gt;
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
                  &lt;div style={{ fontSize:12, fontWeight:700, color: m.key===&quot;kh&quot; ? s.color : m.c }}&gt;
                    {s.macros[m.key]}{m.u}
                  &lt;/div&gt;
                &lt;/div&gt;
              ))}
            &lt;/div&gt;

            &lt;div style={{ marginTop:6, fontSize:11, color:s.color, fontFamily:&quot;monospace&quot; }}&gt;
              ≈ {s.totalVol} ml ✓
            &lt;/div&gt;
          &lt;/button&gt;

          {open===s.id &amp;&amp; (
            &lt;div style={{ borderTop:&quot;0.5px solid #f0ece4&quot;, padding:&quot;8px 13px 12px&quot; }}&gt;
              &lt;p style={{ fontSize:9, fontWeight:700, color:&quot;#ccc&quot;, letterSpacing:&quot;.12em&quot;, margin:&quot;0 0 6px&quot;, fontFamily:&quot;monospace&quot; }}&gt;ZUTATEN&lt;/p&gt;

              &lt;div style={{ display:&quot;flex&quot;, gap:1, height:5, borderRadius:3, overflow:&quot;hidden&quot;, marginBottom:8 }}&gt;
                {s.ingredients.map((ing,i) =&gt; {
                  const cols=[&quot;#d4860a&quot;,&quot;#e67e22&quot;,&quot;#e67e22&quot;,&quot;#1a7a4a&quot;,&quot;#d4860a&quot;,&quot;#888&quot;,&quot;#888&quot;,&quot;#7c3aed&quot;];
                  return &lt;div key={i} style={{ flexBasis:`${Math.max((ing.vol/s.totalVol)*100,1)}%`, background:cols[i%cols.length], opacity:ing.fixed?0.3:0.55 }}/&gt;;
                })}
              &lt;/div&gt;

              {s.ingredients.map((ing,i) =&gt; (
                &lt;div key={i} style={{
                  display:&quot;flex&quot;, justifyContent:&quot;space-between&quot;, alignItems:&quot;flex-start&quot;,
                  padding:&quot;4px 0&quot;,
                  borderBottom: i&lt;s.ingredients.length-1?&quot;0.5px solid #f5f2ee&quot;:&quot;none&quot;,
                  background: ing.fixed?&quot;#f5f3ff&quot;:&quot;transparent&quot;,
                  borderRadius: ing.fixed?4:0,
                  paddingLeft: ing.fixed?4:0,
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

              &lt;div style={{ marginTop:8, fontSize:11, color:&quot;#999&quot;, fontStyle:&quot;italic&quot;, borderLeft:`3px solid ${s.color}35`, paddingLeft:8, lineHeight:1.5 }}&gt;
                {s.note}
              &lt;/div&gt;
            &lt;/div&gt;
          )}
        &lt;/div&gt;
      ))}

      &lt;div style={{ background:&quot;#fff&quot;, borderRadius:10, border:&quot;0.5px solid #e5e0d8&quot;, padding:&quot;9px 12px&quot;, marginTop:4 }}&gt;
        &lt;p style={{ fontSize:9, fontFamily:&quot;monospace&quot;, fontWeight:700, color:&quot;#bbb&quot;, letterSpacing:&quot;.1em&quot;, margin:&quot;0 0 4px&quot; }}&gt;RUHETAG · MAKROS IM KONTEXT&lt;/p&gt;
        &lt;p style={{ fontSize:11, color:&quot;#888&quot;, margin:0, lineHeight:1.5 }}&gt;
          Alle drei liegen bei 580–632 kcal und 62–66 g KH — abgestimmt auf das Ruhetag-Ziel von ~214 g KH und ~1.900 kcal. Fett 18–23 g lässt für Abendessen noch Spielraum.
        &lt;/p&gt;
      &lt;/div&gt;
    &lt;/div&gt;
  );
}
</code></pre></details>
