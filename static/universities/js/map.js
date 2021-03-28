const institution = JSON.parse(document.getElementById('institution').textContent);
console.log(institution.longitude.replace(/[^0-9$.,-]/g, ''))

const institutionMap = L.map('institution-map').setView([ institution.latitude.replace(/[^0-9$.,-]/g, ''),
    institution.longitude.replace(/[^0-9$.,-]/g, '') ], 13);
const attribution = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors';
const tileURL = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'
const tiles = L.tileLayer(tileURL, {attribution});
const marker = L.marker([ institution.latitude.replace(/[^0-9$.,-]/g, ''),
    institution.longitude.replace(/[^0-9$.,-]/g, '') ]).addTo(institutionMap);

tiles.addTo(institutionMap)
marker.bindPopup("<b>" + institution.instname.replace(/\&.*/,'') + "</b>").openPopup();

// New Design Code
let open = document.getElementById('hamburger');
let mainContent = document.getElementById('detail-page-content');
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