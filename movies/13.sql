SELECT people.names
FROM people
JOIN stars ON people.id = stars.person_id
JOIN movie ON stars.movie_id = movies.id
WHERE movies.id
