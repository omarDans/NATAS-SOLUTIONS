## Instructions

- Inside natas11 see a message that says: "Cookies are protected with XOR encryption" and a input that you can use to change the color of the webpage.
- If you go to the source code you will probably get overwhelmed with the amount of php code, close overthewire.org, shutdown pc and quit fore... OK jokes apart, yeah, its more than we had in the previous exercises but the code its not that hard.
- In a summarized way it will check if you have the cookie in memory (data) and if you dont, it will be established with the content of the $defaultdata variable but it will first be base64 encoded, encrypted with xor and encoded in json format. Then the function loadData() will decode this cookie and transform it again into the dictionary doing the same thing as before but in reverse, then it will check if the value "showpassword" is equal to "yes", if so, it will print the password
- So basically we have to create a custom cookie using the steps that the webpage used to create his own cookie. How? Easy:
- Just create a php script with a dictionary like the $defaultdata variable but changuing the "showpassword" to "yes" instead of "no"
- Easy peasy encode it to json.
- Then copy and paste the xor_encrypt func...WAIT but we dont have the fuc**** key, WTF is this, i quit.
- Ok no, no panic, we can still get it. This is like maths: [ 30/10 = 3 ] == [ 30/3 = 10 ]. Diference this is a php expresion: \$outText = \$text[\$i] ^ \$key[\$i % strlen(\$key)] WE CAN DO \$key = \$text[\$i] ^ \$outText[\$i % strlen(\$outText)]
- This way we will get the key that its being used to encrypt to xor.
- And we know \$outText that's the \$defaultdata encoded in json
- Now we have everything to proceed, we first get the xor key and then we use it to create the custom cookie you already know:
- \$data = array( "showpassword"=>"yes", "bgcolor"=>"#ffffff");
- encode to json
- encode to xor using the founded key
- encode to base64
- Easy Cookie.

- ### Of course my friend i created the script for automating this :)
- ![11](https://github.com/user-attachments/assets/6bcdcb23-6f8d-4374-b940-782020b453cb)

- ![11_2](https://github.com/user-attachments/assets/97bce3c4-20c1-47e5-ad1c-2380dbca882e)

## Script Execution
- Execute with `php main.php`
- in linux you can simply install with: `sudo apt-get install php`
- For windows see: https://www.geeksforgeeks.org/how-to-install-php-in-windows-10/

## Important
- I forgot to mention that you can copy the cookie going to the developers tool, Storage tab, Cookies, data. Its going to be URL encoded but you can simply replace the string '%3D' for '='.
