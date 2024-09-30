SELECT title
FROM movies
JOIN stars on movies.id = stars.movie_id
JOIN people on stars.person_id = people.id
WHERE people.name IN 'Bradley Cooper' AND 'Jennifer Lawrence'
GROUP BY movies.title;
