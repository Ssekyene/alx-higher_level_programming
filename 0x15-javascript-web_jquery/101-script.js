/*
adds, removes and clears LI elements from a list when the user clicks
The script must work when it imported from the HEAD tag
*/
$(document).ready(function () {
  $('DIV#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });
  $('DIV#remove_item').click(function () {
    const items = $('UL.my_list li');
    const itemsLength = items.length;
    if (itemsLength > 0) {
      items[itemsLength - 1].remove();
    }
  });
  $('DIV#clear_list').click(function () {
    $('UL.my_list').empty();
  });
});
