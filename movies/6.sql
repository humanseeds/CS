SELECT AVG(rating)
FROM ratings
JOIN movies ON  movie_id
WHERE year = 2012;
