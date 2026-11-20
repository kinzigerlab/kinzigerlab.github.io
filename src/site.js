(function () {
  "use strict";
  var root = document.documentElement;
  var views = Array.prototype.slice.call(document.querySelectorAll(".view"));
  var navLinks = Array.prototype.slice.call(document.querySelectorAll("[data-nav]"));

  // Every address the site answers to. v = view to show, a = element to scroll to, f = publication filter.
  var routes = {
    "": { v: "home" },
    "home": { v: "home" },
    "research": { v: "research" },
    "edna": { v: "research", a: "edna" },
    "genetics": { v: "research", a: "genetics" },
    "partners": { v: "research", a: "partners" },
    "people": { v: "people" },
    "alumni": { v: "people", a: "alumni" },
    "publications": { v: "publications" },
    "publications-edna": { v: "publications", f: "edna" },
    "join": { v: "join" }
  };

  function activate(name) {
    views.forEach(function (el) {
      el.classList.toggle("is-active", el.getAttribute("data-view") === name);
    });
    navLinks.forEach(function (a) {
      if (a.getAttribute("data-nav") === name && name !== "home") {
        a.setAttribute("aria-current", "page");
      } else {
        a.removeAttribute("aria-current");
      }
    });
    countView(name);
  }

  // ---- visit counting (GoatCounter: no cookies, nothing stored about the visitor).
  // Each view is reported as its own page: "/" for home, then "/research", "/people", "/publications", "/join".
  // Moving within a view (to eDNA, alumni, contact) is not counted again. If the counter script is
  // missing or blocked, nothing happens.
  var viewNames = { home: "Home", research: "Research", people: "People", publications: "Publications", join: "Join the lab" };
  var counted = null;
  function countView(name) {
    if (name === counted || !viewNames[name]) { return; }
    var vars = { path: name === "home" ? "/" : "/" + name, title: "The Kinziger Lab: " + viewNames[name] };
    if (counted !== null) { vars.referrer = ""; }   // only the first view carries the site the visitor came from
    counted = name;
    var tries = 0;
    (function send() {
      var gc = window.goatcounter;
      if (!gc || !gc.count) {
        // the counter script loads after this one; give it ten seconds, then give up
        if (tries < 50) { tries += 1; window.setTimeout(send, 200); }
        return;
      }
      if ("visibilityState" in document && document.visibilityState !== "visible") {
        var whenSeen = function () {
          if (document.visibilityState !== "visible") { return; }
          document.removeEventListener("visibilitychange", whenSeen);
          gc.count(vars);
        };
        document.addEventListener("visibilitychange", whenSeen);
        return;
      }
      gc.count(vars);
    })();
  }

  function currentView() {
    var el = document.querySelector(".view.is-active");
    return el ? el.getAttribute("data-view") : null;
  }

  function route() {
    var hash = (window.location.hash || "").replace(/^#/, "");
    if (hash === "contact" || hash === "main") {
      if (!currentView()) { activate("home"); }
      var target = document.getElementById(hash);
      if (target) { target.scrollIntoView(); }
      return;
    }
    var r = routes[hash] || routes[""];
    activate(r.v);
    if (r.f) { setFilter(r.f); }
    if (r.a) {
      var el = document.getElementById(r.a);
      if (el) { el.scrollIntoView(); }
    } else {
      window.scrollTo(0, 0);
    }
  }

  // ---- publications: theme chips and word search
  var list = document.getElementById("publist");
  var pubs = list ? Array.prototype.slice.call(list.querySelectorAll(".pub")) : [];
  var chips = Array.prototype.slice.call(document.querySelectorAll(".chip"));
  var query = document.getElementById("pubq");
  var count = document.getElementById("pubcount");
  var empty = document.getElementById("pubempty");
  var theme = "all";

  function applyFilter() {
    var q = query ? query.value.trim().toLowerCase() : "";
    var shown = 0;
    var lastYear = null;
    pubs.forEach(function (li) {
      var ok = (theme === "all" || li.getAttribute("data-theme") === theme) &&
        (!q || li.textContent.toLowerCase().indexOf(q) !== -1);
      li.hidden = !ok;
      if (ok) {
        shown += 1;
        var y = li.getAttribute("data-year");
        li.classList.toggle("first-of-year", y !== lastYear);
        lastYear = y;
      }
    });
    if (count) {
      count.textContent = shown === pubs.length
        ? "Showing all " + pubs.length + " papers"
        : "Showing " + shown + " of " + pubs.length + " papers";
    }
    if (empty) { empty.hidden = shown !== 0; }
  }

  function setFilter(name) {
    theme = name;
    chips.forEach(function (c) {
      c.setAttribute("aria-pressed", c.getAttribute("data-filter") === name ? "true" : "false");
    });
    applyFilter();
  }

  chips.forEach(function (c) {
    c.addEventListener("click", function () { setFilter(c.getAttribute("data-filter")); });
  });
  if (query) { query.addEventListener("input", applyFilter); }

  // ---- draft notes on and off (remembered for this browser only)
  var toggle = document.getElementById("notes-toggle");
  function setNotes(on) {
    root.classList.toggle("notes-off", !on);
    if (toggle) {
      toggle.textContent = on ? "Hide notes" : "Show notes";
      toggle.setAttribute("aria-pressed", on ? "true" : "false");
    }
    try { window.localStorage.setItem("kl-notes", on ? "on" : "off"); } catch (e) { /* storage unavailable */ }
  }
  if (toggle) {
    var saved = null;
    try { saved = window.localStorage.getItem("kl-notes"); } catch (e) { /* storage unavailable */ }
    setNotes(saved !== "off");
    toggle.addEventListener("click", function () {
      setNotes(root.classList.contains("notes-off"));
    });
  }

  window.addEventListener("hashchange", route);
  route();
})();
