from config import time, os
from config import directory, Fore
from config import usernames

def clear_usernames():
    global usernames
    if usernames:
        usernames = set()
        with open(rf"{directory}\output\usernames.txt", "w"):
            pass
        print(Fore.GREEN + "\nSuccessfully cleared the usernames.\n")
        time.sleep(2.5)
        os.system("cls")
    else:
        print(Fore.RED + "The file 'usernames.txt' is already empty, cannot clear it.")
        time.sleep(2.5)
        os.system("cls")
