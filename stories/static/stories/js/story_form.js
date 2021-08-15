// genre select widget UI
$(document).ready(() => {
    $("#id_genre option[value='']").prop('disabled', true);
})

$('.add-story-form #id_genre').on("change", function(event) {
    $(this).css("color", "#061234");
    $(this).off(event);  // handler only runs once
});