## Instrucions

- Inside natas23 we see a input with the name "Password" and also we can see the source code. Let0's look at that.
- The source code is very simple it checks first if "passwd" exists in the request variable, then, the important comparison, checks if the string "iloveyou" is in "passwd" key and if this string is greater than 10, no, not if the length of the string is greater than 10, literally if the value of "passwd" key is greater than 10. Im sure that when you saw this you thought: "WTF is this shit?? This doesnt make anysense what a stup...No? only me? ok.
- Ok jokes a part, at first this looked weird but its SO STUPID solution. This is php and looks like you can validate the '> 10' comparison if you put the number at first (looks like php doesnt care if it's a integer or a string...).
- If you enter: "11iloveyou" this will return true and will give us the natas24 credentials because it will check if "iloveyou" exists (which it's true) and then if 11 is greater than 10 (which it's also true)
- The problem if you enter "iloveyou11" is that the second comparison will fail and return false because if the string doesnt start with a number php will automatically transform the string to '0' for the numeric comparison
- ![23](https://github.com/user-attachments/assets/4364fdb7-7c81-4e20-b50b-aa728f2f9511)
