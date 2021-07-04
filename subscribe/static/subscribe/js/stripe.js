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


/****** PAYMENT PROCESS ******/

// handle subscription form submit event using Ajax
var form = document.getElementById("subscribe-form");
form.addEventListener("submit", function(event) {
    event.preventDefault();
    awaitingPaymentResult(true);
    createInactiveUser();

    var createInactiveUser = function() {
        // send ajax post request to 'create-inactive-user/' url
        // credit[6]
        $.ajax({
            url: '/subscribe/create-inactive-user/',  // prepend '/' to make route relative to host
            method: 'POST',
            data: getCreateInactiveUserData(),
            dataType: "json",  // data returned from server parsed to JS object
            timeout: 500,
            success: cacheUserAjaxSuccess,
            error: cacheUserAjaxFailure,
        });
        
        var getCreateInactiveUserData = function() {
            /**
             * gather data required for post request to create-inactive-user 
             * endpoint to create inactive user in database prior to attempting payment
             * @return {object} object containing data for post request
             */
            var subscribeForm = document.getElementById('subscribe-form');
            // using {% csrf_token %} in the subscribe form
            var csrfToken = subscribeForm.querySelector('input[name="csrfmiddlewaretoken"]').value;
            var postData = {
                'csrfmiddlewaretoken': csrfToken,
                // User Model data
                'username': subscribeForm.querySelector('input[name="username"]').value,
                'first_name': subscribeForm.querySelector('input[name="first_name"]').value,
                'last_name': subscribeForm.querySelector('input[name="last_name"]').value,
                'email': subscribeForm.querySelector('input[name="email"]').value,
                'password1': subscribeForm.querySelector('input[name="password1"]').value,
                'password2': subscribeForm.querySelector('input[name="password2"]').value,
                // Subscription Model data
                'country': subscribeForm.querySelector('input[name="country"]').value,
                'city': subscribeForm.querySelector('input[name="city"]').value,
                'client_secret': clientSecret,  // from global vars
            };
            return postData;
        }

        var cacheUserAjaxFailure = function() {
            // if not timeout, error message from server 
            // will be shown in django messages
            window.location.reload();
        };

        var cacheUserAjaxSuccess = function(data) {
            var userId = data.userId;  // used to activate or delete cached user
            processPayment();
            
            var processPayment = function() {
                // if card requires authentication Stripe shows a pop-up modal
                stripe.confirmCardPayment(
                    clientSecret, 
                    {
                        payment_method: {
                            card: card,
                        },
                    },
                ).then(function(result) {
                    if (result.error) {
                        // show error to customer
                        showError(result.error.message);
                        deleteCachedUser();
                    } else {
                        // payment was successful
                        // cached user will be activated by webhook handler
                        form.submit();
                    }
                });

                var activateCachedUser = function() {
                    // send ajax post request to '/activate-cached-user/' url
                    $.ajax({
                        url: '/activate-cached-user/',
                        method: 'POST',
                        data: getActivateOrDeleteUserData(),
                        dataType: "json",
                        timeout: 500,
                        success: activateOrDeleteUserAjaxSuccess,
                        error: activateOrDeleteUserAjaxFailure,
                    });
                };

                var deleteCachedUser = function() {
                    // send ajax post request to '/delete-cached-user/' url
                    $.ajax({
                        url: '/delete-cached-user/',
                        method: 'POST',
                        data: getActivateOrDeleteUserData(),
                        dataType: "json",
                        timeout: 500,
                        success: activateOrDeleteUserAjaxSuccess,
                        error: activateOrDeleteUserAjaxFailure,
                    });
                };

                var activateOrDeleteUserAjaxSuccess = function(data) {
                    // redirect to url returned from server
                    window.location.replace(data.redirectUrl);
                }

                var activateOrDeleteUserAjaxFailure = function() {
                    window.location.reload();
                }

                var getActivateOrDeleteUserData = function() {
                    /**
                     * gather data required for post request to activate-cached-user 
                     * @return {object} object containing data for post request
                     */
                    var subscribeForm = document.getElementById('subscribe-form');
                    // using {% csrf_token %} in the subscribe form
                    var csrfToken = subscribeForm.querySelector('input[name="csrfmiddlewaretoken"]').value;
                    var postData = {
                        'csrfmiddlewaretoken': csrfToken,
                        'user_id': userId,
                    };
                    return postData;
                };

                // UI feedback if payment is unsuccessful
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
            };
        };
    };
});


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