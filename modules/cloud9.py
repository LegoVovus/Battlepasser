import requests
import time

domen = "catplay.org"
better_auth = "6NLvXAfCzxS5CTUbn7VuSMtREI2EQKUN.O6j7Zlckv2Lm7hqDlNib1k83DmEhMml88E%2BcHCke3wE%3D"

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
        "mineCount": 3
    }

    r = session.post(f"{BASE_URL}/start", json=payload, timeout=2)
    r.raise_for_status()

    data = r.json()
    print(f"CLOUD9 | Started on {domen}: {data}")

    return data["sessionToken"]

def reveal_tile(session_token, tile_index):
    payload = {
        "sessionToken": session_token,
        "tileIndex": tile_index
    }

    r = session.post(f"{BASE_URL}/reveal", json=payload, timeout=2)
    r.raise_for_status()

    return r.json()

def main():
    while True:
        try:
            session_token = start_game()
            tile_index = 0
            while tile_index <= 22:
                result = reveal_tile(session_token, tile_index)
                print(f"Reveal {tile_index}: {result}")

                if result.get("hitMine") is True:
                    print("Hit mine! Starting new game.. \n")
                    break

                tile_index += 1

                time.sleep(0.25)
            else:
                print("Reached tile 22.\n")
                quit()

        except requests.RequestException as e:
            print(f"HTTP error: {e}")
            time.sleep(2)

        except Exception as e:
            print(f"Unexpected error: {e}")
            time.sleep(2)

if __name__ == "__main__":
    main()