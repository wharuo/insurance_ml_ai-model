// initMap.js
function initMap() {
    console.log("Initializing map...");  // Debugging log
    map = new google.maps.Map(document.getElementById('map'), {
        zoom: 4,
        center: {lat: 56.1304, lng: -106.3468}  // Centered on Canada
    });
    console.log("Map initialized:", map);  // Debugging log
}
