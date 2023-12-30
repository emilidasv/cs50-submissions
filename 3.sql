/*3.sql
The Massachusetts Legislature would like to learn how much money, on average, districts spent per-pupil last year.
In 3.sql, write a SQL query to find the average per-pupil expenditure. Name the column “Average District Per-Pupil Expenditure”.

Note the per_pupil_expenditure column in the expenditures table contains the average amount, per pupil, each district spent last year.
You’ve been asked to find the average of this set of averages, weighting all districts equally regardless of their size.
*/

select avg(per_pupil_expenditure) as 'Average District Per-Pupil Expenditure' from expenditures;

/*select avg(per_pupil_expenditure) as 'Average District Per-Pupil Expenditure' , district_id from expenditures group by district_id;

select avg(expenditures.per_pupil_expenditure) , districts.name as 'Average District Per-Pupil Expenditure' from
expenditures JOIN districts ON expenditures.district_id = districts.id group by districts.name;

select count(*) from
expenditures JOIN districts ON expenditures.district_id = districts.id;
*/
/*
Executing 3.sql results in a table with 1 column and 1 row.
Executing 4.sql results in a table with 2 columns and 10 rows.
Executing 5.sql results in a table with 2 columns and 201 rows.
Executing 6.sql results in a table with 1 column and 9 rows.
Executing 7.sql results in a table with 1 column and 17 rows.
Executing 8.sql results in a table with 2 columns and 396 rows.
Executing 9.sql results in a table with 1 column and 1 row.
Executing 10.sql results in a table with 2 columns and 10 rows.
Executing 11.sql results in a table with 3 columns and 391 rows.
Executing 12.sql results in a table with 3 columns and 65 rows.
*/




