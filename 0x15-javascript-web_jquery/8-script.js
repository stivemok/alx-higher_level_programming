// JavaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json
const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.getJSON(url, function (response) {
  $.each(response.results, function (i, item) {
    $('UL#list_movies').append('<li>' + item.title + '</li>');
  });
});
