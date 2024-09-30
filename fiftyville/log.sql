-- Keep a log of any SQL queries you execute as you solve the mystery.

-- All you know is that the theft took place on July 28, 2023
-- and that it took place on Humphrey Street.


-- Find crime scene description
SELECT description
FROM crime_scene_reports
WHERE month = 7 AND day = 28
AND street = 'Humphrey Street';
-- Theft at 10:15 at bakery. 3 witnesses
-- check the bakery


SELECT *
FROM interviews
WHERE transcript LIKE '%bakery%';
-- Ruth-check footage for vehicle within 10 minutes of crime (10:15-10:25)
-- Eugene-check ATM on Leggett Street
-- Raymond- theif made call < 1min leaving bakery, asked for first flight out of fiftyville for the next day


SELECT *
FROM bakery_security_logs
WHERE year = 2023 AND month = 7 AND day = 28 AND hour = 10 AND minute BETWEEN 15 AND 25;
--this gives 8 different license plates. if we combine this table with people.license_plate we can find
-- 8 names and the suspect must be one of those names. from there we can check atm transactions of those people
--and also check phone call records from those people to find the accomplice


SELECT people.name, bakery_security_logs.activity, bakery_security_logs.license_plate, bakery_security_logs.year,
bakery_security_logs.month, bakery_security_logs.day, bakery_security_logs.hour, bakery_security_logs.minute
FROM bakery_security_logs
JOIN people ON people.license_plate = bakery_security_logs.license_plate
WHERE year = 2023 AND month = 7 AND day = 28 AND hour = 10 AND minute BETWEEN 15 AND 25;
-- Vanessa, Bruce, Barry, Luca, Sofia, Iman, Diana, Kelsey. now we can cross reference these names from atm


SELECT *
FROM atm_transactions
WHERE atm_location = 'Leggett Street'
AND year = 2023 AND month = 7 AND day = 28;
-- now we can cross reference these account numbers with names to see if any of our suspect names match


SELECT name
FROM people
JOIN bank_accounts ON people.id = bank_accounts.person_id
JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number
WHERE atm_location = 'Leggett Street'
AND year = 2023 AND month = 7 AND day = 28 AND transaction_type = 'withdraw';
--with this list we see 4 common suspects, Bruce, Diana, Iman, and Luca!
-- we can no reference these 4 names with flight tickets and phone calls.


SELECT people.name, phone_calls.caller, phone_calls.receiver, phone_calls.duration
FROM phone_calls
JOIN people ON phone_calls.caller = people.phone_number
WHERE phone_calls.year = 2023 AND phone_calls.month = 7 AND phone_calls.day = 28 and
phone_calls.duration < 60;
-- Now we have two main suspects Bruce and Diana!
-- Now lets check the flights, to find the first flight out of fiftyville
-- along with the passenger list and destination


SELECT full_name
FROm airports
WHERE city = 'fiftyville';
