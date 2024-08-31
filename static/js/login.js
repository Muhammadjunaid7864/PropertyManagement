$(document).ready(function(){
    $('#loginButton').on('click', function() {
        var form = $('#loginForm');
        var data = form.serialize();
        var username = $('#username').val()
        var passowrd = $('#password').val()

        $.ajax({
            url: '/login',
            method: 'POST',
            contentType : 'application/json',
            data: JSON.stringify({ 
                username: $('#username').val(),
                password: $('#password').val()
            }),
            success: function(response) {
                if (response.status === 'success') {
                    $.toast({
                        heading: 'Success',
                        text: response.message,
                        showHideTransition: 'slide',
                        icon: 'success'
                    });
                    // Redirect to the home page after successful login
                    window.location.href = response.redirect_url || '/';
                } else {
                    $.toast({
                        heading: 'Error',
                        text: response.message,
                        showHideTransition: 'fade',
                        icon: 'error'
                    });
                }
            },
            error: function(response) {
                $.toast({
                    heading: 'Error',
                    text: response.responseJSON.message || 'An error occurred.',
                    showHideTransition: 'fade',
                    icon: 'error'
                });
            }
        })
    })
})