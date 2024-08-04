## Instructions

- Inside natas12 we can see that we are able to upload (aparently) JPEG files and the access to them, lets see the source code.
- For a better understanding of the php code we are going to also see the request that is sent to the server when we click the upload button.
- [IMAGE HERE]
- So we upload the file and its going to be generated a random name to the file then its going to check the size of the file to check if it exceeds the 1000 bytes limit and then its going to be uploaded.
- Ok, easy, we can just upload a php file that reads the content of the /etc/natas_webpass/natas13 file with the function file_get_contents and then get the password.
- First we create the php file:
- [IMAGE HERE]
- Then we just upload it to the webp...AGAIN! this motherf****** why the extension changed to '.jpg'?!?!
- [IMAGE HERE]
- Yeah, if we look closer to the code, the \$_POST["filename"] expression is not making reference to the name of the file we uploaded, this is the reference to the value of the the 'input' tag that is hidden in the HTML code.
- [IMAGE HERE]
- And the value is generating a random name and adding to the end the '.jpg' extension
- And good news, we can change that easy.
- Again, we upload the file to the website
- And intercepting the request with burp suite we can modify the name extension.
- [IMAGE HERE]
- Now we see the correct file extension '.php' so if we open that file...BADABUM password for natas13