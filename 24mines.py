import random
import time
import requests

import config

domen = config.DOMEN
better_auth = config.TOKEN

BASE_URL = f"https://{domen}/api/arcade/mines"

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


def start_game():
    payload = {
        "betAmount": 0.01,
        "mineCount": 24,
    }

    r = session.post(f"{BASE_URL}/start", json=payload, timeout=1)
    r.raise_for_status()

    data = r.json()
    print(f"Игра начата: {data}")

    return data["sessionToken"]


def reveal_tile(session_token, tile_index):
    payload = {
        "sessionToken": session_token,
        "tileIndex": tile_index,
    }

    r = session.post(f"{BASE_URL}/reveal", json=payload, timeout=2)
    r.raise_for_status()

    return r.json()


def cashout(session_token):
    payload = {
        "sessionToken": session_token,
    }
    try:
        r = session.post(f"{BASE_URL}/cashout", json=payload, timeout=2)
        r.raise_for_status()
        print(f"{r.json()}")
    except requests.RequestException as e:
        print(f"{e}")


def main():
    games_played = 0
    wins = 0
    
    while True:
        try:
            games_played += 1
            print(f"\n--- Game {games_played} (Wins: {wins}) ---")
            
            session_token = start_game()
            
            target_tile = random.randint(0, 24)
            print(f"Trying to open a tile {target_tile}")
            
            result = reveal_tile(session_token, target_tile)
            print(f"Result: {result}")

            if result.get("hitMine") is True:
                print("Explosion! Starting new game.")
                continue

            wins += 1
            print("Success! The only safe tile was found!")
            
            cashout(session_token)
            
            print("Starting another game...")
            time.sleep(0.25)

        except requests.RequestException as e:
            print(f"Error! {e}")
            time.sleep(3)

        except Exception as e:
            print(f"Unexpected error! {e}")
            time.sleep(3)


if __name__ == "__main__":
    main()
