import requests
import config


domen = config.DOMEN
better_auth = config.TOKEN

coin = input("Coin name: ")
amount = float(input("Amount of each trade: "))
type = input("P.S. Auto means buy and then sell coin for that amount\nType of trade (buy/sell/auto): ")

i = int(input("Amount of trades: "))

BASE_URL = f"https://{domen}/api/coin/{coin}/trade"

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

def start_buy(trade):
    payload = {
        "amount": amount,
        "type": trade
    }
    r = session.post(BASE_URL, json=payload, timeout=1)
    r.raise_for_status()

    data = r.json()
    print(f"{type.upper()} | Started on {domen}: {data}")


for counter in range(1, i + 1):
    try:
        if type.upper() == "BUY":
            for counter in range(1, i + 1):
                start_buy("BUY")
        elif type.upper() == "SELL":
            for counter in range(1, i + 1):
                start_buy("SELL")
        elif type.upper() == "AUTO":
            for counter in range(1, i + 1):
                start_buy("BUY")
                start_buy("SELL")
    except requests.RequestException as e:
        print(f"Error! {e}")