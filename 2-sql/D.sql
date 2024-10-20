SELECT *FROM customer WHERE first_name LIKE 'J%'

SELECT *FROM customer WHERE first_name LIKE '%J'

SELECT COUNT(*)FROM customer WHERE first_name LIKE'J%'

SELECT COUNT(*)FROM customer WHERE first_name LIKE '%J'
	
SELECT COUNT(*)FROM customer WHERE first_name LIKE'J%' AND last_name LIKE 'S%'

SELECT *FROM customer WHERE first_name ILIKE 'j%' AND last_name ILIKE 'j%'

SELECT COUNT(*)FROM customer WHERE first_name ILIKE 'j%' AND last_name ILIKE 'j%'

SELECT *FROM customer WHERE first_name LIKE '%er%'

SELECT COUNT(*)FROM customer WHERE first_name LIKE '%er%'

SELECT *FROM customer WHERE first_name LIKE'%her%'

SELECT *FROM customer WHERE first_name LIKE '_her%'

SELECT *FROM customer WHERE first_name NOT LIKE'_her%'

SELECT *FROM customer WHERE first_name LIKE 'A%' ORDER BY last_name

SELECT *FROM customer WHERE first_name LIKE 'A%' AND last_name NOT LIKE 'B%' ORDER BY last_name

SELECT COUNT(amount) from payment WHERE amount>5

SELECT COUNT(*) FROM actor WHERE first_name LIKE'P%'

SELECT COUNT (DISTINCT(district)) FROM address

SELECT DISTINCT(district) FROM address

SELECT COUNT(*) FROM film WHERE rating='R'AND replacement_cost BETWEEN 5 AND 15

SELECT COUNT(*)FROM film WHERE title LIKE '%Truman%'



