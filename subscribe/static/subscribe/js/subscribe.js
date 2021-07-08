"use strict";

/* CREDIT: client js logic below extended from Stripe custom payment flow:
 https://stripe.com/docs/payments/integration-builder */


/****** SETUP ******/

// get required keys from template variables
var stripePublicKey = document.getElementById('id_stripe_public_key').text.slice(1, -1);
var clientSecret = document.getElementById('id_client_secret').text.slice(1, -1);

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
var card = elements.create('card', {
    style: style
});
card.mount('#card-element');


/****** PAYMENT PROCESS ******/

// handle subscription form submit event using Ajax
var form = document.getElementById("subscribe-form");
form.addEventListener("submit", function (event) {
    event.preventDefault();
    awaitingPaymentResult(true);
    createInactiveUser();

    function createInactiveUser() {
        // send ajax post request to 'create-inactive-user/' url
        // credit[6]
        var formData = getCreateInactiveUserData(); // store form data in scope accessible to paymentSuccess callback
        
        $.ajax({
            url: '/subscribe/create-inactive-user/', // prepend '/' to make route relative to host
            method: 'POST',
            data: formData,
            dataType: "json", // data returned from server parsed to JS object
            success: createInactiveUserAjaxSuccess,
            error: createInactiveUserAjaxFailure,
        });

        console.log("ajax call to create-inactive-user was made");  // TEST

        function getCreateInactiveUserData() {
            /**
             * gather data required for post request to create-inactive-user 
             * endpoint to create inactive user in database prior to attempting payment
             * @return {object} object containing data for post request body
             */
            var subscribeForm = document.getElementById('subscribe-form');
            // using {% csrf_token %} in the subscribe form
            var csrfToken = subscribeForm.querySelector('input[name="csrfmiddlewaretoken"]').value;
            var countrySelectElem = subscribeForm.querySelector('#id_country');
            var postData = {
                'csrfmiddlewaretoken': csrfToken,
                // used in subscription_created view
                'country_verbose': countrySelectElem.options[countrySelectElem.selectedIndex].text,
                // User Model data
                'username': subscribeForm.querySelector('input[name="username"]').value,
                'first_name': subscribeForm.querySelector('input[name="first_name"]').value,
                'last_name': subscribeForm.querySelector('input[name="last_name"]').value,
                'email': subscribeForm.querySelector('input[name="email"]').value,
                'password1': subscribeForm.querySelector('input[name="password1"]').value,
                'password2': subscribeForm.querySelector('input[name="password2"]').value,
                // Subscription Model data
                'country': countrySelectElem.value,
                'city': subscribeForm.querySelector('input[name="city"]').value,
                'client_secret': clientSecret, // from global vars
            };
            return postData;
        }

        function createInactiveUserAjaxFailure() {
            // error message will be in django messages
            window.location.reload();
        };

        function createInactiveUserAjaxSuccess(data) {
            var userId = data.userId; // required by deleteInactiveUser function
            /* ATTEMPT PAYMENT */
            processPayment();

            function processPayment () {
                // if card requires authentication Stripe shows a pop-up modal
                stripe.confirmCardPayment(
                    clientSecret, {
                        payment_method: {
                            card: card,
                        },
                    },
                ).then(function (result) {
                    if (result.error) {
                        /* PAYMENT FAILED */
                        deleteInactiveUser();
                    } else {
                        /* PAYMENT SUCCEEDED */
                        paymentSuccess();
                    }
                });

                function paymentSuccess() {
                    // construct url (relative to host) for redirect
                    var firstNameEncoded = encodeURIComponent(formData.first_name);  // encode url params credit[7]
                    var lastNameEncoded = encodeURIComponent(formData.last_name);
                    var emailEncoded = encodeURIComponent(formData.email);
                    var cityEncoded = encodeURIComponent(formData.city);
                    var countryVerboseEncoded = encodeURIComponent(formData.country_verbose);
                    var redirectUrlQueryString = `?first_name=${firstNameEncoded}&last_name=${lastNameEncoded}&email=${emailEncoded}&city=${cityEncoded}&country_verbose=${countryVerboseEncoded}`;
                    var redirectUrl = data.redirectUrlPath + redirectUrlQueryString;
                    // inactive user in database will be activated by webhook handler
                    window.location.replace(redirectUrl);
                }

                function deleteInactiveUser() {
                    // send ajax post request to '/delete-inactive-user/' url
                    // to delete the inactive user instance just created
                    $.ajax({
                        url: '/subscribe/delete-inactive-user/',
                        method: 'POST',
                        data: getDeleteInactiveUserData(),
                        success: deleteInactiveUserAjaxSuccess,
                        error: deleteInactiveUserAjaxFailure,
                    });

                    console.log("ajax call to delete-inactive-user was made");  // TEST

                };

                function deleteInactiveUserAjaxSuccess() {
                    showError(result.error.message); // show feedback for failed payment
                    awaitingPaymentResult(false); // re-enable UI so user can reattempt payment
                }

                function deleteInactiveUserAjaxFailure() {
                    // delete failed and inactive user remains in database 
                    // so reload to allow webhook handler to attempt delete
                    // error message from server will be in django messages
                    window.location.reload();
                }

                function getDeleteInactiveUserData() {
                    /**
                     * gather data required for post request to delete-inactive-user 
                     * @return {object} object containing data for post request body
                     */
                    var subscribeForm = document.getElementById('subscribe-form');
                    // using {% csrf_token %} in the subscribe form
                    var csrfToken = subscribeForm.querySelector(
                        'input[name="csrfmiddlewaretoken"]').value;
                    var postData = {
                        'csrfmiddlewaretoken': csrfToken,
                        'user_id': userId,
                    };
                    return postData;
                };
            };
        };
    };
});


/****** UI HELPERS ******/

// handle realtime validation errors on the card element
card.addEventListener('change', function(event) {
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
        document.getElementById('submit-button').disabled = event.empty; // will enable if not error and not empty
    }
});


// UI feedback for unsuccessful payment
function showError(errorMsgText) {
    var errorDiv = document.getElementById("card-errors");
    var html = `
        <span class="icon" role="alert">
            <i class="fas fa-times"></i>
        </span>
        <span>${errorMsgText}</span>
    `;
    errorDiv.innerHTML = html;
};


function awaitingPaymentResult(isLoading) {
    /**
     * enable/disable UI on subscription page while Stripe attempts payment.
     * display overlay, disable button and card element.
     * @param {Boolean} isLoading - flag to enable or disable.
     */
    if (isLoading) {
        document.getElementById('submit-button').disabled = true;
        card.update({
            'disabled': true
        });
        document.getElementById("spinner").classList.remove("hidden");
        document.getElementById("button-text").classList.add("hidden");
        document.getElementById("loading-overlay").classList.remove("hidden");
    } else {
        card.update({
            'disabled': false
        });
        document.getElementById("spinner").classList.add("hidden");
        document.getElementById("button-text").classList.remove("hidden");
        document.getElementById("loading-overlay").classList.add("hidden");
    }
};