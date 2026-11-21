import time
import requests
import config

domen = config.DOMEN
better_auth = config.TOKEN

hopium = input("Hopium's ID: ")
side_input = input("Side (True/False): ").strip().lower()
side = True if side_input == "true" else False

bet_amount = float(input("Amount of each bet: "))
q = int(input("Amount of bets: "))

BASE_URL = f"https://{domen}/api/hopium/questions/{hopium}/bet"

COOKIES = {
    '__Secure-better-auth.session_token': better_auth,
}

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:148.0) Gecko/20100101 Firefox/148.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': f'https://{domen}',
    'Content-Type': 'application/json',
    'Origin': f'https://{domen}',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'DNT': '1',
    'Priority': 'u=0',
}

session = requests.Session()
session.cookies.update(COOKIES)
session.headers.update(HEADERS)

def bet():
    payload = {
        "amount": bet_amount,
        "side": side,
    }

    r = session.post(BASE_URL, json=payload)
    r.raise_for_status()
    return r.json()

for counter in range(1, q + 1):
    try:
        data = bet()
        print(f"Request #{counter} success! {data}")
    except requests.RequestException as e:
        print(f"Error while #{counter}: {e}")
        if e.response is not None:
            print(f"Server's answer: {e.response.text}")
        time.sleep(2)