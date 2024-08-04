## Instructions

- Inside natas19 they tell us that the code is almost the same as previous exercise but the IDs are no longer sequential. What does this mean? Lets find out.
- Lets first see how the PHPSESSID cookie is being save:
- ![19](https://github.com/user-attachments/assets/8f1b5275-e9c7-40d4-9372-32b670c2ef08)

- WAIT! its amazingly long, this is imposible to brute force, its the end of the world, THE END OF THE UNIVERSE, NOOOOOOOOOOOOoooooooooo........ 
- Are you sure? Yeah, i thought that too im gonna be honest but, this is nothing more than a hex string, lets upload this to CyberChef and see his secrets...
- ![19_2](https://github.com/user-attachments/assets/5ff9ae41-ff50-4dc6-93d7-daf488862cc1)

- yeah, its the same thing as before but now is in HEX format and is adding the username we entered with a slash. Again, this is open to brute force, we only need to generate the correct PHPSESSID which means we need to generate random numbers from 1 to 640 concatenate to '-admin' then format it to HEX and send it.
- So lets run the script i created for you with love: `python main.py`
- ![19_3](https://github.com/user-attachments/assets/07198605-8be5-47fa-b8f7-874797595730)

*Again, you can add more workers for more cracking speed (or less, if your pc is going to explote)*

## Python install
- for linux: https://docs.python-guide.org/starting/install3/linux/
- for windows: https://www.python.org/downloads/windows/
