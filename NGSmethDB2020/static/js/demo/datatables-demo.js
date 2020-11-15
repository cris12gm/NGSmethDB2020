// Call the dataTables jQuery plugin
$(document).ready(function() {
  // QuerySNP
  $('#dataTableSamples').DataTable({
    "order":[[1, "desc"]]
  });
  $('#dataTableMeth').DataTable({
    "order":[[1, "desc"]]
  });
}); 