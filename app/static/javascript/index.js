//navbar
console.log("Test")
const navEl = document.querySelector('.navbar');
window.addEventListener('scroll', function () {
    // Metoda me Y te madhe
    if (window.scrollY > 60) {
        navEl.classList.add('navbar-scrolled');
    } else {
        navEl.classList.remove('navbar-scrolled');
    }
})

