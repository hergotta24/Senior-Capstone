// register.js
document.getElementById('registrationForm').addEventListener('submit', function(event) {
    event.preventDefault();

    // Collect form data
    const formData = {
        username: this.elements.username.value,
        email: this.elements.email.value,
        password1: this.elements.password1.value,
        password2: this.elements.password2.value
    };

    // Send form data using fetch post request
    fetch('/register/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken') // Function to get CSRF token
        },
        body: JSON.stringify(formData)
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        } else {
            return response.json().then(data => Promise.reject(data));
        }
    })
    .then(data => {
        console.log(data.message);
        // Handle successful registration
    })
    .catch(error => {
        console.error('Error:', error);
        // Handle registration errors
    });
});

// Function to get CSRF token from cookie
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}