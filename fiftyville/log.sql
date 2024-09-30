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
-- Raymond- theif made call leaving bakery, asked for first flight out of fiftyville for the next day


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
AND year = 2023 AND month = 7 and day = 28;
-- now we can cross reference these account numbers with namesto see if any of our suspect names match


SELECT 
