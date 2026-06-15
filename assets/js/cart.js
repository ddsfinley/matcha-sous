/* =============================================================
   MATCHA SOUS — Cart (localStorage-backed)
   A lightweight, framework-free cart shared across every page.
   Note: checkout is a front-end demo — no real payment is taken.
   ============================================================= */
(function () {
  "use strict";
  var KEY = "ms_cart_v1";
  var ORDER_KEY = "ms_last_order";

  function read() {
    try { return JSON.parse(localStorage.getItem(KEY)) || []; }
    catch (e) { return []; }
  }
  function write(items) {
    localStorage.setItem(KEY, JSON.stringify(items));
    document.dispatchEvent(new CustomEvent("cart:change", { detail: items }));
  }
  function keyOf(it) { return it.id + "::" + (it.variant || ""); }

  var Cart = {
    items: function () { return read(); },
    count: function () { return read().reduce(function (n, i) { return n + i.qty; }, 0); },
    subtotal: function () { return read().reduce(function (s, i) { return s + i.price * i.qty; }, 0); },
    add: function (item) {
      var items = read();
      var k = keyOf(item);
      var ex = items.filter(function (i) { return keyOf(i) === k; })[0];
      if (ex) { ex.qty += (item.qty || 1); }
      else { items.push(Object.assign({ qty: 1 }, item)); }
      write(items);
      return Cart.count();
    },
    setQty: function (k, qty) {
      var items = read();
      items.forEach(function (i) { if (keyOf(i) === k) { i.qty = Math.max(1, qty); } });
      write(items);
    },
    remove: function (k) { write(read().filter(function (i) { return keyOf(i) !== k; })); },
    clear: function () { write([]); },
    keyOf: keyOf,
    /* persist a mock order so the confirmation page has something to show */
    placeOrder: function (customer) {
      var items = read();
      var order = {
        number: "MS-" + Math.floor(100000 + Math.random() * 899999),
        date: new Date().toISOString(),
        items: items,
        subtotal: Cart.subtotal(),
        shipping: 0,
        tax: Math.round(Cart.subtotal() * 0.0 * 100) / 100,
        total: Cart.subtotal(),
        customer: customer || {}
      };
      localStorage.setItem(ORDER_KEY, JSON.stringify(order));
      Cart.clear();
      return order;
    },
    lastOrder: function () {
      try { return JSON.parse(localStorage.getItem(ORDER_KEY)); }
      catch (e) { return null; }
    }
  };

  window.MSCart = Cart;
  window.MSmoney = function (n) {
    return "$" + Number(n).toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  };

  function updateBadges() {
    var c = Cart.count();
    document.querySelectorAll(".cart-count").forEach(function (el) {
      el.textContent = c;
      el.setAttribute("data-empty", c === 0 ? "true" : "false");
    });
  }
  document.addEventListener("cart:change", updateBadges);
  document.addEventListener("DOMContentLoaded", updateBadges);
})();
