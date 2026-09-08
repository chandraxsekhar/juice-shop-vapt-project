# OWASP Juice Shop — Web Application Penetration Test

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/r-chandra-shekar-a620aa252)
[![Email](https://img.shields.io/badge/Email-chandur483%40gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:chandur483@gmail.com)
[![Report](https://img.shields.io/badge/📄_Report-View_PDF-blue?style=for-the-badge)](./report)
[![Toolkit](https://img.shields.io/badge/🛠️_Toolkit-View_Code-success?style=for-the-badge)](./tools)

A self-directed black-box penetration test of OWASP Juice Shop (self-hosted via Docker),
conducted August 12–16, 2026. Manual testing guided by the OWASP Web Security Testing
Guide (WSTG) and PTES, covering both unauthenticated and authenticated attack surface.

## Findings

| Severity | Count |
|---|---|
| Critical | 2 |
| Moderate | 3 |
| Informational | 2 |

| ID | Finding | Severity |
|---|---|---|
| WEB-01 | SQL Injection → Authentication Bypass | Critical |
| WEB-02 | Weak/Default Administrative Credentials | Critical |
| WEB-03 | IDOR / Broken Object-Level Authorization — Basket Endpoint | Moderate |
| WEB-04 | DOM-based XSS via Search Functionality | Moderate |
| WEB-05 | User Enumeration via Registration Endpoint | Moderate |
| WEB-06 | Missing Server-Side Password Length Validation | Informational |
| WEB-07 | Missing Account Lockout / Rate Limiting | Informational |

## Contents

- [`report/`](./report) — full penetration test report (PDF)
- [`tools/`](./tools) — Python PoC toolkit independently re-verifying 5 of the 7
  findings via script, not just manual click-through (see toolkit README for usage)

## Contact

LinkedIn: linkedin.com/in/r-chandra-shekar-a620aa252
Email: chandur483@gmail.com
