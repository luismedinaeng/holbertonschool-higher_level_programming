$(document).ready(function () {
  $('INPUT#btn_translate').click(translate);
});

function translate () {
  const lang = $('INPUT#language_code').val();
  $.get('https://fourtonfish.com/hellosalut/?lang=' + lang, function (data) {
    $('DIV#hello').text(data.hello);
  });
}
