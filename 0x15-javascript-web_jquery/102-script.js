document.addEventListener('DOMContentLoaded', (e) => {
  const Input = $('INPUT#language_code');
  const Button = $('INPUT#btn_translate');
  const display = $('DIV#hello');

  Button.on('click', function (e) {
    const value = Input.val();
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=' + value;
    $.get(url, function (data, status) {
      console.log(data);
    });
  });
});
