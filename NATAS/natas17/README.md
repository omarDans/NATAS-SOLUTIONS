## Instructions

- Inside natas17 we see a input where looks like we can check the existence of an username ( again probably SQL injection ). Lets see the source code
- THe source code is the same as natas15, but this time we dont get any response from the server because the little rats commented the 'echo' lines so, what can we do now?.
- This is called blind SQL injection (https://portswigger.net/web-security/sql-injection/blind)
- When you dont get information when you do a SQL injection you have to look to other alternatives, in this case we are going to use a 'delay based injection'. This is when you inject SQL code that causes the database to wait and, in consecuence, delay the response of the server. This is what we can do:
"-IF(1=1, SLEEP(1), 0)#
This causes the database to sleep for 1 second, so we are going to receive the response of the server later than normally.
- Ok, i cant really tell you why i used the character '-' in this SQL injection, i know that when i researched in the internet for diferent types of blind SQL injections i, in one moment, had to see this but i dont know what it does exactly.
- One thing i can tell you is that you can change that SQL injection to something like:
- natas" AND IF(1=1, SLEEP(1), 0)#
- That will create the same result, so suite yourself
- Anyways, knowing all this we can do, AGAIN, the same as before, a brute force python script that validates if a character/string is inside the /etc/natas_webpass/natas18 file by injecting this:
"-IF(EXISTS(SELECT * FROM users WHERE username="natas18" AND password LIKE BINARY "%'+c+'%"), SLEEP(0.4), 0)#
- Look, i would explain this, but im using the same concepts that i explained in the previous levels so you should be able to understand it :)
- The only thing new here is the EXISTS() function, this only checks if the output of the query its not returning null.
- So know, in the python script im checking if the response of the server has been delayed 1 or more seconds. The rest of the script is also the same the previous ones.
- So know we only have to execute the python script: `python main.py`
- [IMAGE HERE]

- You should be aware that if you are not getting a password with length of 32 characters, the passowrd isnt't right. Dont blame my script, blame you internet connection or overthewire.org servers ( but probably your internet connection ).
## Python install
- for linux: https://docs.python-guide.org/starting/install3/linux/
- for windows: https://www.python.org/downloads/windows/