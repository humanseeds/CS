SELECT AVG(rating)
FROM ratings
JOIN movies ON  ratingmovie_id
WHERE year = 2012;
