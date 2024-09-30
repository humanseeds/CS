SELECT title
FROM movies
JOIN stars on movies.id = stars.movie_id
JOIN people on stars.person_id = people.id
WHERE people.name IN ('Bradley Cooper', 'Jennifer Lawrence')
GROUP BY  movies.id, movies.title
HAVING COUNT(DISTINCT people.id) = 2;
