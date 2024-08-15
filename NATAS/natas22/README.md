## Instructions

- Inside natas22 we have no information about the level other than the 'view source code' button, so let's see that.
- There are two php codes, the first one checks if 'revelio' param has been sent throught a GET request and then, if you are an admin. If you are not an admin it will send a HTTP request with the header "Location /" which essentially will get us to the starting point because the second script will not execute.
- The second php script checks if 'revelio' param has been sent throught a GET request and then it will print the natas23 credentials if it was true.
- The trick here is that you can't send the request through the browser, you need to send the raw request and ignore external headers (that's what i understood, i didnt understand it fully, i just looked around, saw curl somewhere, tried it and worked).
- Using curl you can do that so you can use: `curl -u natas22:d8rwGBl0Xslg3b76uh3fEbSlnOUBlozz http://natas22.natas.labs.overthewire.org?revelio`
- [IMAGE HERE]
- And that's it, you will retrieve the credentials for natas23, easy.

*Some times the credentials for the levels change, remember to change the password on the curl command if that's the case*

nata