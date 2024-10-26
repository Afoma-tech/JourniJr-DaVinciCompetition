function initMap() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(success, error);
    } else {
        alert("Geolocation is not supported by this browser.");
    }

    function success(position) {
        const userCoords = [position.coords.latitude, position.coords.longitude];
        const map = L.map('map').setView(userCoords, 12);

        // Add OpenStreetMap tiles
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(map);

        // Five restaurants with random nearby coordinates
        const restaurants = [
            {
                id: 1,
                name: "Stockholms Gästabud",
                cuisine: "Traditional Swedish",
                rating: "4.5 stars",
                price: "$$",
                coords: getRandomCoordinates(userCoords, 0.05),
            },
            {
                id: 2,
                name: "Lilla Ego",
                cuisine: "Italian",
                rating: "4.1 stars",
                price: "$$$",
                coords: getRandomCoordinates(userCoords, 0.05),
            },
            {
                id: 3,
                name: "Auberge Du Pommier",
                cuisine: "French",
                rating: "4.8 stars",
                price: "$$$$",
                coords: getRandomCoordinates(userCoords, 0.05),
            },
            {
                id: 4,
                name: "Mandarin Restaurant",
                cuisine: "Chinese",
                rating: "4.0 stars",
                price: "$",
                coords: getRandomCoordinates(userCoords, 0.05),
            },
            {
                id: 5,
                name: "Jacobs & Co. Steakhouse",
                cuisine: "Steakhouse",
                rating: "3.8 stars",
                price: "$$$$$",
                coords: getRandomCoordinates(userCoords, 0.05),
            }
        ];

        // Add markers for each restaurant
        restaurants.forEach(restaurant => {
            const marker = L.marker(restaurant.coords).addTo(map);
            marker.bindPopup(`<b>${restaurant.name}</b><br>${restaurant.cuisine}<br>Rating: ${restaurant.rating}`);
            marker.on('click', () => {
                updateDetails(restaurant);
            });
        });

        // Add a marker for the user's location
        L.marker(userCoords).addTo(map).bindPopup("You are here").openPopup();
    }

    function error() {
        alert("Unable to retrieve your location.");
    }

    function getRandomCoordinates(center, range) {
        const lat = center[0] + (Math.random() * range * 2 - range);
        const lng = center[1] + (Math.random() * range * 2 - range);
        return [lat, lng];
    }

    function updateDetails(restaurant) {
        const detailsSection = document.getElementById("restaurant-details");
        detailsSection.innerHTML = `
            <strong>${restaurant.name}</strong><br>
            Cuisine: ${restaurant.cuisine}<br>
            Rating: ${restaurant.rating}<br>
            Price: ${restaurant.price}<br><br>
        `;
    }
}

// Initialize map on DOM content loaded
document.addEventListener('DOMContentLoaded', initMap);

function goBack() {
    window.history.back();
}
