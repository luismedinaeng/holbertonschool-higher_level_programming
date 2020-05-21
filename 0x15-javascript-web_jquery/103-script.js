$(document).ready(function () {
  $('INPUT#btn_translate').click(translate);
  $('INPUT#language_code').keypress(function (event) {
    if (event.which === 13) {
      translate();
    }
  });
});

function translate () {
  const lang = $('INPUT#language_code').val();
  $.get('https://fourtonfish.com/hellosalut/?lang=' + lang, function (data) {
    $('DIV#hello').text(data.hello);
  });
}
