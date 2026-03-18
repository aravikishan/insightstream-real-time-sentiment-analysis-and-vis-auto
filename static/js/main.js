// main.js

document.addEventListener('DOMContentLoaded', function() {
    const navLinks = document.querySelectorAll('.nav-link');
    const currentLocation = location.pathname;

    navLinks.forEach(link => {
        if(link.getAttribute('href') === currentLocation) {
            link.classList.add('active');
        }
    });

    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', function(event) {
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const message = document.getElementById('message').value;

            if (!name || !email || !message) {
                event.preventDefault();
                alert('Please fill in all fields.');
            }
        });
    }

    // Smooth scrolling for anchor links
    const smoothScroll = function(targetEl, duration) {
        const target = document.querySelector(targetEl);
        const targetPosition = target.getBoundingClientRect().top;
        const startPosition = window.pageYOffset;
        const startTime = null;

        const ease = function(t, b, c, d) {
            t /= d / 2;
            if (t < 1) return c / 2 * t * t + b;
            t--;
            return -c / 2 * (t * (t - 2) - 1) + b;
        };

        const animation = function(currentTime) {
            if (startTime === null) startTime = currentTime;
            const timeElapsed = currentTime - startTime;
            const run = ease(timeElapsed, startPosition, targetPosition, duration);
            window.scrollTo(0, run);
            if (timeElapsed < duration) requestAnimationFrame(animation);
        };
        requestAnimationFrame(animation);
    };

    const scrollTo = function() {
        const links = document.querySelectorAll('.nav-link');
        links.forEach(each => {
            each.addEventListener('click', function() {
                const currentTarget = this.getAttribute('href');
                smoothScroll(currentTarget, 1000);
            });
        });
    };
    scrollTo();
});