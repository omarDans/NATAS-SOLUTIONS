## Instructions

- Inside natas18 we see a login form where we can input a username and a password to login. They say to us that we need to login as admin to retrieve credentials for natas19. Lets see the source code
- This is a long code, and long code is equal to long explanations, lets see if i can:
- First of all lets clears things out, this is a Session hijacking attack, you can see that in the code, there is only one part of the code where the form inputs are validating and that is not going to get us to anywere because it's imposible to login as admin entering the username and password. ( the isValidAdminLogin() it's going to return always 0, and we need \$_SESSION['admin'] to be 1 )
- So lets dive into the function my_session_start() ( this is the important stuff ). As you can see this is checking if PHPSESSID exists in the cookie and if it is a valid ID ( only needs to be a number to be a valid ID ).
- If everything is ok its going to check if 'admin' is in \$_SESSION variable ( variable that generates in the function session_start(), see: https://www.php.net/manual/es/reserved.variables.session.php) if its not, which means that we didnt enter as admin, its going to set \$_SESSION['admin'] = 0 which means that us dont get password, bad.
- Lets try to login in the webpage and see what PHPSESSID do we get:
- [IMAGE HERE]
- [IMAGE HERE]
So they tell us that we logged in as a regular user bla bla bla ok, i already know i didnt enter as admin yeah...And we receive the PHPSESSID 264. Why is that? This is thanks to this line of code: `session_id(createID($_REQUEST["username"]));`
- This is creating a random ID between 1 and 640 for my previously inputed username ( see CreateID() function ). The problem here is that the amount of ID are very low ( $maxid = 640 ) so, knowing that there are only 640 posibilities we can check all one by one and eventually we are going to hit the Session ID for admin.
- OK, easy, another brute force script, execute with: `python main.py`

By the way, this time i added threading, which is going to make the cracking amazingly faster. The more amount of workers you add, the faster it is.

## Python install
- for linux: https://docs.python-guide.org/starting/install3/linux/
- for windows: https://www.python.org/downloads/windows/