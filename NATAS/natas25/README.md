## Instructions

- Ok, first of all, this level is hard, i also wasnt able to find the solution for my own.
- Inside natas25 we have a text and a drop menu where we can select the language.
- If we look the source code we can see 3 important functions: setlanguage(), safeinclude() and logRequest().
- The safeinclude() function validates the value comming from \$_REQUEST["lang"]. The problem is that this validation is not safe ( yeah, i also thought it was safe ). the first 'if' is checking if user is trying directory traversal ( this is basically manipulating the path with '../' allowing access to any superior directory.) but the thing is that is doing it by replacing '../' with '' so, imagine the value of "lang" is: ".../...//". This is going to be procesed for safeinclude() function and is going to finish like this: "../".
- Basically we are able to directory traversal anyway but, now we have yet another problem, we can't just access the file /etc/natas_webpass/natas26 because there is another check for the string "natas_webpass" that makes it imposible to do it this way. What we can access is the log file that is created in the function logRequest().
- ![25](https://github.com/user-attachments/assets/8716a6db-b18c-45bd-9e2e-34237363c67a)

- ![25_2](https://github.com/user-attachments/assets/e60be5b5-dee1-4fdb-ba5c-23f815341efc)

- As you can see we did a directory traversal to access this log file ( i didnt mentioned that the name of the log file is being created using the session id so you need to put yours after natas25_ ). We are getting a notice that the __GREETING, __MSG, __FOOTER variables are undefined, ofcourse, this file doesnt have declared those variables. let's see how the file should look to have these variables defined, we can do this by looking the /language/en file.
- ![25_3](https://github.com/user-attachments/assets/44e3885a-33f3-46aa-aacb-87ebb5314d9b)

- I used the command: `curl -u natas25:ckELKUWZUfpOv6uxS6M7lXBpBssJZ4Ws http://natas25.natas.labs.overthewire.org/language/en` but you can do it on the browser and then: right click, 'view source code'
- Ok so finally if we look at logRequest() function we can see that its using the value of the 'User Agent' header for adding more info to the log file. We can change this User Agent and create a php script that reads the content of the file /etc/natas_webpass/natas26 and then saves it to one of the three variables (__GREETINGS, __MSG, __FOOTER).
- This is the requests that we need to send to the server (using burp suite):
- ![25_4](https://github.com/user-attachments/assets/6a4b03c8-2991-4dfd-b5c8-a19d6fe7e89b)

- ![25_5](https://github.com/user-attachments/assets/740ba955-d49e-4865-be44-e47551d07726)

- And we get the password
- tricky level, very tricky level...
- I got humbled with this one.
