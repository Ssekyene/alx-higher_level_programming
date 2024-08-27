/*
toggles the class of the <header> element when
the user clicks on the tag DIV#toggle_header
*/
$(document).ready(function () {
  $('DIV#toggle_header').click(function () {
    const header = $('header');
    if (header.hasClass('green')) {
      header.removeClass('green').addClass('red');
    } else {
      header.removeClass('red').addClass('green');
    }
  });
});
