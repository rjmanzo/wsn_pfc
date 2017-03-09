$(document).ready(function() {
  var table = $('#DataTable').DataTable({
        language: language_d,  // global variable defined in html
        dom: 'lBfrtip',
            buttons: [
            'csv','pdf'
          ],
        lengthMenu: [[10, 25, 50, -1], [10, 25, 50, 'All']],
        //order: [[ 6, "asc" ]],
        searching: true,
        processing: true,
        serverSide: true,
        ajax: TABLA_LIST_JSON_URL,
        //ajax:'/wsn/api-table',
        //stateSave: true,
    });
});
