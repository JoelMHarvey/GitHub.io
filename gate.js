// Site password gate. One password unlocks every gated page on the site;
// unlock persists in this browser (localStorage) until cleared.
//
// To change the password: run
//   printf 'jmh:NEWPASSWORD' | sha256sum
// and paste the hash below. Honest limitation of a static site: this is a
// front-door deterrent, not encryption — the page files themselves are
// still in the public repo. Anything genuinely sensitive belongs behind a
// real server (research hub / ops), not here.
(function () {
  var HASH = "ed05301a98dd6a6b78a2fb3b599ced7a33312336c2cf24fdc6195df1cffdb04c";
  var KEY = "jmh_gate";
  try {
    if (localStorage.getItem(KEY) === HASH) return;
  } catch (e) { /* storage blocked: gate still works, just asks every visit */ }

  // Hide the page immediately (script runs from <head>, before body renders).
  var style = document.createElement("style");
  style.textContent = "body{display:none!important}";
  document.documentElement.appendChild(style);

  function unlockUI() {
    var wrap = document.createElement("div");
    wrap.id = "jmh-gate";
    wrap.innerHTML =
      '<div style="position:fixed;inset:0;background:#22303c;display:flex;align-items:center;' +
      'justify-content:center;z-index:99999;font-family:-apple-system,BlinkMacSystemFont,' +
      "'Segoe UI',sans-serif\">" +
      '<form id="jmh-gate-form" style="text-align:center;max-width:280px;width:90%">' +
      '<div style="font-size:2rem;margin-bottom:0.4rem">🔒</div>' +
      '<div style="color:#8fa3b3;margin-bottom:1rem;font-size:0.95rem">This site is private.</div>' +
      '<input id="jmh-gate-pw" type="password" autocomplete="current-password" placeholder="Password" ' +
      'style="width:100%;padding:0.65rem 0.9rem;border-radius:10px;border:1px solid #3d5570;' +
      'background:#2c3d4d;color:#e8eef3;font-size:1rem;outline:none;text-align:center">' +
      '<div id="jmh-gate-err" style="color:#d8a0a0;font-size:0.85rem;height:1.2rem;margin-top:0.5rem"></div>' +
      "</form></div>";
    document.documentElement.appendChild(wrap);
    var input = wrap.querySelector("#jmh-gate-pw");
    input.focus();
    wrap.querySelector("#jmh-gate-form").addEventListener("submit", function (e) {
      e.preventDefault();
      var pw = input.value;
      crypto.subtle
        .digest("SHA-256", new TextEncoder().encode("jmh:" + pw))
        .then(function (buf) {
          var hex = Array.from(new Uint8Array(buf))
            .map(function (b) { return b.toString(16).padStart(2, "0"); })
            .join("");
          if (hex === HASH) {
            try { localStorage.setItem(KEY, HASH); } catch (e2) {}
            wrap.remove();
            style.remove();
          } else {
            wrap.querySelector("#jmh-gate-err").textContent = "Not it — try again.";
            input.value = "";
            input.focus();
          }
        });
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", unlockUI);
  } else {
    unlockUI();
  }
})();
