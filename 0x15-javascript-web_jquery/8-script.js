$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  $(data.results).each(function (index) {
    $('UL#list_movies').append('<li>' + this.title + '</li>');
  });
});
