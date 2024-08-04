## Instructions

- Inside natas7 we see two buttons: Home and About. 
- If we inspect the HTML code we can see that the button Home redirects to 'index.php?page=home'. The button About redirect to 'index.php?page=about'.
- This url syntax means that we are sending a GET request to the file 'index.php' and the 'page' param with value home/about
- The thing is that the way that index.php script works is by opening a file, reading its content and outputing the content to the website
- We now that all the password are stored inside '/etc/natas_webpass/' because that's what they told us at the beginning of the exercises (https://overthewire.org/wargames/natas/) and also in the HTML comment bellow the 'a' tags
- Knowing this we only have to change the redirecto to the file containing the natas8 password, like this:
- ![7](https://github.com/user-attachments/assets/2601125f-4408-4258-b6d7-2d850c7272fb)

- Now we only have to press the button and see the magic
- ![7_2](https://github.com/user-attachments/assets/8f62c2ec-e6dd-4340-8c44-d68aa288b332)

