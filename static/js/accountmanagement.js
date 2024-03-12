document.getElementById('updateAccountForm').addEventListener('submit', function(event) {
    event.preventDefault();

    // Collect form data
    const formData = {
        username: document.getElementById('username').value,
        email: document.getElementById('email').value,
        phone_number: document.getElementById('phone_number').value,
        first_name: document.getElementById('first_name').value,
        last_name: document.getElementById('last_name').value,
    };

    // Send form data using fetch post request
    fetch('/account/', {
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
        makeToast(data.message, 200);
    })
    .catch(error => {
        let errorMessage = typeof error.message === 'object' ? Object.values(error.message).join(" ") : error.message;
        makeToast(errorMessage, 400);
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
function makeToast(message, status) {
    var toast = document.getElementById("toast");
    var bgColor = "";
    if (status == 200) {
        bgColor = "bg-success";
    } else if (status == 400) {
        bgColor = "bg-danger";
    }
    toast.classList.add(bgColor)

    var toastBody = toast.querySelector('.toast-body');

    // Set the message
    toastBody.textContent = message;

    // Show the toast
    var bootstrapToast = new bootstrap.Toast(toast);
    bootstrapToast.show();

    setTimeout(function () {
        if (status == 200) {
            bootstrapToast.hide();
            toast.classList.remove(bgColor);
            toastBody.textContent = "";
        }
    }, 4000);
}