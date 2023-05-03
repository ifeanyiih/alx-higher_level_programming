$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data, textStatus) {
  if (textStatus === 'success') {
    const results = data.results;
    for (const result of results) {
      $('UL#list_movies').append($('<li></li>').text(result.title));
    }
  }
});
