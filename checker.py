from config import os, keyboard, Fore, requests, time
from update_title import update_title
from config import TiktokUsernameChecker


def checker():
    if TiktokUsernameChecker.usernames:
        os.system("cls")
        for username in TiktokUsernameChecker.usernames:
            if keyboard.is_pressed("space"):
                os.system("cls")
                print(Fore.RED + "Stopping the TikTok Username Checker!")
                break
            request = requests.get(TiktokUsernameChecker.endpoint + username)
            if request.status_code == 200:
                TiktokUsernameChecker.tried_usernames.add(username)

                if "followingcount" not in request.text.lower():
                    TiktokUsernameChecker.available += 1
                    TiktokUsernameChecker.available_usernames.add(username)
                    print(Fore.GREEN + "[Available/Banned] " + request.url)
                elif "followingcount" in request.text.lower() or username.isdigit():
                    TiktokUsernameChecker.unavailable += 1
                    print(Fore.RED + "[Unavailable]      " + request.url)
            else:
                print("Ratelimited!")

            update_title("checker")

        for username in TiktokUsernameChecker.tried_usernames: # Remove all tried usernames from usernames
            TiktokUsernameChecker.usernames.remove(username)

        TiktokUsernameChecker.tried_usernames = set() # Reset tried_usernames variable

        try:
            f = TiktokUsernameChecker.WriteOrRead("available_usernames.txt", "x")
        except FileExistsError:
            f = TiktokUsernameChecker.WriteOrRead("available_usernames.txt", "a")
        finally:
            for username in TiktokUsernameChecker.available_usernames:
                f.write(username + "\n")
            f.close()
                
        print(f"\nYou have checked {TiktokUsernameChecker.available+TiktokUsernameChecker.unavailable} usernames. The results are the following:\n\nAvailable: {TiktokUsernameChecker.available}\nUnavailable: {TiktokUsernameChecker.unavailable}\n\nAll of the available usernames has been saved in a file named 'available_usernames.txt' in the output folder.")
        input("\nPress enter to continue.")
        os.system("cls")
        keyboard.read_event(suppress=True)
    else:
        print(Fore.RED + "The file 'usernames.txt' is empty. Please generate usernames via the menu or input usernames in the file.")
        time.sleep(3)
        os.system("cls")