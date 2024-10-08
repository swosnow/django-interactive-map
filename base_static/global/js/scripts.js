var map = L.map('map').setView([-22.587086, -43.011987], 13);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

var circle = L.circle([-22.587086, -43.011987], {
    color: 'red',
    fillColor: '#f03',
    fillOpacity: 0.5,
    radius: 500
}).addTo(map);

map.on('click', (event) => {
    L.marker([event.latlng.lat, event.latlng.lng]).addTo(map)
})