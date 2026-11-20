import requests

better_auth = ""
domen = ""

BASE_URL = f"https://{domen}/api/arcade"

COOKIES = {
    '__Secure-better-auth.session_token': better_auth,
}

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:148.0) Gecko/20100101 Firefox/148.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': f'https://{domen}/arcade',
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

def coinflip(amount, side):
    payload = {
        "amount": amount,
        "side": side
    }

    r = session.post(f"{BASE_URL}/coinflip", json=payload, timeout=1)
    r.raise_for_status()

    data = r.json()
    print(f"COINFLIP | Started on {domen}: {data}")

def slots(amount):
    payload = {
        "amount": amount
    }

    r = session.post(f"{BASE_URL}/slots", json=payload, timeout=1)
    r.raise_for_status()

    data = r.json()
    print(f"SLOTS | Started on {domen}: {data}")
