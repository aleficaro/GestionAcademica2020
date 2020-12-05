$(function () {
    $('#data').DataTable({
        responsive: true,
        // autoWidth: true,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {'action': 'buscardato'}, // parametros
            dataSrc: ""
        },
        columns: [
            // se toman los valores de las columnas del modelo
            {"data": "id_grado"},
            {"data": "jornada"},
            {"data": "n_grado"},
            {"data": "capacidad"},
            {"data": "ACCION"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/erp/category/update/' + row.id_pago + '/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="/erp/category/delete/' + row.id_pago + '/" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
});