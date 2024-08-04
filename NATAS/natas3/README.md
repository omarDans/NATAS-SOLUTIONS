## Instructions

- We open developers tool ( in my case is f12 )
- We see the html code inside the 'Inspector' tab
- We see a comment that says: "No more information leaks!! Not even Google will find it this time... "
- They say that not even Google will find it, we can asume that they way to go is looking into the "robots.txt" file. (http://natas3.natas.labs.overthewire.org/robots.txt)
- [ A robots.txt file tells search engine crawlers which URLs the crawler can access on your site. This is used mainly to avoid overloading your site with requests; it is not a mechanism for keeping a web page out of Google. ]
- Inside the robots.txt we see a folder called: "s3cr3t":
- ![3](https://github.com/user-attachments/assets/57fe60f8-71e1-411f-bd55-6cc060a3972d)

- Of course if we enter there we will get the natas4 password inside the user.txt file:
- ![3_2](https://github.com/user-attachments/assets/cd6ab4fa-45e9-458e-8ee0-6c05b72782e8)
