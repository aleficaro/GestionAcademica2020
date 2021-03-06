$(function () {
    $('#data').DataTable({
        responsive: true,
        // autoWidth: true,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {'action': 'buscarmateria'}, // parametros
            dataSrc: ""
        },
        columns: [
            {"data": "id_materia"},
            {"data": "grado"},
            {"data": "nmateria"},
            {"data": "intensidad"},
            {"data": "ACCION"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="/erp/category/delete/' + row.dni + '/" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
});