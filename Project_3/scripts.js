$(document).ready(function() {
    $('#contact-us').click(function() {
        $('#contact-form-popup').toggleClass('hidden');
    });

    $('#contact-form').submit(function(event) {
        event.preventDefault();
        var formData = $(this).serialize();
        $.ajax({
            url: $(this).attr('action'),
            method: 'POST',
            data: formData,
            success: function(response) {
                alert('Form submitted successfully!');
                $('#contact-form-popup').addClass('hidden');
            },
            error: function(error) {
                alert('An error occurred. Please try again.');
            }
        });
    });
});
