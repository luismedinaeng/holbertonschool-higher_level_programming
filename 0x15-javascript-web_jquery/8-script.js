$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (json) {
  json.results.forEach(element => $('ul#list_movies').append('<li>' + element.title + '</li>'));
});
