// New Design Code
let open = document.getElementById('hamburger');
let mainContent = document.querySelector('.users-modal');
let changeIcon = true;
let windowSize = window.innerWidth

open.addEventListener("click", function(){

    let overlay = document.querySelector('.overlay');
    let nav = document.querySelector('nav');
    let icon = document.querySelector('.menu-toggle i');

    overlay.classList.toggle("menu-open");
    nav.classList.toggle("menu-open");
    mainContent.classList.add("d-none");

    if (windowSize > 800) {
        mainContent.classList.remove("d-none");
    }

    if (changeIcon) {
        icon.classList.remove("fa-bars");
        icon.classList.add("fa-times");

        changeIcon = false;
    }
    else {
        icon.classList.remove("fa-times");
        icon.classList.add("fa-bars");
        mainContent.classList.remove("d-none");
        changeIcon = true;
    }
});

