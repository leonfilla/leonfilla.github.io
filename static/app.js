// Leons Rezepte – kleine Helfer ohne Abhängigkeiten.
(() => {
  "use strict";
  const $ = (s, el = document) => el.querySelector(s);
  const $$ = (s, el = document) => [...el.querySelectorAll(s)];
  const zahl = (x) => {
    const r = Math.abs(x) >= 100 ? Math.round(x) : Math.round(x * 10) / 10;
    return String(r).replace(".", ",");
  };

  // ---- Suche (Startseite): Freitext + Status + Bereich
  const feld = $("#suchfeld");
  const indexEl = $("#suchindex");
  const STATUS_NAME = { aktiv: "Aktiv", unfertig: "Unfertig", archiv: "Archiv", idee: "Idee" };
  if (feld && indexEl) {
    const index = JSON.parse(indexEl.textContent);
    const liste = $("#treffer"), zahlEl = $("#treffer-zahl"), bereichSel = $("#such-bereich");
    const chips = $$("[data-such-st]");
    const aktiveStati = () => chips.filter((c) => c.getAttribute("aria-pressed") === "true").map((c) => c.dataset.suchSt);
    const zeige = () => {
      const woerter = feld.value.toLowerCase().trim().split(/\s+/).filter(Boolean);
      const stati = aktiveStati(), bereich = bereichSel.value;
      const gefiltert = stati.length < chips.length || bereich;
      if (!woerter.length && !gefiltert) { liste.hidden = true; zahlEl.hidden = true; liste.innerHTML = ""; return; }
      const rang = (e) => ({ aktiv: 0, unfertig: 1, archiv: 2, idee: 3 }[e.v ? "archiv" : e.s] ?? 4);
      const treffer = index
        .filter((e) => stati.includes(e.v ? "archiv" : e.s) && (!bereich || e.bid === bereich) && woerter.every((w) => e.q.includes(w)))
        .sort((a, b) => rang(a) - rang(b) || a.t.localeCompare(b.t, "de"));
      zahlEl.textContent = `${treffer.length} Treffer`;
      zahlEl.hidden = false;
      liste.innerHTML = treffer.length
        ? treffer.slice(0, 200).map((e) => {
            const st = e.v ? "archiv" : e.s;
            const marke = e.v ? "Ältere Version" : (st !== "aktiv" ? STATUS_NAME[st] : "");
            return `<li class="st-${st}"><a href="${e.u}"><span>${esc(e.t)}</span><small>${esc(e.b)}${marke ? ` <em class="marke-status ${st}">${marke}</em>` : ""}</small></a></li>`;
          }).join("")
        : '<li class="leise" style="padding:9px 10px">Nichts gefunden.</li>';
      liste.hidden = false;
    };
    feld.addEventListener("input", zeige);
    bereichSel.addEventListener("change", zeige);
    chips.forEach((c) => c.addEventListener("click", () => {
      c.setAttribute("aria-pressed", c.getAttribute("aria-pressed") === "true" ? "false" : "true"); zeige();
    }));
    feld.addEventListener("keydown", (e) => {
      if (e.key === "Enter") { const a = $("a", liste); if (a) location.href = a.href; }
      if (e.key === "Escape") { feld.value = ""; zeige(); }
    });
  }

  // ---- Filterleiste auf Bereichsseiten
  $$("[data-filterbar]").forEach((bar) => {
    const chips = $$("[data-st]", bar), text = $("[data-filter-text]", bar), leer = $(".filter-leer", bar);
    const nurNeu = $("[data-nur-neu]", bar);
    const items = $$("[data-filter-item]");
    const anwenden = () => {
      const stati = chips.filter((c) => c.getAttribute("aria-pressed") === "true").map((c) => c.dataset.st);
      const woerter = text.value.toLowerCase().trim().split(/\s+/).filter(Boolean);
      let sichtbar = 0;
      items.forEach((el) => {
        const st = (el.dataset.status || "").split(" ");
        const neuOk = !nurNeu || nurNeu.getAttribute("aria-pressed") !== "true" || el.hasAttribute("data-neu");
        const ok = neuOk && st.some((s) => stati.includes(s)) && woerter.every((w) => (el.dataset.q || "").includes(w));
        el.hidden = !ok; if (ok) sichtbar++;
      });
      $$("[data-filter-gruppe]").forEach((g) => { g.hidden = !$$("[data-filter-item]", g).some((el) => !el.hidden); });
      leer.hidden = sichtbar > 0;
    };
    chips.forEach((c) => c.addEventListener("click", () => {
      c.setAttribute("aria-pressed", c.getAttribute("aria-pressed") === "true" ? "false" : "true"); anwenden();
    }));
    if (nurNeu) nurNeu.addEventListener("click", () => {
      nurNeu.setAttribute("aria-pressed", nurNeu.getAttribute("aria-pressed") === "true" ? "false" : "true"); anwenden();
    });
    text.addEventListener("input", anwenden);
  });
  function esc(s) { return String(s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" })[c]); }

  // ---- Kopieren (xBloom-App)
  $$("[data-kopie]").forEach((knopf) => {
    knopf.addEventListener("click", async () => {
      const text = knopf.dataset.kopie;
      try {
        await navigator.clipboard.writeText(text);
      } catch {
        const ta = Object.assign(document.createElement("textarea"), { value: text });
        ta.style.position = "fixed"; ta.style.opacity = "0";
        document.body.append(ta); ta.select(); document.execCommand("copy"); ta.remove();
      }
      knopf.dataset.ok = "";
      setTimeout(() => delete knopf.dataset.ok, 1800);
    });
  });

  // ---- Skalierung
  $$(".skalierer input").forEach((input) => {
    const basis = parseFloat(input.dataset.basis) || 1;
    const update = () => {
      const f = (parseFloat(String(input.value).replace(",", ".")) || basis) / basis;
      $$("[data-menge]").forEach((el) => { el.textContent = zahl(parseFloat(el.dataset.menge) * f); });
    };
    input.addEventListener("input", update);
  });

  // ---- Zutaten abhaken
  $$(".abhaken").forEach((tr) => tr.addEventListener("click", () => tr.classList.toggle("erledigt")));

  // ---- Kochmodus: Display wach halten, Schritt für Schritt
  let wakeLock = null;
  const wachHalten = async () => {
    try { if ("wakeLock" in navigator) wakeLock = await navigator.wakeLock.request("screen"); } catch { /* egal */ }
  };
  document.addEventListener("visibilitychange", () => {
    if (document.visibilityState === "visible" && document.body.classList.contains("kochmodus")) wachHalten();
  });
  const schritte = $$(".schritt");
  const setzeAktiv = (i) => {
    schritte.forEach((s, j) => {
      s.classList.toggle("aktiv", j === i);
      s.classList.toggle("erledigt", j < i);
    });
    if (schritte[i]) schritte[i].scrollIntoView({ behavior: "smooth", block: "center" });
  };
  $$("[data-kochmodus]").forEach((knopf) => {
    knopf.addEventListener("click", async () => {
      const an = document.body.classList.toggle("kochmodus");
      knopf.textContent = an ? "Kochmodus beenden" : "Kochmodus";
      if (an) { await wachHalten(); setzeAktiv(0); }
      else { wakeLock?.release(); wakeLock = null; schritte.forEach((s) => s.classList.remove("aktiv", "erledigt")); }
    });
  });
  schritte.forEach((s, i) => s.addEventListener("click", (e) => {
    if (!document.body.classList.contains("kochmodus") || e.target.closest(".timer")) return;
    setzeAktiv(s.classList.contains("aktiv") ? i + 1 : i);
  }));

  // ---- Timer
  const fmtZeit = (s) => `${Math.floor(s / 60)}:${String(s % 60).padStart(2, "0")}`;
  let audio = null;
  const piep = () => {
    try {
      audio = audio || new (window.AudioContext || window.webkitAudioContext)();
      [0, 0.35, 0.7].forEach((t) => {
        const o = audio.createOscillator(), g = audio.createGain();
        o.frequency.value = 880; o.connect(g); g.connect(audio.destination);
        g.gain.setValueAtTime(0.25, audio.currentTime + t);
        g.gain.exponentialRampToValueAtTime(0.001, audio.currentTime + t + 0.3);
        o.start(audio.currentTime + t); o.stop(audio.currentTime + t + 0.3);
      });
    } catch { /* kein Audio */ }
    navigator.vibrate?.([300, 150, 300]);
  };
  $$(".timer").forEach((t) => {
    const dauer = parseInt(t.dataset.sekunden, 10);
    let ende = null, iv = null;
    const stop = () => { clearInterval(iv); iv = null; ende = null; t.classList.remove("laeuft"); };
    t.addEventListener("click", () => {
      if (t.classList.contains("fertig")) { t.classList.remove("fertig"); t.textContent = `▶ ${fmtZeit(dauer)}`; return; }
      if (iv) { stop(); t.textContent = `▶ ${fmtZeit(dauer)}`; return; }
      audio = audio || new (window.AudioContext || window.webkitAudioContext)();  // im Klick freischalten
      ende = Date.now() + dauer * 1000;
      t.classList.add("laeuft");
      const tick = () => {
        const rest = Math.max(0, Math.round((ende - Date.now()) / 1000));
        t.textContent = `■ ${fmtZeit(rest)}`;
        if (rest === 0) { stop(); t.classList.add("fertig"); t.textContent = `✓ ${t.dataset.titel} fertig`; piep(); }
      };
      tick(); iv = setInterval(tick, 500);
    });
  });

  // ---- Nach oben
  const hoch = $(".nach-oben");
  if (hoch) {
    addEventListener("scroll", () => { hoch.hidden = scrollY < 600; }, { passive: true });
    hoch.addEventListener("click", () => scrollTo({ top: 0, behavior: "smooth" }));
  }
})();
