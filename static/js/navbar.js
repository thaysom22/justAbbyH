/* 
attach click event listener navbar toggler to:
* toggle .hide class for all content after navbar in document
* toggle between bars and times icons for collapsible navbar toggler
*/
$('.navbar-toggler').click(() => {
    $('#hide-when-nav-expanded').toggleClass('hide');
    $('.navbar-toggler-icon i').toggleClass(['fa-ellipsis-h', 'fa-times']);
});

