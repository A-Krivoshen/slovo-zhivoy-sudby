/**
 * Site-wide lightbox: enlarge, gallery, keyboard, swipe,
 * pinch-to-zoom + pan (touch), wheel zoom (desktop), double-tap / double-click.
 */
(function () {
  "use strict";

  var SELECTOR =
    ".post-content figure img, .post-content p > img, .md-content figure img, .entry-cover img";

  var MIN_SCALE = 1;
  var MAX_SCALE = 5;
  var DOUBLE_MS = 300;

  function isSkippable(img) {
    if (!img || img.tagName !== "IMG") return true;
    if (img.closest("a[href]") && !img.closest("figure")) {
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
    var dc = img.getAttribute("data-caption");
    if (dc && dc.trim()) return dc.trim();
    var fig = img.closest("figure");
    if (fig) {
      var cap = fig.querySelector("figcaption");
      if (cap) return cap.textContent.trim();
    }
    return (img.getAttribute("alt") || "").trim();
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
      '<div class="szhs-lightbox__stage">' +
      '  <div class="szhs-lightbox__viewport">' +
      '    <img class="szhs-lightbox__img" alt="" draggable="false">' +
      "  </div>" +
      '  <p class="szhs-lightbox__caption"></p>' +
      '  <p class="szhs-lightbox__hint" hidden>Сведите/разведите пальцы для масштаба · перетащите · двойной тап сбрасывает</p>' +
      "</div>" +
      '<button type="button" class="szhs-lightbox__nav szhs-lightbox__nav--next" aria-label="Следующее">›</button>';
    document.body.appendChild(root);
    return root;
  }

  var ui = null;
  var gallery = [];
  var index = 0;
  var scale = 1;
  var panX = 0;
  var panY = 0;
  var lastTap = 0;
  var pointers = {};
  var pinchStartDist = 0;
  var pinchStartScale = 1;
  var panStartX = 0;
  var panStartY = 0;
  var panOriginX = 0;
  var panOriginY = 0;
  var isPanning = false;
  var lastFocus = null;

  function ensureUI() {
    if (ui) return ui;
    ui = createUI();
    ui.querySelector(".szhs-lightbox__close").addEventListener("click", close);
    ui.querySelector(".szhs-lightbox__nav--prev").addEventListener("click", function (e) {
      e.stopPropagation();
      if (scale > 1.05) return;
      show(index - 1);
    });
    ui.querySelector(".szhs-lightbox__nav--next").addEventListener("click", function (e) {
      e.stopPropagation();
      if (scale > 1.05) return;
      show(index + 1);
    });
    ui.addEventListener("click", function (e) {
      if (e.target === ui || e.target.classList.contains("szhs-lightbox__stage")) close();
    });

    var vp = ui.querySelector(".szhs-lightbox__viewport");
    var img = ui.querySelector(".szhs-lightbox__img");

    /* wheel zoom */
    vp.addEventListener(
      "wheel",
      function (e) {
        if (!ui.classList.contains("is-open")) return;
        e.preventDefault();
        var delta = e.deltaY > 0 ? 0.9 : 1.1;
        setScale(scale * delta, e.clientX, e.clientY);
      },
      { passive: false }
    );

    /* double-click desktop */
    img.addEventListener("dblclick", function (e) {
      e.preventDefault();
      if (scale > 1.2) resetTransform();
      else setScale(2.5, e.clientX, e.clientY);
    });

    /* pointer events for pan + pinch */
    vp.addEventListener("pointerdown", onPointerDown);
    vp.addEventListener("pointermove", onPointerMove);
    vp.addEventListener("pointerup", onPointerUp);
    vp.addEventListener("pointercancel", onPointerUp);
    vp.addEventListener("pointerleave", function (e) {
      if (pointers[e.pointerId]) onPointerUp(e);
    });

    return ui;
  }

  function applyTransform() {
    if (!ui) return;
    var img = ui.querySelector(".szhs-lightbox__img");
    img.style.transform =
      "translate(" + panX + "px," + panY + "px) scale(" + scale + ")";
    ui.classList.toggle("is-zoomed", scale > 1.05);
  }

  function clampPan() {
    if (scale <= 1) {
      panX = 0;
      panY = 0;
      return;
    }
    var img = ui.querySelector(".szhs-lightbox__img");
    var rect = img.getBoundingClientRect();
    var maxX = Math.max(0, (rect.width - window.innerWidth) / 2 + 40);
    var maxY = Math.max(0, (rect.height - window.innerHeight) / 2 + 40);
    /* use natural size * scale relative to viewport */
    var nw = img.naturalWidth || img.clientWidth;
    var nh = img.naturalHeight || img.clientHeight;
    var displayW = Math.min(window.innerWidth * 0.95, nw) * scale;
    var displayH = Math.min(window.innerHeight * 0.85, nh) * scale;
    maxX = Math.max(0, (displayW - window.innerWidth) / 2 + 24);
    maxY = Math.max(0, (displayH - window.innerHeight) / 2 + 24);
    panX = Math.min(maxX, Math.max(-maxX, panX));
    panY = Math.min(maxY, Math.max(-maxY, panY));
  }

  function setScale(s, cx, cy) {
    var prev = scale;
    scale = Math.min(MAX_SCALE, Math.max(MIN_SCALE, s));
    if (scale === 1) {
      panX = 0;
      panY = 0;
    } else if (cx != null && cy != null && prev > 0) {
      /* zoom toward pointer — simple proportional pan adjust */
      var ratio = scale / prev;
      panX = panX * ratio;
      panY = panY * ratio;
    }
    clampPan();
    applyTransform();
  }

  function resetTransform() {
    scale = 1;
    panX = 0;
    panY = 0;
    applyTransform();
  }

  function pointerList() {
    return Object.keys(pointers).map(function (k) {
      return pointers[k];
    });
  }

  function dist(a, b) {
    var dx = a.x - b.x;
    var dy = a.y - b.y;
    return Math.sqrt(dx * dx + dy * dy);
  }

  function onPointerDown(e) {
    if (!ui || !ui.classList.contains("is-open")) return;
    pointers[e.pointerId] = { x: e.clientX, y: e.clientY };
    try {
      e.currentTarget.setPointerCapture(e.pointerId);
    } catch (err) {}
    var pts = pointerList();
    if (pts.length === 2) {
      pinchStartDist = dist(pts[0], pts[1]);
      pinchStartScale = scale;
      isPanning = false;
    } else if (pts.length === 1) {
      panStartX = e.clientX;
      panStartY = e.clientY;
      panOriginX = panX;
      panOriginY = panY;
      isPanning = scale > 1.05;
      /* double-tap */
      var now = Date.now();
      if (now - lastTap < DOUBLE_MS) {
        e.preventDefault();
        if (scale > 1.2) resetTransform();
        else setScale(2.5, e.clientX, e.clientY);
        lastTap = 0;
      } else {
        lastTap = now;
      }
    }
  }

  function onPointerMove(e) {
    if (!pointers[e.pointerId]) return;
    pointers[e.pointerId] = { x: e.clientX, y: e.clientY };
    var pts = pointerList();
    if (pts.length === 2 && pinchStartDist > 0) {
      e.preventDefault();
      var d = dist(pts[0], pts[1]);
      setScale(pinchStartScale * (d / pinchStartDist));
    } else if (pts.length === 1 && isPanning) {
      e.preventDefault();
      panX = panOriginX + (e.clientX - panStartX);
      panY = panOriginY + (e.clientY - panStartY);
      clampPan();
      applyTransform();
    }
  }

  function onPointerUp(e) {
    delete pointers[e.pointerId];
    var pts = pointerList();
    if (pts.length < 2) pinchStartDist = 0;
    if (pts.length === 0) isPanning = false;
    if (pts.length === 1) {
      panStartX = pts[0].x;
      panStartY = pts[0].y;
      panOriginX = panX;
      panOriginY = panY;
      isPanning = scale > 1.05;
    }
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
    var hint = box.querySelector(".szhs-lightbox__hint");

    resetTransform();
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
    if (hint) {
      hint.hidden = false;
      hint.textContent =
        document.documentElement.lang === "en"
          ? "Pinch to zoom · drag to pan · double-tap to reset"
          : "Сведите/разведите пальцы для масштаба · перетащите · двойной тап сбрасывает";
    }

    box.classList.add("is-open");
    document.body.classList.add("szhs-lightbox-open");
    try {
      box.querySelector(".szhs-lightbox__close").focus({ preventScroll: true });
    } catch (err) {}
  }

  function open(img) {
    lastFocus = document.activeElement;
    gallery = collectGallery(img);
    index = Math.max(0, gallery.indexOf(img));
    show(index);
  }

  function close() {
    if (!ui) return;
    ui.classList.remove("is-open");
    document.body.classList.remove("szhs-lightbox-open");
    var big = ui.querySelector(".szhs-lightbox__img");
    if (big) {
      big.removeAttribute("src");
      big.style.transform = "";
    }
    resetTransform();
    if (lastFocus && lastFocus.focus) {
      try {
        lastFocus.focus({ preventScroll: true });
      } catch (err) {}
    }
    lastFocus = null;
  }

  document.addEventListener("click", function (e) {
    var img = e.target.closest("img");
    if (!img || isSkippable(img)) return;
    if (!img.matches(SELECTOR) && !img.closest(".entry-cover")) return;
    if (img.closest(".header, .footer, .logo")) return;
    e.preventDefault();
    open(img);
  });

  document.addEventListener("keydown", function (e) {
    if (!ui || !ui.classList.contains("is-open")) return;
    if (e.key === "Escape") {
      if (scale > 1.05) resetTransform();
      else close();
    }
    if (e.key === "ArrowLeft" && scale <= 1.05) show(index - 1);
    if (e.key === "ArrowRight" && scale <= 1.05) show(index + 1);
    if (e.key === "+" || e.key === "=") setScale(scale * 1.15);
    if (e.key === "-" || e.key === "_") setScale(scale * 0.85);
    if (e.key === "0") resetTransform();
  });

  /* swipe only when not zoomed */
  var touchX = null;
  document.addEventListener(
    "touchstart",
    function (e) {
      if (!ui || !ui.classList.contains("is-open") || scale > 1.05) return;
      if (e.touches.length !== 1) return;
      touchX = e.changedTouches[0].screenX;
    },
    { passive: true }
  );
  document.addEventListener(
    "touchend",
    function (e) {
      if (touchX == null || !ui || !ui.classList.contains("is-open") || scale > 1.05)
        return;
      var dx = e.changedTouches[0].screenX - touchX;
      touchX = null;
      if (Math.abs(dx) < 50) return;
      if (dx > 0) show(index - 1);
      else show(index + 1);
    },
    { passive: true }
  );
})();
