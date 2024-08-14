## Instructions

- Inside natas8 we again need to input a secret key and we can see the source code.
- Seeing the source code we can see that the value that we will input is going to be sent throught a POST request and it will be compared to $encodedsecret variable but before is going to be encoded using the function 'encodeSecret()'.
- This function first encodes to base64, then reverses the string and finally transforms the characters to hex
- Knowing this, we can just do the same as the 'encodeSecret' function but in reverse.
- First: We transform the string from hex to ascii. 
- Second: We reverse the string.
- Third: We decode in base64.

- You can use Cyberchef for this (https://gchq.github.io/CyberChef/) or you can use my python script for comfort
- execute with: `python main.py`
- ![8](https://github.com/user-attachments/assets/7233c2c8-f601-4235-8023-98db4eb3e50d)


- Once we get the secret key, we input it and we will get the password:
- ![8_2](https://github.com/user-attachments/assets/5e9965b3-11a9-4797-bf90-822bff5a8b4e)


## Python install
- for linux: https://docs.python-guide.org/starting/install3/linux/
- for windows: https://www.python.org/downloads/windows/
