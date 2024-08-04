## Instructions

- Inside natas14 we see a login page and we can see the source code.
- Looking inside the source code we can see that its going to be performed a SQL query with the values we inputed from login page. This is classic SQL injection example.
- For those who doesnt know: https://www.w3schools.com/sql/sql_injection.asp
- We also have now the posibility to manipulate the request and send through GET the param 'debug', this way we can see how is going to be the SQL query.
- So what injection we can do here? Like i said before this is CLASSIC sql injection example so we are going to use classic sql injection: '" OR 1=1-- '
- First we put '"' so we break out of the username string, this way we can execute SQL code.
- Then we simply add a condition operator 'OR 1=1'. Now the sql query looks like:
SELECT * from users where username="" OR 1=1" and password=""
- We are almost good to go, now we have the problem that the upper query its not going to execute because the syntax its wrong, we want to get rid off everything after our SQL injection so we add '-- '. This is how you can comment code in SQL ( comments in programming are for clarify and better understanding of the code, so it doesnt get interpreterd nor executed ), now everything after this is going to be a SQL comment ( remember, it is not executed )
- Now the query is:
SELECT * from users where username="" OR 1=1-- " and password=""
- Which is the same as:
SELECT * from users where username="" OR 1=1

- And this query means that is going to retrieve everything ( '*' ) from the table 'users' where the username is "" or if 1=1, i think everyone agreeds that 1 is in fact equal to 1 so its going to get absolutely all usernames from the 'users' table

- Coming back to the php code, this only checks if the databse is sending info back, if the number of rows is greater than 0 we get the natas15 password.
- [IMAGE HERE]