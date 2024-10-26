function initMap() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(success, error);
    } else {
        alert("Geolocation is not supported by this browser.");
    }

    function success(position) {
        const userCoords = [position.coords.latitude, position.coords.longitude];
        const map = L.map('map').setView(userCoords, 12); // Center map on user location

        // Add OpenStreetMap tiles
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(map);

        // Doctor data with random coordinates
        const doctors = [
            {
                id: 1,
                name: "Dr. Ishfaq M.",
                specialization: "Family Physician",
                languages: ["English", "Swedish"],
                distance: "Approx. 4.6 mi",
                price: "$51",
                coords: getRandomCoordinates(userCoords, 0.05), // Generate random coordinates
            },
            {
                id: 2,
                name: "Dr. Brian L.",
                specialization: "Dermatologist",
                languages: ["Swedish"],
                distance: "Approx. 4.6 mi",
                price: "$47",
                coords: getRandomCoordinates(userCoords, 0.05), // Generate random coordinates
            }
        ];

        // Add markers for each doctor
        doctors.forEach(doctor => {
            const marker = L.marker(doctor.coords).addTo(map);
            marker.bindPopup(`<b>${doctor.name}</b><br>${doctor.specialization}`);
            // Listen for click events on marker to update details
            marker.on('click', () => {
                updateDetails(doctor);
            });
        });

        // Add a marker for the user's location
        L.marker(userCoords).addTo(map).bindPopup("You are here").openPopup();
    }

    function error() {
        alert("Unable to retrieve your location.");
    }

    function getRandomCoordinates(center, range) {
        const lat = center[0] + (Math.random() * range * 2 - range); // Random latitude
        const lng = center[1] + (Math.random() * range * 2 - range); // Random longitude
        return [lat, lng];
    }

    function updateDetails(doctor) {
        const detailsSection = document.getElementById("doctor-details");
        detailsSection.innerHTML = `
            <strong>${doctor.name}</strong><br>
            ${doctor.specialization}<br>
            Languages: ${doctor.languages.join(', ')}<br>
            Distance: ${doctor.distance}<br>
            Price: ${doctor.price}<br><br>
        `;
    }
}

// Initialize map on DOM content loaded
document.addEventListener('DOMContentLoaded', initMap);

function goBack() {
    window.history.back();
}
