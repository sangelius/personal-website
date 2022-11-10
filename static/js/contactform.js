$(document).ready(function(){ // wait for the page to finish loading

    // submit contact info through ajax
    function submit_contact() {
        $.ajax({
            url : "/submit-contact/", // the endpoint
            type : "POST", // http method
            data : $("#contactForm").serialize(), // serialized form data

            // handle a successful response
            success : function(response_data) {
                if (response_data.stat == 'ok') { // success
                    console.log('worked');
                    
                    //$('#form_content').slideUp(); // hide the form fields
                    $('#form_content').slideUp(function() { // hide the form fields
                       $(window).trigger('resize').trigger('scroll'); // to reset parallax
                    });
                    $('#contact_result').html('<div class="contact_success">'
                        + response_data.success
                        + '</div>');
                    $(window).trigger('resize').trigger('scroll'); // to reset parallax
                } else { // error
                    $('#contact_result').html('<div class="text-danger contact_error">'
                        + response_data.error_info
                        + '</div>');
                    var errors = jQuery.parseJSON(response_data.errors);

                    // add error descriptions
                    if (errors.name) {
                        $('#contact_name_error').html(errors.name[0].message);
                    } else {
                        $('#contact_name_error').empty();
                    }
                    if (errors.email) {
                        $('#contact_email_error').html(errors.email[0].message);
                    } else {
                        $('#contact_email_error').empty();
                    }
                    if (errors.phone) {
                        $('#contact_phone_error').html(errors.phone[0].message);
                    } else {
                        $('#contact_phone_error').empty();
                    }
                    if (errors.message) {
                        $('#contact_message_error').html(errors.message[0].message);
                    } else {
                        $('#contact_message_error').empty();
                    }
                    $(window).trigger('resize').trigger('scroll'); // to reset parallax
                    $('#contactForm').find(':submit').prop('disabled', false); // allow form submit again
                }
            },

            // handle a non-successful response
            error : function(xhr,errmsg,err) {
                $('#contact_result').html('<div class="text-danger contact_error">Oops! We have encountered an error.</div>');
                $(window).trigger('resize').trigger('scroll'); // to reset parallax
                $('#contactForm').find(':submit').prop('disabled', false); // allow form submit again
            }
        });
    };

    // do not allow submit; send through ajax instead
    $('#contactForm').submit(function(e) {
        e.preventDefault();
        $('#contactForm').find(':submit').prop('disabled', true); // do not allow multipe form submits
        submit_contact();
    });

    // do not allow enter to submit form
    $('#contactForm input').on('keyup keypress', function(e) {
        var keyCode = e.keyCode || e.which;
        if (keyCode === 13) {
          e.preventDefault();
          return false;
        }
    });

    // CREATE PHONE MASK
    $('#id_phone').keydown(function (e) {
        var key = e.which || e.charCode || e.keyCode || 0;
        $phone = $(this);
        // Don't let them remove the starting '('
        if ($phone.val().length === 1 && (key === 8 || key === 46)) {
                $phone.val('(');
            return false;
        }
        // Reset if they highlight and type over first char.
        else if ($phone.val().charAt(0) !== '(') {
                $phone.val('('+String.fromCharCode(e.keyCode)+'');
        }
        // Auto-format- do not expose the mask as the user begins to type
        if (key !== 8 && key !== 9) {
            if ($phone.val().length === 4) {
                $phone.val($phone.val() + ')');
            }
            if ($phone.val().length === 5) {
                $phone.val($phone.val() + ' ');
            }
            if ($phone.val().length === 9) {
                $phone.val($phone.val() + '-');
            }
        }
        // Allow numeric (and tab, backspace, delete) keys only
        return (key == 8 ||
                key == 9 ||
                key == 46 ||
                (key >= 48 && key <= 57) ||
                (key >= 96 && key <= 105));
    });
    $('#id_phone').bind('focus click', function () {
        $phone = $(this);
        if ($phone.val().length === 0) {
            $phone.val('(');
        }
        else {
            var val = $phone.val();
            $phone.val('').val(val); // Ensure cursor remains at the end
        }
    });
    $('#id_phone').blur(function () {
        $phone = $(this);
        if ($phone.val() === '(') {
            $phone.val('');
        }
    });

});
