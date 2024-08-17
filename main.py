# MADE BY @MDEVIO ON GITHUB

try: # Trying to import the required packages & functions
    from config import TiktokUsernameChecker
    from config import os, time
    from config import Fore, init
    from username_generator import username_generator
    from checker import checker
    from update_title import update_title
    from clear_usernames import clear_usernames

except ImportError as package_not_installed: # If ImportError is raised, error message is sent.
    input(f"Package {package_not_installed} is not installed. Please follow the instructions on github.\nPress enter to exit the program.")
    exit()


def main():
    while True:
        try:
            update_title("main")
            print("\n" + TiktokUsernameChecker.title + "\n\n")
            menu = int(input("[1] Start the TikTok Username Checker\n[2] Username Generator\n[3] Clear 'usernames.txt' and cache\n[4] Exit\n\nYour choice: "))
            break

        except ValueError:
            print(Fore.RED + "\nChoose either 1, 2, 3 or 4.\n")
            time.sleep(2.5)
            os.system("cls")

    if menu == 1:
        checker()
    elif menu == 2:
        username_generator()
    elif menu == 3:
        clear_usernames()
    elif menu == 4:
        exit()
    else:
        print(Fore.RED + "\nChoose either 1, 2, 3 or 4.\n")
        time.sleep(2.5)
        os.system("cls")


if __name__ == "__main__":
    while True:
        init(autoreset=True) # Initiate colorama in terminal
        f = TiktokUsernameChecker.WriteOrRead("usernames.txt", "r")
        for username in f.readlines():
            username = username.rstrip()
            TiktokUsernameChecker.usernames.add(username)

        main()