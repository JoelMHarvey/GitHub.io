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
    // The gate is the front door, so it wears the site's own clothes:
    // same slate ground and radial glows, the wordmark with its amber
    // full stop, card-styled form, and a visible button (Enter works too).
    var wrap = document.createElement("div");
    wrap.id = "jmh-gate";
    // vibecheck-ignore-next-line: innerhtml-assignment — fixed literal markup, nothing interpolated
    wrap.innerHTML =
      '<div style="position:fixed;inset:0;display:flex;align-items:center;justify-content:center;' +
      "z-index:99999;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;" +
      "background:radial-gradient(1100px 500px at 85% -10%,#2c3d4d 0%,transparent 60%)," +
      'radial-gradient(900px 600px at -10% 110%,#253646 0%,transparent 55%),#1b2733">' +
      '<form id="jmh-gate-form" style="text-align:center;max-width:300px;width:90%;' +
      'background:#2c3d4d;border:1px solid #3d5570;border-radius:12px;padding:2rem 1.8rem">' +
      '<div style="font-size:1.6rem;font-weight:700;letter-spacing:-0.02em;color:#fff;margin-bottom:0.3rem">' +
      'Joel Harvey<span style="color:#e8b04b">.</span></div>' +
      '<div style="color:#9db1c0;margin-bottom:1.1rem;font-size:0.9rem">This site is private.</div>' +
      '<input id="jmh-gate-pw" type="password" autocomplete="current-password" placeholder="Password" ' +
      'style="width:100%;padding:0.65rem 0.9rem;border-radius:10px;border:1px solid #3d5570;' +
      'background:#1b2733;color:#e8eef3;font-size:1rem;outline:none;text-align:center;box-sizing:border-box">' +
      '<button type="submit" style="width:100%;margin-top:0.7rem;padding:0.65rem 0.9rem;border:0;' +
      'border-radius:10px;background:#e8b04b;color:#1b2733;font-size:1rem;font-weight:600;cursor:pointer">' +
      "Enter</button>" +
      '<div id="jmh-gate-err" style="color:#e0a8a8;font-size:0.85rem;height:1.2rem;margin-top:0.6rem"></div>' +
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
