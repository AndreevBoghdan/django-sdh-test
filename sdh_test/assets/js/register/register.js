$( document ).ready(function() {

    jQuery(function() {
        var options_register = {
            beforeSubmit: function(form, options) {
                $('input').attr('disabled', 'disabled');
            },
            success: function(responseText) {
                $(".user_register-error").remove();
                //alert(responseText);
                console.log(responseText);
                 $('input').removeAttr('disabled');
                window.location = '/accounts/register/complete/';

                },
            error:  function(resp){
                $('input').removeAttr('disabled');
                $(".user_register_error").remove();
                var id = '';
                var errors = JSON.parse(resp.responseText);
                for (error in errors) {
                    error_text = errors[error];
                    id="#id_"+error;
                    $(id).after("<p class='user_register_error'>"+error_text+"</p>");
                    }
                },
        };
        
        jQuery('#ajaxform-user-register').ajaxForm(options_register);

    });

});








