/*In 7.sql, write a SQL query to count the number of players who bat (or batted) right-handed and throw (or threw) left-handed, or vice versa.
In 8.sql, write a SQL query to find the average height and weight, rounded to two decimal places, of baseball players who debuted on or after January 1st, 2000. Return the columns with the name “Average Height” and “Average Weight”, respectively.
In 9.sql, write a SQL query to find the players who played their final game in the MLB in 2022. Sort the results alphabetically by first name, then by last name.
In 10.sql, write SQL query to answer a question of your choice. This query should:
Make use of AS to rename a column
Involve at least condition, using WHERE
Sort by at least one column using ORDER BY


sqlite> .schema players
CREATE TABLE IF NOT EXISTS "players" (
    "id" INTEGER,
    "first_name" TEXT,
    "last_name" TEXT,
    "bats" TEXT,
    "throws" TEXT,
    "weight" INTEGER,
    "height" INTEGER,
    "debut" NUMERIC,
    "final_game" NUMERIC,
    "birth_year" INTEGER,
    "birth_month" INTEGER,
    "birth_day" INTEGER,
    "birth_city" TEXT,
    "birth_state" TEXT,
    "birth_country" TEXT,
    PRIMARY KEY("id")
);
*/
