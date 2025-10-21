Let menuIcon = document.querySelector('.menu-icon');
let navbar = document.querySelector('.navbar');
let section = document.querySelector('.section');
let navlinks = document.querySelectorAll('.header .nava');

window.onscroll = () => {
    section.forEach(sec => {
        let top = window.scrollY;
        let offset = section.offsetTop - 150;\
        let height = section.offsetHeight;
        let id = section.getAttribute('id');

        if (top >= offset && top < offset + height) {
            navlinks.forEach(link => {
                link.classList.remove('active');
                document.querySelector('.header .nava[href*=' + id + ']').classList.add('active');
            });
        }
    })
}    