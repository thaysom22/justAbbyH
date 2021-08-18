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
        color: '#061234',
        fontFamily: 'serif',
        fontSize: '16px',
        '::placeholder': {
            color: '#6c757d'
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


/****** UI HELPERS ******/

// country select widget UI
$(document).ready(() => {
    $('select#id_country option[selected]').prop('disabled', true);
})

$('select#id_country').on("change", function(event) {
    $(this).css("color", "#061234");
    $(this).off(event);  // handler only runs once
});

// handle realtime validation feedback on the card element
card.addEventListener('change', function(event) {
    var errorDiv = document.getElementById('card-errors');
    var html;
    if (event.error) {
        html = `
            <span class="icon card-error" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span class="card-error">${event.error.message}</span>
        `;
        document.getElementById('submit-button').disabled = true;
    } else if (event.complete) {
        html = `
            <span class="icon card-info" role="alert">
                <i class="fas fa-info"></i>
            </span>
            <span class="card-info">Your card will be charged $${document.getElementById('id_subscription_cost').text}</span>
        `;
        document.getElementById('submit-button').disabled = false;
    } else {
        html = '';
        document.getElementById('submit-button').disabled = true;
    }
    errorDiv.innerHTML = html;
});


// UI feedback for unsuccessful payment
function showError(errorMsgText) {
    var errorDiv = document.getElementById("card-errors");
    var html = `
        <span class="icon card-error" role="alert">
            <i class="fas fa-times"></i>
        </span>
        <span class="card-error">${errorMsgText}</span>
    `;
    errorDiv.innerHTML = html;
};


function awaitingResult(isLoading, payment) {
    /**
     * enable/disable UI on subscription page while Stripe attempts payment.
     * display overlay, disable button and card element.
     * @param {Boolean} isLoading - flag to enable or disable.
     */
    if (payment) {
        if (isLoading) {
            document.getElementById('submit-button').disabled = true;
            card.update({
                'disabled': true
            });
            $("#loading-overlay").removeClass("hidden");
            $(".subscribe-navbar,.subscribe-text-wrapper,.subscribe-form-wrapper").addClass("hidden"); 
        } else {
            document.getElementById('submit-button').disabled = false;
            card.update({
                'disabled': false
            });
            $("#loading-overlay").addClass("hidden");
            $(".subscribe-navbar,.subscribe-text-wrapper,.subscribe-form-wrapper").removeClass("hidden");
        }
    } else {
        if (isLoading) {
            $('fieldset').find('input').prop('readonly', true);
            document.getElementById('submit-button').disabled = true;
            card.update({
                'disabled': true
            });
        } else {
            $('fieldset').find('input').prop('readonly', false);
            document.getElementById('submit-button').disabled = false;
            card.update({
                'disabled': false
            });
        }
    }

    
};


/****** PAYMENT PROCESS ******/

// handle subscription form submit event using Ajax
var form = document.getElementById("subscribe-form");
form.addEventListener("submit", function (event) {
    event.preventDefault();
    awaitingResult(true, false);  // disable form
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

        function createInactiveUserAjaxFailure(xhr) {

            displayFormErrors(xhr); // add form error messages returned in response data to DOM
            awaitingResult(false, false);  // renable form

            function displayFormErrors(xhr) {
                var formErrors = xhr.responseJSON.errors;
                for (const [fieldName, errorsArray] of Object.entries(formErrors)) {
                    $('.help-error').remove();  // remove error messages from previous submit attempts
                    errorsArray.forEach((errorMsg, index) => {
                        $(`#id_${fieldName}`).parent().append(
                            `<p id="error_${index+1}_id_${fieldName}" class="help-block help-error"><strong>${errorMsg}</strong></p>`
                        );
                    });
                }
            }
        };

        function createInactiveUserAjaxSuccess(data) {
            /* ATTEMPT PAYMENT */
            awaitingResult(false, false);
            awaitingResult(true, true);
            processPayment();

            function processPayment() {
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
                        // createInactiveUser succeeded so inactive user exists in db
                        showError(result.error.message); // update UI feedback for failed payment
                        confirmDeletionOfInactiveUser(data.inactiveUserId);
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
                    var usernameEncoded = encodeURIComponent(formData.username);
                    var redirectUrlQueryString = `?first_name=${firstNameEncoded}&last_name=${lastNameEncoded}&email=${emailEncoded}&username=${usernameEncoded}`;
                    var redirectUrl = data.redirectUrlPath + redirectUrlQueryString;
                    // inactive user in database will be activated via webhook handler
                    window.location.replace(redirectUrl);
                }

                function confirmDeletionOfInactiveUser(inactiveUserId) {
                    // send ajax post request to '/confirm-deletion-of-inactive-user/' url
                    $.ajax({
                        url: '/subscribe/confirm-deletion-of-inactive-user/',
                        method: 'POST',
                        data: getConfirmDeletionOfInactiveUserData(inactiveUserId),
                        success: confirmDeletionOfInactiveUserAjaxSuccess,
                        error: confirmDeletionOfInactiveUserAjaxFailure,
                    });
                };

                function confirmDeletionOfInactiveUserAjaxSuccess() {
                    // confirmed inactive user not in DB 
                    awaitingResult(false, true);; // re-enable UI so user can reattempt payment
                }

                function confirmDeletionOfInactiveUserAjaxFailure() {
                    // could not confirm deletion of inactive user from database...
                    // reload page to allow time for webhook handler to confirm delete.
                    // error message from server will be in django messages.
                    window.location.reload();
                }

                function getConfirmDeletionOfInactiveUserData(inactiveUserId) {
                    /**
                     * serialize data required for post request
                     * @param {int} id for inactive user in DB (from createInactiveUser response)
                     * @return {object} object containing data for post request body
                     */
                    var subscribeForm = document.getElementById('subscribe-form');
                    // include {% csrf_token %} in the subscribe form
                    var csrfToken = subscribeForm.querySelector(
                        'input[name="csrfmiddlewaretoken"]').value;
                    var postData = {
                        'csrfmiddlewaretoken': csrfToken,
                        'inactive_user_id': inactiveUserId,
                    };
                    return postData;
                };
            };
        };
    };
});

