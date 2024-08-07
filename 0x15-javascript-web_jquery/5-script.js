$(document).ready(function() {
  $("#add_item").click(function(){
    let item = $("<li>Item</li>");
    $("ul.my_list").append(item);
 });
});
