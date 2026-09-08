import requests
import time
def run_web05(target):
    existing_payload = {
        "email": "admin@juice-sh.op",
        "password": "Test1234!",
        "passwordRepeat": "Test1234!"
    }
    response = requests.post(f"{target}/api/Users/", json=existing_payload)

    new_email = f"newuser_{int(time.time())}@test.com"
    new_payload = {
        "email": new_email,
        "password": "Test1234!",
        "passwordRepeat": "Test1234!"
    }
    new_response = requests.post(f"{target}/api/Users/", json=new_payload)

    if response.status_code == 400 and new_response.status_code == 201:
        return {
            "id": "WEB-05",
            "vulnerable": True,
            "plain_english": "The site reveals whether an email is already registered, which helps attackers build a list of real accounts to target.",
            "technical": "Registration endpoint returns different status codes for existing (400) vs new (201) accounts, enabling account enumeration."
        }
    else:
        return {
            "id": "WEB-05",
            "vulnerable": False,
            "plain_english": "Could not distinguish existing vs new accounts this run.",
            "technical": "Both registration attempts returned the same status code; enumeration not confirmed."
        }
