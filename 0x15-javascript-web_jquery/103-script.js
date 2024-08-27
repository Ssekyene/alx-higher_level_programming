/*
fetches and prints how to say “Hello” depending on the language
The language code will be the value entered in the tag INPUT#language_code (ex: es, fr, en etc.)
The translation must be fetched when the user clicks on INPUT#btn_translate OR presses ENTER
when the focus is on INPUT#language_code
*/
function postLang () {
  const lang = $('INPUT#language_code').val();
  $.ajax({
    type: 'POST',
    url: 'https://hellosalut.stefanbohacek.dev/?lang=' + lang,
    success: (translation) => {
      $('DIV#hello').text(translation.hello);
    },
    error: () => {
      console.log('Error loading orders');
    }
  });
}

window.onload = () => {
  $('INPUT#btn_translate').focus(() => {
    $('INPUT#btn_translate').keypress((key) => {
      if (key.which === 13) {
        postLang();
      }
    });
    $('INPUT#btn_translate').click(() => {
      postLang();
    });
  });
};
