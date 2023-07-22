// Window on load
window.onload = function () {

    // Add event listener to the form
    document.querySelector('city-submit').addEventListener('submit', function (event) {
        event.preventDefault();

        // Get the city name from the form
        let city = document.getElementById('city').value;

        // Send a POST request
        fetch('/add', {
            method: 'POST',
            body: JSON.stringify({ city: city }),
            headers: {
                'Content-Type': 'application/json',
            },
        })
            .then((response) => response.json())
            .then((data) => {
                if (data.success) {
                    console.log(`City: ${data.city} was added successfully.`);
                    createCard();
                } else {
                    console.error(data.message);
                }
            })
            .catch((error) => {
                console.error(`Error: ${error}`);
            });
    });

    // Function to Add a new city card
    function createCard() {
        // Grab the cards div and create a new card
        let cardsDiv = document.getElementById('cards');
        let newCard = document.createElement('div');
        newCard.className = 'card evening-morning';

        // Fill the card with the city data inside the template literal
        newCard.innerHTML = `
            <div class="card evening-morning">
            <div class="delete-wrapper">
                <form action="{{ url_for('delete_city', city_id=city.id) }}" method="POST" class="delete-form">
                    <input type="hidden" name="delete" value="">
                    <button class="delete-button" type="submit" id="delete-button">&#10006;</button>
                </form>
            </div>
            <div class="degrees"><span>{{ city.temp }}<span class="celsius"> °C</span></span></div>
            <div class="state">{{ city.state }}</div>
            <div class="empty"></div>
            <div class="city">{{ city.city|title }}</div>
        </div>
        `;

        // Append the new card to the cards div
        cardsDiv.appendChild(newCard);
    }

    // Add delete button event listeners
    document.querySelector('cards').addEventListener('click', function (event) {
        if (event.target.classList.contains('delete-button')) {
            event.preventDefault();

            // Get the parent card element of the clicked delete button
            const card = event.target.closest('.card');

            // Get the city id from the data attribute of the card
            let cityId = card.dataset.cityId;

            // Send a DELETE request
            fetch(`/delete/${cityId}`, {
                method: 'DELETE',
            })
                .then((response) => response.json())
                .then((data) => {
                    if (data.success) {
                        console.log(`City: ${data.city} was deleted successfully.`);
                        // Remove the card from the DOM
                        card.remove();
                    } else {
                        console.error(data.message);
                    }
                })
                .catch((error) => {
                    console.error(`Error: ${error}`);
                });
        }
    });
};
