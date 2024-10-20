SELECT *FROM job
--INSERT
INSERT INTO job(job_name)VALUES('Cowboy')
SELECT *FROM job

--------------------
--DELETE	
DELETE FROM job WHERE job_name='Cowboy'RETURNING job_id,job_name
SELECT *FROM job

--------------------
	
CREATE TABLE information (info_id SERIAL PRIMARY KEY,title 
	VARCHAR(500) NOT NULL,person VARCHAR(50)NOT NULL UNIQUE)
SELECT * FROM information

--------------------
--ALTER	
ALTER TABLE information RENAME TO new_info
SELECT * FROM information--error=>does not exist
SELECT * FROM new_info

--------------------
	
ALTER TABLE new_info RENAME COLUMN person TO people
SELECT * FROM new_info

--------------------
	
INSERT INTO new_info(title)VALUES('some new title')--ERROR
	
ALTER TABLE new_info ALTER COLUMN people DROP NOT NULL
INSERT INTO new_info(title)VALUES('some new title')
SELECT * FROM new_info

--------------------
	
ALTER TABLE new_info DROP COLUMN people
SELECT * FROM new_info

--------------------
	
ALTER TABLE new_info DROP COLUMN people--error because that column is not exist now

ALTER TABLE new_info DROP COLUMN IF EXISTS people

CREATE TABLE employees(emp_id SERIAL PRIMARY KEY,first_name 
	VARCHAR(50) NOT NULL,last_name VARCHAR(50)NOT NULL,
	birthdate DATE CHECK (birthdate>'1900-01-01'),
	hire_date DATE CHECK (hire_date>birthdate),salary INTEGER CHECK (salary>0) 
)
SELECT *FROM employees

--------------------
	
INSERT INTO employees(first_name,last_name,birthdate,hire_date,salary)
VALUES('Jose','portilla','1990-11-03','2010-01-01',100)
SELECT *FROM employees

--------------------
	
INSERT INTO employees(first_name,last_name,birthdate,hire_date,salary)
VALUES('John','Smith','1990-11-03','2010-01-01',100)
SELECT *FROM employees

--------------------

--CONDITIONAL EXPRESSION
SELECT *FROM customer

SELECT customer_id FROM customer
SELECT customer_id,
CASE
	WHEN (customer_id<=100)THEN 'Premium'
	WHEN(customer_id BETWEEN 100 AND 200)THEN'Plus'
	ELSE'Normal'
END
FROM customer

SELECT customer_id FROM customer
SELECT customer_id,
	CASE
	WHEN (customer_id<100) then 'nikita'
	else'normal'
end
	from customer
	
--------------------
	
SELECT customer_id,
CASE
	WHEN (customer_id<=100)THEN 'Premium'
	WHEN(customer_id BETWEEN 100 AND 200)THEN'Plus'
	ELSE'Normal'
END AS customer_class
FROM customer

--------------------
	
SELECT customer_id,
CASE customer_id
	WHEN 2 THEN 'Winner'
	WHEN 5 THEN 'Second place'
	ELSE 'Normal'
END AS raffle_results	
FROM customer
--------------------------
	
SELECT *FROM film
SELECT rental_rate FROM film

SELECT rental_rate,
CASE rental_rate
	WHEN 0.99 THEN '1'
	WHEN 4.99 THEN '5'
	WHEN 2.99 THEN '3'
	ELSE 'NORMAL'
END 	
FROM film

-----------------
	
SELECT
SUM(CASE rental_rate
	WHEN 0.99 THEN 1
	ELSE 0 
END) AS number_of_bargains
FROM film

--IMPORT\4,EXPORT FUNCTIONALITY OF PGADMIN
























