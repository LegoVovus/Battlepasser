import time
import requests
import config

domen = config.DOMEN
better_auth = config.TOKEN

coin = input("Coins name: ")
q = int(input("Amount of coins: "))

BASE_URL = f"https://{domen}/api/coin"

COOKIES = {
    # 'cf_clearance': cf_clearance,
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

def create_coin(current_token, ticker):
    payload = {
        "name": current_token,
        "symbol": ticker,
    }

    headers_backup = session.headers.copy()
    
    if 'Content-Type' in session.headers:
        del session.headers['Content-Type']

    try:
        r = session.post(f"{BASE_URL}/create", data=payload)
        r.raise_for_status()
        print(f" Успешно создано: {r.json()}")
    finally:
        session.headers = headers_backup

def start_buy(ticker):
    payload = {
        "amount": 1,
        "type": "BUY"
    }

    session.headers['Content-Type'] = 'application/json'
    
    r = session.post(f"{BASE_URL}/{ticker}/trade", json=payload)
    r.raise_for_status()
        
    data = r.json()
    print(f" Успешная покупка: {data}")

for counter in range(1, q + 1):
    current_token = f"{coin}{counter}"
    ticker = f"{counter}{coin}".upper()
    print(f"\n--- Обработка монеты {current_token} (#{counter}/{q}) ---")
    try:
        create_coin(current_token, ticker)
        start_buy(ticker)
    except requests.RequestException as e:
        print(f"Ошибка при отправке запроса #{counter}: {e}")
        time.sleep(2)
        if hasattr(e, 'response') and e.response is not None:
            print(f"Ответ сервера: {e.response.text}")
        time.sleep(5)
    time.sleep(120)