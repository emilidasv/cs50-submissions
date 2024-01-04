SELECT artist AS 'Brigthess Eastern Capital Artist' FROM views WHERE english_title LIKE "%Capital%" ORDER BY brightness DESC LIMIT 1;

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
