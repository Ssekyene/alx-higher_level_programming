/*
fetches and prints how to say “Hello” depending on the language
You should use this API service: https://www.fourtonfish.com/hellosalut/hello/
The language code will be the value entered in the tag INPUT#language_code (ex: es, fr, en etc.)
The translation must be fetched when the user clicks on INPUT#btn_translate
*/
window.onload = () => {
  $('INPUT#btn_translate').click(() => {
    const lang = $('INPUT#language_code').val();
    $.ajax({
      type: 'POST',
      url: 'https://hellosalut.stefanbohacek.dev/?lang=' + lang,
      success: (translation) => {
        $('DIV#hello').text(translation.hello);
      },
      error: () => {
        console.log('Error loading api');
      }
    });
  });
};
