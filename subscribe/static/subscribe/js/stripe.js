// get required keys from template variables
var stripePublicKey = document.getElementById('id_stripe_public_key').text.slice(1,-1);
var clientSecret = document.getElementById('id_client_secret').text.slice(1,-1);

/* client js logic below based on: https://stripe.com/docs/payments/integration-builder */

// create Stripe instance with public key and create Elements instance
var stripe = Stripe(stripePublicKey);  
var elements = stripe.elements();
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

 // create stripe UI element and add to subscribe form html
var card = elements.create('card', {style: style});
card.mount('#card-element');

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

// handle subscription form submit event
var form = document.getElementById("subscribe-form");
form.addEventListener("submit", function(event) {
    event.preventDefault();
    awaitingPaymentResult(true);
    payWithCard(stripe, card, clientSecret);
});

// Calls stripe.confirmCardPayment
// If the card requires authentication Stripe shows a pop-up modal to
// prompt the user to enter authentication details without leaving your page.
var payWithCard = function(stripe, card, clientSecret) {
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
            // The payment succeeded!
            orderComplete(result.paymentIntent.id);
        }
    });
};

// display overlay, disable button and card element on form submit
var awaitingPaymentResult = function(isLoading) {  
    if (isLoading) {
        document.getElementById('submit-button').disabled = true;
        card.update({ 'disabled': true });
        document.getElementById("spinner").classList.remove("hidden");
        document.getElementById("button-text").classList.add("hidden");
        document.getElementById("loading-overlay").classList.remove("hidden");
    } else {
        document.getElementById('submit-button').disabled = false;
        card.update({ 'disabled': false });
        document.getElementById("spinner").classList.add("hidden");
        document.getElementById("button-text").classList.remove("hidden");
        document.getElementById("loading-overlay").classList.add("hidden");
    }
};

// posts form data once payment completes
var orderComplete = function(paymentIntentId) {
    form.submit();  
};

// show the customer the error from Stripe if their card fails to charge
var showError = function(errorMsgText) {
  awaitingPaymentResult(false);
  var errorMsg = document.getElementById("card-errors");
  errorMsg.textContent = errorMsgText;
  setTimeout(function() {
    errorMsg.textContent = "";
  }, 4000);
};





