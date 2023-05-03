$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data, statusText) {
  if (statusText === 'success') {
    $('DIV#hello').text(data.hello);
  }
});
