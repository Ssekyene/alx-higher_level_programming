$(document).ready(function() {
  $.ajax({
    url: "https://swapi-api.alx-tools.com/api/films/?format=json",
    method: "GET",
    success: function(data) {
      const movies = data.results;
      const movieList = $("#list_movies");

      movies.forEach(function(movie) {
        const title = movie.title;
        const listItem = $("<li></li>").text(title);
        movieList.append(listItem);
      });
    },
  });
});
