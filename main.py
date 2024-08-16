# MADE BY @MDEVIO ON GITHUB

try: # Trying to import the required packages & functions
    from config import os, time
    from config import Fore, init
    from config import directory, title, usernames
    from config import available, unavailable, duplicates
    from username_generator import username_generator
    from checker import checker
    from update_title import update_title
    from clear_usernames import clear_usernames

except ImportError as package_not_installed: # If ImportError is raised, error message is sent.
    input(f"Package {package_not_installed} is not installed. Please follow the instructions on github.\nPress enter to exit the program.")
    exit()


def main():
    global available, unavailable, duplicates
    while True:
        try:
            update_title()
            print("\n" + title)
            menu = int(input("[1] Start the TikTok Username Checker\n[2] Username Generator\n[3] Clear 'usernames.txt'\n[4] Exit\n\nYour choice: "))
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


while True:
    init(autoreset=True) # Initiate colorama in terminal
    try:
        with open(rf"{directory}\output\usernames.txt", "r") as f:
            lines = f.readlines()
            for username in lines:
                username = username.rstrip()
                usernames.add(username)

    except FileNotFoundError:
        with open(rf"{directory}\output\usernames.txt", "x") as f:
            pass

    main()