## Instructions

- This level is very interesting, let me show you:
- So, we have a login form, yeah, wharever, lets see the source code.
- Assuming you already looked at the code you have to know now that the basic funcionality is:
- Checks if the user we introduced and that it's stored in the variable \$_REQUEST["username"] exits.
- If doesnt exists createUser() function its called. This function checks if we are not doing something strange with the user by trimming \$usr variable ( key part of the exploit, will see ). Then it will sanitize input ( another key part ) and finally it will be get stored in the db.
- If the user we introduced exists, it will check if the credentials are ok, and then it will show the data ( username and password ) for that user using the dumpData() function ( and another key part ).
- Whats the problem with the functions: createUser() and dumpData()? The problem it's the way that this code performs with the two of them together.
- Because imagine if this line doesnt exists:
- ![27](https://github.com/user-attachments/assets/5ad0cce7-3c87-45c7-936c-01d61abbdc92)

- We can input a username like: "natas28 " ( with a space ) with any password, this user will be created, then if we login into this user, checkCredentials() will check if everything is correct and finally dumpdata() will show the data for "natas28" not "natas28 " this is because the dumpdata() function trims the username ( trim = delete white spaces at the begining and end of a string ). Look:
- ![27_2](https://github.com/user-attachments/assets/b8fda6d4-51fb-4db8-b55b-7edca3e6e43e)

- Sadly, createUser() checks if we are inputing white spaces in the username parameter so we cant do this...Well, yes we can because this same function is extracting the first 64 characters from the username input:
- ![27_3](https://github.com/user-attachments/assets/03a4cabe-c634-41aa-8382-3afb3e94e9f3)

- So what happens if we input the username "natas28" followed by 57 whitespaces? this adds up 64 characters. Now wharever shit we put after this it's going to be ignored but this is important because if we add one more character like 'a' this character is going to make us bypass trim() check.
- In summary this give us the posibility to create the user "natas28\<x57 whitespaces\>" that at the end is going to get trimmed by dumpData() function and give us the information from "natas28".
- I created the script for doing this automatically but you can do it mannually ( good luck typing 57 whitespaces ). Execute with: `python main.py`
-  ![27_4](https://github.com/user-attachments/assets/ba697ca1-44df-4fef-b796-46bc925c52ec)



## Python install
- for linux: https://docs.python-guide.org/starting/install3/linux/
- for windows: https://www.python.org/downloads/windows/
