// genre select widget UI
$(document).ready(() => {
    $('select#id_genre option[selected]').prop('disabled', true);
})

$('select#id_genre').on("change", function(event) {
    $(this).css("color", "#061234");
    $(this).off(event);  // handler only runs once
});