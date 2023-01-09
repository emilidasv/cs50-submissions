SELECT people.name
FROM people
JOIN stars
ON people.id=stars.person_id
JOIN movies
ON movies.id = stars.movie_id
WHERE ((movies.id IN
(SELECT stars.movie_id FROM people JOIN stars ON people.id = stars.person_id
WHERE (stars.movie_id IN (SELECT movies.id FROM movies) and
        (stars.person_id IN (SELECT id from people

            WHERE name = "Kevin Bacon" and birth = 1958)))))
and
(NOT(people.name =="Kevin Bacon" and people.birth = 1958)));






