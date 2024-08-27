/*
 fetches from https://hellosalut.stefanbohacek.dev/?lang=fr and
 displays the value of hello from that fetch in the HTML tag DIV#hello

 The script must work when it is imported from the <head> tag
*/
$(document).ready(function () {
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    method: 'GET',
    success: function (data) {
      const helloValue = data.hello;
      $('DIV#hello').text(helloValue);
    }
  });
});
