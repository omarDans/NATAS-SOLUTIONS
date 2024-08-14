## Instructions

- Inside natas21 we see a note that says: "this website is colocated with http://natas21-experimenter.natas.labs.overthewire.org"
This means that the two websites (http://natas21.natas.labs.overthewire.org/ and http://natas21-experimenter.natas.labs.overthewire.org/) are sharing the same server so they can share sessions and stuff ( but very important here, the sessions )
- Also we can see the classic message that we cant get the credentials for natas22 unless we are logged in as admin.
- Seeing the source code of the main natas21 website is pointless, only checks if admin key inside \$_SESSION variable is equal to 1 then prints or not the credentials.
- ![21](https://github.com/user-attachments/assets/519da9f3-31e0-49cb-a416-5f3440132c39)

- If we enter the second website we see that we have a form where we can input values that will change the appearence of the website. Looking really innocent but this has a big problem.
- Seeing the source code we see this:
- ![21_2](https://github.com/user-attachments/assets/bbda8b5a-d468-455a-8b1c-bfcf2cc3a556)

- This is acctually all we need to resolve the exercise. This is getting all the keys and values from the request and save it into \$_SESSION variable as it was. Remember what we needed to loggin as admin? That's right, admin key has to be equal to 1, so we can modify the request and send a parameter with name 'admin' and value '1'. Look:
- ![21_3](https://github.com/user-attachments/assets/de33167a-c777-4d2b-93ba-3e4702c3d869)

- This is how the request looks like when we press the update button. We can do this:
- ![21_4](https://github.com/user-attachments/assets/c4c9b65d-7f4f-40ae-a16a-173a381c1d52)

- As you can see, we simply add the param admin=1, now the \$_SESSION is going to be populated with the key 'admin' and the value '1'. So we have a cookie with the right conditions to get the credentials now.
- We only need to copy the cookie from "natas21-experimenter", paste it in "natas21" and refresh
- ![21_5](https://github.com/user-attachments/assets/5249b6ff-fcdb-4745-b918-79a0334c26ac)

- ![21_6](https://github.com/user-attachments/assets/146d2254-6787-42d2-a267-90303b88314a)

- ![21_7](https://github.com/user-attachments/assets/a78a8f4f-115e-46cb-a288-57f3043e6a7f)

- And we get the credentials
#### Code injection
- So there is another way of doing this if you dong want to use burpsuite. The second website has a HTML injection vulnerability so you could inject the input tag with the name=admin and value=1. Here is where the injection resides:
- ![21_8](https://github.com/user-attachments/assets/6695e7ce-a6e0-4c5e-b672-9418eb7574fd)

- you can inject html code because you have access to the \$val variable. The injection looks like this: `center' /><br><input name='admin' value='1'`
- after inputing this, you have to click update button two times (the second is the one that sends the admin=1).
- Anyways, you can literally write the HTML code manually but this way is cooler. Also this is a XSS vulnerability.
