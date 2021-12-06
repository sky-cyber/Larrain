$("input[name='value']").TouchSpin({
    min: 0,
    max: 100,
    step: 1
});

var tblproduct;

var vents = {
    items: {
        client: '',
        date_joined: '',
        subtotal: 0,
        value: 0,
        total: 0,
        products: []
    },
    calculate_invoice: function () {
        var subtotal = 0;
        $.each(this.items.products, function (pos, dict) {
            if (parseInt(dict.offerPrice) === 0) {
                dict.subtotal = dict.qty * parseInt(dict.salePrice);
                subtotal += dict.subtotal
            } else {
                dict.subtotal = dict.qty * parseInt(dict.offerPrice);
                subtotal += dict.subtotal
            }
        });
        this.items.subtotal = subtotal;

        this.items.total = this.items.subtotal

        $('input[name = "subtotal"]').val(this.items.subtotal);

        $('input[name = "total"]').val(this.items.total);
    },
    add: function (item) {
        this.items.products.push(item)
        this.list()
    },
    list: function () {
        this.calculate_invoice();
        tblproduct = -$('#tblproduct').DataTable({
            responsive: true,
            autoWidth: false,
            destroy: true,
            data: this.items.products,
            columns: [
                {"data": "id"},
                {"data": "name"},
                {"data": "category.name"},
                {"data": "salePrice"},
                {"data": "offerPrice"},
                {"data": "qty"},
                {"data": "subtotal"},
            ],
            columnDefs: [
                {
                    targets: [0],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<a rel="remove" class="btn btn-danger btn-sm btn-flat text-white"><i class="fas fa-trash-alt"></i></a>';

                    }
                },
                {
                    targets: [-3],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '$' + (data);
                    }
                },
                {
                    targets: [-2],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="qty" class="form-control form-control-sm" autocomplete="off" value="' + row.qty + '">';
                    }
                },
                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '$' + (data);
                    }
                },
            ],
            rowCallback(row, data, displayNum, displayIndex, dataIndex) {
                $(row).find('input[name="qty"]').TouchSpin({
                    min: 1,
                    max: 1000000,
                    step: 1
                });
            },
            initComplete: function (settings, json) {
            }
        });
    }
};

$('input[name="search"]').autocomplete({
    source: function (request, response) {
        $.ajax({
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'search_products',
                'term': request.term
            },
            dataType: 'json',
        }).done(function (data) {
            response(data);
        }).fail(function (jqXHR, textStatus, errorThrown) {
            alert(textStatus + ': ' + errorThrown);
        }).always(function (data) {

        });
    },
    delay: 500,
    minlength: 3,
    select: function (event, ui) {
        event.preventDefault()
        console.clear()
        ui.item.qty = 1;
        ui.item.subtotal = 0;
        console.log(vents.items);
        vents.add(ui.item)
        $(this).val('');
    }
});

$(function () {

    $('.select2').select2({
        theme: "bootstrap4",
        language: 'es',
    });

    $('#tblproduct tbody')
        .on('click', 'a[rel="remove"]', function () {
            var tr = tblproduct.cell($(this).closest('td, li')).index();
            vents.items.products.splice(tr.row, 1);
            vents.list();
        })
        .on('change', 'input[name="qty"]', function () {
            console.clear();
            var qty = parseInt($(this).val());
            var tr = tblproduct.cell($(this).closest('td, li')).index();
            vents.items.products[tr.row].qty = qty;
            vents.calculate_invoice();
            $('td:eq(6)', tblproduct.row(tr.row).node()).html('$' + vents.items.products[tr.row].subtotal);
        });

    $('.btnRemoveAll').on('click', function () {
        vents.items.products = []
        vents.list()
    });
});


