select title from movies
WHERE (
    id IN
       ( SELECT stars.movie_id FROM stars
          JOIN people ON stars.person_id=people.id
          WHERE people.name = "Johnny Depp")
    and
    id IN
        (SELECT stars.movie_id FROM stars
        JOIN people ON stars.person_id=people.id
        WHERE people.name = "Helena Bonham Carter"));
