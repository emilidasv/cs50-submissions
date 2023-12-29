/**
In 6.sql, list the titles of episodes from season 6 (2008) that were released early, in 2007.*/

SELECT title from episodes WHERE season = 6 and air_date < "2008-01-31";
/*
+------------------------+
|         title          |
+------------------------+
| Digit's B-Day Surprise |
| When Penguins Fly      |
+------------------------+
/*


/
