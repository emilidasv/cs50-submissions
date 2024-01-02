CREATE TABLE table_temp (
id INTEGER,
"sentence_nr" INTEGER,
"character_nr" INTEGER,
"message_length" INTEGER,
 PRIMARY KEY("id")
);









INSERT INTO table_temp (id, "sentence_nr","character_nr","message_length" ) VALUES(1,14,98,4);
INSERT INTO table_temp (id, "sentence_nr","character_nr","message_length" ) VALUES(2,114,3,5);
INSERT INTO table_temp (id, "sentence_nr","character_nr","message_length" ) VALUES(3,618,72,9);
INSERT INTO table_temp (id, "sentence_nr","character_nr","message_length" ) VALUES(4,630,7,3);
INSERT INTO table_temp (id, "sentence_nr","character_nr","message_length" ) VALUES(5,932,12,5);
INSERT INTO table_temp (id, "sentence_nr","character_nr","message_length" ) VALUES(6,2230,50,7);
INSERT INTO table_temp (id, "sentence_nr","character_nr","message_length" ) VALUES(7,2346,44,10);
INSERT INTO table_temp (id, "sentence_nr","character_nr","message_length" ) VALUES(8,3041,14,5);

/*.import --csv --skip 1 private.csv table_temp*/


CREATE VIEW "message" AS
SELECT substr("sentence", "charnr", "msglght") as "phrase"
FROM
(select table_temp."character_nr" as "charnr", table_temp."message_length" as "msglght", sentences.sentence as "sentence" from table_temp
JOIN sentences ON (table_temp.sentence_nr = sentences.id));
