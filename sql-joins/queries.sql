-- Joining two tables so that every column and record appears, regardless of if there is an owner_id.
SELECT * FROM owners 
FULL JOIN vehicles 
ON owners.id = vehicles.owner_id;

-- Count the number of cars for each owner. Display the owners first_name, last_name and count of vehicles.
-- The first_name should be ordered in ascending order.
SELECT o.first_name, o.last_name, COUNT(*)
FROM owners o 
FULL JOIN vehicles v 
ON o.id = v.owner_id 
GROUP BY (first_name, last_name) 
ORDER BY first_name;

-- Count the number of cars for each owner and display the average price for each of the cars as integers. Display the owners
-- first_name, last_name, average price and count of vehicles. The first_name should be ordered in descending order. Only
-- display the results with more than one vehicle and an average price greater than 10000.

SELECT o.first_name, o.last_name, ROUND(AVG(price)) AS average_price, COUNT(*)
FROM owners o 
FULL JOIN vehicles v 
ON o.id = v.owner_id 
GROUP BY (first_name, last_name)
HAVING COUNT(*) > 1 AND ROUND(AVG(price)) > 10000
ORDER BY first_name desc;
