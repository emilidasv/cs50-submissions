/*
In 9.sql, write a query that counts the number of episodes released in Cyberchase’s first 6 years, from 2002 to 2007, inclusive.
*/
select count(episode_in_season) from episodes where air_date < "2008-01-01";
/*
+--------------------------+
| count(episode_in_season) |
+--------------------------+
| 74                       |
+--------------------------+
*/
