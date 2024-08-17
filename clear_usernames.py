from config import time, os
from config import Fore
from config import TiktokUsernameChecker

def clear_usernames():
    if TiktokUsernameChecker.usernames:
        TiktokUsernameChecker.usernames = set()
        TiktokUsernameChecker.WriteOrRead("usernames.txt", "w")
        print(Fore.GREEN + "\nSuccessfully cleared the usernames.\n")
        time.sleep(2.5)
        os.system("cls")
    else:
        print(Fore.RED + "The file 'usernames.txt' is already empty, cannot clear it.")
        time.sleep(2.5)
        os.system("cls")
