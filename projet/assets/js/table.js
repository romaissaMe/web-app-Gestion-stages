$(document).ready(function() {
    $('#example').DataTable( {
        responsive: {
            details: {
                type: 'column',
                searchable:false
            }
        },
        columnDefs: [ {
            className: 'dtr-control',
            orderable: false,
            targets:   0

        } ],
        order: [ 1, 'asc' ]
    } );
} );