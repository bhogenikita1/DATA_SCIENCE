SELECT firstname,income,age from customers
	WHERE income>50000 AND (age<30 OR age>=50)
AND (country='Japan' OR country='Australia')
	
SELECT SUM(totalamount) FROM orders WHERE (orderdate>='2004-06-01'
	AND orderdate<='2004-06-01' )
	AND totalamount>100

SELECT firstname,income,age FROM customers WHERE 
income>50000 AND (age<30 or age>=50)
AND(country='Japan'OR country='Australia')

SELECT firstname,gender FROM users WHERE NOT gender='m';

SELECT COUNT(firstname)FROM customers WHERE gender='f' and state='or'

SELECT COUNT(income)FROM customers WHERE age>44 and income>=100000;








