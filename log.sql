-- Keep a log of any SQL queries you execute as you solve the mystery.
sqlite3 fiftyville.db

-- which tables to we have i db?
>.tables

> airports              crime_scene_reports   people
atm_transactions      flights               phone_calls
bakery_security_logs  interviews
bank_accounts         passengers


-- Which columns in each tables
>.schema airports

sqlite> .schema airports
CREATE TABLE airports (
    id INTEGER,
    abbreviation TEXT,
    full_name TEXT,
    city TEXT,
    PRIMARY KEY(id)
);
sqlite> .schema crime_scene_reports
CREATE TABLE crime_scene_reports (
    id INTEGER,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    street TEXT,
    description TEXT,
    PRIMARY KEY(id)
);
sqlite> .schema people
CREATE TABLE people (
    id INTEGER,
    name TEXT,
    phone_number TEXT,
    passport_number INTEGER,
    license_plate TEXT,
    PRIMARY KEY(id)
);

sqlite> .schema atm_transactions
CREATE TABLE atm_transactions (
    id INTEGER,
    account_number INTEGER,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    atm_location TEXT,
    transaction_type TEXT,
    amount INTEGER,
    PRIMARY KEY(id)
);
sqlite> .schema flights
CREATE TABLE flights (
    id INTEGER,
    origin_airport_id INTEGER,
    destination_airport_id INTEGER,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    hour INTEGER,
    minute INTEGER,
    PRIMARY KEY(id),
    FOREIGN KEY(origin_airport_id) REFERENCES airports(id),
    FOREIGN KEY(destination_airport_id) REFERENCES airports(id)
);
sqlite> .schema phone_calls
CREATE TABLE phone_calls (
    id INTEGER,
    caller TEXT,
    receiver TEXT,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    duration INTEGER,
    PRIMARY KEY(id)
);
sqlite> .schema bakery_security_logs
CREATE TABLE bakery_security_logs (
    id INTEGER,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    hour INTEGER,
    minute INTEGER,
    activity TEXT,
    license_plate TEXT,
    PRIMARY KEY(id)
);
sqlite> .schema interviews
CREATE TABLE interviews (
    id INTEGER,
    name TEXT,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    transcript TEXT,
    PRIMARY KEY(id)
);

sqlite> .schema bank_accounts
CREATE TABLE bank_accounts (
    account_number INTEGER,
    person_id INTEGER,
    creation_year INTEGER,
    FOREIGN KEY(person_id) REFERENCES people(id)
);

sqlite> .schema passengers
CREATE TABLE passengers (
    flight_id INTEGER,
    passport_number INTEGER,
    seat TEXT,
    FOREIGN KEY(flight_id) REFERENCES flights(id)
);

-- get the crime scene report. We know it  cs50 duck was involved and it happened on Humphrey Street , so two alternative questions. (Gives same answer)
SELECT description  FROM crime_scene_reports where month = 7
and day = 28 and
description like '%%cs50%%';

SELECT description  FROM crime_scene_reports where month = 7
and day = 28 and
street like 'Humphrey Street';

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                       description                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery. Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery. |
| Littering took place at 16:36. No known witnesses.                                                                                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+




-- FRom report we can see that theft of the CS50 duck took place at
-- 10:15am at the Humphrey Street bakery.
-- Interviews were conducted today with three
-- witnesses who were present at the time – each of
-- their interview transcripts mentions the bakery.

--Check the bakery security logs to see who had entered.

SELECT activity, hour, minute, license_plate
FROM bakery_security_logs
WHERE month = 7 and day = 28;

-- Which licence plate was in the bakery at 10:15, i.e. license plate had entered but not exited at 10;15?


--which car had entered before the crime this day?
SELECT activity, hour, minute, license_plate
FROM bakery_security_logs
WHERE month = 7 and day = 28 and
hour < 10 and minute < 16 and
activity = 'entrance';

--Which of them had not already extited from parking lot.
SELECT activity, hour, minute, license_plate
FROM bakery_security_logs
WHERE month = 7 and day = 28 and
hour < 10 and minute < 16 and
activity = 'entrance' and license_plate NOT IN (SELECT license_plate
FROM bakery_security_logs
WHERE month = 7 and day = 28 and
hour < 10 and minute < 16 and
activity = 'exit');


-- But here I assume tha tyou have to entered from parking. But nothing says that the thief entered with a car so assumption is wrong.
-- also if there was someone helping in a car then they migh not be ther ewhen theft happened so these two are not the only one that might is suspect to helped.
-- But they are still suspected to either be thief or helper in a car.
+----------+------+--------+---------------+
| activity | hour | minute | license_plate |
+----------+------+--------+---------------+
| entrance | 9    | 14     | 4328GD8       |
| entrance | 9    | 15     | 5P2BI95       |
+----------+------+--------+---------------+


--Potential suspect cars  4328GD8  and 5P2BI95

comment the first person exit at 10:16 was 5P2BI95

SELECT name from people WHERE license_plate ='5P2BI95';
+---------+
|  name   |
+---------+
| Vanessa |
+---------+

SELECT name from people WHERE license_plate ='4328GD8';
+------+
| name |
+------+
| Luca |

-- CHeck what was said in the interviews.
    --Clue , thief took out money from atm at
    -- clue told someone to buy an ticket from airport same day
    select name, transcript from interviews WHERE month = 7 and day = 28;
--+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
--|  name   |                                                                                                                                                     transcript                                                                                                                                                      |
--+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
--| Jose    | “Ah,” said he, “I forgot that I had not seen you for some weeks. It is a little souvenir from the King of Bohemia in return for my assistance in the case of the Irene Adler papers.”                                                                                                                               |
--| Eugene  | “I suppose,” said Holmes, “that when Mr. Windibank came back from France he was very annoyed at your having gone to the ball.”                                                                                                                                                                                      |
--| Barbara | “You had my note?” he asked with a deep harsh voice and a strongly marked German accent. “I told you that I would call.” He looked from one to the other of us, as if uncertain which to address.                                                                                                                   |
--| Ruth    | Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away. If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.                                                          |
--| Eugene  | I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.                                                                                                 |
--| Raymond | As the thief was leaving the bakery, they called someone who talked to them for less than a minute. In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow. The thief then asked the person on the other end of the phone to purchase the flight ticket. |
--| Lily    | Our neighboring courthouse has a very annoying rooster that crows loudly at 6am every day. My sons Robert and Patrick took the rooster to a city far, far away, so it may never bother us again. My sons have successfully arrived in Paris.                                                                        |
--+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

--Which account number took out money from legget street that day.
select account_number from atm_transactions WHere month = 7 and day = 28 and atm_location like 'Leggett street';


--WHo did take out the money?
--Thief took out money from ATM at Legget street earlier same day

select name from people where id IN (select person_id from bank_accounts where account_number IN (select account_number from atm_transactions WHere month = 7 and day = 28 and atm_location like 'Leggett street'));
+---------+
|  name   |
+---------+
| Kenny   |
| Iman    |
| Benista |
| Taylor  |
| Brooke  |
| Luca    |
| Diana   |
| Bruce   |
| Kaelyn  |
+---------+

-- do the aboev ith join instead.
--First join bank accounts with atm_transactions

select *
from bank_accounts INNER JOIN atm_transactions
ON bank_accounts.account_number  = atm_transactions.account_number;

--second, only choose transactions on leggitt street on 7/28
select *
from bank_accounts INNER JOIN atm_transactions
ON bank_accounts.account_number  = atm_transactions.account_number
WHERE atm_transactions.month = 7 and atm_transactions.day = 28 and atm_transactions.atm_location like "Leggett street";

-- People who took out money on leggit street on 7/28 is:
select name from people
where people.id IN (select bank_accounts.person_id
from bank_accounts INNER JOIN atm_transactions
ON bank_accounts.account_number  = atm_transactions.account_number
WHERE atm_transactions.month = 7 and atm_transactions.day = 28 and atm_transactions.atm_location like "Leggett street");

+---------+
|  name   |
+---------+
| Kenny   |
| Iman    |
| Benista |
| Taylor  |
| Brooke  |
| Luca    |
| Diana   |
| Bruce   |
| Kaelyn  |
+---------+

-- abbreviatrion fro Fiftyvill airport


Select abbreviation from airports where city = 'Fiftyville';
+--------------+
| abbreviation |
+--------------+
| CSF          |
+--------------+
Select id from airports where city = 'Fiftyville';

select id from flights where month = 7 and day = 29 and
origin_airport_id IN (Select id from airports where city = 'Fiftyville');

--WHich flights goes out 7/29 and what time?


select id , hour, minute from flights where month = 7 and day = 29 and
origin_airport_id IN (Select id from airports where city = 'Fiftyville');
+----+------+--------+
| id | hour | minute |
+----+------+--------+
| 18 | 16   | 0      |
| 23 | 12   | 15     |
| 36 | 8    | 20     |
| 43 | 9    | 30     |
| 53 | 15   | 20     |
+----+------+--------+

-- earliest flight tomorrow is 8:20 id 36

-- who is on the flight of the people taking out money
select name from people where id IN (select person_id from bank_accounts where account_number IN (select account_number from atm_transactions WHere month = 7 and day = 28 and atm_location like 'Leggett street')) and passport_number IN(select passport_number from passengers where flight_id = 36 );
+--------+
|  name  |
+--------+
| Kenny  |
| Taylor |
| Luca   |
| Bruce  |
+--------+

--With help of inner join as above
select name from people where id IN

--potential suspect to be thief Kenny, Luca, Taylor, Bruce, They all took out money and have ticket for first flight tomorrow morning.


-- Thief called someone...potentila thiefs phonenumber
select name, phone_number from people where id IN (select person_id from bank_accounts where account_number IN (select account_number from atm_transactions WHere month = 7 and day = 28 and atm_location like 'Leggett street')) and passport_number IN(select passport_number from passe
ngers where flight_id = 36 );
+--------+----------------+
|  name  |  phone_number  |
+--------+----------------+
| Kenny  | (826) 555-1652 |
| Taylor | (286) 555-6063 |
| Luca   | (389) 555-5198 |
| Bruce  | (367) 555-5533 |
+--------+----------------+

select caller, receiver from phone_calls where month = 7 and day = 28 and
caller IN (select phone_number from people where id IN (select person_id from bank_accounts where account_number IN (select account_number from atm_transactions WHere month = 7 and day = 28 and atm_location like 'Leggett street')) and passport_number IN(select passport_number from passengers where flight_id = 36 ));


-- WHo did potential thief call?
select name from people where phone_number IN (select receiver from phone_calls where month = 7 and day = 28 and
caller IN (select phone_number from people where id IN (select person_id from bank_accounts where account_number IN (select account_number from atm_transactions WHere month = 7 and day = 28 and atm_location like 'Leggett street')) and passport_number IN(select passport_number from passengers where flight_id = 36 )));
+---------+
|  name   |
+---------+
| James   |
| Gregory |
| Carl    |
| Robin   |
| Doris   |
| Deborah |
| Angela  |
+---------+

--for less than a minute
select name from people where phone_number IN (select receiver from phone_calls where month = 7 and day = 28 and
duration <60 and
caller IN (select phone_number from people where id IN (select person_id from bank_accounts where account_number IN (select account_number from atm_transactions WHere month = 7 and day = 28 and atm_location like 'Leggett street')) and passport_number IN(select passport_number from passengers where flight_id = 36 )));




--Was ayone of these in the parking lot just ater the duck was stolen? Still at parking lot at 10.36
SELECT license_plate
FROM bakery_security_logs
WHERE month = 7 and day = 28 and
hour < 10 and minute < 36 and
activity = 'entrance' and license_plate NOT IN (SELECT license_plate
FROM bakery_security_logs
WHERE month = 7 and day = 28 and
hour < 10 and minute < 36 and
activity = 'exit');


--THese people were in the parking lot just after the theft
select name from people where license_plate IN (SELECT license_plate
FROM bakery_security_logs
WHERE month = 7 and day = 28 and
hour < 10 and minute < 36 and
activity = 'entrance' and license_plate NOT IN (SELECT license_plate
FROM bakery_security_logs
WHERE month = 7 and day = 28 and
hour < 10 and minute < 36 and
activity = 'exit'));
+---------+
|  name   |
+---------+
| Vanessa |
| Barry   |
| Iman    |
| Sofia   |
| Taylor  |
| Luca    |
| Bruce   |
+---------+

-- DId the phone call got o any of thease cars?

-- potentail helper Bruce and Luca were both in parking lot just after the theftm they were both in the first flight out.
--Both Luca and Bruce took out money same day,




--start over

--Who did take out money and are on the first flight out next morning.
-- earliest flight tomorrow is 8:20 id 36

-- who is on the flight of the people taking out money
select name from people where id IN (select person_id from bank_accounts where account_number IN (select account_number from atm_transactions WHere month = 7 and day = 28 and atm_location like 'Leggett street')) and passport_number IN(select passport_number from passengers where flight_id = 36 );
+--------+
|  name  |
+--------+
| Kenny  |
| Taylor |
| Luca   |
| Bruce  |
+--------+

--Potentiel thiefs are Kenny, Taylor, Luca and Bruce
-- who of them left parking about 10.25 , ten minutes after theft.
select name from people where license_plate IN (SELECT license_plate
FROM bakery_security_logs
WHERE month = 7 and day = 28 and activity ='exit';

-- who of the people that will fliy out and took iut money exited the parking lot that day.
select license_plate , hour, minute FROM bakery_security_logs
WHERE month = 7 and day = 28 and activity ='exit' and
license_plate IN (select license_plate from people where name in
(select name from people where id IN (select person_id from bank_accounts where account_number IN (select account_number from atm_transactions WHere month = 7 and day = 28 and atm_location like 'Leggett street')) and passport_number IN(select passport_number from passengers where flight_id = 36 )
));
+---------------+
| license_plate |
+---------------+
| 94KL13X       |
| 4328GD8       |
| 1106N58       |
+---------------+
SELECT name from people WHERE license_plate ='4328GD8';
+------+
| name |
+------+
| Luca |
+------+
SELECT name from people WHERE license_plate ='94KL13X';
+-------+
| name  |
+-------+
| Bruce |
SELECT name from people WHERE license_plate ='1106N58';
+--------+
|  name  |
+--------+
| Taylor |
+--------+

--when they did leave?
select license_plate , hour, minute FROM bakery_security_logs
WHERE month = 7 and day = 28 and activity ='exit' and
license_plate IN (select license_plate from people where name in
(select name from people where id IN (select person_id from bank_accounts where account_number IN (select account_number from atm_transactions WHere month = 7 and day = 28 and atm_location like 'Leggett street')) and passport_number IN(select passport_number from passengers where flight_id = 36 )
));
+---------------+------+--------+
| license_plate | hour | minute |
+---------------+------+--------+
| 94KL13X       | 10   | 18     |
| 4328GD8       | 10   | 19     |
| 1106N58       | 10   | 35     |
+---------------+------+--------+

--when did they enter?
select license_plate , hour, minute FROM bakery_security_logs
WHERE month = 7 and day = 28 and activity ='entrance' and
license_plate IN (select license_plate from people where name in
(select name from people where id IN (select person_id from bank_accounts where account_number IN (select account_number from atm_transactions WHere month = 7 and day = 28 and atm_location like 'Leggett street')) and passport_number IN(select passport_number from passengers where flight_id = 36 )
));
+---------------+------+--------+
| license_plate | hour | minute |
+---------------+------+--------+
| 94KL13X       | 8    | 23     |
| 1106N58       | 8    | 34     |
| 4328GD8       | 9    | 14     |
+---------------+------+--------+

--they all entered befoer theft and all left after theft. so all can be the thief

-- the thief called someone in parking lot

-- thief drove away 10 minutes after theft.  --> can't be Taylor he left 20 minutes after theft
-- potential thiefs are Bruce and Luca



select name from people where phone_number IN (select receiver from phone_calls where month = 7 and day = 28 and
duration <60 and
caller IN (select phone_number from people where id IN (select person_id from bank_accounts where account_number IN (select account_number from atm_transactions WHere month = 7 and day = 28 and atm_location like 'Leggett street')) and passport_number IN(select passport_number from passengers where flight_id = 36 )));
+-------+
| name  |
+-------+
| James |
| Robin |
| Doris |
+-------+

select name from people where phone_number IN (select receiver from phone_calls where month = 7 and day = 28 and
duration <60 and caller =(367) 555-5533);

sqlite> select phone_number from people where name = 'Bruce';
+----------------+
|  phone_number  |
+----------------+
| (367) 555-5533 |
+----------------+
sqlite> select phone_number from people where name = 'Luca';
+----------------+
|  phone_number  |
+----------------+
| (389) 555-5198 |
+----------------+

select caller, receiver from phone_calls where month = 7 and day = 28 and
duration <60;
+----------------+----------------+
|     caller     |    receiver    |
+----------------+----------------+
| (130) 555-0289 | (996) 555-8899 |
| (499) 555-9472 | (892) 555-8872 |
| (367) 555-5533 | (375) 555-8161 |
| (499) 555-9472 | (717) 555-1342 |
| (286) 555-6063 | (676) 555-6554 |
| (770) 555-1861 | (725) 555-3243 |
| (031) 555-6622 | (910) 555-3251 |
| (826) 555-1652 | (066) 555-9701 |
| (338) 555-6650 | (704) 555-2131 |
+----------------+----------------+

--Bruce did call someone less than 1 minute
--Luca didn't

--Bruce is a the thief.
--Robin is the helper.

-- He went on the plan to New York City


-- the helper (375) 555-8161
select name from people where phone_number = '(375) 555-8161';

select name from people where phone_number = '(375) 555-8161';
+-------+
| name  |
+-------+
| Robin |

select destination_airport_id from flights where id = 36;
+------------------------+
| destination_airport_id |
+------------------------+
| 4                      |
+------------------------+

 select city from airports where id =4;
+---------------+
|     city      |
+---------------+
| New York City |