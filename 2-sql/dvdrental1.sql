SELECT *FROM payment;

SELECT COUNT(*)FROM payment;

SELECT COUNT(amount)FROM payment;

SELECT amount FROM payment;

SELECT DISTINCT (amount)FROM payment;

SELECT COUNT DISTINCT amount FROM payment;-->it is showing error

SELECT COUNT(DISTINCT amount)FROM payment;

SELECT *FROM customer WHERE first_name='Jared';

SELECT *FROM film WHERE rental_rate >4;

SELECT *FROM film WHERE rental_rate>4 AND replacement_cost>=19.99;

SELECT *FROM film WHERE rental_rate>4 AND replacement_cost>=19.99 AND rating='R';

SELECT title FROM film WHERE rental_rate>4 AND replacement_cost>=19.99 AND rating='R';

SELECT COUNT (title) FROM film WHERE rental_rate>4 AND replacement_cost>=19.99 AND rating='R';

SELECT COUNT(*) FROM film WHERE rental_rate>4 AND replacement_cost>=19.99 AND rating='R';

SELECT COUNT(*)FROM film WHERE rating='R'OR rating='PG-13';

SELECT *FROM film WHERE rating!='R';

/*ch1:A customer forgot their wallet at our store we need to trcak down their email to inform them
what is the email for the customer with the name Nancy Thomas?        
*/

SELECT email FROM customer WHERE first_name='Nancy' AND last_name='Thomas';

SELECT *FROM film
	
/*ch2:A customer wants to know what the movie "Outlaw Hanky" is about
Could you give them the description for the movie "Outlaw Hanky"?*/

SELECT description FROM film WHERE title='Outlaw Hanky'


