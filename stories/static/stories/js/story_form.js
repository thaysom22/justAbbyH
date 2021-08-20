// genre select widget UI
$(document).ready(() => {
    $("#id_genre option[value='']").prop('disabled', true);
    if ($('#id_genre').children('option[selected]').attr('value') != '') {
        $("#id_genre").css("color", "#061234");
    }
});

$('.add-story-form #id_genre').on("change", function(event) {
    $(this).css("color", "#061234");
    $(this).off(event);  // handler only runs once
});

$('#delete-story-link').on("click", function(event) {
    var response = window.confirm("Are you sure you want to delete this story?");
    if (!response) {
        event.preventDefault();
    }
});

// disable form on submit
$('#story-form').submit(function() {
    $('fieldset').find('input').prop('readonly', true);
    $('#submit-button').text("Processing...");
    $('#submit-button').prop('disabled', true);
});
