import requests
import json
import time
from colorama import init, Fore
init()

payload = {
    "captcha": "",
    "type": ""
}

hwid = input(Fore.YELLOW + "[INFO] Enter your hwid: ")
code = "cacc"

print(Fore.BLUE + "[STATUS] Bypassing...")

session = requests.Session()
session.post(f"https://api-gateway.platoboost.com/v1/sessions/auth/8/{hwid}", json=payload)
time.sleep(5)
session.put(f"https://api-gateway.platoboost.com/v1/sessions/auth/8/{hwid}/{code}")
response = session.get(f"https://api-gateway.platoboost.com/v1/authenticators/8/{hwid}").text

print(Fore.GREEN + f'[SUCCESS] Your key: {json.loads(response)["key"]}')
