/* 
attach event handler to hide each 
message on dismiss icon click
*/
$('.message .message-dismiss-icon').click(function() {
    $(this).parent().addClass("hide");
});

/* set timeout to hide messages automatically after delay */
setTimeout(() => {
    $('.messages').addClass("hide");
}, 15000);