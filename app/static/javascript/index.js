//navbar
console.log("Test")
const navEl = document.querySelector('.navbar');
window.addEventListener('scroll', function () {
    // Metoda me Y te madhe
    if (window.scrollY > 56) {
        navEl.classList.add('navbar-scrolled');
    } else if (window.scrollY < 56) {
        navEl.classList.remove('navbar-scrolled');
    }
})

