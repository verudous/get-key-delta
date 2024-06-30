import requests
import time
import json
from colorama import init, Fore
init()

hwid = input(Fore.YELLOW + "[INFO] Enter your hwid: ")
code = "79ca"

print(Fore.BLUE + "[STATUS] Bypassing...")

payload = {
    "captcha":"",
    "type":"Turnstile"
}

session = requests.Session()
session.post(f"https://api-gateway.platoboost.com/v1/sessions/auth/8/{hwid}", json=payload)
session.put(f"https://api-gateway.platoboost.com/v1/sessions/auth/8/{hwid}/{code}")
time.sleep(5)
session.put(f"https://api-gateway.platoboost.com/v1/sessions/auth/8/{hwid}/{code}")
response = session.get(f"https://api-gateway.platoboost.com/v1/authenticators/8/{hwid}").text

print(Fore.GREEN + f'[SUCCESS] Your key: {json.loads(response)["key"]}')
