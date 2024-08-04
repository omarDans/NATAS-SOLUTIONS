## Instructions

- Inside natas5 we see the message: Access disallowed. You are not logged in.
- We will have to see the request build, so we open burp suite and intercept the request.
- We see that in the 'Cookie' header we have one value with the name 'loggedin=0'
- I think this is very straight forward, we only need to change this value from 0 to 1 ( loggedin=1 )
- [IMAGE HERE]
- [IMAGE HERE]