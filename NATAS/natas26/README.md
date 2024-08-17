## Instructions

- This levels are getting harder and harder. Lets go straight forward and see the source code.
- Very looong code. The important parts are the ones where we unserialize the \$_COOKIE["drawing"] value, why is that? Because this function, unserialize(), is vulnerable. What this function does is getting a serialize value like "O:4:"Test":1:{s:4:"prop";s:5:"hello";}" at it will transform it again to the original data type BUT, important BUT, in the case it's and object it will call the defined methods ( functions ) that this object has. Look: https://www.php.net/manual/en/function.unserialize.php
- In this source code, we have a class Logger ( object ) with the method __destruct() ( the __construct will not be called by unserialize() ) so if we pass a serilized Logger object to the unserialized() function, the method __destruct will be called
- [IMAGE HERE]
- We encounter the unserilized function 2 times and, its unserializing the base64_decoded value of \$_COOKIE["drawing"], so if we manipulate the content of this cookie we can be able to create a file ( because of the way __destruct works ). Im sure if you look to the php script i created you will understand how this exploit is working.
- Basically, the script is creating this malicious cookie for us so after executing the script with: `php main.php` we will copy the cookie and replace it in our browser.
- [IMAGE HERE]
- [IMAGE HERE]
- Then we will refresh and if everything went well we created the file in folder img/ with the name shell.php. ( i named it this way because you can acctually create a webshell, sssh, dont tell anyone )
- [IMAGE HERE]
- And voilá, you get the credentials for natas27.

*Yeah, you will probably get 300 times the password, that's because there are 300 files named shell.php with the same code from other users that resolved this CTF ( you acctually dont have to do nothing, just go to /img/shell.php)*