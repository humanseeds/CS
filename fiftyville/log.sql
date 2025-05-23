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
-- we can now reference these 4 names with flight tickets and phone calls.


SELECT people.name, phone_calls.caller, phone_calls.receiver, phone_calls.duration
FROM phone_calls
JOIN people ON phone_calls.caller = people.phone_number
WHERE phone_calls.year = 2023 AND phone_calls.month = 7 AND phone_calls.day = 28 and
phone_calls.duration < 60;
-- Now we have two main suspects Bruce and Diana!
-- after searching passenger info on flights to determine the thief, we can use these
-- phone numbers to find the accomplice
-- Bruce   | (367) 555-5533 | (375) 555-8161 | 45
-- Diana   | (770) 555-1861 | (725) 555-3243 | 49
-- Now lets check the flights, to find the first flight out of fiftyville
-- along with the passenger list and destination


SELECT flights.*,origin_airports.full_name AS origin_name, destination_airports.full_name AS destination_name
FROM flights
JOIN airports AS origin_airports ON flights.origin_airport_id = origin_airports.id
JOIN airports AS destination_airports ON flights.destination_airport_id = destination_airports.id
WHERE origin_airports.city LIKE '%Fiftyville%'
AND flights.year = 2023 AND flights.month = 7 AND flights.day = 29
ORDER BY flights.hour, flights.minute
LIMIT 1;
-- we know the city is Fiftyville,so after searching for the next flight out of the city of Fiftyville we find a flight from
-- ID 36 from Fiftyville Regional Airport to LaGuaria Airport! the Thief went to new York! Now we can check the passengers for the flight


SELECT people.name, people.passport_number
FROM passengers
JOIN people ON passengers.passport_number = people.passport_number
WHERE passengers.flight_id = "36";
AND (people.name = 'Bruce' OR people.name = 'Diana');
-- Bruce is the thief! we know this from her licence plate, atm record, and now verified with flight record to New York
-- now we need to check her phone records and see who she called


Select people.name, people.phone_number
FROM people
WHERE people.phone_number = '(375) 555-8161';
--since we already have the call record from Bruce from earlier, a simple search showed us that the accomplice is Robin
