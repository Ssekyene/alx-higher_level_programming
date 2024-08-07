$(document).ready(function() {
  $.ajax({
    url: "https://fourtonfish.com/hellosalut/?lang=fr",
    method: "GET",
    success: function(data) {
     const helloFr = data.hello;
     $("#hello").text(helloFr);
    },
  });
});
