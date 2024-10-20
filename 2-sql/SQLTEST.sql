'''1.	Write a SQL statement to create a simple table countries, 
including columns country_id,country_name and region_id which already exist.
'''
CREATE TABLE countries(country_id SERIAL PRIMARY KEY,country_name VARCHAR(20) UNIQUE NOT NULL,region_id INTEGER UNIQUE NOT NULL)

SELECT *FROM countries;	

'''
2.	Create the two tables Sales and products and insert some sample data into them.
Sales table columns: 
sale_id	product_id	quantity_sold	sale_date	total_price

Products table columns:
product_id	product_name	category	unit_price

Filter the Sales table to show only sales with a total_price greater than $100.
'''
CREATE TABLE Sales(Sale_id SERIAL PRIMARY KEY,product_id INTEGER UNIQUE NOT NULL,quantity_sold INTEGER NOT NULL,sale_date DATE,total_price INTEGER UNIQUE NOT NULL)
INSERT INTO Sales(product_id,quantity_sold,sale_date,total_price)VALUES('1','20','12/05/2023','2000');
INSERT INTO Sales(product_id,quantity_sold,sale_date,total_price)VALUES('2','10','31/05/2023','50');
INSERT INTO Sales(product_id,quantity_sold,sale_date,total_price)VALUES('3','5','16/03/2024','110');
INSERT INTO Sales(product_id,quantity_sold,sale_date,total_price)VALUES('4','15','12/04/2024','90');

SELECT *FROM Sales;

SELECT *FROM Sales WHERE total_price>100;

CREATE TABLE Products(product_id SERIAL PRIMARY KEY,product_name VARCHAR(30) UNIQUE NOT NULL,
	category VARCHAR(50) UNIQUE NOT NULL,unit_price INTEGER UNIQUE NOT NULL);
INSERT INTO Products(product_name,category,unit_price)VALUES('TV','Electronics','20000')
INSERT INTO Products(product_name,category,unit_price)VALUES('Blackboard','non_electronics','10000')
INSERT INTO Products(product_name,category,unit_price)VALUES('notebook','grocerry','100')
INSERT INTO Products(product_name,category,unit_price)VALUES('lipstics','cosmetic','250')

SELECT *FROM Products;

'''
3.	Retrieve the total_price of all sales, rounding the values to two decimal places.
'''	
SELECT round (SUM(total_price),2) FROM Sales ;
'''
	
4.	Calculate the total revenue generated from sales of products in the ‘Electronics’ category.
'''	
SELECT sum(unit_price,)category from Products group by(category)

'''
5.	Retrieve the product_name and category from the Products table, 
	ordering the results by category in ascending order.
'''
SELECT product_name,category FROM Products ORDER BY category;
