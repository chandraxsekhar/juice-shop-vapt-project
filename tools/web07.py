import requests

def run_web07(target):
    payload = {
        "email": "admin@juice-sh.op",
        "password": "wrongpassword"
    }
    all_status_codes = []
    for i in range(15):
        response = requests.post(f"{target}/rest/user/login", json=payload)
        all_status_codes.append(response.status_code)

    if all(code == 401 for code in all_status_codes):
        return {
            "id": "WEB-07",
            "vulnerable": True,
            "plain_english": "The login page never blocks repeated wrong password attempts, making it easy to guess passwords automatically.",
            "technical": "15 consecutive failed login attempts all returned HTTP 401 with no lockout or rate-limiting response, indicating brute-force protection is absent."
        }
    else:
        return {
            "id": "WEB-07",
            "vulnerable": False,
            "plain_english": "Some form of lockout or rate limiting was detected.",
            "technical": "Response codes changed across the 15 attempts, suggesting lockout or rate-limiting is in place."
        }
