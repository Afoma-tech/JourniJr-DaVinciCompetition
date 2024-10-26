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

        // Five doctors with random nearby coordinates
        const doctors = [
            {
                id: 1,
                name: "Dr. Ishfaq M.",
                specialization: "Family Physician",
                languages: ["English", "Swedish"],
                distance: "Approx. 4.6 mi",
                price: "$51",
                coords: getRandomCoordinates(userCoords, 0.05),
            },
            {
                id: 2,
                name: "Dr. Brian L.",
                specialization: "Dermatologist",
                languages: ["Swedish"],
                distance: "Approx. 3.2 mi",
                price: "$47",
                coords: getRandomCoordinates(userCoords, 0.05),
            },
            {
                id: 3,
                name: "Dr. Edmond S.",
                specialization: "Pediatrician",
                languages: ["Swedish", "English", "Japanese"],
                distance: "Approx. 4.1 mi",
                price: "$48",
                coords: getRandomCoordinates(userCoords, 0.05),
            },
            {
                id: 4,
                name: "Dr. Steve H.",
                specialization: "Dentist",
                languages: ["Swedish", "Korean"],
                distance: "Approx. 6.6 mi",
                price: "$43",
                coords: getRandomCoordinates(userCoords, 0.05),
            },
            {
                id: 5,
                name: "Dr. Sarah L.",
                specialization: "Eye Doctor",
                languages: ["Swedish", "Portuguese"],
                distance: "Approx. 2.0 mi",
                price: "$53",
                coords: getRandomCoordinates(userCoords, 0.05),
            }
        ];

        // Add markers for each doctor
        doctors.forEach(doctor => {
            const marker = L.marker(doctor.coords).addTo(map);
            marker.bindPopup(`<b>${doctor.name}</b><br>${doctor.specialization}`);
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
        const lat = center[0] + (Math.random() * range * 2 - range);
        const lng = center[1] + (Math.random() * range * 2 - range);
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
