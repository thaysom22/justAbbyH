/* CREDIT: client js logic below based on: https://stripe.com/docs/payments/integration-builder */


/****** SETUP ******/  

// get required keys from template variables
var stripePublicKey = document.getElementById('id_stripe_public_key').text.slice(1,-1);
var clientSecret = document.getElementById('id_client_secret').text.slice(1,-1);

// create Stripe instance with public key and create Elements instance
var stripe = Stripe(stripePublicKey);  
var elements = stripe.elements();

// styles for card element
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

 // create stripe UI element and mount to subscribe form
var card = elements.create('card', {style: style});
card.mount('#card-element');


/****** DELAY FORM SUBMIT TO COMPLETE PAYMENT ON CLIENT ******/

// handle subscription form submit event
var form = document.getElementById("subscribe-form");
form.addEventListener("submit", function(event) {
    event.preventDefault();
    awaitingPaymentResult(true);
    // send ajax post request to cache inactive user endpoint
    // credit[6]
    $.ajax({
        url: '/subscribe/cache-inactive-user/',
        method: 'POST',
        data: getCacheUserData(),
        dataType: "json",  // data from server parsed to JS object
        timeout: 500,
        success: ajaxSuccess,
        error: ajaxFailure,
    });    
});

var ajaxSuccess = function(data) {
    
}

var ajaxFailure = function() {
    // if not timeout, error will be in django messages
    location.reload();
}

var getCacheUserData = function() {
    /**
     * gather data required for post request to cache-inactive-user 
     * endpoint to create inactive user in database prior to attempting payment
     * @return {object} object containing data for post request
     */
    var subscribeForm = document.getElementById('subscribe-form');
    // using {% csrf_token %} in the subscribe form
    var csrfToken = subscribeForm.querySelector('input[name="csrfmiddlewaretoken"]').value;
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'username': subscribeForm.querySelector('input[name="username"]').value,
        'first_name': subscribeForm.querySelector('input[name="first_name"]').value,
        'last_name': subscribeForm.querySelector('input[name="last_name"]').value,
        'email': subscribeForm.querySelector('input[name="email"]').value,
        'password1': subscribeForm.querySelector('input[name="password1"]').value,
        'password2': subscribeForm.querySelector('input[name="password2"]').value,
    };
    return postData;
}


var createUserSubscription = function() {

    // If card requires authentication Stripe shows a pop-up modal
    stripe.confirmCardPayment(
        clientSecret, 
        {
            payment_method: {
                card: card,
            },
        },
    ).then(function(result) {
        if (result.error) {
            // Show error to your customer
            showError(result.error.message);
        } else {
            // The payment succeeded: post form data
            form.submit();  
        }
    });
};

// show the customer the error from Stripe if their card fails to charge
var showError = function(errorMsgText) {
    awaitingPaymentResult(false);
    var errorDiv = document.getElementById("card-errors");
    var html = `
        <span class="icon" role="alert">
            <i class="fas fa-times"></i>
        </span>
        <span>${errorMsgText}</span>
    `;
    errorDiv.innerHTML = html;
};


/****** UI HELPERS ******/

// handle realtime validation errors on the card element
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        errorDiv.innerHTML = html;
        document.getElementById('submit-button').disabled = true;
    } else {
        errorDiv.innerHTML = '';
        document.getElementById('submit-button').disabled = event.empty;  // will enable if not error and not empty
    }
});

// display overlay, disable button and card element on form submit
var awaitingPaymentResult = function(isLoading) {  
    if (isLoading) {
        document.getElementById('submit-button').disabled = true;
        card.update({ 'disabled': true });
        document.getElementById("spinner").classList.remove("hidden");
        document.getElementById("button-text").classList.add("hidden");
        document.getElementById("loading-overlay").classList.remove("hidden");
    } else {
        card.update({ 'disabled': false });
        document.getElementById("spinner").classList.add("hidden");
        document.getElementById("button-text").classList.remove("hidden");
        document.getElementById("loading-overlay").classList.add("hidden");
    }
};