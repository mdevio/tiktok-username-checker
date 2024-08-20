from config import time, os, shutil
from config import Fore
from config import TiktokUsernameChecker

def clear_usernames():
    if os.path.exists(TiktokUsernameChecker.pycache_dir):
        shutil.rmtree(TiktokUsernameChecker.pycache_dir)
        print(Fore.GREEN + "\nSuccessfully cleared the pycache.\n")
        time.sleep(1)
    if TiktokUsernameChecker.usernames:
        TiktokUsernameChecker.usernames = set()
        f = TiktokUsernameChecker.WriteOrRead("usernames.txt", "w")
        f.close()
        print(Fore.GREEN + "\nSuccessfully cleared the usernames.\n")
        time.sleep(1)
        os.system("cls")
    else:
        print(Fore.RED + "The file 'usernames.txt' is already empty, cannot clear it.")
        time.sleep(2)
        os.system("cls")