## Instructions

- Inside natas10 we see the same thing as in natas9 but now looks like there is a little bit of input validation ( not enough sadly )
- Because of how the grep commando works we can abuse this to read the content of natas11 file
- Inputing the following: "a /etc/natas_webpass/"natas11
- This will result in the command formating into: "grep -i a /etc/natas_webpass/natas11 dictionary.txt"
- What is going to happen is that grep will search for the character 'a' in /etc/natas_webpass/natas11 and if finds the character it will spit out the entire line.
- Maybe is diferent password at the moment you are reading this so, if it doesnt work for you just try another character: b, c, d...
- [IMAGE HERE]
- [IMAGE HERE]