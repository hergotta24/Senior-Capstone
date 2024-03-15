let imagesArray = []
let imgNum = 0;
let max = 1;

let slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
    showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
    showSlides(slideIndex = n);
}

function addImage() {
    imgNum++
    if (imgNum === 6) {
        max = 0;
        $('#addSlide').remove()
        $('#addDemo').remove()
    }
    let newImage = document.getElementById('imageInput').files[0];
    imagesArray.push(newImage);
    let imageURL = URL.createObjectURL(newImage);
    let img = $('<img src="" alt="image" style="object-fit: contain">');
    img.attr('src', imageURL);
    let newSlide = $('<div class="mySlides d-flex w-100 h-100 justify-content-center" style="max-height: inherit"></div>');
    let div = $('<div class="numbertext" style="left:0"><span class="slideNum"></span> / <span class="slideSize"></span></div>')
    div.children('.slideNum').text(imgNum)
    div.children('.slideSize').text(imagesArray.length + max)
    newSlide.append(div)
    newSlide.append(img)

    $('#slideContainer').prepend(newSlide)
    newSlide.addClass("d-none")
    $('.slideSize').each(function () {
        $(this).text(imagesArray.length + max)
    })
    slideIndex = 1;

    let newDemo = $('<div class="col-auto position-relative my-auto" style="max-height: inherit;min-width: 16.6%;max-width: 16.6%">\n' +
        '                                <img class="demo cursor" src="" style="max-height: inherit; width:100%; object-fit: scale-down"\n' +
        '                                     onclick="currentSlide(1)" alt="image">\n' +
        '                            </div>')
    newDemo.children(".demo").attr('src', imageURL)
    $('#demoContainer').prepend(newDemo)

    document.getElementById('imageInput').value = ''


    showSlides(slideIndex)
}


function showSlides(n) {
    console.log("it's working")
    let slides = document.getElementsByClassName("mySlides");
    //let dots = document.getElementsByClassName("demo");
    //let captionText = document.getElementById("caption");
    if (n > slides.length) {
        slideIndex = 1
    }
    if (n < 1) {
        slideIndex = slides.length
    }
    let count = 1
    $('.mySlides').each(function () {
        $(this).addClass("d-none")
        $(this).children(".numbertext").children(".slideNum").text(count)
        console.log(count)
        count++
    })

    count = 1
    $('.demo').each(function () {
        $(this).attr('onclick', "currentSlide(" + count + ")")
        count++
    })
    /*for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }*/
    slides[slideIndex - 1].classList.remove("d-none")
    //dots[slideIndex - 1].className += " active";
    //captionText.innerHTML = dots[slideIndex - 1].alt;
}


$(document).ready(function () {
    $('#create-product').on('click', function (event) {
        event.preventDefault();

        // Retrieve form data
        const productName = $('#product-name').val();
        const productPrice = $('#product-price').val();
        const productQOH = $('#product-qoh').val();
        const productDescription = $('#product-description').text();

        const formData = {
            name: productName,
            price: productPrice,
            qoh: productQOH,
            description: productDescription,


        }
        let url = window.location.pathname

        // Send form data using fetch post request
        fetch('/productcreation/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken') // Function to get CSRF token
            },
            body: JSON.stringify(formData)
        })
            .then(response => {
                if (response.ok) {
                    console.log("Product Created");
                    return response.json();
                } else {
                    return response.json().then(data => Promise.reject(data));
                }
            })
            .then(data => {
                makeToast(data.message, 200);
                setTimeout(function () {
                    window.location.href = "/storefront";
                }, 4000); // 3000 milliseconds = 3 seconds
            })
            .catch(error => {
                console.error('Error:', error);
                let errorMessage = typeof error.message === 'object' ? Object.values(error.message).join(" ") : error.message;
                makeToast(errorMessage, 400);
            });
    })
})

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
    let toast = document.getElementById("toast");
    let bgColor = "";
    if (status === 200) {
        bgColor = "bg-success";
    } else if (status === 400) {
        bgColor = "bg-danger";
    }
    toast.classList.add(bgColor)

    let toastBody = toast.querySelector('.toast-body');

    // Set the message
    toastBody.textContent = message;

    // Show the toast
    let bootstrapToast = new bootstrap.Toast(toast);
    bootstrapToast.show();

    setTimeout(function () {
        if (status === 200) {
            bootstrapToast.hide();
            toast.classList.remove(bgColor);
            toastBody.textContent = "";
        }
    }, 4000);
}