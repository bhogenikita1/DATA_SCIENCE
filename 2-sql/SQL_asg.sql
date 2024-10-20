/*Assignment-1 
Create table with following specifications
•	log_id: A primary key with SERIAL key to uniquely identify each log entry.
•	machine_id: The ID of the machine.
•	production_date: The date of production.
•	production_shift: The shift during which production took place (e.g., 'Morning', 'Evening').
•	products_produced: The number of products produced during the shift.
•	defects: The number of defective products.
•	runtime: The total runtime of the machine during the shift in hours.
Enter the following data
(1, '2024-06-01', 'Morning', 500, 5, 8.0), (1, '2024-06-01', 'Evening', 450, 3, 7.5), 
	(2, '2024-06-01', 'Morning', 480, 2, 7.8), (2, '2024-06-01', 'Evening', 470, 4, 8.1), 
	(3, '2024-06-01', 'Morning', 510, 6, 8.2), (3, '2024-06-01', 'Evening', 520, 1, 7.9), 
	(1, '2024-06-02', 'Morning', 490, 3, 8.0), (1, '2024-06-02', 'Evening', 460, 2, 7.6),
	(2, '2024-06-02', 'Morning', 475, 1, 7.9), (2, '2024-06-02', 'Evening', 465, 5, 8.3), 
	(3, '2024-06-02', 'Morning', 505, 4, 8.0), (3, '2024-06-02', 'Evening', 515, 3, 8.2);
	
 In Manufacturers monitor production data to ensure efficient operations and quality control, 
	identify machines with the highest defect rates and their average runtimes.
--==>
*/
CREATE TABLE production_logs(log_id SERIAL PRIMARY KEY,machine_id INTEGER NOT NULL,
	production_date DATE NOT NULL ,production_shift VARCHAR(50) NOT NULL,products_produced INTEGER NOT NULL,
	defects INTEGER NOT NULL,runtime FLOAT NOT NULL 
	) 

SELECT *FROM production_logs
	
INSERT INTO production_logs (machine_id,production_date,production_shift,products_produced,defects,runtime)
	VALUES(1, '2024-06-01', 'Morning', 500, 5, 8.0), (1, '2024-06-01', 'Evening', 450, 3, 7.5), 
	(2, '2024-06-01', 'Morning', 480, 2, 7.8), (2, '2024-06-01', 'Evening', 470, 4, 8.1), 
	(3, '2024-06-01', 'Morning', 510, 6, 8.2), (3, '2024-06-01', 'Evening', 520, 1, 7.9), 
	(1, '2024-06-02', 'Morning', 490, 3, 8.0), (1, '2024-06-02', 'Evening', 460, 2, 7.6),
	(2, '2024-06-02', 'Morning', 475, 1, 7.9), (2, '2024-06-02', 'Evening', 465, 5, 8.3), 
	(3, '2024-06-02', 'Morning', 505, 4, 8.0), (3, '2024-06-02', 'Evening', 515, 3, 8.2);

SELECT *FROM production_logs

SELECT machine_id ,AVG (defects::FLOAT/products_produced)AS defect_rate,AVG(runtime) 
	AS avg_runtime FROM production_logs GROUP BY machine_id ORDER BY defect_rate DESC

/*
Assignment- 2)
Create table with following specifications
•	grade_id: A primary key with auto-increment to uniquely identify each grade entry.
•	student_id: The ID of the student.
•	course_id: The ID of the course.
•	grade: The grade received by the student.
•	grade_date: The date when the grade was recorded.
Insert following values
(1, 101, 85.5, '2024-01-15'), (1, 102, 78.0, '2024-02-20'), (2, 101, 92.0, '2024-01-15'),
	(2, 103, 88.5, '2024-03-10'), (3, 102, 74.0, '2024-02-20'), (3, 103, 81.5, '2024-03-10'), 
	(4, 101, 67.0, '2024-01-15'), (4, 104, 90.0, '2024-04-05'), (5, 102, 85.0, '2024-02-20'), 
	(5, 104, 87.0, '2024-04-05');
	
Educational institutions track student performance to provide targeted support and interventions.
identify students with an average grade below a passing threshold in their courses.
==>*/
CREATE TABLE student(grade_id SERIAL PRIMARY KEY,student_id INTEGER NOT NULL,course_id INTEGER NOT NULL, 
	grade FLOAT NOT NULL,grade_date DATE NOT NULL)
DROP TABLE student
SELECT *FROM student
	
INSERT INTO student(student_id,course_id,grade,grade_date)
VALUES(1, 101, 85.5, '2024-01-15'), (1, 102, 78.0, '2024-02-20'), (2, 101, 92.0, '2024-01-15'),
	(2, 103, 88.5, '2024-03-10'), (3, 102, 74.0, '2024-02-20'), (3, 103, 81.5, '2024-03-10'), 
	(4, 101, 67.0, '2024-01-15'), (4, 104, 90.0, '2024-04-05'), (5, 102, 85.0, '2024-02-20'), 
	(5, 104, 87.0, '2024-04-05');

SELECT *FROM student	

/*Educational institutions track student performance to provide targeted support and interventions.
identify students with an average grade below a passing threshold in their courses.
*/	
SELECT student_id,AVG(grade) AS avg_grade 
FROM student 
GROUP BY student_id
HAVING AVG(grade) <80

/*Assignment-3
Create table with following specifications
Creation:
•	customer_id: A primary key with auto-increment to uniquely identify each customer.
•	first_name: The first name of the customer.
•	last_name: The last name of the customer.
•	email: The email address of the customer.
•	phone_number: The phone number of the customer.
•	address: The street address of the customer.
•	city: The city where the customer lives.
•	state: The state where the customer lives.
•	zip_code: The postal code of the customer's address.
•	plan_id: The ID of the customer's telecom plan.
•	last_call_date: The date of the customer's last call.
Insert following values
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Elm St', 'Springfield', 'IL', '62701', 1, '2024-06-01'),
('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', '456 Oak St', 'Springfield', 'IL', '62701', 2, '2024-05-15'),
('Alice', 'Johnson', 'alice.johnson@example.com', '555-123-4567', '789 Pine St', 'Shelbyville', 'IL', '62565', 3, '2024-04-20'),
('Bob', 'Brown', 'bob.brown@example.com', '444-555-6666', '101 Maple St', 'Capital City', 'IL', '62702', 1, '2024-06-10'), 
('Charlie', 'Davis', 'charlie.davis@example.com', '333-444-5555', '202 Cedar St', 'Springfield', 'IL', '62701', 2, '2024-03-30'),
('Diana', 'Evans', 'diana.evans@example.com', '222-333-4444', '303 Birch St', 'Shelbyville', 'IL', '62565', 3, '2024-06-20'), 
('Ethan', 'Foster', 'ethan.foster@example.com', '111-222-3333', '404 Spruce St', 'Capital City', 'IL', '62702', 1, '2024-02-14'),
('Fiona', 'Garcia', 'fiona.garcia@example.com', '999-888-7777', '505 Ash St', 'Springfield', 'IL', '62701', 2, '2024-05-05'), 
('George', 'Harris', 'george.harris@example.com', '888-777-6666', '606 Walnut St', 'Shelbyville', 'IL', '62565', 3, '2024-01-25'), 
('Hannah', 'Irvine', 'hannah.irvine@example.com', '777-666-5555', '707 Hickory St', 'Capital City', 'IL', '62702', 1, '2024-06-22');

Telecom companies analyze customer data to identify patterns that indicate potential churn.
categorizes customers based on their activity levels, indicating their risk of churn.
*/
CREATE TABLE customer_detail(customer_id SERIAL PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	email VARCHAR (100)NOT NULL,
	phone_number VARCHAR(15)NOT NULL,
	address VARCHAR(200)NOT NULL,
	city VARCHAR(50)NOT NULL,
	state VARCHAR(50) NOT NULL,
	zip_code VARCHAR(10)NOT NULL,
	plan_id INTEGER NOT NULL,
	last_call_date DATE NOT NULL)
--DROP TABLE customer_detail	
SELECT *FROM customer_detail

INSERT INTO customer_detail(first_name,last_name,email,phone_number,address,city,
	state,zip_code,plan_id,last_call_date)VALUES
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Elm St', 'Springfield', 'IL', '62701', 1, '2024-06-01'),
('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', '456 Oak St', 'Springfield', 'IL', '62701', 2, '2024-05-15'),
('Alice', 'Johnson', 'alice.johnson@example.com', '555-123-4567', '789 Pine St', 'Shelbyville', 'IL', '62565', 3, '2024-04-20'),
('Bob', 'Brown', 'bob.brown@example.com', '444-555-6666', '101 Maple St', 'Capital City', 'IL', '62702', 1, '2024-06-10'), 
('Charlie', 'Davis', 'charlie.davis@example.com', '333-444-5555', '202 Cedar St', 'Springfield', 'IL', '62701', 2, '2024-03-30'),
('Diana', 'Evans', 'diana.evans@example.com', '222-333-4444', '303 Birch St', 'Shelbyville', 'IL', '62565', 3, '2024-06-20'), 
('Ethan', 'Foster', 'ethan.foster@example.com', '111-222-3333', '404 Spruce St', 'Capital City', 'IL', '62702', 1, '2024-02-14'),
('Fiona', 'Garcia', 'fiona.garcia@example.com', '999-888-7777', '505 Ash St', 'Springfield', 'IL', '62701', 2, '2024-05-05'), 
('George', 'Harris', 'george.harris@example.com', '888-777-6666', '606 Walnut St', 'Shelbyville', 'IL', '62565', 3, '2024-01-25'), 
('Hannah', 'Irvine', 'hannah.irvine@example.com', '777-666-5555', '707 Hickory St', 'Capital City', 'IL', '62702', 1, '2024-06-22');

SELECT *FROM customer_detail
/*Telecom companies analyze customer data to identify patterns that indicate potential churn.
categorizes customers based on their activity levels, indicating their risk of churn.*/
SELECT 
    customer_id,
    first_name,
    last_name,
    email,
    last_call_date,
    CASE
        WHEN last_call_date >= CURRENT_DATE - INTERVAL '30 days' THEN 'Active'
        WHEN last_call_date >= CURRENT_DATE - INTERVAL '90 days' THEN 'At Risk'
        ELSE 'Inactive'
    END AS activity_level
FROM 
    customer_detail

	
/*Assignment-4	
•   Table Creation:
•	product_id: A primary key with auto-increment to uniquely identify each product.
•	product_name: The name of the product.
•	category: The category to which the product belongs.
•	quantity: The quantity of the product in stock.
•	price: The price of the product.
•	supplier: The supplier of the product.
•	last_restock_date: The date when the product was last restocked.
•  Inserting Data:
('Laptop', 'Electronics', 50, 799.99, 'TechSupplier Inc.', '2024-06-01'), 
('Smartphone', 'Electronics', 150, 499.99, 'MobileDistributors Ltd.', '2024-05-25'), 
('Desk Chair', 'Furniture', 80, 89.99, 'OfficeSupplies Co.', '2024-05-15'), 
('Notebook', 'Stationery', 200, 2.99, 'PaperGoods Inc.', '2024-06-10'), 
('Water Bottle', 'Accessories', 120, 9.99, 'Lifestyle Products', '2024-06-05'), 
('Headphones', 'Electronics', 70, 149.99, 'TechSupplier Inc.', '2024-06-08'), 
('Desk Lamp', 'Furniture', 60, 29.99, 'OfficeSupplies Co.', '2024-05-20'), 
('Backpack', 'Accessories', 90, 49.99, 'TravelGear Ltd.', '2024-06-12'),
('Pen', 'Stationery', 300, 1.49, 'PaperGoods Inc.', '2024-06-03'),
('Monitor', 'Electronics', 40, 199.99, 'TechSupplier Inc.', '2024-06-15');
	
Retailers need to manage their inventory to ensure products are in stock and to avoid overstocking.
	identify products with low stock levels.

*/
CREATE TABLE product_details(product_id SERIAL PRIMARY KEY,product_name VARCHAR(50) 
NOT NULL,cattegory VARCHAR(50) NOT NULL, quantity INTEGER NOT NULL,price FLOAT 
NOT NULL,supplier VARCHAR(50) NOT NULL,last_restock_date DATE NOT NULL)
		
SELECT *FROM product_details

INSERT INTO product_details(product_name,cattegory,quantity,price,supplier,last_restock_date)
VALUES('Laptop', 'Electronics', 50, 799.99, 'TechSupplier Inc.', '2024-06-01'), 
		('Smartphone', 'Electronics', 150, 499.99, 'MobileDistributors Ltd.', '2024-05-25'), 
		('Desk Chair', 'Furniture', 80, 89.99, 'OfficeSupplies Co.', '2024-05-15'), 
		('Notebook', 'Stationery', 200, 2.99, 'PaperGoods Inc.', '2024-06-10'), 
		('Water Bottle', 'Accessories', 120, 9.99, 'Lifestyle Products', '2024-06-05'), 
		('Headphones', 'Electronics', 70, 149.99, 'TechSupplier Inc.', '2024-06-08'), 
		('Desk Lamp', 'Furniture', 60, 29.99, 'OfficeSupplies Co.', '2024-05-20'), 
		('Backpack', 'Accessories', 90, 49.99, 'TravelGear Ltd.', '2024-06-12'),
		('Pen', 'Stationery', 300, 1.49, 'PaperGoods Inc.', '2024-06-03'),
		('Monitor', 'Electronics', 40, 199.99, 'TechSupplier Inc.', '2024-06-15');	

SELECT *FROM product_details

SELECT product_id,product_name,cattegory,quantity,price,supplier, last_restock_date 
FROM product_details 
WHERE quantity<=75


/*Assignment-5
  Table Creation:
•	patient_id: A primary key with auto-increment to uniquely identify each patient.
•	first_name: The first name of the patient.
•	last_name: The last name of the patient.
•	date_of_birth: The date of birth of the patient.
•	gender: The gender of the patient.
•	phone_number: The phone number of the patient.
•	email: The email address of the patient.
•	address: The street address of the patient.
•	city: The city where the patient lives.
•	state: The state where the patient lives.
•	zip_code: The postal code of the patient's address.
•	medical_history: A text field to store the medical history of the patient.
•	last_visit_date: The date of the patient's last visit.
•  Inserting Data:
('John', 'Doe', '1980-01-15', 'Male', '123-456-7890', 'john.doe@example.com', '123 Elm St', 'Springfield', 'IL', '62701', 'Hypertension', '2024-06-01'),
('Jane', 'Smith', '1990-02-20', 'Female', '987-654-3210', 'jane.smith@example.com', '456 Oak St', 'Springfield', 'IL', '62701', 'Diabetes', '2024-05-25'), 
('Alice', 'Johnson', '1975-03-30', 'Female', '555-123-4567', 'alice.johnson@example.com', '789 Pine St', 'Shelbyville', 'IL', '62565', 'Asthma', '2024-06-10'),
('Bob', 'Brown', '1965-04-10', 'Male', '444-555-6666', 'bob.brown@example.com', '101 Maple St', 'Capital City', 'IL', '62702', 'High Cholesterol', '2024-05-15'), 
('Charlie', 'Davis', '1985-05-20', 'Male', '333-444-5555', 'charlie.davis@example.com', '202 Cedar St', 'Springfield', 'IL', '62701', 'Allergies', '2024-06-05'), 
('Diana', 'Evans', '2000-06-25', 'Female', '222-333-4444', 'diana.evans@example.com', '303 Birch St', 'Shelbyville', 'IL', '62565', 'Migraine', '2024-06-20'), 
('Ethan', 'Foster', '1970-07-15', 'Male', '111-222-3333', 'ethan.foster@example.com', '404 Spruce St', 'Capital City', 'IL', '62702', 'Arthritis', '2024-06-12'), 
('Fiona', 'Garcia', '1995-08-10', 'Female', '999-888-7777', 'fiona.garcia@example.com', '505 Ash St', 'Springfield', 'IL', '62701', 'Depression', '2024-05-30'), 
('George', 'Harris', '1988-09-05', 'Male', '888-777-6666', 'george.harris@example.com', '606 Walnut St', 'Shelbyville', 'IL', '62565', 'Hypertension', '2024-04-25'), 
('Hannah', 'Irvine', '1992-10-12', 'Female', '777-666-5555', 'hannah.irvine@example.com', '707 Hickory St', 'Capital City', 'IL', '62702', 'Diabetes', '2024-06-22');

	Healthcare providers need to manage patient records efficiently for better healthcare delivery.
	Write query retrieves patient information for those who visited within a specific date range.
*/
CREATE TABLE patient(patient_id SERIAL PRIMARY KEY,first_name VARCHAR(50) NOT NULL,last_name VARCHAR(50)NOT NULL,
	date_of_birth DATE NOT NULL,gender VARCHAR(10)NOT NULL,phone_number VARCHAR(15) NOT NULL,
	email VARCHAR(100)NOT NULL, address VARCHAR(100) NOT NULL,city VARCHAR(20)NOT NULL, state VARCHAR(20) NOT NULL,
	zip_code INTEGER NOT NULL, medical_history VARCHAR(100) NOT NULL,last_visit_date DATE NOT NULL)

SELECT *FROM patient
DROP TABLE patient
INSERT INTO patient(first_name,last_name,date_of_birth,gender,phone_number,email,
	address,city,state,zip_code,medical_history,last_visit_date)VALUES
('John', 'Doe', '1980-01-15', 'Male', '123-456-7890', 'john.doe@example.com', '123 Elm St', 'Springfield', 'IL', '62701', 'Hypertension', '2024-06-01'),
('Jane', 'Smith', '1990-02-20', 'Female', '987-654-3210', 'jane.smith@example.com', '456 Oak St', 'Springfield', 'IL', '62701', 'Diabetes', '2024-05-25'), 
('Alice', 'Johnson', '1975-03-30', 'Female', '555-123-4567', 'alice.johnson@example.com', '789 Pine St', 'Shelbyville', 'IL', '62565', 'Asthma', '2024-06-10'),
('Bob', 'Brown', '1965-04-10', 'Male', '444-555-6666', 'bob.brown@example.com', '101 Maple St', 'Capital City', 'IL', '62702', 'High Cholesterol', '2024-05-15'), 
('Charlie', 'Davis', '1985-05-20', 'Male', '333-444-5555', 'charlie.davis@example.com', '202 Cedar St', 'Springfield', 'IL', '62701', 'Allergies', '2024-06-05'), 
('Diana', 'Evans', '2000-06-25', 'Female', '222-333-4444', 'diana.evans@example.com', '303 Birch St', 'Shelbyville', 'IL', '62565', 'Migraine', '2024-06-20'), 
('Ethan', 'Foster', '1970-07-15', 'Male', '111-222-3333', 'ethan.foster@example.com', '404 Spruce St', 'Capital City', 'IL', '62702', 'Arthritis', '2024-06-12'), 
('Fiona', 'Garcia', '1995-08-10', 'Female', '999-888-7777', 'fiona.garcia@example.com', '505 Ash St', 'Springfield', 'IL', '62701', 'Depression', '2024-05-30'), 
('George', 'Harris', '1988-09-05', 'Male', '888-777-6666', 'george.harris@example.com', '606 Walnut St', 'Shelbyville', 'IL', '62565', 'Hypertension', '2024-04-25'), 
('Hannah', 'Irvine', '1992-10-12', 'Female', '777-666-5555', 'hannah.irvine@example.com', '707 Hickory St', 'Capital City', 'IL', '62702', 'Diabetes', '2024-06-22');

SELECT*FROM patient

SELECT patient_id,first_name,last_name,date_of_birth,gender,phone_number,email,address,city,
    state,zip_code,medical_history,last_visit_date
FROM patient
WHERE last_visit_date BETWEEN '2024-05-01' AND '2024-05-31'


/*Assignment-6
Financial institutions need to detect and prevent fraudulent transactions. 
Write query identifies transactions above a certain threshold within a specified date range
for further investigation. 
Table Creation:
•	transaction_id: A primary key with auto-increment to uniquely identify each transaction.
•	account_id: The ID of the account associated with the transaction.
•	transaction_date: The date and time when the transaction occurred.
•	transaction_amount: The amount of money involved in the transaction.
•	transaction_type: The type of transaction (e.g., 'Credit', 'Debit').
•	merchant: The merchant where the transaction occurred.
•	location: The location of the merchant.
•	status: The status of the transaction (e.g., 'Completed', 'Pending').
Inserting Data:
(1, '2024-06-01 10:00:00', 1000.00, 'Credit', 'Amazon', 'Online', 'Completed'), 
(1, '2024-06-01 12:30:00', 500.00, 'Debit', 'Walmart', 'Springfield', 'Completed'), 
(2, '2024-06-02 09:45:00', 15000.00, 'Credit', 'Apple Store', 'Chicago', 'Pending'), 
(2, '2024-06-02 11:00:00', 200.00, 'Debit', 'Starbucks', 'Chicago', 'Completed'), 
(3, '2024-06-03 14:15:00', 250.00, 'Debit', 'Target', 'Springfield', 'Completed'), 
(3, '2024-06-03 16:20:00', 30000.00, 'Credit', 'Tesla', 'San Francisco', 'Pending'), 
(4, '2024-06-04 08:30:00', 120.00, 'Debit', 'McDonalds', 'Springfield', 'Completed'), 
(4, '2024-06-04 10:50:00', 6000.00, 'Credit', 'Best Buy', 'Chicago', 'Pending'), 
(5, '2024-06-05 15:10:00', 70.00, 'Debit', 'CVS Pharmacy', 'Springfield', 'Completed'),
(5, '2024-06-05 17:00:00', 22000.00, 'Credit', 'Louis Vuitton', 'New York', 'Pending');
*/

CREATE TABLE transactions(transaction_id SERIAL PRIMARY KEY,account_id INTEGER NOT NULL,transaction_date TIMESTAMP NOT NULL,
	transaction_amount FLOAT NOT NULL, transaction_type VARCHAR(10)NOT NULL,merchant VARCHAR(50)NOT NULL,
	location VARCHAR(50) NOT NULL,status VARCHAR(15)NOT NULL)

SELECT *FROM transactions
DROP TABLE transactions
INSERT INTO transactions(account_id,transaction_date,transaction_amount,transaction_type,merchant,location,status)
VALUES(1, '2024-06-01 10:00:00', 1000.00, 'Credit', 'Amazon', 'Online', 'Completed'), 
(1, '2024-06-01 12:30:00', 500.00, 'Debit', 'Walmart', 'Springfield', 'Completed'), 
(2, '2024-06-02 09:45:00', 15000.00, 'Credit', 'Apple Store', 'Chicago', 'Pending'), 
(2, '2024-06-02 11:00:00', 200.00, 'Debit', 'Starbucks', 'Chicago', 'Completed'), 
(3, '2024-06-03 14:15:00', 250.00, 'Debit', 'Target', 'Springfield', 'Completed'), 
(3, '2024-06-03 16:20:00', 30000.00, 'Credit', 'Tesla', 'San Francisco', 'Pending'), 
(4, '2024-06-04 08:30:00', 120.00, 'Debit', 'McDonalds', 'Springfield', 'Completed'), 
(4, '2024-06-04 10:50:00', 6000.00, 'Credit', 'Best Buy', 'Chicago', 'Pending'), 
(5, '2024-06-05 15:10:00', 70.00, 'Debit', 'CVS Pharmacy', 'Springfield', 'Completed'),
(5, '2024-06-05 17:00:00', 22000.00, 'Credit', 'Louis Vuitton', 'New York', 'Pending');

SELECT *FROM transactions

SELECT transaction_id,account_id,transaction_date,transaction_amount, transaction_type,merchant,location,status
FROM transactions
WHERE transaction_amount>=1000.0 AND transaction_date BETWEEN '2024-06-01' AND'2024-06-05'
