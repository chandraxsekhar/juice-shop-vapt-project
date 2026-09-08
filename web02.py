import requests
def run_web02(target):
    payload = {
        "email": "admin@juice-sh.op",
        "password": "admin123"
    }
    response = requests.post(f"{target}/rest/user/login", json=payload)

    if response.status_code == 200:
        return {
            "id": "WEB-02",
            "vulnerable": True,
            "plain_english": "The admin account uses a common, easily guessed password.",
            "technical": "Login succeeded (HTTP 200) using a known weak credential pair (admin123, present in common wordlists) — no injection required."
        }
    else:
        return {
            "id": "WEB-02",
            "vulnerable": False,
            "plain_english": "The weak password did not work.",
            "technical": "Login attempt with admin123 did not return HTTP 200; credential not confirmed weak."
        }
