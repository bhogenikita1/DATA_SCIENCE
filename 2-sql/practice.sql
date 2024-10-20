SELECT state,gender FROM customers WHERE gender='F' AND state='OR' or gender='F'and state='NY';
SELECT state,gender FROM customers WHERE gender='F'AND(state='OR' or state='NY')

