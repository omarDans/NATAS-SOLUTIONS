## Instructions

- Inside natas20 we can see an input field that says: "Your name:" and they are saying to us that for retrieve the credentials for natas21 we must be logged in as admin. Lets see the source code.
- Again we encounter a long code. I was a little dizzy too when i saw it. I encountered a lot of new concepts and i must say that this level was a journey for me (i still have parts that i dont understand).
- In this code we found a lot of functions, the interesting ones are "mywrite" and "myread". Also we have the session_set_save_handler() which gives us and idea that sessions are gonna to be managed mannually.
- BTW, in this level i used the "debug" option when sending the requests, in previous levels it was almost completely useless but here, helped to understand the flow of the program.
- When we enter a value inside the input field, this value it's going to be sent through a GET request to the server with a param called "name". The value of this param is going to populate the superglobal variable $_SESSION["name"] as you can see here:
- ![20](https://github.com/user-attachments/assets/88eac571-469a-4f18-a134-d4d6faa167ef)

Then the function "mywrite" its going to read the content of the variable $_SESSION, save it in this format: "name \<value\>\n" and finally save it in the path: "/var/lib/php/sessions/mysess\_\<id\>" ( id is the value of the cookie PHPSESSID ).
- The function "myread" can read a session file that was saved by "mywrite". The way it does that is by getting the content of the session file ( the one in the path: "/var/lib/php/sessions/mysess\_\<id\>" ) and then it separated the lines by '\n' (enter) character to find the lines and then the lines are separated by " " character (space, duh). Then it will save it in the $_SESSION.
- Ok lets understand this better with examples:
- if we input "user" the content of the $_SESSION variable is going to be: "'name' : 'user'"
- Then "mywrite" is going to save it in the session file like this: "name user\n"
- Then "myread" is going to get the content of the file with the text: "name user\n" and, to populate the \$_SESSION variable, its going to separate by the "\n" characters first which will lead to this: "name user" and then its going to separate the string by " " characters, so its going to create a list like this: {name, user}. So $_SESSION its going to have the key "name" with the variable "user" ( \$_SESSION["name"] = "user" ).
- SO, understanding how this code is working, what happens if we input something like this: "wharever\nadmin 1"? ( yeah, i forgot to sat that for retrieving the natas21 credentials, \$_SESSION has to have the parameter "admin" with the value "1" )
- This input is going to be managed by the function "myread" and is going to create two keys: \$_SESSION["name"] = "wharever" and \$_SESSION["admin"] = 1. The second one is what we wanted the hole time, GG.
Thanks to the lack of input validation and a little of python magic. We can get the credentials.
Execute with: `python3 main.py`
- ![20_2](https://github.com/user-attachments/assets/ed812f57-20c0-47a1-9b66-1438fa3e2bb9)


*I want to reiterate that this level was a little bit confuse to me so i cant really explain it better sorry*
*Also, I HAVE NO FUCKING idea why it only works with python or sending raw requests with curl, i tried to do it in the browser with burp suite and shit but i couldnt do it, again sorry. If anyone knows i would be all ears*.

## Python install
- for linux: https://docs.python-guide.org/starting/install3/linux/
- for windows: https://www.python.org/downloads/windows/
