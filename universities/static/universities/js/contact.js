// Contact Page information
const sendEmail = document.getElementById('contact');
const emailRecipient = 'seniordesign908@gmail.com'
const emailSender = document.getElementById('emailInput');
const emailContent = document.getElementById('messageContent');
const contactPageSendEmail = document.getElementById('contact-page');


sendEmail.addEventListener('click', function () {

    let mailto_link = 'mailto:' + emailRecipient;

    window = window.open(mailto_link, 'emailWindow');
    if (window && window.open && !window.closed) {
        window.close();
    }
});


// New Design Code
let open = document.getElementById('hamburger');
let mainContent = document.getElementById('home-page-content');
let changeIcon = true;
let windowSize = window.innerWidth

open.addEventListener("click", function () {

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
    } else {
        icon.classList.remove("fa-times");
        icon.classList.add("fa-bars");
        mainContent.classList.remove("d-none");
        changeIcon = true;
    }
});