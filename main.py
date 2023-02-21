import requests
from colorama import Fore
token = input(f"Token{Fore.LIGHTBLACK_EX}:{Fore.WHITE}>> ")
    token=token
def blockAllFriends(token):
    set_console_title("Private")
    headers = {"authorization": token, "user-agent": "bruh6/9"}
    json = {"type": 2}
    block_friends_request = requests.get("https://canary.discord.com/api/v9/users/@me/relationships", headers=headers).json()
    for i in block_friends_request:
        requests.put(
            f"https://canary.discord.com/api/v9/users/@me/relationships/{i['id']}",
            headers=headers,
            json=json,
        )
        print(f"{Fore.WHITE}[{Fore.LIGHTCYAN_EX}f{Fore.WHITE}] Friend Has been blocked| {i['id']}")
