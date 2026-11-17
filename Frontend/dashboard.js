/* ==========================================================================
   dashboard.js
   Behaviour for the dashboard shell. Plain JavaScript, no libraries.

   What it does:
     1. Sidebar: collapses to icons on desktop, opens as a drawer on mobile
     2. Remembers the collapsed state between visits (desktop only)
     3. Shows a tooltip next to each icon while the sidebar is collapsed
     4. Adds a shadow to the top bar once the page is scrolled
     5. Click ripple on elements that have the data-ripple attribute
     6. Hides the announcement badge when its count is 0

   The CSS in home-dashboard.css reacts to these classes on
   .dashboard-container:
     is-sidebar-collapsed   desktop: icon-only sidebar
     is-sidebar-open        mobile:  drawer is open
     is-preload             briefly set on load so no transition plays
   ========================================================================== */

(function () {
  "use strict";

  /* ---------- Elements ---------- */
  var container = document.querySelector(".dashboard-container");
  var sidebar = document.getElementById("sidebar");
  var toggleButton = document.getElementById("menu-toggle");
  var backdrop = document.getElementById("sidebar-backdrop");
  var topbar = document.querySelector(".top-navbar");
  var badge = document.getElementById("announcement-badge");

  // If the page has no sidebar (a simple inner page), do nothing.
  if (!container || !sidebar || !toggleButton) {
    return;
  }

  /* ---------- Settings ---------- */
  var STORAGE_KEY = "sms.sidebar.collapsed";

  // Same breakpoint as the CSS: 992px and up is "desktop".
  var desktopQuery = window.matchMedia("(min-width: 992px)");
  var reducedMotionQuery = window.matchMedia("(prefers-reduced-motion: reduce)");

  function isDesktop() {
    return desktopQuery.matches;
  }

  /* ---------- Saved state (localStorage can be blocked, so guard it) ---------- */
  function readSavedCollapsed() {
    try {
      return window.localStorage.getItem(STORAGE_KEY) === "true";
    } catch (error) {
      return false;
    }
  }

  function saveCollapsed(value) {
    try {
      window.localStorage.setItem(STORAGE_KEY, String(value));
    } catch (error) {
      /* Not saving is fine, the sidebar still works. */
    }
  }

  /* ---------- Keeps ARIA attributes and scroll lock in step with the state ---------- */
  function syncState() {
    var desktop = isDesktop();
    var collapsed = container.classList.contains("is-sidebar-collapsed");
    var open = container.classList.contains("is-sidebar-open");

    // The button reports whether the menu is currently expanded.
    toggleButton.setAttribute("aria-expanded", String(desktop ? !collapsed : open));

    // A closed drawer sits off-screen, so keep it out of the Tab order.
    if ("inert" in sidebar) {
      sidebar.inert = !desktop && !open;
    }

    // Stop the page behind the open drawer from scrolling.
    document.documentElement.classList.toggle("is-scroll-locked", !desktop && open);
  }

  /* ---------- Mobile drawer ---------- */
  function openDrawer() {
    container.classList.add("is-sidebar-open");
    syncState();
    var firstLink = sidebar.querySelector(".sidebar-link");
    if (firstLink) {
      firstLink.focus();
    }
  }

  function closeDrawer(returnFocus) {
    container.classList.remove("is-sidebar-open");
    syncState();
    if (returnFocus) {
      toggleButton.focus();
    }
  }

  /* ---------- Toggle button ---------- */
  toggleButton.addEventListener("click", function () {
    if (isDesktop()) {
      var collapsed = container.classList.toggle("is-sidebar-collapsed");
      saveCollapsed(collapsed);
      hideTooltip();
      syncState();
    } else if (container.classList.contains("is-sidebar-open")) {
      closeDrawer(false);
    } else {
      openDrawer();
    }
  });

  // Tapping the dimmed area closes the drawer.
  if (backdrop) {
    backdrop.addEventListener("click", function () {
      closeDrawer(false);
    });
  }

  // Escape closes the drawer and puts focus back on the toggle button.
  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape" && container.classList.contains("is-sidebar-open")) {
      closeDrawer(true);
    }
  });

  // Choosing a link on mobile closes the drawer.
  sidebar.addEventListener("click", function (event) {
    if (!isDesktop() && event.target.closest(".sidebar-link")) {
      closeDrawer(false);
    }
  });

  // Rotating a tablet or resizing the window can cross the breakpoint.
  function onBreakpointChange() {
    if (isDesktop()) {
      container.classList.remove("is-sidebar-open");
      container.classList.toggle("is-sidebar-collapsed", readSavedCollapsed());
    } else {
      container.classList.remove("is-sidebar-collapsed");
    }
    hideTooltip();
    syncState();
  }

  if (desktopQuery.addEventListener) {
    desktopQuery.addEventListener("change", onBreakpointChange);
  } else if (desktopQuery.addListener) {
    desktopQuery.addListener(onBreakpointChange); // older Safari
  }

  /* ---------- Tooltip for the collapsed sidebar ---------- */
  var tooltip = document.createElement("div");
  tooltip.className = "sidebar-tooltip";
  tooltip.setAttribute("role", "tooltip");
  document.body.appendChild(tooltip);

  function showTooltip(link) {
    if (!isDesktop() || !container.classList.contains("is-sidebar-collapsed")) {
      return;
    }
    var label = link.querySelector(".sidebar-text");
    if (!label) {
      return;
    }
    var rect = link.getBoundingClientRect();
    tooltip.textContent = label.textContent.trim();
    tooltip.style.top = rect.top + rect.height / 2 + "px";
    tooltip.style.left = rect.right + 14 + "px";
    tooltip.classList.add("is-visible");
  }

  function hideTooltip() {
    tooltip.classList.remove("is-visible");
  }

  sidebar.addEventListener("mouseover", function (event) {
    var link = event.target.closest(".sidebar-link");
    if (link) {
      showTooltip(link);
    }
  });

  sidebar.addEventListener("mouseout", function (event) {
    if (event.target.closest(".sidebar-link")) {
      hideTooltip();
    }
  });

  // Keyboard users get the same tooltip when a link receives focus.
  sidebar.addEventListener("focusin", function (event) {
    var link = event.target.closest(".sidebar-link");
    if (link) {
      showTooltip(link);
    }
  });

  sidebar.addEventListener("focusout", hideTooltip);

  var menu = sidebar.querySelector(".sidebar-menu");
  if (menu) {
    menu.addEventListener("scroll", hideTooltip, { passive: true });
  }

  /* ---------- Top bar shadow after scrolling ---------- */
  function onScroll() {
    if (topbar) {
      topbar.classList.toggle("is-scrolled", window.scrollY > 4);
    }
  }

  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* ---------- Click ripple ---------- */
  document.addEventListener("pointerdown", function (event) {
    if (reducedMotionQuery.matches) {
      return;
    }
    var target = event.target.closest("[data-ripple]");
    if (!target || event.button > 0) {
      return;
    }

    var rect = target.getBoundingClientRect();
    var size = Math.max(rect.width, rect.height) * 2;
    var ripple = document.createElement("span");

    ripple.className = "ripple";
    ripple.style.width = size + "px";
    ripple.style.height = size + "px";
    ripple.style.left = event.clientX - rect.left - size / 2 + "px";
    ripple.style.top = event.clientY - rect.top - size / 2 + "px";

    target.appendChild(ripple);
    ripple.addEventListener("animationend", function () {
      ripple.remove();
    });
  });

  /* ---------- Announcement badge ---------- */
  // Call SMSPortal.setAnnouncementCount(5) from any other script to update it.
  function setAnnouncementCount(count) {
    if (!badge) {
      return;
    }
    var number = Math.max(0, parseInt(count, 10) || 0);
    badge.textContent = number > 99 ? "99+" : String(number);
    badge.hidden = number === 0;
  }

  window.SMSPortal = window.SMSPortal || {};
  window.SMSPortal.setAnnouncementCount = setAnnouncementCount;

  if (badge) {
    setAnnouncementCount(badge.textContent);
  }

  /* ---------- Start-up ---------- */
  // Apply the saved state with transitions switched off, so the sidebar
  // does not visibly animate into place when the page opens.
  container.classList.add("is-preload");

  if (isDesktop() && readSavedCollapsed()) {
    container.classList.add("is-sidebar-collapsed");
  }

  syncState();

  window.requestAnimationFrame(function () {
    window.requestAnimationFrame(function () {
      container.classList.remove("is-preload");
    });
  });
})();