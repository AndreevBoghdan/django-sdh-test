$( document ).ready(function() {

    $('#generate_new_code').click(function(){
        var ajaxUrl = "/registration/generate_new_code/"
        var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
        $.ajax({
            type: "POST",
            url: ajaxUrl,
            beforeSend: function(xhr, settings) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            },
            success: function(data){
                var res = JSON.parse(data);
                if ('new_code' in res) {
                    $('#invitation_code').val(res['new_code']);
                }
            },
            error: function (xhr, ajaxOptions, thrownError) {
                alert('error');
            }
        });
    });


});








