/*13.sql
In 13.sql, write a SQL query to answer a question you have about the data! The query should:

Involve at least one JOIN or subquery
*/

select avg(expenditures.per_pupil_expenditure) , districts.name as 'Average District Per-Pupil Expenditure' from
expenditures JOIN districts ON expenditures.district_id = districts.id group by districts.name;
