## Instructions

- Inside natas6 we see that we can input a value.Also we can see the source code.
- Seeing the source code we see that we will be able to get the natas7 password if the second 'if' condition is true.
- In the condition the variable '$secret' to the value received from the input through POST request ( $_POST['secret'] )
- ![6](https://github.com/user-attachments/assets/12e4b208-f20c-4e05-b662-040aa7030502)

- As you can see, 'secret' is the name of the key that is being sent through a POST request. To reference this, in php you use: $_POST['key_name'] ( in this case key_name = secret )
- But in this case we dont need to manipulate any request, we only need to undertand the php code and where is coming from the '$secret' variable
- The $secret variable is coming from the include at the top of the script. include option is for load external files to the code ( php in this case ). In this case we are loading a file ( secret.inc ) that has the '$secret' variable declared.
- If we access to the file (http://natas6.natas.labs.overthewire.org/includes/secret.inc) we will see the variable declared in the HTML Inspector
- ![6_2](https://github.com/user-attachments/assets/f8bedc86-524c-4878-887d-e15b525ac78c)

- We just need to copy and paste that into the input field
- ![6_3](https://github.com/user-attachments/assets/58736d35-c037-46a4-a2c7-13a491e884c9)

- ![6_4](https://github.com/user-attachments/assets/38fc375f-cd21-4ea2-8051-e1f153be8071)

