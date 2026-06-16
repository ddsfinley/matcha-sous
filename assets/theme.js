/* Matcha Sous — Shopify theme UI (nav, reveal, accordion, qty steppers, gallery).
   Cart & checkout are handled natively by Shopify. */
(function () {
  "use strict";
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  var header = $(".site-header");
  if (header) { var on = function () { header.classList.toggle("scrolled", window.scrollY > 12); }; on(); window.addEventListener("scroll", on, { passive: true }); }

  var menu = $(".mobile-menu"), ob = $(".nav-toggle"), cb = $(".mm-close");
  function setMenu(o) { if (!menu) return; menu.classList.toggle("open", o); document.body.style.overflow = o ? "hidden" : ""; if (ob) ob.setAttribute("aria-expanded", o ? "true" : "false"); }
  if (ob) ob.addEventListener("click", function () { setMenu(true); });
  if (cb) cb.addEventListener("click", function () { setMenu(false); });
  if (menu) $$(".mm-link", menu).forEach(function (a) { a.addEventListener("click", function () { setMenu(false); }); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") setMenu(false); });

  var rev = $$(".reveal");
  if (rev.length && "IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (es) { es.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); } }); }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });
    rev.forEach(function (el) { io.observe(el); });
  } else { rev.forEach(function (el) { el.classList.add("in"); }); }

  $$(".acc-trigger").forEach(function (b) {
    b.addEventListener("click", function () {
      var p = b.nextElementSibling, o = b.getAttribute("aria-expanded") === "true";
      b.setAttribute("aria-expanded", o ? "false" : "true");
      p.style.maxHeight = o ? "0px" : p.scrollHeight + "px";
    });
  });

  $$(".qty").forEach(function (q) {
    var i = $("input", q), m = $("[data-qty-minus]", q), p = $("[data-qty-plus]", q);
    var floor = parseInt((i && i.min) || "1", 10);
    if (m) m.addEventListener("click", function () { i.value = Math.max(floor, (parseInt(i.value, 10) || 1) - 1); });
    if (p) p.addEventListener("click", function () { i.value = (parseInt(i.value, 10) || 0) + 1; });
  });

  var gm = $("[data-gallery-main]");
  if (gm) $$("[data-gallery-thumb]").forEach(function (t) {
    t.addEventListener("click", function () {
      gm.src = t.getAttribute("data-src"); gm.alt = t.getAttribute("data-alt") || "";
      $$("[data-gallery-thumb]").forEach(function (x) { x.setAttribute("aria-current", "false"); });
      t.setAttribute("aria-current", "true");
    });
  });

  $$("[data-year]").forEach(function (e) { e.textContent = new Date().getFullYear(); });
})();
