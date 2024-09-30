-- Keep a log of any SQL queries you execute as you solve the mystery.

-- All you know is that the theft took place on July 28, 2023
-- and that it took place on Humphrey Street.


-- Find crime scene description
SELECT description
FROM crime_scene_reports
WHERE month = 7 AND day = 28
AND street = 'Humphrey Street';
-- 3 witnesses mentioning bakery,
-- and additional littering crime took place at 4:36pm no witnesses
-- from this I need to search the interviews and bakery_security_logs



