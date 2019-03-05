
$(document).ready(function() {
    // https://datatables.net/reference/option/dom
    $('#result_table').DataTable({
        dom: '<"top"f>rt<"bottom"ip><"clear">'
    });
    $('#saved_stock').DataTable({
        dom: '<"top"f>rt<"bottom"ip><"clear">'
    });
});

$(document).ready(function() {
    $('#save_as_csv').DataTable({
        dom: 'frtipB',
        buttons: ['copy', 'csv']
    });
});
