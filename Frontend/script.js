// Wait until the HTML document is fully parsed and loaded
document.addEventListener("DOMContentLoaded", function () {

    // ==========================================
    // 1. SELECTING CORE SCREENS & ELEMENTS
    // ==========================================
    const loginScreen = document.getElementById("login-screen");
    const dashboardScreen = document.getElementById("dashboard-screen");
    const loginForm = document.getElementById("login-form");
    const logoutBtn = document.getElementById("btn-logout");

    // ==========================================
    // 2. APP SCREEN SWITCHING LOGIC (SPA FLOW)
    // ==========================================
    
    // Handle Login Form Submission
    if (loginForm) {
        loginForm.addEventListener("submit", function (e) {
            e.preventDefault(); // Prevent standard page reloads

            // Smoothly switch views using the helper .d-none visibility class
            loginScreen.classList.add("d-none");
            dashboardScreen.classList.remove("d-none");
            
            // Adjust body view structure dynamically for dashboard view context
            document.body.style.backgroundColor = "#f8fafc"; 
        });
    }

    // Handle Logout System Actions
    if (logoutBtn) {
        logoutBtn.addEventListener("click", function (e) {
            e.preventDefault(); // Stay inside the SPA environment

            // Return cleanly back into initial login prompt structures
            dashboardScreen.classList.add("d-none");
            loginScreen.classList.remove("d-none");
            
            // Revert basic wrapper styling variables back into standard themes
            document.body.style.backgroundColor = "#f1f5f9";
            
            // Reset fields inside login forms upon explicit account logout operations
            if (loginForm) loginForm.reset();
        });
    }

    // ==========================================
    // 3. SECURE PASSWORD VISIBILITY TOGGLE
    // ==========================================
    const passwordInput = document.getElementById("login-password");
    const togglePassword = document.querySelector(".toggle-password");

    if (togglePassword && passwordInput) {
        togglePassword.addEventListener("click", function () {
            // Check state conditions and translate input formats smoothly
            const isPassword = passwordInput.getAttribute("type") === "password";
            passwordInput.setAttribute("type", isPassword ? "text" : "password");
            
            // Alter font-awesome vector class arrays based on visibility updates
            this.classList.toggle("fa-eye");
            this.classList.toggle("fa-eye-slash");
        });
    }

    // ==========================================
    // 4. SIDEBAR MENU SELECTION ACTIONS
    // ==========================================
    const menuLinks = document.querySelectorAll(".sidebar-menu a");

    menuLinks.forEach(link => {
        link.addEventListener("click", function (e) {
            e.preventDefault(); // Block empty routing issues
            
            // Clear current structural selection layers across other options
            menuLinks.forEach(item => item.classList.remove("active"));
            
            // Highlight current dynamic menu target instantly
            this.classList.add("active");
        });
    });

    // ==========================================
    // 5. NOTIFICATION ALERTS DISMISSALS
    // ==========================================
    const notification = document.querySelector(".notification-icon");
    if (notification) {
        notification.addEventListener("click", function () {
            alert("You have 3 new unread system updates!");
            const badge = this.querySelector(".badge");
            if (badge) badge.style.display = "none"; // Conceal dynamic counters upon click actions
        });
    }
});