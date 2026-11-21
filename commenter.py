import time
import requests
import config

domen = config.DOMEN
better_auth = config.TOKEN

coin = input("Coins name: ")
content = input("Comment: ")
quantity = int(input("Amount of comments: "))

BASE_URL = f"https://{domen}/api/coin/{coin}/comments"


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

def comment():
    payload = {
        "content": content,
    }

    r = session.post(BASE_URL, json=payload)
    r.raise_for_status()
    return r.json()

for counter in range(1, quantity + 1):
    try:
        data = comment()
        print(f"Запрос #{counter} успешен {data}")
    except requests.RequestException as e:
        print(f"Ошибка при отправке запроса #{counter}: {e}")
        if e.response is not None:
            print(f"Ответ сервера: {e.response.text}")
        time.sleep(2)