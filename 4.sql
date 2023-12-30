/*4.sql
Some cities have more public schools than others. In 4.sql, write a SQL query to find the 10 cities with the most public schools.
Your query should return the names of the cities and the number of public schools within them,
ordered from greatest number of public schools to least. If two cities have the same number of public schools, order them alphabetically.
*/
/*
select count(schools.name) , districts.name from schools JOIN districts ON schools.district_id = districts.id
WHERE schools.type LIKE '%pub%' group by districts.id order by count(schools.name) desc , schools.name DESC limit 10;
*/

select count(name) , city from schools WHERE type LIKE '%pub%' group by city order by count(name) DESC, city DESC limit 10;
