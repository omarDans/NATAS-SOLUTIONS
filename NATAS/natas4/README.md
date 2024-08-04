## Instructions

- Inside natas4 we see the message: Access disallowed. You are visiting from "" while authorized users should come only from "http://natas5.natas.labs.overthewire.org/"
- ¡For this exercise we have to use burp suite for manipulating the requests!
- We open burpsuite and we go to proxy tab, after that we open the browser and enter in: http://natas4.natas.labs.overthewire.org/
- We enable "intercept on" and refresh the page to get the request that is being sent, this is what we should see:
- [IMAGE HERE]
- We see that the 'Referer' header has the value "http://natas4.natas.labs.overthewire.org/" (important: if we dont see the 'Referer' header we can just add it like: Referer: value) we need to change this to the natas5 URL so that we tell the server that the request is coming from natas5 and not from natas4
- [IMAGE HERE]
- [IMAGE HERE]