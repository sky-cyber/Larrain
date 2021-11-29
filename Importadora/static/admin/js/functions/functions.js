function message_error(obj) {
    var html = '<ul style="text-align: left">';
    $.each(obj, function (key, value) {
        html += '<li>' + key + ': ' + value + '</li>';

    });
    html += '</ul>';
    swal.fire({
        title: 'Upss.. Error!',
        html: html,
        icon: 'error'
    });
}


function submit_with_ajax(url, parameter, callback) {
    $.confirm({
        theme: 'material',
        title: 'Confirmación',
        icon: 'fa fa-info',
        content: '¿Está seguro de realizar la siguiente acción?',
        columnClass: 'medium',
        typeAnimated: true,
        cancelButtonClass: 'btn-primary',
        draggable: true,
        dragWindowBorder: false,
        buttons: {
            info: {
                text: "Si",
                btnClass: 'btn-primary',
                action: function () {
                    $.ajax({
                        url: url,
                        type: 'POST',
                        data: parameter,
                        dataType: 'json',
                    }).done(function (data) {
                        if (!data.hasOwnProperty('error')) {
                            callback();
                            return false;
                        }
                        message_error(data.error);
                    }).fail(function (jqXHR, textStatus, errorThrown) {
                        alert(textStatus + ': ' + errorThrown);
                    }).always(function (data) {

                    });
                }
            },
            danger: {
                text: "No",
                btnClass: 'btn-red',
                action: function () {

                }
            },
        }
    })
}




