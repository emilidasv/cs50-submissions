
-- *** The Lost Letter ***
/*
Clerk, my name’s Anneke. I live over at 900 Somerville Avenue. Not long ago, I sent out a special letter.
It’s meant for my friend Varsha. She’s starting a new chapter of her life at 2 Finnegan Street, uptown.
(That address, let me tell you: it was a bit tricky to get right the first time.) The letter is a congratulatory note—a
cheery little paper hug from me to her, to celebrate this big move of hers. Can you check if it’s made its way to her yet?
*/

SELECT id FROM addresses WHERE "address" = '900 Somerville Avenue';
/* address_id =432*/
SELECT id FROM addresses WHERE "address" = '2 Finnegan Street';
/* no result  hm*/

SELECT id, address FROM addresses WHERE "address" LIKE '%2 Fin%';
/* id 854
+-----+-------------------+
| id  |      address      |
+-----+-------------------+
| 854 | 2 Finnigan Street |
+-----+-------------------+
misspelled?
*/



SELECT id FROM packages WHERE from_address_id = 432;
SELECT address_id,action, driver_id FROM scans WHERE id IN ( SELECT id FROM packages WHERE from_address_id = 432);

SELECT contents, from_address_id, to_address_id FROM packages WHERE from_address_id IN (4792, 6885, 9670,3852);

SELECT addresss FROM addresses WHERE id IN (SELECT address_id FROM scans WHERE package_id IN(384,2437, 3529, 5436));
/*+------------------------+
|        address         |
+------------------------+
| 900 Somerville Avenue  |
| 25 Hancock Street      |
| 59 Ted Williams Way    |
| 73 Yarmouth Place      |
| 2 Finnigan Street      |
| 91 Ward Court          |
| 388 Jackson Avenue     |
| 77 Waverly Place       |
| 24 Morris Street       |
| 558 Camden Street      |
| 950 Brannon Harris Way |
| 8760 Nay Street        |
+------------------------+
SELECT contents, from_address_id, to_address_id FROM packages WHERE to_address_id = 854;
+-----------------------+-----------------+---------------+
|       contents        | from_address_id | to_address_id |
+-----------------------+-----------------+---------------+
| Congratulatory letter | 432             | 854           |
| Push pins             | 7376            | 854           |
+-----------------------+-----------------+---------------+
the packages was deliverd to wrong adress.
*/


SELECT * FROM packages WHERE
from_address_id = (SELECT id FROM addresses WHERE "address" = '900 Somerville Avenue') AND
to_address_id = (SELECT id FROM addresses WHERE "address" LIKE '2 Fin%');

+-----+-----------------------+-----------------+---------------+
| id  |       contents        | from_address_id | to_address_id |
+-----+-----------------------+-----------------+---------------+
| 384 | Congratulatory letter | 432             | 854           |
+-----+-----------------------+-----------------+---------------+

SELECT * FROM scans WHERE package_id = (
    SELECT id FROM packages WHERE
from_address_id = (SELECT id FROM addresses WHERE "address" = '900 Somerville Avenue') AND
to_address_id = (SELECT id FROM addresses WHERE "address" LIKE '2 Fin%')
);
+----+-----------+------------+------------+--------+----------------------------+
| id | driver_id | package_id | address_id | action |         timestamp          |
+----+-----------+------------+------------+--------+----------------------------+
| 54 | 1         | 384        | 432        | Pick   | 2023-07-11 19:33:55.241794 |
| 94 | 1         | 384        | 854        | Drop   | 2023-07-11 23:07:04.432178 |
+----+-----------+------------+------------+--------+----------------------------+
SELECT * FROM addresses WHERE id = 854;
+-----+-------------------+-------------+
| id  |      address      |    type     |
+-----+-------------------+-------------+
| 854 | 2 Finnigan Street | Residential |
+-----+-------------------+-------------+


-- *** The Devious Delivery ***


-- *** The Forgotten Gift ***

