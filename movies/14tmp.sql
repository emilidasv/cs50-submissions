SELECT movie_id FROM from movies

SELECT name from people JOIN stars ON people.id = stars.person_id
WHERE movie_id IN(SELECT movie_id from starsWHERE people.id = (
SELECT id from people WHERE name = "Kevin Bacon" and birth = 1958));


SELECT id from people WHERE name = "Kevin Bacon" and birth = 1958)


SELECT stars.movie_id, people.name FROM people JOIN stars ON people.id = stars.person_id
WHERE id = (SELECT id from people WHERE name = "Kevin Bacon" and birth = 1958);


SELECT stars.movie_id, people.name FROM people JOIN stars ON people.id = stars.person_id
WHERE stars.movie_id =
(SELECT id from people WHERE name = "Kevin Bacon" and birth = 1958);


Kevins personid = SELECT id from people WHERE name = "Kevin Bacon" and birth = 1958

movies that Kevin is in:
SELECT stars.movie_id FROM people JOIN stars ON people.id = stars.person_id
WHERE (stars.movie_id IN (SELECT movies.id FROM movies) and
        (stars.person_id IN (SELECT id from people
            WHERE name = "Kevin Bacon" and birth = 1958)));

SELECT  people.name from people JOIN movies
ON people.movie_id = movies.id WHERE movies.id IN
(SELECT stars.movie_id FROM people JOIN stars ON people.id = stars.person_id
WHERE (stars.movie_id IN (SELECT movies.id FROM movies) and
        (stars.person_id IN (SELECT id from people
            WHERE name = "Kevin Bacon" and birth = 1958))));


            SELECT people.name
FROM movies
JOIN stars
ON stars.movie_id = movies.id
JOIN people
ON people.id = stars.person_id
WHERE movie.id IN
    (SELECT )