## Instructions

- Inside natas13 we see that now we can "only" upload image files!, lets see the source code to see if its true.
- In the source code we see basically the same code but now is checking if the file we are uploading is a image using the function exif_imagetype()
- The problem with this function is that it's very easy to bypass because it only checks for the first 4 bytes of the file to see if the signature is the same as a image JPEG file. (bytes: "\xFF\xD8\xFF\xE0")
- DOCUMENTATION: https://www.php.net/manual/es/function.exif-imagetype.php

- So if we create a file with the first 4 bytes "\xFF\xD8\xFF\xE0" and then php code we can do the same thing as before in natas12.
- Execute the python script with: `python bypassExif.py`
- [IMAGE HERE]
- This script is going to create a payload.php file that if we upload to the website it's going to execute the file_get_contents() php function to read the content of the file /etc/natas_webpass/natas14 and get the natas14 password.
- ¡We have to change the random filname that generates when we upload the file!
- [IMAGE HERE]
- And then go to the uploaded file and see the password :D
- [IMAGE HERE]

## Python install

- for linux: https://docs.python-guide.org/starting/install3/linux/
- for windows: https://www.python.org/downloads/windows/