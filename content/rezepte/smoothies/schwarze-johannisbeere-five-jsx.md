---
titel: schwarze_johannisbeere_five.jsx
status: aktiv
datum: '2026-04-24'
quelle:
  typ: claude
  url: https://claude.ai/chat/e243ac2d-4628-41b9-ae87-39b4cf14f878
  hinweis: Protein-Smoothies für Frühstück und Muskelaufbau
importiert: true
---

<details><summary>Ursprüngliche Datei</summary><pre><code>import { useState } from &quot;react&quot;;

const note_sj = &quot;Schwarze Johannisbeeren sind sehr herb — jedes Rezept enthält einen Süßungspartner (Banane, Mango, Dattel oder Pfirsich).&quot;;

const smoothies = [
  {
    id: 1,
    name: &quot;SJ Spinach Banana Walnut&quot;,
    badge: &quot;Vit. K · Folat · ALA&quot;,
    color: &quot;#1a7a4a&quot;,
    training: &quot;universell&quot;,
    desc: &quot;Spinat deckt Vit. K + Folat · Walnuss für ALA · Banane süßt + bindet · Leinsamen ergänzt Omega-3 · ausgewogenste Variante&quot;,
    macros: { kcal: 688, p: 45, f: 28, kh: 68, bal: 12 },
    ingredients: [
      { name: &quot;Vollmilch 3,8 %&quot;,           amt: &quot;229 ml&quot;, vol: 229 },
      { name: &quot;TK Schwarze Johannisbeeren&quot;,  amt: &quot;120 g&quot;,  vol: 114, tag: &quot;Vit. C ~215 mg · Anthocyane&quot;, tc: &quot;#5a1a7a&quot; },
      { name: &quot;TK Banane&quot;,                  amt: &quot;75 g&quot;,   vol: 71,  tag: &quot;süßt + bindet&quot;, tc: &quot;#1a7a4a&quot; },
      { name: &quot;TK Blattspinat&quot;,             amt: &quot;50 g&quot;,   vol: 47,  tag: &quot;Vit. K + Folat&quot;, tc: &quot;#1a7a4a&quot; },
      { name: &quot;Walnüsse, ganz&quot;,             amt: &quot;15 g&quot;,   vol: 17,  tag: &quot;ALA Omega-3&quot;, tc: &quot;#d4860a&quot; },
      { name: &quot;Haferflocken, fein&quot;,         amt: &quot;25 g&quot;,   vol: 40 },
      { name: &quot;Leinsamen, gemahlen&quot;,        amt: &quot;10 g&quot;,   vol: 12,  tag: &quot;ALA&quot;, tc: &quot;#d4860a&quot; },
      { name: &quot;35 g Pulver + 5 g Kreatin&quot;, amt: &quot;fix&quot;,    vol: 50,  fixed: true },
    ],
    totalVol: 580,
    note: &quot;Farbe: tief violett-grün · Spinat geschmacklich unsichtbar hinter Johannisbeere&quot;,
  },
  {
    id: 2,
    name: &quot;SJ Beet Banana Hemp Oat&quot;,
    badge: &quot;NO-Boost · höchste KH&quot;,
    color: &quot;#8b1a4a&quot;,
    training: &quot;post Zone 2 · beste Wahl&quot;,
    desc: &quot;SJ + Rote Beete = maximale Anthocyan-Nitrat-Synergie · höchste KH für Glykogenwiederherstellung · Meersalz für Na-Ausgleich&quot;,
    macros: { kcal: 666, p: 47, f: 31, kh: 73, bal: 11 },
    ingredients: [
      { name: &quot;Vollmilch 3,8 %&quot;,           amt: &quot;230 ml&quot;, vol: 230 },
      { name: &quot;TK Schwarze Johannisbeeren&quot;,  amt: &quot;120 g&quot;,  vol: 114, tag: &quot;Anthocyane + Nitrat-Synergie&quot;, tc: &quot;#5a1a7a&quot; },
      { name: &quot;Rohe Rote Beete, gerieben&quot;, amt: &quot;65 g&quot;,   vol: 62,  tag: &quot;Nitrat roh ↑↑&quot;, tc: &quot;#c0392b&quot; },
      { name: &quot;TK Banane&quot;,                  amt: &quot;75 g&quot;,   vol: 71,  tag: &quot;schnelle KH&quot;, tc: &quot;#1a7a4a&quot; },
      { name: &quot;Hanfsamen, geschält&quot;,        amt: &quot;18 g&quot;,   vol: 20,  tag: &quot;Mg · vollst. AS&quot;, tc: &quot;#1a6b8a&quot; },
      { name: &quot;Haferflocken, fein&quot;,         amt: &quot;28 g&quot;,   vol: 45 },
      { name: &quot;Meersalz&quot;,                   amt: &quot;1 Prise&quot;,vol: 0,   tag: &quot;Na post-run&quot;, tc: &quot;#1a6b8a&quot; },
      { name: &quot;35 g Pulver + 5 g Kreatin&quot;, amt: &quot;fix&quot;,    vol: 50,  fixed: true },
    ],
    totalVol: 592,
    note: &quot;Rote Beete zuletzt einfüllen · stärkste post-Zone-2 Option · Beete + SJ = tief violett&quot;,
  },
  {
    id: 3,
    name: &quot;SJ Mango Spinach Chia Oat&quot;,
    badge: &quot;Vit. C ↑↑ · leichteste Variante&quot;,
    color: &quot;#7c3aed&quot;,
    training: &quot;leicht · Ruhetag möglich&quot;,
    desc: &quot;Kein Bananenanteil · Mango übernimmt Süße und Cremigkeit · Spinat + SJ = höchste Vit.-C-Kombination · niedrigstes Fett&quot;,
    macros: { kcal: 584, p: 42, f: 18, kh: 66, bal: 12 },
    ingredients: [
      { name: &quot;Vollmilch 3,8 %&quot;,           amt: &quot;214 ml&quot;, vol: 214 },
      { name: &quot;TK Schwarze Johannisbeeren&quot;,  amt: &quot;120 g&quot;,  vol: 114, tag: &quot;Vit. C ~215 mg&quot;, tc: &quot;#5a1a7a&quot; },
      { name: &quot;TK Mango&quot;,                   amt: &quot;130 g&quot;,  vol: 123, tag: &quot;Süße · Cremigkeit · Vit. C&quot;, tc: &quot;#e67e22&quot; },
      { name: &quot;TK Blattspinat&quot;,             amt: &quot;55 g&quot;,   vol: 52,  tag: &quot;Vit. K&quot;, tc: &quot;#1a7a4a&quot; },
      { name: &quot;Chiasamen&quot;,                  amt: &quot;12 g&quot;,   vol: 12,  tag: &quot;Omega-3&quot;, tc: &quot;#d4860a&quot; },
      { name: &quot;Haferflocken, fein&quot;,         amt: &quot;22 g&quot;,   vol: 35 },
      { name: &quot;35 g Pulver + 5 g Kreatin&quot;, amt: &quot;fix&quot;,    vol: 50,  fixed: true },
    ],
    totalVol: 600,
    note: &quot;Farbe: dunkelviolett · Mango muss in voller Menge dabei sein — sonst kommt die Herbheit der SJ durch&quot;,
  },
  {
    id: 4,
    name: &quot;SJ Cherry Broccoli Almond&quot;,
    badge: &quot;DOMS · Sulforaphan&quot;,
    color: &quot;#1a5a8a&quot;,
    training: &quot;Recovery · nach hartem Training&quot;,
    desc: &quot;SJ + Sauerkirsche = doppelte COX-Hemmung · Brokkoli direkt aus TK für Sulforaphan · Dattel süßt + bindet ohne Banane · Mandeln für Vit. E&quot;,
    macros: { kcal: 660, p: 45, f: 23, kh: 75, bal: 13 },
    ingredients: [
      { name: &quot;Vollmilch 3,8 %&quot;,           amt: &quot;210 ml&quot;, vol: 210 },
      { name: &quot;TK Schwarze Johannisbeeren&quot;,  amt: &quot;100 g&quot;,  vol: 95,  tag: &quot;Anthocyane · COX-Hemmer&quot;, tc: &quot;#5a1a7a&quot; },
      { name: &quot;TK Sauerkirschen&quot;,           amt: &quot;100 g&quot;,  vol: 95,  tag: &quot;DOMS↓ · Anthocyane&quot;, tc: &quot;#c0392b&quot; },
      { name: &quot;TK Brokkoli&quot;,               amt: &quot;70 g&quot;,   vol: 66,  tag: &quot;Sulforaphan · Nrf2↑&quot;, tc: &quot;#1a7a4a&quot; },
      { name: &quot;Mandeln, ganz&quot;,             amt: &quot;18 g&quot;,   vol: 20,  tag: &quot;Vit. E · Calcium&quot;, tc: &quot;#d4860a&quot; },
      { name: &quot;Medjool-Dattel, entkernt&quot;,  amt: &quot;1 Stk. (~18 g)&quot;, vol: 15, tag: &quot;Süße + Bindung&quot;, tc: &quot;#888&quot; },
      { name: &quot;Haferflocken, fein&quot;,         amt: &quot;25 g&quot;,   vol: 40 },
      { name: &quot;35 g Pulver + 5 g Kreatin&quot;, amt: &quot;fix&quot;,    vol: 50,  fixed: true },
    ],
    totalVol: 591,
    note: &quot;Brokkoli nie auftauen · stärkste anti-inflammatorische Kombination der fünf&quot;,
  },
  {
    id: 5,
    name: &quot;SJ Peach Carrot Hemp Oat&quot;,
    badge: &quot;Beta-Carotin · Vit. A · Mg&quot;,
    color: &quot;#d4860a&quot;,
    training: &quot;leicht-mittel&quot;,
    desc: &quot;Pfirsich übernimmt Süße und Cremigkeit · Karotte deckt Vit. A vollständig · Hanfsamen für Mg + AS · niedrigste kcal der fünf&quot;,
    macros: { kcal: 600, p: 45, f: 22, kh: 62, bal: 11 },
    ingredients: [
      { name: &quot;Vollmilch 3,8 %&quot;,           amt: &quot;212 ml&quot;, vol: 212 },
      { name: &quot;TK Schwarze Johannisbeeren&quot;,  amt: &quot;110 g&quot;,  vol: 104, tag: &quot;Anthocyane · Vit. C ~200 mg&quot;, tc: &quot;#5a1a7a&quot; },
      { name: &quot;TK Pfirsich&quot;,               amt: &quot;130 g&quot;,  vol: 123, tag: &quot;Süße · Kalium&quot;, tc: &quot;#e67e22&quot; },
      { name: &quot;TK Karotte, gegart&quot;,        amt: &quot;70 g&quot;,   vol: 66,  tag: &quot;Beta-Carotin · Vit. A &gt;100 %&quot;, tc: &quot;#d4860a&quot; },
      { name: &quot;Hanfsamen, geschält&quot;,        amt: &quot;15 g&quot;,   vol: 17,  tag: &quot;Mg · vollst. AS&quot;, tc: &quot;#1a6b8a&quot; },
      { name: &quot;Haferflocken, fein&quot;,         amt: &quot;25 g&quot;,   vol: 40 },
      { name: &quot;35 g Pulver + 5 g Kreatin&quot;, amt: &quot;fix&quot;,    vol: 50,  fixed: true },
    ],
    totalVol: 612,
    note: &quot;Farbe: dunkelviolett-orange · niedrigste kcal + KH der fünf · gut wenn Abendessen kalorienreicher geplant&quot;,
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
          POST ZONE 2 · TK SCHWARZE JOHANNISBEERE · MAX. 600 ML
        &lt;/p&gt;
        &lt;h1 style={{ fontSize:19, fontWeight:700, color:&quot;#1a1a1a&quot;, margin:&quot;0 0 3px&quot; }}&gt;5 Johannisbeer-Smoothies&lt;/h1&gt;
        &lt;p style={{ fontSize:12, color:&quot;#999&quot;, margin:0 }}&gt;35 g Vetain Neutral · 5 g Kreatin · Vollmilch · Nüsse/Saaten/Flocken&lt;/p&gt;
      &lt;/div&gt;

      &lt;div style={{ background:&quot;#fff8e8&quot;, borderRadius:8, padding:&quot;7px 11px&quot;, marginBottom:12, border:&quot;0.5px solid #d4860a30&quot;, fontSize:11, color:&quot;#7a4a00&quot; }}&gt;
        {note_sj}
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
              &lt;span style={{ fontSize:22, fontWeight:800, color:s.color+&quot;30&quot;, fontFamily:&quot;monospace&quot;, lineHeight:1, flexShrink:0 }}&gt;
                0{s.id}
              &lt;/span&gt;
              &lt;div style={{ flex:1 }}&gt;
                &lt;div style={{ display:&quot;flex&quot;, alignItems:&quot;center&quot;, gap:6, flexWrap:&quot;wrap&quot;, marginBottom:3 }}&gt;
                  &lt;span style={{ fontSize:10, fontWeight:700, padding:&quot;2px 8px&quot;, borderRadius:20, background:s.color+&quot;14&quot;, color:s.color, fontFamily:&quot;monospace&quot; }}&gt;
                    {s.badge}
                  &lt;/span&gt;
                  &lt;span style={{ fontSize:10, color:&quot;#ccc&quot;, fontFamily:&quot;monospace&quot; }}&gt;{s.training}&lt;/span&gt;
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
                  const baseColors=[&quot;#d4860a&quot;,&quot;#5a1a7a&quot;,&quot;#c0392b&quot;,&quot;#1a7a4a&quot;,&quot;#e67e22&quot;,&quot;#888&quot;,&quot;#1a6b8a&quot;,&quot;#7c3aed&quot;];
                  return &lt;div key={i} style={{ flexBasis:`${(ing.vol/s.totalVol)*100}%`, background:baseColors[i%baseColors.length], opacity:ing.fixed?0.3:0.55 }}/&gt;;
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
                    {!ing.fixed &amp;&amp; ing.vol&gt;0 &amp;&amp; &lt;div style={{ fontSize:9, color:&quot;#ddd&quot; }}&gt;≈ {ing.vol} ml&lt;/div&gt;}
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

      &lt;p style={{ fontSize:10, color:&quot;#ddd&quot;, textAlign:&quot;center&quot;, fontFamily:&quot;monospace&quot;, marginTop:4 }}&gt;TIPPE FÜR ZUTATEN&lt;/p&gt;
    &lt;/div&gt;
  );
}
</code></pre></details>
