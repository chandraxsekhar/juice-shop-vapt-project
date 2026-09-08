from web01 import run_web01
from web02 import run_web02
from web03 import run_web03
from web05 import run_web05
from web07 import run_web07

target = "http://localhost:3000"

print("VAPT Toolkit — select a finding to run:")
print("1. WEB-01: SQL Injection Auth Bypass")
print("2. WEB-02: Weak Admin Credentials")
print("3. WEB-03: IDOR on Basket Endpoint")
print("4. WEB-05: User Enumeration")
print("5. WEB-07: Missing Account Lockout")
print("all. Run all findings")

choice = input("Pick a number (or 'all'): ")

if choice == "1":
    result = run_web01(target)
    print(f"\n{result['id']}")
    if result["vulnerable"]:
        print(f"[+] VULNERABLE — {result['plain_english']}")
        print(f"    Technical: {result['technical']}")
    else:
        print(f"[-] Not vulnerable — {result['plain_english']}")
        print(f"    Technical: {result['technical']}")

elif choice == "2":
    result = run_web02(target)
    print(f"\n{result['id']}")
    if result["vulnerable"]:
        print(f"[+] VULNERABLE — {result['plain_english']}")
        print(f"    Technical: {result['technical']}")
    else:
        print(f"[-] Not vulnerable — {result['plain_english']}")
        print(f"    Technical: {result['technical']}")

elif choice == "3":
    result = run_web03(target)
    print(f"\n{result['id']}")
    if result["vulnerable"]:
        print(f"[+] VULNERABLE — {result['plain_english']}")
        print(f"    Technical: {result['technical']}")
    else:
        print(f"[-] Not vulnerable — {result['plain_english']}")
        print(f"    Technical: {result['technical']}")

elif choice == "4":
    result = run_web05(target)
    print(f"\n{result['id']}")
    if result["vulnerable"]:
        print(f"[+] VULNERABLE — {result['plain_english']}")
        print(f"    Technical: {result['technical']}")
    else:
        print(f"[-] Not vulnerable — {result['plain_english']}")
        print(f"    Technical: {result['technical']}")

elif choice == "5":
    result = run_web07(target)
    print(f"\n{result['id']}")
    if result["vulnerable"]:
        print(f"[+] VULNERABLE — {result['plain_english']}")
        print(f"    Technical: {result['technical']}")
    else:
        print(f"[-] Not vulnerable — {result['plain_english']}")
        print(f"    Technical: {result['technical']}")

elif choice == "all":
    functions = [run_web01, run_web02, run_web03, run_web05, run_web07]
    results = []
    for func in functions:
        result = func(target)
        results.append(result)

    for r in results:
        print(f"\n{r['id']}")
        if r["vulnerable"]:
            print(f"[+] VULNERABLE — {r['plain_english']}")
            print(f"    Technical: {r['technical']}")
        else:
            print(f"[-] Not vulnerable — {r['plain_english']}")
            print(f"    Technical: {r['technical']}")

else:
    print("Not a valid choice")
