/*
You might notice that when running

SELECT * FROM "listings" LIMIT 5;
the results look quite wonky! The description column contains descriptions with many line breaks,
each of which are printed to your terminal.

In no_descriptions.sql, write a SQL statement to create a view named no_descriptions that includes
all of the columns in the listings table except for description.

select id, property_type, host_name, accommodates, bedrooms from listings limit 5;

*/
CREATE VIEW "no_descriptions" AS
select id, property_type, host_name, accommodates, bedrooms from listings;
