## Instructions

- Inside natas15 we see a input where looks like we can check the existence of an user, also we can see the source code.
- Inside the source code we see again a SQL query. One that can be manipulated by the user input, the problem here is that this time if the query sends back data we receive "This user exits" else "This user doesn't exist" instead of directly getting the passowrd, shit.
- Again, is the moment to script, we are going to brute force the password sending a special SQL query.
- If we send: 'natas16" and password LIKE BINARY "a%" #' this its how the query will look.
'SELECT * from users where username="natas16" and password LIKE BINARY "a%" #"'
This basically what is doing is checking if the password for user natas16, inside the 'users' table,starts with the character "a". You see the point? If we create a programa that test all posible characters one by one we can get the password for natas16
- It's going to be very long to explain the code here step by step but basically what it does is send a POST request testing the characters one by one and if it founds the "exists" string in the response it will save that character into 'filtered_chars' variable ( this is for optimization purposes, it will make the password cracking faster if we know first the characters that are in the password ) then it will start to crack the passowrd doing the same thing but concatenating the characters that are correct.
- ![15](https://github.com/user-attachments/assets/e1bbc21d-2af1-403b-93a7-16e73c51104c)


- Execute the python code with: `python main.py`

## Python install

- for linux: https://docs.python-guide.org/starting/install3/linux/
- for windows: https://www.python.org/downloads/windows/
