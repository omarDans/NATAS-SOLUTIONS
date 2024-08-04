## Instructions

- Inside natas9 we see that we have a input asking for a word and that we can see the source code
- In the source code looks like we are executing the linux command 'grep -i $key dictionary.txt'. This basically finds all coincidences of the \$key value in the dictionary.txt file.
- The problem here is that we can input anything we want ( no character filtering ) and in linux we can concatenate commands with ';' character.
- So we can input something like: "; cat /etc/natas_webpass/natas10
- ![9](https://github.com/user-attachments/assets/0d9a7581-1409-45e8-ac9f-6e8efad16d7b)

- 'cat' command will read the content of the file natas10 and output it into standard output ( more easily: the webpage ) so we will be able to see the natas10 password:
- ![9_2](https://github.com/user-attachments/assets/aa0c4e10-71ab-4205-8c8b-92ed0eb743f6)

