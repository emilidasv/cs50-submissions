/*
In 12.sql, count the number of unique episode titles.

*/
SELECT COUNT(DISTINCT title) FROM episodes;



/*
sqlite> .tables
episodes
sqlite> .schema episodes
CREATE TABLE IF NOT EXISTS "episodes" (
    "id" INTEGER,
    "season" INTEGER,
    "episode_in_season" INTEGER,
    "title" TEXT,
    "topic" TEXT,
    "air_date" NUMERIC,
    "production_code" TEXT,
    PRIMARY KEY("id")
*/
