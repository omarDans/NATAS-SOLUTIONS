## Instructions

- We open developers tool ( in my case is f12 )
- We see the html code inside the 'Inspector' tab
- We see a comment that says: "No more information leaks!! Not even Google will find it this time... "
- They say that not even Google will find it, we can asume that they way to go is looking into the "robots.txt" file. (http://natas3.natas.labs.overthewire.org/robots.txt)
- [ A robots.txt file tells search engine crawlers which URLs the crawler can access on your site. This is used mainly to avoid overloading your site with requests; it is not a mechanism for keeping a web page out of Google. ]
- Inside the robots.txt we see a folder called: "s3cr3t":
- [IMAGE HERE]
- Of course if we enter there we will get the natas4 password inside the user.txt file:
- [IMAGE HERE]