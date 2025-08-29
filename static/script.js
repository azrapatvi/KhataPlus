// Smooth scrolling
function scrollTo(target) {
    const element = document.querySelector(target);
    if (element) {
        const offsetTop = element.offsetTop - 80;
        window.scrollTo({
            top: offsetTop,
            behavior: 'smooth'
        });
    }
}

// Smooth scroll for all anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        scrollTo(this.getAttribute('href'));
    });
});

// Theme toggle
// Theme toggle
function toggleTheme() {
    const body = document.body;
    const icon = document.querySelector('#themeToggle i');

    if (body.getAttribute('data-theme') === 'dark') {
        // Switch to light
        body.removeAttribute('data-theme');
        icon.className = 'bi bi-moon';
        localStorage.setItem('theme', 'light');
    } else {
        // Switch to dark
        body.setAttribute('data-theme', 'dark');
        icon.className = 'bi bi-sun';
        localStorage.setItem('theme', 'dark');
    }
}


// Load saved theme
document.addEventListener('DOMContentLoaded', function () {
    const savedTheme = localStorage.getItem('theme');
    const icon = document.querySelector('#themeToggle i');

    if (savedTheme === 'dark') {
        document.body.setAttribute('data-theme', 'dark');
        icon.className = 'bi bi-sun';
    }
});

// Close mobile menu on link click
document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', () => {
        const collapse = document.querySelector('.navbar-collapse');
        if (collapse.classList.contains('show')) {
            new bootstrap.Collapse(collapse).hide();
        }
    });
});


