---
titel: restday_three_new.jsx
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
    name: &quot;Strawberry Zucchini Cacao&quot;,
    badge: &quot;Kakao · Vit. C · Ballaststoffe&quot;,
    bc: &quot;#8b2a2a&quot;,
    desc: &quot;Zucchini verdoppelt Volumen ohne Kalorien oder Geschmack. Kakao-Flavanole + Erdbeeren-Vit. C synergistisch. Dessertartig ohne Banane.&quot;,
    macros: { kcal: 524, p: 45, f: 20, kh: 47, bal: 11 },
    fills: [&quot;Vit. C ~75 %&quot;, &quot;Mg ~70 %&quot;, &quot;Flavanole ↑&quot;],
    ings: [
      { n: &quot;Vollmilch 3,8 %&quot;,           a: &quot;228 ml&quot;, v: 228, t: null },
      { n: &quot;TK Erdbeeren&quot;,               a: &quot;150 g&quot;,  v: 142, t: &quot;Vit. C · Anthocyane&quot; },
      { n: &quot;TK Zucchini, roh gewürfelt&quot;, a: &quot;120 g&quot;,  v: 114, t: &quot;Volumen · neutral&quot; },
      { n: &quot;Rohkakao-Pulver, ungesüßt&quot;,  a: &quot;12 g&quot;,   v: 14,  t: &quot;Flavanole · Mg&quot; },
      { n: &quot;Haferflocken, fein&quot;,          a: &quot;25 g&quot;,   v: 40,  t: null },
      { n: &quot;Chiasamen&quot;,                   a: &quot;12 g&quot;,   v: 12,  t: &quot;ALA&quot; },
      { n: &quot;35 g Pulver + 5 g Kreatin&quot;,  a: &quot;fix&quot;,    v: 50,  t: null, fix: true },
    ],
    vol: 600,
    note: &quot;Farbe: dunkelrot-braun · Erdbeere + Kakao dominieren · Zucchini komplett unsichtbar · süßester der drei&quot;,
    color: &quot;#8b2a2a&quot;,
  },
  {
    id: 2,
    name: &quot;Blackberry Carrot Mango&quot;,
    badge: &quot;Beta-Carotin · Anthocyane&quot;,
    bc: &quot;#7c1a7a&quot;,
    desc: &quot;Vit. A &gt;100 % RDA durch Karotte + Mango. Brombeeren für Vit. K und Anthocyane. Niedrigstes Fett. Erdig-fruchtig.&quot;,
    macros: { kcal: 540, p: 42, f: 16, kh: 55, bal: 10 },
    fills: [&quot;Vit. A &gt;100 %&quot;, &quot;Anthocyane ↑↑&quot;, &quot;niedrigstes Fett&quot;],
    ings: [
      { n: &quot;Vollmilch 3,8 %&quot;,         a: &quot;212 ml&quot;, v: 212, t: null },
      { n: &quot;TK Brombeeren&quot;,            a: &quot;120 g&quot;,  v: 114, t: &quot;Anthocyane · Vit. K&quot; },
      { n: &quot;TK Karotte, gegart&quot;,       a: &quot;90 g&quot;,   v: 85,  t: &quot;Beta-Carotin · Vit. A&quot; },
      { n: &quot;TK Mango&quot;,                 a: &quot;100 g&quot;,  v: 95,  t: &quot;Vit. C · KH&quot; },
      { n: &quot;Haferflocken, fein&quot;,        a: &quot;20 g&quot;,   v: 32,  t: null },
      { n: &quot;Leinsamen, gemahlen&quot;,       a: &quot;10 g&quot;,   v: 12,  t: &quot;ALA&quot; },
      { n: &quot;35 g Pulver + 5 g Kreatin&quot;,a: &quot;fix&quot;,    v: 50,  t: null, fix: true },
    ],
    vol: 600,
    note: &quot;Farbe: tiefviolett-orange · erdig-fruchtig · Vit. A Tagesziel allein in diesem Rezept&quot;,
    color: &quot;#7c1a7a&quot;,
  },
  {
    id: 3,
    name: &quot;Pineapple Cucumber Spinach Date&quot;,
    badge: &quot;Bromelain · Vit. K · Hydration&quot;,
    bc: &quot;#1a5a8a&quot;,
    desc: &quot;Gurke zu 96 % Wasser — maximale Hydration. Ananas Bromelain anti-inflammatorisch. Dattel süßt ohne Banane. Frischester Smoothie der gesamten Sammlung.&quot;,
    macros: { kcal: 531, p: 42, f: 16, kh: 58, bal: 9 },
    fills: [&quot;Bromelain&quot;, &quot;Vit. K ~200 %&quot;, &quot;Hydration ↑↑&quot;],
    ings: [
      { n: &quot;Vollmilch 3,8 %&quot;,              a: &quot;205 ml&quot;,       v: 205, t: null },
      { n: &quot;TK Ananas&quot;,                     a: &quot;120 g&quot;,        v: 114, t: &quot;Bromelain · Vit. C&quot; },
      { n: &quot;Salatgurke, frisch&quot;,            a: &quot;110 g&quot;,        v: 105, t: &quot;Hydration&quot; },
      { n: &quot;TK Blattspinat&quot;,               a: &quot;50 g&quot;,         v: 47,  t: &quot;Vit. K · Folat&quot; },
      { n: &quot;Medjool-Dattel, entkernt&quot;,      a: &quot;1 Stk. (~18 g)&quot;,v: 12, t: &quot;Süße + KH&quot; },
      { n: &quot;Haferflocken, fein&quot;,             a: &quot;20 g&quot;,         v: 32,  t: null },
      { n: &quot;Chiasamen&quot;,                      a: &quot;10 g&quot;,         v: 10,  t: &quot;Omega-3&quot; },
      { n: &quot;Bio-Limette, ½ mit Schale&quot;,     a: &quot;½ Stk.&quot;,       v: 25,  t: &quot;Flavonoide&quot; },
      { n: &quot;35 g Pulver + 5 g Kreatin&quot;,     a: &quot;fix&quot;,          v: 50,  t: null, fix: true },
    ],
    vol: 600,
    note: &quot;Farbe: hellgelb-grün · Gurke frisch (TK = matschig) · Limette mit Schale da Bio&quot;,
    color: &quot;#1a5a8a&quot;,
  },
];

const mc = [
  { k: &quot;kcal&quot;, l: &quot;kcal&quot;,         c: &quot;#1a1a1a&quot;, u: &quot;&quot; },
  { k: &quot;p&quot;,    l: &quot;Protein&quot;,      c: &quot;#7c3aed&quot;, u: &quot;g&quot; },
  { k: &quot;f&quot;,    l: &quot;Fett&quot;,         c: &quot;#d4860a&quot;, u: &quot;g&quot; },
  { k: &quot;kh&quot;,   l: &quot;KH&quot;,           c: &quot;#1a7a4a&quot;, u: &quot;g&quot; },
  { k: &quot;bal&quot;,  l: &quot;Ballaststoffe&quot;,c: &quot;#1a6b8a&quot;, u: &quot;g&quot; },
];

const barColors = [&quot;#d4860a&quot;,&quot;#c0392b&quot;,&quot;#1a7a4a&quot;,&quot;#f39c12&quot;,&quot;#888&quot;,&quot;#1a6b8a&quot;,&quot;#8b4a1a&quot;,&quot;#e67e22&quot;,&quot;#7c3aed&quot;];

export default function App() {
  const [open, setOpen] = useState(1);
  return (
    &lt;div style={{ fontFamily:&quot;Georgia,serif&quot;, background:&quot;#f9f7f3&quot;, minHeight:&quot;100vh&quot;, padding:&quot;1rem 1rem 3rem&quot;, maxWidth:480, margin:&quot;0 auto&quot; }}&gt;

      &lt;div style={{ marginBottom:&quot;1rem&quot; }}&gt;
        &lt;p style={{ fontSize:10, color:&quot;#bbb&quot;, letterSpacing:&quot;.12em&quot;, margin:&quot;0 0 3px&quot;, fontFamily:&quot;monospace&quot; }}&gt;RUHETAG · 3 NEUE VARIANTEN · 600 ML&lt;/p&gt;
        &lt;h1 style={{ fontSize:19, fontWeight:700, color:&quot;#1a1a1a&quot;, margin:&quot;0 0 3px&quot; }}&gt;Komplett andere Smoothies&lt;/h1&gt;
        &lt;p style={{ fontSize:12, color:&quot;#999&quot;, margin:0 }}&gt;Vollmilch · 35 g Pulver · 5 g Kreatin · kein Nussanteil&lt;/p&gt;
      &lt;/div&gt;

      {smoothies.map(s =&gt; (
        &lt;div key={s.id} style={{
          background:&quot;#fff&quot;, borderRadius:12, marginBottom:10, overflow:&quot;hidden&quot;,
          border:`0.5px solid ${open===s.id ? s.color+&quot;55&quot; : &quot;#e5e0d8&quot;}`,
          transition:&quot;border-color .15s&quot;,
        }}&gt;
          &lt;button onClick={() =&gt; setOpen(open===s.id ? null : s.id)}
            style={{ width:&quot;100%&quot;, background:&quot;none&quot;, border:&quot;none&quot;, padding:&quot;12px 13px 10px&quot;, textAlign:&quot;left&quot;, cursor:&quot;pointer&quot; }}&gt;

            &lt;div style={{ display:&quot;flex&quot;, alignItems:&quot;flex-start&quot;, gap:8 }}&gt;
              &lt;div style={{ flex:1 }}&gt;
                &lt;div style={{ display:&quot;flex&quot;, alignItems:&quot;center&quot;, gap:6, flexWrap:&quot;wrap&quot;, marginBottom:3 }}&gt;
                  &lt;span style={{ fontSize:10, fontWeight:700, padding:&quot;2px 8px&quot;, borderRadius:20,
                    background:s.color+&quot;15&quot;, color:s.color, fontFamily:&quot;monospace&quot; }}&gt;{s.badge}&lt;/span&gt;
                &lt;/div&gt;
                &lt;div style={{ fontSize:14, fontWeight:700, color:&quot;#1a1a1a&quot; }}&gt;{s.name}&lt;/div&gt;
                &lt;p style={{ fontSize:11, color:&quot;#888&quot;, margin:&quot;3px 0 0&quot;, lineHeight:1.5 }}&gt;{s.desc}&lt;/p&gt;
              &lt;/div&gt;
              &lt;span style={{ color:&quot;#ccc&quot;, fontSize:13, flexShrink:0, marginTop:2 }}&gt;{open===s.id?&quot;▲&quot;:&quot;▼&quot;}&lt;/span&gt;
            &lt;/div&gt;

            &lt;div style={{ display:&quot;grid&quot;, gridTemplateColumns:&quot;repeat(5,1fr)&quot;, gap:5, marginTop:9 }}&gt;
              {mc.map(m =&gt; (
                &lt;div key={m.k} style={{ background:&quot;#f9f7f3&quot;, borderRadius:7, padding:&quot;5px 3px&quot;, textAlign:&quot;center&quot;,
                  border: m.k===&quot;kh&quot; ? `0.5px solid ${s.color}45` : &quot;0.5px solid transparent&quot; }}&gt;
                  &lt;div style={{ fontSize:9, color:&quot;#ccc&quot;, marginBottom:1 }}&gt;{m.l}&lt;/div&gt;
                  &lt;div style={{ fontSize:12, fontWeight:700, color: m.k===&quot;kh&quot; ? s.color : m.c }}&gt;
                    {s.macros[m.k]}{m.u}
                  &lt;/div&gt;
                &lt;/div&gt;
              ))}
            &lt;/div&gt;

            &lt;div style={{ display:&quot;flex&quot;, gap:5, flexWrap:&quot;wrap&quot;, marginTop:7 }}&gt;
              {s.fills.map((f,i) =&gt; (
                &lt;span key={i} style={{ fontSize:10, padding:&quot;2px 7px&quot;, borderRadius:20,
                  background:s.color+&quot;10&quot;, color:s.color, border:`0.5px solid ${s.color}25` }}&gt;{f}&lt;/span&gt;
              ))}
            &lt;/div&gt;
          &lt;/button&gt;

          {open===s.id &amp;&amp; (
            &lt;div style={{ borderTop:&quot;0.5px solid #f0ece4&quot;, padding:&quot;8px 13px 12px&quot; }}&gt;
              &lt;div style={{ display:&quot;flex&quot;, justifyContent:&quot;space-between&quot;, alignItems:&quot;center&quot;, marginBottom:6 }}&gt;
                &lt;span style={{ fontSize:9, fontWeight:700, color:&quot;#ccc&quot;, letterSpacing:&quot;.12em&quot;, fontFamily:&quot;monospace&quot; }}&gt;ZUTATEN&lt;/span&gt;
                &lt;span style={{ fontSize:10, color:s.color, fontWeight:600 }}&gt;≈ {s.vol} ml&lt;/span&gt;
              &lt;/div&gt;
              &lt;div style={{ display:&quot;flex&quot;, gap:1, height:5, borderRadius:3, overflow:&quot;hidden&quot;, marginBottom:8 }}&gt;
                {s.ings.map((ing,i) =&gt; (
                  &lt;div key={i} style={{ flexBasis:`${(ing.v/s.vol)*100}%`,
                    background:barColors[i], opacity:ing.fix?0.3:0.55 }} /&gt;
                ))}
              &lt;/div&gt;
              {s.ings.map((ing,i) =&gt; (
                &lt;div key={i} style={{
                  display:&quot;flex&quot;, justifyContent:&quot;space-between&quot;, alignItems:&quot;flex-start&quot;,
                  padding:&quot;4px 0&quot;,
                  borderBottom: i&lt;s.ings.length-1 ? &quot;0.5px solid #f5f2ee&quot; : &quot;none&quot;,
                  background: ing.fix ? &quot;#f5f3ff&quot; : &quot;transparent&quot;,
                  borderRadius: ing.fix ? 4 : 0,
                  paddingLeft: ing.fix ? 4 : 0,
                }}&gt;
                  &lt;div&gt;
                    &lt;span style={{ fontSize:13, color: ing.fix?&quot;#7c3aed&quot;:&quot;#333&quot; }}&gt;{ing.n}&lt;/span&gt;
                    {ing.t &amp;&amp; &lt;span style={{ fontSize:10, color:s.color, marginLeft:5, fontFamily:&quot;monospace&quot; }}&gt;· {ing.t}&lt;/span&gt;}
                  &lt;/div&gt;
                  &lt;div style={{ textAlign:&quot;right&quot;, marginLeft:8, flexShrink:0 }}&gt;
                    &lt;div style={{ fontSize:11, fontWeight:700, color:&quot;#bbb&quot; }}&gt;{ing.a}&lt;/div&gt;
                    {!ing.fix &amp;&amp; &lt;div style={{ fontSize:9, color:&quot;#ddd&quot; }}&gt;≈ {ing.v} ml&lt;/div&gt;}
                  &lt;/div&gt;
                &lt;/div&gt;
              ))}
              &lt;div style={{ marginTop:8, fontSize:11, color:&quot;#999&quot;, fontStyle:&quot;italic&quot;,
                borderLeft:`3px solid ${s.color}35`, paddingLeft:8, lineHeight:1.5 }}&gt;
                {s.note}
              &lt;/div&gt;
            &lt;/div&gt;
          )}
        &lt;/div&gt;
      ))}

      &lt;div style={{ background:&quot;#fff&quot;, borderRadius:10, border:&quot;0.5px solid #e5e0d8&quot;, padding:&quot;9px 12px&quot;, marginTop:2 }}&gt;
        &lt;p style={{ fontSize:9, fontFamily:&quot;monospace&quot;, fontWeight:700, color:&quot;#bbb&quot;, letterSpacing:&quot;.1em&quot;, margin:&quot;0 0 4px&quot; }}&gt;UNTERSCHIEDE ZU DEN VORHERIGEN 3&lt;/p&gt;
        &lt;p style={{ fontSize:12, color:&quot;#888&quot;, margin:0, lineHeight:1.5 }}&gt;
          Kein Blaubeeren · kein Rote Beete · keine Erbsen. Stattdessen: Zucchini + Kakao · Brombeere + Karotte · Gurke + Ananas. Drei komplett andere Geschmackswelten und Farbprofile.
        &lt;/p&gt;
      &lt;/div&gt;
    &lt;/div&gt;
  );
}
</code></pre></details>
