SELECT amount AS rental_price FROM payment

SELECT SUM (amount) AS net_revenue FROM payment

SELECT COUNT(amount) AS num_transactions FROM payment

SELECT COUNT (*) AS num_transactions FROM payment

SELECT customer_id,SUM(amount) FROM payment GROUP BY customer_id

SELECT customer_id,SUM(amount) AS total_spent FROM payment GROUP BY customer_id

SELECT customer_id,SUM(amount) AS total_spent FROM payment 
	GROUP BY customer_id HAVING SUM(amount)>100 
	
--#############################
	
--JOINS--

--INNER JOIN--
SELECT *from payment

SELECT payment_id,payment.customer_id,first_name 
	FROM payment INNER JOIN customer ON payment.customer_id=customer.customer_id


--by changing the order also gives the same result
SELECT payment_id,payment.customer_id,first_name 
	FROM customer INNER JOIN payment ON payment.customer_id=customer.customer_id

select payment_id,payment.customer_id,first_name from payment inner join 
	customer on customer.customer_id=payment.customer_id	
	
--FULL JOIN--
	
SELECT *FROM customer FULL OUTER JOIN payment ON customer.customer_id=payment.customer_id
	
--LEFT JOIN--
	
SELECT *FROM film

SELECT *FROM inventory

SELECT film.film_id,title,inventory_id FROM film LEFT JOIN inventory ON
	inventory.film_id=film.film_id
	
SELECT film.film_id,title,inventory_id,store_id FROM film LEFT JOIN inventory ON
	inventory.film_id=film.film_id

SELECT film.film_id,title,inventory_id,store_id FROM film LEFT JOIN inventory ON
	inventory.film_id=film.film_id WHERE inventory.film_id IS null

--RIGHT JOIN--

SELECT film.film_id,title,inventory_id,store_id FROM inventory RIGHT JOIN film ON
	inventory.film_id=film.film_id 

SELECT film.film_id,title,inventory_id,store_id FROM inventory RIGHT JOIN film ON
	inventory.film_id=film.film_id WHERE inventory.film_id IS null

--CHALLENGE 1	
SELECT *FROM customer

SELECT *FROM address

SELECT *FROM address INNER JOIN customer ON address.address_id=customer.address_id

SELECT *FROM address INNER JOIN customer ON address.address_id=customer.address_id
	WHERE district='California'

SELECT district,email FROM address INNER JOIN customer 
	ON address.address_id=customer.address_id WHERE district='California'

--CHALLENGE 2	
SELECT *FROM film

SELECT *FROM actor

SELECT *FROM film_actor

SELECT *FROM actor INNER JOIN film_actor ON actor.actor_id=film_actor.actor_id

SELECT *FROM actor INNER JOIN film_actor ON actor.actor_id=film_actor.actor_id 
	INNER JOIN film ON film_actor.film_id=film.film_id

SELECT title,first_name,last_name FROM actor INNER JOIN film_actor ON actor.actor_id=film_actor.actor_id 
	INNER JOIN film ON film_actor.film_id=film.film_id

SELECT title,first_name,last_name FROM actor INNER JOIN film_actor 
	ON actor.actor_id=film_actor.actor_id 
	INNER JOIN film ON film_actor.film_id=film.film_id 
	WHERE first_name='Nick' AND last_name='Wahlberg'

SELECT *FROM payment






