/**
 * Lightweight site-wide lightbox for content images.
 * Click any photo in article content / covers to enlarge; Esc / backdrop / × to close;
 * ← → for gallery on the same page.
 */
(function () {
  "use strict";

  var SELECTOR =
    ".post-content figure img, .post-content p > img, .md-content figure img, .entry-cover img";

  function isSkippable(img) {
    if (!img || img.tagName !== "IMG") return true;
    if (img.closest("a[href]") && !img.closest("figure")) {
      /* leave plain linked images that are navigation icons alone */
      var a = img.closest("a[href]");
      if (a && !/\.(jpe?g|png|webp|gif)(\?|$)/i.test(a.getAttribute("href") || "")) {
        return true;
      }
    }
    if (img.width > 0 && img.width < 40 && img.height > 0 && img.height < 40) return true;
    if (img.classList.contains("szhs-no-lightbox")) return true;
    var src = img.getAttribute("src") || "";
    if (!src || src.indexOf("data:") === 0) return true;
    return false;
  }

  function fullSrc(img) {
    return img.currentSrc || img.src || img.getAttribute("src");
  }

  function captionFor(img) {
    var fig = img.closest("figure");
    if (fig) {
      var cap = fig.querySelector("figcaption");
      if (cap) return cap.textContent.trim();
    }
    return img.getAttribute("alt") || "";
  }

  function collectGallery(fromImg) {
    var root =
      fromImg.closest(".post-content, .md-content, article.post-single, main") ||
      document;
    var list = [];
    root.querySelectorAll(SELECTOR).forEach(function (img) {
      if (!isSkippable(img)) list.push(img);
    });
    if (list.indexOf(fromImg) === -1) list.unshift(fromImg);
    return list;
  }

  function createUI() {
    var root = document.createElement("div");
    root.className = "szhs-lightbox";
    root.setAttribute("role", "dialog");
    root.setAttribute("aria-modal", "true");
    root.setAttribute("aria-label", "Просмотр фотографии");
    root.innerHTML =
      '<button type="button" class="szhs-lightbox__close" aria-label="Закрыть">×</button>' +
      '<span class="szhs-lightbox__counter" aria-live="polite"></span>' +
      '<button type="button" class="szhs-lightbox__nav szhs-lightbox__nav--prev" aria-label="Предыдущее">‹</button>' +
      '<div class="szhs-lightbox__dialog">' +
      '  <img class="szhs-lightbox__img" alt="">' +
      '  <p class="szhs-lightbox__caption"></p>' +
      "</div>" +
      '<button type="button" class="szhs-lightbox__nav szhs-lightbox__nav--next" aria-label="Следующее">›</button>';
    document.body.appendChild(root);
    return root;
  }

  var ui = null;
  var gallery = [];
  var index = 0;

  function ensureUI() {
    if (ui) return ui;
    ui = createUI();
    ui.querySelector(".szhs-lightbox__close").addEventListener("click", close);
    ui.querySelector(".szhs-lightbox__nav--prev").addEventListener("click", function (e) {
      e.stopPropagation();
      show(index - 1);
    });
    ui.querySelector(".szhs-lightbox__nav--next").addEventListener("click", function (e) {
      e.stopPropagation();
      show(index + 1);
    });
    ui.addEventListener("click", function (e) {
      if (e.target === ui) close();
    });
    return ui;
  }

  function show(i) {
    if (!gallery.length) return;
    index = (i + gallery.length) % gallery.length;
    var img = gallery[index];
    var box = ensureUI();
    var big = box.querySelector(".szhs-lightbox__img");
    var cap = box.querySelector(".szhs-lightbox__caption");
    var counter = box.querySelector(".szhs-lightbox__counter");
    var prev = box.querySelector(".szhs-lightbox__nav--prev");
    var next = box.querySelector(".szhs-lightbox__nav--next");

    big.src = fullSrc(img);
    big.alt = img.getAttribute("alt") || "";
    var c = captionFor(img);
    cap.textContent = c;
    cap.hidden = !c;
    counter.textContent = gallery.length > 1 ? index + 1 + " / " + gallery.length : "";
    prev.disabled = gallery.length < 2;
    next.disabled = gallery.length < 2;
    prev.hidden = gallery.length < 2;
    next.hidden = gallery.length < 2;

    box.classList.add("is-open");
    document.body.classList.add("szhs-lightbox-open");
  }

  function open(img) {
    gallery = collectGallery(img);
    index = Math.max(0, gallery.indexOf(img));
    show(index);
  }

  function close() {
    if (!ui) return;
    ui.classList.remove("is-open");
    document.body.classList.remove("szhs-lightbox-open");
    var big = ui.querySelector(".szhs-lightbox__img");
    if (big) big.removeAttribute("src");
  }

  document.addEventListener("click", function (e) {
    var img = e.target.closest("img");
    if (!img || isSkippable(img)) return;
    if (!img.matches(SELECTOR) && !img.closest(".entry-cover")) return;
    /* don't hijack logo in header */
    if (img.closest(".header, .footer, .logo")) return;
    e.preventDefault();
    open(img);
  });

  document.addEventListener("keydown", function (e) {
    if (!ui || !ui.classList.contains("is-open")) return;
    if (e.key === "Escape") close();
    if (e.key === "ArrowLeft") show(index - 1);
    if (e.key === "ArrowRight") show(index + 1);
  });

  /* touch swipe */
  var touchX = null;
  document.addEventListener(
    "touchstart",
    function (e) {
      if (!ui || !ui.classList.contains("is-open")) return;
      touchX = e.changedTouches[0].screenX;
    },
    { passive: true }
  );
  document.addEventListener(
    "touchend",
    function (e) {
      if (touchX == null || !ui || !ui.classList.contains("is-open")) return;
      var dx = e.changedTouches[0].screenX - touchX;
      touchX = null;
      if (Math.abs(dx) < 50) return;
      if (dx > 0) show(index - 1);
      else show(index + 1);
    },
    { passive: true }
  );
})();
