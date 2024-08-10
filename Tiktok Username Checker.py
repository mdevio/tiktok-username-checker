import requests
from colorama import Fore
import ctypes
import os
import time
directory = os.path.dirname(os.path.abspath(__file__)) # Get directory path
usernames = []

with open(rf"{directory}\main\usernames.txt", "r") as f:
    lines = f.readlines()
    for username in lines:
        username = username.rstrip()
        usernames.append(username)

if not usernames:
    print("You have no usernames in the usernames.txt file.")
    time.sleep(3)
    exit()

def update_title():
    remaining = len(usernames) - (available + unavailable)
    ctypes.windll.kernel32.SetConsoleTitleW(f"Username Checker for TikTok | Available: {available} | Unavailable: {unavailable} | Remaining: {remaining} | Total: {available + unavailable}")


title = r"""
$$$$$$$$\ $$\ $$\    $$$$$$$$\        $$\             $$\   $$\                                                                                  $$$$$$\  $$\                           $$\                           
\__$$  __|\__|$$ |   \__$$  __|       $$ |            $$ |  $$ |                                                                                $$  __$$\ $$ |                          $$ |                          
   $$ |   $$\ $$ |  $$\ $$ | $$$$$$\  $$ |  $$\       $$ |  $$ | $$$$$$$\  $$$$$$\   $$$$$$\  $$$$$$$\   $$$$$$\  $$$$$$\$$$$\   $$$$$$\        $$ /  \__|$$$$$$$\   $$$$$$\   $$$$$$$\ $$ |  $$\  $$$$$$\   $$$$$$\  
   $$ |   $$ |$$ | $$  |$$ |$$  __$$\ $$ | $$  |      $$ |  $$ |$$  _____|$$  __$$\ $$  __$$\ $$  __$$\  \____$$\ $$  _$$  _$$\ $$  __$$\       $$ |      $$  __$$\ $$  __$$\ $$  _____|$$ | $$  |$$  __$$\ $$  __$$\ 
   $$ |   $$ |$$$$$$  / $$ |$$ /  $$ |$$$$$$  /       $$ |  $$ |\$$$$$$\  $$$$$$$$ |$$ |  \__|$$ |  $$ | $$$$$$$ |$$ / $$ / $$ |$$$$$$$$ |      $$ |      $$ |  $$ |$$$$$$$$ |$$ /      $$$$$$  / $$$$$$$$ |$$ |  \__|
   $$ |   $$ |$$  _$$<  $$ |$$ |  $$ |$$  _$$<        $$ |  $$ | \____$$\ $$   ____|$$ |      $$ |  $$ |$$  __$$ |$$ | $$ | $$ |$$   ____|      $$ |  $$\ $$ |  $$ |$$   ____|$$ |      $$  _$$<  $$   ____|$$ |      
   $$ |   $$ |$$ | \$$\ $$ |\$$$$$$  |$$ | \$$\       \$$$$$$  |$$$$$$$  |\$$$$$$$\ $$ |      $$ |  $$ |\$$$$$$$ |$$ | $$ | $$ |\$$$$$$$\       \$$$$$$  |$$ |  $$ |\$$$$$$$\ \$$$$$$$\ $$ | \$$\ \$$$$$$$\ $$ |      
   \__|   \__|\__|  \__|\__| \______/ \__|  \__|       \______/ \_______/  \_______|\__|      \__|  \__| \_______|\__| \__| \__| \_______|       \______/ \__|  \__| \_______| \_______|\__|  \__| \_______|\__|      
                                                                                                                                                                                                                      
                                                                                                                                                                                                                      
                                                                                                                                                                                                                      """

while True:
    available_usernames = []
    available = 0
    unavailable = 0
    update_title()
    print("\n" + title)
    menu = int(input("[1] Start the TikTok Username Checker\n[2] Exit\n\nYour choice: "))

    if menu == 1:
        for _ in usernames:
            request = requests.get(f"https://www.tiktok.com/@{_}")

            if "avatarlarger" in request.text.lower():
                available += 1
                available_usernames.append(_)
                update_title()
                print(Fore.GREEN + request.url + Fore.RESET)
            elif "avatarlarger" not in request.text.lower():
                unavailable += 1
                update_title()
                print(Fore.RED + request.url + Fore.RESET)
            else:
                print("Error!")
                
        print(f"All of the {available+unavailable} usernames were checked. The results are the following:\n\nAvailable: {available}\nUnavailable: {unavailable}\n\nAll of the available names were saved in a txt file called 'Available Usernames.txt' in the main folder in the same directory as the python file.")
        time.sleep(5)

        try:
            with open(rf"{directory}\main\Available Usernames.txt", "x") as f:
                for username in available_usernames:
                    f.write(username + "\n")
        except FileExistsError:
            with open(rf"{directory}\main\Available Usernames.txt", "w") as f:
                for username in available_usernames:
                    f.write(username + "\n")
    elif menu == 2:
        break
    else:
        print("Choose either 1 or 2.")
