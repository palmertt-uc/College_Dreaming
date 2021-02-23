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