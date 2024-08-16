from config import usernames, directory, tried_usernames, available_usernames
from config import available, unavailable, duplicates
from config import os, keyboard, Fore, requests, time
from update_title import update_title


def checker():
    global available, unavailable, duplicates
    os.system("cls")
    if usernames:
        for username in usernames:
            if keyboard.is_pressed("space"):
                os.system("cls")
                print(Fore.RED + "Stopping the TikTok Username Checker!")
                break
            if username in tried_usernames:
                duplicates += 1
                update_title()
                print(Fore.YELLOW + "[Duplicate] " + f"https://www.tiktok.com/@{username}")
            elif username not in tried_usernames:
                request = requests.get(f"https://www.tiktok.com/@{username}")
                tried_usernames.add(username)

                if "followingcount" not in request.text.lower():
                    available += 1
                    available_usernames.add(username)
                    update_title()
                    print(Fore.GREEN + "[Available/Banned] " + request.url)
                elif "followingcount" in request.text.lower() or username.isdigit():
                    unavailable += 1
                    update_title()
                    print(Fore.RED + "[Unavailable]      " + request.url)
                elif request.status_code != 200:
                    print("Ratelimited!")
                else:
                    print("Error!")

        try:
            with open(rf"{directory}\output\available_usernames.txt", "x") as f:
                for username in available_usernames:
                    f.write(username + "\n")
        except FileExistsError:
            with open(rf"{directory}\output\available_usernames.txt", "w") as f:
                for username in available_usernames:
                    f.write(username + "\n")
                
        print(f"\nAll of the {available+unavailable} usernames were checked. The results are the following:\n\nAvailable: {available}\nUnavailable: {unavailable}\nDuplicates: {duplicates}\n\nAll of the available names were saved in a txt file called 'available_usernames.txt' in the output folder in the same directory as the python file.")
        input("Press enter to continue.")
        os.system("cls")
    else:
        print(Fore.RED + "The file 'usernames.txt' is empty. Please generate usernames via the menu or input usernames in the file.")
        time.sleep(3)