// get required keys from template variables
var stripePublicKey = document.getElementById('id_stripe_public_key').text.slice(1,-1);
var clientSecret = document.getElementById('id_client_secret').text.slice(1,-1);

/* client logic based on: https://stripe.com/docs/payments/integration-builder */

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
    } else {
        errorDiv.innerHTML = '';
    }
});