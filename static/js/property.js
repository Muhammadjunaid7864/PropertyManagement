$(document).ready(function() {
    var table = $('#propertyTable').DataTable({
        columnDefs: [{
            "defaultContent": "-",
            "targets": "_all"
          }]
    });

    // Handle form submission
    $('#propertyForm').on('submit', function(e) {
        e.preventDefault();

        var formData = new FormData(this);

        $.ajax({
            url: "/property",
            type: "POST",
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                if (response.status === "success") {
                    if (response.redirect_url) {
                        window.location.href = response.redirect_url;
                    }
                    var imageTags = '';
                    response.images.forEach(function(image) {
                        imageTags += '<img src="' + image + '" alt="Property Image" width="100">';
                    });

                    table.row.add([
                        response.name,
                        response.description,
                        $('#user_id option:selected').text(),
                        imageTags,
                        '<button class="btn btn-primary view-property" data-property-id="' + response.id + '"><i class="fa fa-eye"></i></button>' +
                        '<button class="btn btn-warning edit-property" data-property-id="' + response.id + '"><i class="fa fa-edit"></i></button>' +
                        '<button class="btn btn-danger delete-property" data-property-id="' + response.id + '"><i class="fa fa-trash"></i></button>'
                    ]).draw(false);

                    $('#propertyModal').modal('hide');
                    $('#propertyForm')[0].reset();

                    $.toast({
                        heading: 'Success',
                        text: response.message,
                        showHideTransition: 'slide',
                        icon: 'success'
                    });
                }
            },
            error: function(xhr) {
                var errorMessage = xhr.responseJSON?.message || 'An error occurred.';
                $.toast({
                    heading: 'Error',
                    text: errorMessage,
                    showHideTransition: 'fade',
                    icon: 'error'
                });
            }
        });
    });

    // Handle view button click
    $('#propertyTable').on('click', '.view-property', function() {
        var propertyId = $(this).data('property-id');
        window.location.href = '/property/' + propertyId;
    });

    // Handle delete button click
    $('#propertyTable').on('click', '.delete-property', function() {
        var propertyId = $(this).data('property-id');
        const swalWithBootstrapButtons = Swal.mixin({
            customClass: {
                confirmButton: "btn btn-success",
                cancelButton: "btn btn-danger"
            },
            buttonsStyling: false
        });

        swalWithBootstrapButtons.fire({
            title: "Are you sure?",
            text: "You won't be able to revert this!",
            icon: "warning",
            showCancelButton: true,
            confirmButtonText: "Yes, delete it!",
            cancelButtonText: "No, cancel!",
            reverseButtons: true
        }).then((result) => {
            if (result.isConfirmed) {
                $.ajax({
                    url: "/delete_property",
                    type: "DELETE",
                    data: JSON.stringify({ id: propertyId }),
                    contentType: "application/json",
                    success: function(response) {
                        if (response.status === "success") {
                            if (response.redirect_url) {
                                window.location.href = response.redirect_url;
                            }
                            // table.row($(this).closest('tr')).remove().draw();
                            swalWithBootstrapButtons.fire({
                                title: "Deleted!",
                                text: "Your Property has been deleted.",
                                icon: "success"
                            });
                        }
                    },
                    error: function(response) {
                        alert(response.responseJSON.message || 'An error occurred.');
                    }
                });
            } else if (result.dismiss === Swal.DismissReason.cancel) {
                swalWithBootstrapButtons.fire({
                    title: "Cancelled",
                    text: "Your imaginary Property is safe :)",
                    icon: "error"
                });
            }
        });
    });
});
