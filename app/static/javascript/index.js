//navbar

const navEl = document.querySelector('navbar');
window.addEventListener('scroll', function(){
    if(window.scrolly>56){
        navEl.classList.add('navbar-scrolled');
    } else if(window.scrolly<56){
        navEl.classList.remove('navbar-scrolled');
    }
})
