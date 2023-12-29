/*
In 9.sql, write a SQL query to find the English title and artist of the print with the highest brightness.
*/

SELECT english_title, artist FROM views ORDER BY brightness DESC LIMIT 1;

/*SELECT english_title, artist, MAX(brightness FROM views;*/

/*
In 10.sql, write a SQL query to answer a question of your choice about the prints. The query should:
Make use of AS to rename a column
Involve at least one condition, using WHERE
Sort by at least one column, using ORDER BY


sqlite> .tables
views
sqlite> .schema views
CREATE TABLE IF NOT EXISTS "views" (
    "id" INTEGER,
    "print_number" INTEGER,
    "english_title" TEXT,
    "japanese_title" TEXT,
    "artist" TEXT,
    "average_color" TEXT,
    "brightness" NUMERIC,
    "contrast" NUMERIC,
    "entropy" NUMERIC,
    PRIMARY KEY("id")

*/
