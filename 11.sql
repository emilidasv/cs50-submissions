/*

In 11.sql, list the titles of episodes from season 5, in reverse alphabetical order.
*/
SELECT title from episodes WHERE season=5 ORDER by title DESC;
/*
+------------------------+
|         title          |
+------------------------+
| The Halloween Howl     |
| The Flying Parallinis  |
| The Fairy Borg Father  |
| On the Line            |
| Inside Hacker          |
| EcoHaven Ooze          |
| Designing Mr. Perfect  |
| Crystal Clear          |
| A Fraction of a Chance |
| A Clean Sweep          |
+------------------------+





