/* 
attach click event listener navbar toggler to:
* toggle .hide class for all content after navbar in document
* toggle .hide class on instagram nav link so it does not display when nav is collapsed
* toggle between bars and times icons for collapsible navbar toggler
*/
$('.navbar-toggler').click(() => {
    $('#hide-when-nav-expanded').toggleClass('hide');
    $('.navbar-nav .nav-instagram').toggleClass('hide');
    $('.navbar-toggler-icon i').toggleClass(['fa-bars', 'fa-times']);
});

