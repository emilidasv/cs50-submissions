CREATE TABLE table_temp (
id INTEGER,
"sentence_nr" INTEGER,
"character_nr" INTEGER,
"message_length" INTEGER,
 PRIMARY KEY("id")
);


.import --csv --skip 1 private.csv table_temp


CREATE VIEW "message" AS
SELECT substr("sentence", "charnr", "msglght") as "phrase"
FROM
(select table_temp."character_nr" as "charnr", table_temp."message_length" as "msglght", sentences.sentence as "sentence" from table_temp
JOIN sentences ON (table_temp.sentence_nr = sentences.id));
