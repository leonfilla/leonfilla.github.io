---
titel: heidelbeeren_three.jsx
status: aktiv
datum: '2026-04-24'
quelle:
  typ: claude
  url: https://claude.ai/chat/e243ac2d-4628-41b9-ae87-39b4cf14f878
  hinweis: Protein-Smoothies für Frühstück und Muskelaufbau
importiert: true
---

<details><summary>Ursprüngliche Datei</summary><pre><code>const smoothies = [
  {
    name: &quot;Heidelbeere Spinach Walnut Oat&quot;,
    badge: &quot;Vit. K · Folat · ALA&quot;,
    color: &quot;#1a7a4a&quot;,
    desc: &quot;Spinat deckt Vit. K und Folat · Walnüsse für ALA · Banane für Bindung · ausgewogenste Variante&quot;,
    macros: { kcal: 703, p: 48, f: 27, kh: 69, bal: 12 },
    ingredients: [
      { name: &quot;Vollmilch 3,8 %&quot;, amt: &quot;215 ml&quot;, vol: 215 },
      { name: &quot;TK Heidelbeeren&quot;, amt: &quot;130 g&quot;, vol: 123, tag: &quot;Anthocyane&quot;, tc: &quot;#7c3aed&quot; },
      { name: &quot;TK Banane&quot;, amt: &quot;80 g&quot;, vol: 76 },
      { name: &quot;TK Blattspinat&quot;, amt: &quot;55 g&quot;, vol: 52, tag: &quot;Vit. K + Folat&quot;, tc: &quot;#1a7a4a&quot; },
      { name: &quot;Walnüsse, ganz&quot;, amt: &quot;18 g&quot;, vol: 20, tag: &quot;ALA Omega-3&quot;, tc: &quot;#d4860a&quot; },
      { name: &quot;Haferflocken, fein&quot;, amt: &quot;28 g&quot;, vol: 44 },
      { name: &quot;35 g Pulver + 5 g Kreatin&quot;, amt: &quot;fix&quot;, vol: 50, fixed: true },
    ],
    totalVol: 580,
    note: &quot;Farbe: tiefviolett-grün · klassischste Kombination&quot;,
  },
  {
    name: &quot;Heidelbeere Beet Banana Hemp&quot;,
    badge: &quot;NO · Anthocyane · höchste KH&quot;,
    color: &quot;#c0392b&quot;,
    desc: &quot;Rote Beete roh + Heidelbeeren = stärkste Nitrat-Anthocyan-Kombination · höchste KH für post-run · Meersalz für Elektrolyte&quot;,
    macros: { kcal: 681, p: 48, f: 23, kh: 75, bal: 11 },
    ingredients: [
      { name: &quot;Vollmilch 3,8 %&quot;, amt: &quot;225 ml&quot;, vol: 225 },
      { name: &quot;TK Heidelbeeren&quot;, amt: &quot;130 g&quot;, vol: 123, tag: &quot;Anthocyane&quot;, tc: &quot;#7c3aed&quot; },
      { name: &quot;Rohe Rote Beete, gerieben&quot;, amt: &quot;65 g&quot;, vol: 62, tag: &quot;Nitrat roh ↑↑&quot;, tc: &quot;#c0392b&quot; },
      { name: &quot;TK Banane&quot;, amt: &quot;80 g&quot;, vol: 76 },
      { name: &quot;Hanfsamen, geschält&quot;, amt: &quot;18 g&quot;, vol: 20, tag: &quot;Mg · AS&quot;, tc: &quot;#1a6b8a&quot; },
      { name: &quot;Haferflocken, fein&quot;, amt: &quot;25 g&quot;, vol: 40 },
      { name: &quot;Meersalz&quot;, amt: &quot;1 Prise&quot;, vol: 0, tag: &quot;Elektrolyt&quot;, tc: &quot;#1a6b8a&quot; },
      { name: &quot;35 g Pulver + 5 g Kreatin&quot;, amt: &quot;fix&quot;, vol: 50, fixed: true },
    ],
    totalVol: 596,
    note: &quot;Rote Beete zuletzt einfüllen · beste post-Zone-2 Wahl&quot;,
  },
  {
    name: &quot;Heidelbeere Broccoli Peach Brazil&quot;,
    badge: &quot;Sulforaphan · Selen&quot;,
    color: &quot;#1a5a8a&quot;,
    desc: &quot;Brokkoli für Sulforaphan · Pfirsich als Bananenersatz · 2 Paranüsse decken 100 % Selen-Tagesbedarf — schließt strukturelle Lücke&quot;,
    macros: { kcal: 648, p: 48, f: 20, kh: 65, bal: 13 },
    ingredients: [
      { name: &quot;Vollmilch 3,8 %&quot;, amt: &quot;220 ml&quot;, vol: 220 },
      { name: &quot;TK Heidelbeeren&quot;, amt: &quot;120 g&quot;, vol: 114, tag: &quot;Anthocyane&quot;, tc: &quot;#7c3aed&quot; },
      { name: &quot;TK Brokkoli&quot;, amt: &quot;75 g&quot;, vol: 71, tag: &quot;Sulforaphan · Nrf2↑&quot;, tc: &quot;#1a7a4a&quot; },
      { name: &quot;TK Pfirsich&quot;, amt: &quot;110 g&quot;, vol: 104, tag: &quot;Kalium · cremig&quot;, tc: &quot;#e67e22&quot; },
      { name: &quot;Paranüsse, ganz&quot;, amt: &quot;2 Stk. (~14 g)&quot;, vol: 16, tag: &quot;Selen 100 % RDA&quot;, tc: &quot;#7a5a1a&quot; },
      { name: &quot;Haferflocken, fein&quot;, amt: &quot;25 g&quot;, vol: 40 },
      { name: &quot;35 g Pulver + 5 g Kreatin&quot;, amt: &quot;fix&quot;, vol: 50, fixed: true },
    ],
    totalVol: 615,
    note: &quot;Brokkoli nie auftauen · Paranüsse max. 2 Stk./Tag · schließt Selen-Lücke der gesamten Sammlung&quot;,
  },
];

import { useState } from &quot;react&quot;;

export default function App() {
  const [open, setOpen] = useState(null);
  return (
    &lt;div style={{ fontFamily:&quot;Georgia,serif&quot;, background:&quot;#f9f7f3&quot;, minHeight:&quot;100vh&quot;, padding:&quot;1rem 1rem 3rem&quot;, maxWidth:480, margin:&quot;0 auto&quot; }}&gt;
      &lt;div style={{ marginBottom:&quot;1rem&quot; }}&gt;
        &lt;p style={{ fontSize:10, color:&quot;#bbb&quot;, letterSpacing:&quot;.12em&quot;, margin:&quot;0 0 3px&quot;, fontFamily:&quot;monospace&quot; }}&gt;TK HEIDELBEEREN · MAX. 600 ML&lt;/p&gt;
        &lt;h1 style={{ fontSize:19, fontWeight:700, color:&quot;#1a1a1a&quot;, margin:&quot;0 0 3px&quot; }}&gt;3 Heidelbeeren-Smoothies&lt;/h1&gt;
        &lt;p style={{ fontSize:12, color:&quot;#999&quot;, margin:0 }}&gt;Vollmilch · 35 g Pulver · 5 g Kreatin · Gemüse in allen drei&lt;/p&gt;
      &lt;/div&gt;

      {smoothies.map((s, idx) =&gt; (
        &lt;div key={idx} style={{ background:&quot;#fff&quot;, borderRadius:12, border:`0.5px solid ${open===idx ? s.color+&quot;55&quot;:&quot;#e5e0d8&quot;}`, marginBottom:10, overflow:&quot;hidden&quot; }}&gt;
          &lt;button onClick={() =&gt; setOpen(open===idx ? null : idx)}
            style={{ width:&quot;100%&quot;, background:&quot;none&quot;, border:&quot;none&quot;, padding:&quot;12px 13px 10px&quot;, textAlign:&quot;left&quot;, cursor:&quot;pointer&quot; }}&gt;
            &lt;div style={{ display:&quot;flex&quot;, alignItems:&quot;flex-start&quot;, gap:8 }}&gt;
              &lt;div style={{ flex:1 }}&gt;
                &lt;div style={{ display:&quot;flex&quot;, alignItems:&quot;center&quot;, gap:6, flexWrap:&quot;wrap&quot;, marginBottom:3 }}&gt;
                  &lt;span style={{ fontSize:22, fontWeight:800, color:s.color+&quot;25&quot;, fontFamily:&quot;monospace&quot;, lineHeight:1 }}&gt;0{idx+1}&lt;/span&gt;
                  &lt;span style={{ fontSize:10, fontWeight:700, padding:&quot;2px 8px&quot;, borderRadius:20, background:s.color+&quot;14&quot;, color:s.color, fontFamily:&quot;monospace&quot; }}&gt;{s.badge}&lt;/span&gt;
                &lt;/div&gt;
                &lt;div style={{ fontSize:14, fontWeight:700, color:&quot;#1a1a1a&quot; }}&gt;{s.name}&lt;/div&gt;
                &lt;p style={{ fontSize:11, color:&quot;#888&quot;, margin:&quot;3px 0 0&quot;, lineHeight:1.5 }}&gt;{s.desc}&lt;/p&gt;
              &lt;/div&gt;
              &lt;span style={{ color:&quot;#ccc&quot;, fontSize:13, flexShrink:0, marginTop:4 }}&gt;{open===idx ? &quot;▲&quot;:&quot;▼&quot;}&lt;/span&gt;
            &lt;/div&gt;

            &lt;div style={{ display:&quot;grid&quot;, gridTemplateColumns:&quot;repeat(5,1fr)&quot;, gap:5, marginTop:9 }}&gt;
              {[{l:&quot;kcal&quot;,v:s.macros.kcal,c:&quot;#1a1a1a&quot;,u:&quot;&quot;},{l:&quot;Protein&quot;,v:s.macros.p,c:&quot;#7c3aed&quot;,u:&quot;g&quot;},{l:&quot;Fett&quot;,v:s.macros.f,c:&quot;#d4860a&quot;,u:&quot;g&quot;},{l:&quot;KH&quot;,v:s.macros.kh,c:s.color,u:&quot;g&quot;},{l:&quot;Ballaststoffe&quot;,v:s.macros.bal,c:&quot;#1a6b8a&quot;,u:&quot;g&quot;}].map((m,i) =&gt; (
                &lt;div key={i} style={{ background:&quot;#f9f7f3&quot;, borderRadius:7, padding:&quot;5px 3px&quot;, textAlign:&quot;center&quot;, border: i===3 ? `0.5px solid ${s.color}45`:&quot;0.5px solid transparent&quot; }}&gt;
                  &lt;div style={{ fontSize:9, color:&quot;#ccc&quot;, marginBottom:1 }}&gt;{m.l}&lt;/div&gt;
                  &lt;div style={{ fontSize:12, fontWeight:700, color:m.c }}&gt;{m.v}{m.u}&lt;/div&gt;
                &lt;/div&gt;
              ))}
            &lt;/div&gt;
            &lt;div style={{ marginTop:6, fontSize:11, color:s.color, fontFamily:&quot;monospace&quot; }}&gt;≈ {s.totalVol} ml ✓&lt;/div&gt;
          &lt;/button&gt;

          {open===idx &amp;&amp; (
            &lt;div style={{ borderTop:&quot;0.5px solid #f0ece4&quot;, padding:&quot;8px 13px 12px&quot; }}&gt;
              &lt;p style={{ fontSize:9, fontWeight:700, color:&quot;#ccc&quot;, letterSpacing:&quot;.12em&quot;, margin:&quot;0 0 6px&quot;, fontFamily:&quot;monospace&quot; }}&gt;ZUTATEN&lt;/p&gt;

              {/* Volume bar */}
              &lt;div style={{ display:&quot;flex&quot;, gap:1, height:5, borderRadius:3, overflow:&quot;hidden&quot;, marginBottom:8 }}&gt;
                {s.ingredients.map((ing,i) =&gt; {
                  const colors=[&quot;#d4860a&quot;,&quot;#7c3aed&quot;,&quot;#c0392b&quot;,&quot;#1a7a4a&quot;,&quot;#7a5a1a&quot;,&quot;#888&quot;,&quot;#7c3aed&quot;];
                  const pct=(ing.vol/s.totalVol)*100;
                  return &lt;div key={i} style={{ flexBasis:`${pct}%`, background:colors[i], opacity:ing.fixed?0.3:0.55 }}/&gt;;
                })}
              &lt;/div&gt;

              {s.ingredients.map((ing,i) =&gt; (
                &lt;div key={i} style={{ display:&quot;flex&quot;, justifyContent:&quot;space-between&quot;, alignItems:&quot;flex-start&quot;, padding:&quot;4px 0&quot;, borderBottom: i&lt;s.ingredients.length-1?&quot;0.5px solid #f5f2ee&quot;:&quot;none&quot;, background:ing.fixed?&quot;#f5f3ff&quot;:&quot;transparent&quot;, borderRadius:ing.fixed?4:0, paddingLeft:ing.fixed?4:0 }}&gt;
                  &lt;div&gt;
                    &lt;span style={{ fontSize:13, color:ing.fixed?&quot;#7c3aed&quot;:&quot;#333&quot; }}&gt;{ing.name}&lt;/span&gt;
                    {ing.tag &amp;&amp; &lt;span style={{ fontSize:10, color:ing.tc||s.color, marginLeft:5, fontFamily:&quot;monospace&quot; }}&gt;· {ing.tag}&lt;/span&gt;}
                  &lt;/div&gt;
                  &lt;div style={{ textAlign:&quot;right&quot;, marginLeft:8, flexShrink:0 }}&gt;
                    &lt;div style={{ fontSize:11, fontWeight:700, color:&quot;#bbb&quot; }}&gt;{ing.amt}&lt;/div&gt;
                    {!ing.fixed &amp;&amp; ing.vol &gt; 0 &amp;&amp; &lt;div style={{ fontSize:9, color:&quot;#ddd&quot; }}&gt;≈ {ing.vol} ml&lt;/div&gt;}
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
