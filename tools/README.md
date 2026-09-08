# Juice Shop VAPT PoC Toolkit

A Python toolkit that programmatically demonstrates 5 vulnerabilities identified during a manual black-box web application penetration test against [OWASP Juice Shop](https://owasp-juice.shop/), self-hosted via Docker.

This isn't just a scanner — each finding was first confirmed manually (Burp Suite, OWASP WSTG + PTES methodology), then converted into a standalone, reusable Python function as proof of concept. Output is dual-audience by design: every result includes a plain-English explanation and a technical detail line, matching how findings are communicated in a real client report.

## Findings covered

| ID | Finding | Severity | Endpoint |
|---|---|---|---|
| WEB-01 | SQL Injection → Authentication Bypass | Critical | `POST /rest/user/login` |
| WEB-02 | Weak/Default Admin Credentials | Critical | `POST /rest/user/login` |
| WEB-03 | IDOR on Basket Endpoint | Moderate | `GET /rest/basket/{id}` |
| WEB-05 | User Enumeration | Moderate | `POST /api/Users/` |
| WEB-07 | Missing Account Lockout / Rate Limiting | Informational | `POST /rest/user/login` |

## Setup

```bash
# 1. Start Juice Shop locally
docker run --rm -p 3000:3000 bkimminich/juice-shop
```
> ⚠️ Verify this matches how you actually ran your container (tag, flags, port) — adjust if different.

```bash
# 2. Install dependencies
pip install requests

# 3. Run the toolkit
python3 toolkit.py
```

## Usage

The toolkit presents a menu — pick a single finding by number, or run all 5 at once:

```
VAPT Toolkit — select a finding to run:
1. WEB-01: SQL Injection Auth Bypass
2. WEB-02: Weak Admin Credentials
3. WEB-03: IDOR on Basket Endpoint
4. WEB-05: User Enumeration
5. WEB-07: Missing Account Lockout
all. Run all findings
Pick a number (or 'all'):
```

## Sample output

Real output from a live run against a local Juice Shop instance:

```
WEB-01
[+] VULNERABLE — An attacker could log in as admin without knowing the real password.
    Technical: SQL injection in the login email field bypassed authentication — a crafted string broke out of the intended SQL query and returned HTTP 200.
WEB-02
[+] VULNERABLE — The admin account uses a common, easily guessed password.
    Technical: Login succeeded (HTTP 200) using a known weak credential pair (admin123, present in common wordlists) — no injection required.
WEB-03
[+] VULNERABLE — A logged-in user can view another user's shopping basket just by guessing an ID number.
    Technical: Basket endpoint did not verify the requesting token's own basket ID against the requested ID — swapping to a neighboring ID returned HTTP 200 with another user's data (IDOR).
WEB-05
[+] VULNERABLE — The site reveals whether an email is already registered, which helps attackers build a list of real accounts to target.
    Technical: Registration endpoint returns different status codes for existing (400) vs new (201) accounts, enabling account enumeration.
WEB-07
[+] VULNERABLE — The login page never blocks repeated wrong password attempts, making it easy to guess passwords automatically.
    Technical: 15 consecutive failed login attempts all returned HTTP 401 with no lockout or rate-limiting response, indicating brute-force protection is absent.
```

## Project structure

```
tools/
├── toolkit.py      # menu + dispatch across all 5 findings
├── web01.py        # SQL injection auth bypass
├── web02.py        # weak admin credentials
├── web03.py        # IDOR on basket endpoint
├── web05.py        # user enumeration
└── web07.py        # missing account lockout
```

## Scope note

This toolkit covers the 5 findings suited to automated PoC demonstration. Two additional findings from the full assessment (DOM-based XSS, missing password length validation) were confirmed manually but intentionally not scripted — see the full pentest report for details on all 7 findings.

## Disclaimer

Built and tested only against a local, self-hosted Juice Shop instance for educational/portfolio purposes. Not intended for use against systems without explicit authorization.
