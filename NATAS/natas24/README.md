## Instructions

- Inside natas24 we can see again a input with the name "Password" and the classic 'View sorucecode" button.
- The source code button has almost the same code as the previous exercise, diference is that in this one we are only comparing the string inputed in \$_REQUEST["passwd"] and another one that is censored. We are using strcmp() to do this, and this is the problem.
- The problem is that strcmp() has a problem comparing diferent datatypes, its meant to compare string to string but if we input a diferent datatype it will return NULL ( NULL == 0 ). So this will give us the password because `!0 == 1` and 1 is true.
- [IMAGE HERE]
- So let's see what happens if we input an array instead of a string
- We can do it like this:
- [IMAGE HERE]
- [IMAGE HERE]
- Yeah, this give us the password as expected.
