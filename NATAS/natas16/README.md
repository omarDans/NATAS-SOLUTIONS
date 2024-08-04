## Instructions

- Inside natas16 we find ourselves in a situation similar to that of the natas10 exercise, we have an input where we can retrieve all word containing the inputed character/string inside dictionary.txt but, now looks like they are filtering more characters than before. Lets look the source code.
- In the source code we see that before executing the 'grep' command is going to check if the variable \$key contains the characters: [;|&`\'"]
- So know we can't get the password directly like in natas10, again we have to create a script to brute force the password, this is the logic:
- We are going to input: doomed$(grep \<character\> /etc/natas_webpass/natas17)
- First we need to understand that with $() we can get the output of a any command so, in this case, if the character we are testing is inside /etc/natas_webpass/natas17 the output of the command is going to be the password, this is going to concatenate to doomed and be something like: 'dommed0RoJwHdSKWFTYR5WuiAewauSuNaBXned' this doesnt exists inside the dictionary.txt file, so we are not going to get any output.
- ![16](https://github.com/user-attachments/assets/8fed5b7f-c64c-4bf0-b0a5-7c9716a0163c)

- See now? if the character is in the password file it's going to return output; if it is not, it returns nothing 
- So basically we have to make python script like before but in this case if we found 'doomed' in the server response means that that character was not the correct one.
- Something worth to notice is that in the script when we are cracking the password, after filtering the characters, the command we are sending is: doomed$(grep ^\<character\> /etc/natas_webpass/natas17), here we are adding the '^' character, this is for telling 'grep' that has to test starting from the begining. This is a visual example:
- ![16_2](https://github.com/user-attachments/assets/d9f4f62c-41eb-46db-9354-c642b065b936)

- Now its time to execute the script and get the password: `python main.py`
- ![16_3](https://github.com/user-attachments/assets/a030bddb-d252-45d0-bd6d-85c3cbe35d7d)


## Python install
- for linux: https://docs.python-guide.org/starting/install3/linux/
- for windows: https://www.python.org/downloads/windows/

