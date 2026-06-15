/* =============================================================
   MATCHA SOUS — UI behaviour
   Header, mobile nav, scroll reveal, accordions, gallery,
   product add-to-cart, cart page, checkout, confirmation, forms.
   ============================================================= */
(function () {
  "use strict";

  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };
  var money = window.MSmoney;
  var Cart = window.MSCart;

  /* ---- product image map (used for cart thumbnails) ---- */
  var PRODUCT_IMAGE = "assets/images/product-device.svg";

  /* ---------- Toast ---------- */
  var toastEl;
  function toast(msg) {
    if (!toastEl) {
      toastEl = document.createElement("div");
      toastEl.className = "toast";
      toastEl.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6 9 17l-5-5"/></svg><span></span>';
      document.body.appendChild(toastEl);
    }
    $("span", toastEl).textContent = msg;
    toastEl.classList.add("show");
    clearTimeout(toastEl._t);
    toastEl._t = setTimeout(function () { toastEl.classList.remove("show"); }, 2600);
  }
  window.MStoast = toast;

  /* ---------- Header on scroll ---------- */
  var header = $(".site-header");
  if (header) {
    var onScroll = function () { header.classList.toggle("scrolled", window.scrollY > 12); };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  /* ---------- Mobile menu ---------- */
  var menu = $(".mobile-menu");
  var openBtn = $(".nav-toggle");
  var closeBtn = $(".mm-close");
  function setMenu(open) {
    if (!menu) return;
    menu.classList.toggle("open", open);
    document.body.style.overflow = open ? "hidden" : "";
    if (openBtn) openBtn.setAttribute("aria-expanded", open ? "true" : "false");
  }
  if (openBtn) openBtn.addEventListener("click", function () { setMenu(true); });
  if (closeBtn) closeBtn.addEventListener("click", function () { setMenu(false); });
  if (menu) $$(".mm-link", menu).forEach(function (a) { a.addEventListener("click", function () { setMenu(false); }); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") setMenu(false); });

  /* ---------- Scroll reveal ---------- */
  var reveals = $$(".reveal");
  if (reveals.length && "IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("in"); });
  }

  /* ---------- Accordions (FAQ / specs) ---------- */
  $$(".acc-trigger").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var panel = btn.nextElementSibling;
      var open = btn.getAttribute("aria-expanded") === "true";
      btn.setAttribute("aria-expanded", open ? "false" : "true");
      panel.style.maxHeight = open ? "0px" : panel.scrollHeight + "px";
    });
  });

  /* ---------- Quantity steppers ---------- */
  $$(".qty").forEach(function (q) {
    var input = $("input", q);
    var minus = $("[data-qty-minus]", q);
    var plus = $("[data-qty-plus]", q);
    function clamp() { input.value = Math.max(1, parseInt(input.value, 10) || 1); }
    if (minus) minus.addEventListener("click", function () { input.value = Math.max(1, (parseInt(input.value, 10) || 1) - 1); input.dispatchEvent(new Event("change", { bubbles: true })); });
    if (plus) plus.addEventListener("click", function () { input.value = (parseInt(input.value, 10) || 1) + 1; input.dispatchEvent(new Event("change", { bubbles: true })); });
    if (input) input.addEventListener("change", clamp);
  });

  /* ---------- PDP: variant swatches ---------- */
  $$("[data-swatch-group]").forEach(function (group) {
    $$(".swatch", group).forEach(function (sw) {
      sw.addEventListener("click", function () {
        $$(".swatch", group).forEach(function (s) { s.setAttribute("aria-pressed", "false"); });
        sw.setAttribute("aria-pressed", "true");
        var label = $("[data-selected-variant]");
        if (label) label.textContent = sw.getAttribute("data-variant");
      });
    });
  });

  /* ---------- PDP: gallery ---------- */
  var galleryMain = $("[data-gallery-main]");
  if (galleryMain) {
    $$("[data-gallery-thumb]").forEach(function (thumb) {
      thumb.addEventListener("click", function () {
        var src = thumb.getAttribute("data-src");
        var alt = thumb.getAttribute("data-alt") || "";
        galleryMain.src = src;
        galleryMain.alt = alt;
        $$("[data-gallery-thumb]").forEach(function (t) { t.setAttribute("aria-current", "false"); });
        thumb.setAttribute("aria-current", "true");
      });
    });
  }

  /* ---------- Add to cart ---------- */
  $$("[data-add-to-cart]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var variant = "Onyx";
      var pressed = $('.swatch[aria-pressed="true"]');
      if (pressed) variant = pressed.getAttribute("data-variant");
      var qtyInput = $("[data-pdp-qty]");
      var qty = qtyInput ? Math.max(1, parseInt(qtyInput.value, 10) || 1) : 1;
      Cart.add({
        id: btn.getAttribute("data-id") || "matcha-sous",
        title: btn.getAttribute("data-title") || "Matcha Sous Mixer",
        price: parseFloat(btn.getAttribute("data-price")) || 149,
        variant: variant,
        image: btn.getAttribute("data-image") || PRODUCT_IMAGE,
        href: "product.html"
      });
      if (btn.hasAttribute("data-buy-now")) { window.location.href = "checkout.html"; return; }
      toast("Added to cart — " + variant);
    });
  });

  /* ---------- Cart page ---------- */
  var cartRoot = $("#cart-root");
  if (cartRoot) renderCart();

  function renderCart() {
    var items = Cart.items();
    var empty = $("#cart-empty");
    var layout = $("#cart-layout");
    if (!items.length) {
      if (empty) empty.style.display = "";
      if (layout) layout.style.display = "none";
      return;
    }
    if (empty) empty.style.display = "none";
    if (layout) layout.style.display = "";

    var lines = $("#cart-lines");
    lines.innerHTML = items.map(function (it) {
      var k = Cart.keyOf(it);
      return '' +
        '<div class="cart-line" data-key="' + k + '">' +
          '<a class="thumb" href="product.html"><img src="' + it.image + '" alt="' + it.title + '" loading="lazy"></a>' +
          '<div class="cart-line-info">' +
            '<h3 class="serif">' + it.title + '</h3>' +
            '<p class="variant">Finish: ' + it.variant + '</p>' +
            '<div class="qty" data-line-qty>' +
              '<button type="button" data-qty-minus aria-label="Decrease quantity">&minus;</button>' +
              '<input type="number" min="1" value="' + it.qty + '" aria-label="Quantity">' +
              '<button type="button" data-qty-plus aria-label="Increase quantity">+</button>' +
            '</div>' +
          '</div>' +
          '<div class="line-right">' +
            '<div class="price serif">' + money(it.price * it.qty) + '</div>' +
            '<button class="remove" type="button" data-remove>Remove</button>' +
          '</div>' +
        '</div>';
    }).join("");

    /* wire line controls */
    $$(".cart-line", lines).forEach(function (line) {
      var k = line.getAttribute("data-key");
      var input = $("input", line);
      var minus = $("[data-qty-minus]", line);
      var plus = $("[data-qty-plus]", line);
      minus.addEventListener("click", function () { Cart.setQty(k, (parseInt(input.value, 10) || 1) - 1); renderCart(); });
      plus.addEventListener("click", function () { Cart.setQty(k, (parseInt(input.value, 10) || 1) + 1); renderCart(); });
      input.addEventListener("change", function () { Cart.setQty(k, parseInt(input.value, 10) || 1); renderCart(); });
      $("[data-remove]", line).addEventListener("click", function () { Cart.remove(k); renderCart(); toast("Item removed"); });
    });

    var sub = Cart.subtotal();
    if ($("#cart-subtotal")) $("#cart-subtotal").textContent = money(sub);
    if ($("#cart-total")) $("#cart-total").textContent = money(sub);
  }

  /* ---------- Checkout page ---------- */
  var checkoutForm = $("#checkout-form");
  if (checkoutForm) {
    var items = Cart.items();
    if (!items.length) { window.location.href = "cart.html"; return; }
    renderCheckoutSummary();
    checkoutForm.addEventListener("submit", function (e) {
      e.preventDefault();
      var data = {};
      $$("input, select", checkoutForm).forEach(function (f) { if (f.name) data[f.name] = f.value; });
      Cart.placeOrder(data);
      window.location.href = "order-confirmation.html";
    });
  }

  function renderCheckoutSummary() {
    var wrap = $("#checkout-lines");
    var items = Cart.items();
    if (wrap) {
      wrap.innerHTML = items.map(function (it) {
        return '' +
          '<div class="mini-line">' +
            '<div class="thumb"><img src="' + it.image + '" alt="' + it.title + '"><span class="q">' + it.qty + '</span></div>' +
            '<div class="nm"><b>' + it.title + '</b><br><span>Finish: ' + it.variant + '</span></div>' +
            '<div class="serif">' + money(it.price * it.qty) + '</div>' +
          '</div>';
      }).join("");
    }
    var sub = Cart.subtotal();
    if ($("#co-subtotal")) $("#co-subtotal").textContent = money(sub);
    if ($("#co-total")) $("#co-total").textContent = money(sub);
  }

  /* ---------- Confirmation page ---------- */
  var confirmRoot = $("#confirm-root");
  if (confirmRoot) {
    var order = Cart.lastOrder();
    if (!order) { confirmRoot.innerHTML = '<p class="muted center">No recent order found. <a href="product.html" class="link-arrow">Shop Matcha Sous</a></p>'; }
    else {
      if ($("#order-number")) $("#order-number").textContent = order.number;
      if ($("#order-email")) $("#order-email").textContent = order.customer.email || "your inbox";
      var lines = $("#confirm-lines");
      if (lines) {
        lines.innerHTML = order.items.map(function (it) {
          return '<div class="o-row"><span>' + it.title + ' &times; ' + it.qty + ' <span class="muted">(' + it.variant + ')</span></span><span>' + money(it.price * it.qty) + '</span></div>';
        }).join("");
      }
      if ($("#confirm-total")) $("#confirm-total").textContent = money(order.total);
    }
  }

  /* ---------- Mock forms (contact / newsletter) ---------- */
  $$("[data-mock-form]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var msg = form.getAttribute("data-success") || "Thank you — we'll be in touch shortly.";
      var note = $("[data-form-note]", form);
      form.reset();
      if (note) { note.textContent = msg; note.hidden = false; }
      else { toast(msg); }
    });
  });

  /* ---------- Footer year ---------- */
  $$("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
