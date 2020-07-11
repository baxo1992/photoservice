const navSlide = () => {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav');
    const main = document.querySelector('.main');
    const navLinks = document.querySelectorAll('.nav li');

    burger.addEventListener('click', () => {
        nav.classList.toggle('nav-active');
        main.classList.toggle('blurMe');

        navLinks.forEach((link, index) => {
            if (link.style.animation) {
                link.style.animation = '';
            } else {
                link.style.animation = `navLinkFade 0.5s ease forwards ${index /7 + 0}s`;
            }
        });

        burger.classList.toggle('toggle');
    });

    

}

navSlide()