SELECT movies.titles, ratings.rating
FROM movies
JOIN ratings ON movies.id = ratings.movie_id
WHERE movie.year = 2010
ORDER BY ratings.rating DESC, movies.title ASC;
