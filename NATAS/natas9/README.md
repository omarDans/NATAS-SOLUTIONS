## Instructions

- Inside natas9 we see that we have a input asking for a word and that we can see the source code
- In the source code looks like we are executing the linux command 'grep -i $key dictionary.txt'. This basically finds all coincidences of the \$key value in the dictionary.txt file.
- The problem here is that we can input anything we want ( no character filtering ) and in linux we can concatenate commands with ';' character.
- So we can input something like: "; cat /etc/natas_webpass/natas10
- [IMAGE HERE]
- 'cat' command will read the content of the file natas10 and output it into standard output ( more easily: the webpage ) so we will be able to see the natas10 password:
- [IMAGE HERE]
