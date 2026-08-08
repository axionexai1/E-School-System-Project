/* ==========================================================================
   Sidebar toggle behavior
   Click the menu icon -> sidebar collapses to icon-only, dashboard content
   expands to take the freed space. Click again -> expands back.
   ========================================================================== */

document.addEventListener("DOMContentLoaded", function () {
  const sidebar = document.getElementById("sidebar");
  const menuToggle = document.getElementById("menu-toggle");

  if (!sidebar || !menuToggle) return;

  // Restore last state so it stays collapsed/expanded after page reload
  const savedState = localStorage.getItem("sidebarCollapsed");
  if (savedState === "true") {
    sidebar.classList.add("sidebar-collapsed");
    sidebar.classList.remove("sidebar-expanded");
  }

  menuToggle.addEventListener("click", function () {
    const isCollapsed = sidebar.classList.toggle("sidebar-collapsed");
    sidebar.classList.toggle("sidebar-expanded", !isCollapsed);

    // Remember choice for next visit
    localStorage.setItem("sidebarCollapsed", isCollapsed);

    // Accessibility: tell screen readers the menu state
    menuToggle.setAttribute("aria-expanded", String(!isCollapsed));
  });
});