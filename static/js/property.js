$(document).ready(function() {
    $('#propertyTable').DataTable();

    $('#propertyForm').on('submit', function(e) {
        e.preventDefault();

        var formData = new FormData(this);

        $.ajax({
            url: "{{ url_for('app_bp.properties') }}",
            type: "POST",
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                if (response.status === 'success') {
                    var imageTags = '';
                    response.images.forEach(function(image) {
                        imageTags += '<img src="' + image + '" alt="Property Image" width="100">';
                    });

                    $('#propertyTable').DataTable().row.add([
                        response.name,
                        response.description,
                        $('#user_id option:selected').text(),
                        imageTags
                    ]).draw();

                    // Close the modal
                    $('#propertyModal').modal('hide');
                    // Clear the form
                    $('#propertyForm')[0].reset();
                    $.toast({
                        heading: 'Success',
                        text: response.message,
                        showHideTransition: 'slide',
                        icon: 'success'
                    });
                    if (response.redirect_url) {
                        window.location.href = response.redirect_url;
                    }
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
        });
    });
});