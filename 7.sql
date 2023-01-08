SELECT movies.title , ratings.rating from movies
INNER JOIN ratings ON movies.id = ratings.movie_id
WHERE ratings.rating > 0 ORDER BY ratings.rating DESC, movies.title DESC;


