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
WHERE year = 2023 AND month = 7 AND day =28 AND hour = 10 AND minute = BETWEEN 15 AND 25;




