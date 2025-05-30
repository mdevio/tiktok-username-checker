# MADE BY @MDEVIO ON GITHUB

try: # Trying to import the required packages & functions
    from config import TiktokUsernameChecker
    from config import os, time, keyboard
    from config import Fore, init
    from username_generator import username_generator
    from checker import checker_main
    from update_title import update_title
    from clear_usernames import clear_usernames

except ImportError as package_not_installed: # If ImportError is raised, error message is sent.
    input(f"{package_not_installed} is installed. Please follow the instructions on github.\nPress enter to exit the program.")
    exit()


def main():
    """
    Main function which holds the main menu for the program.
    """
    while True:
        update_title("main")
        for i in range(0, 10):
            print("CHECK USERNAME AVAILABILITY ACROSS 20 PLATFORMS WITH ONLY 1 CLICK: https://usernamechecker.online/")
            time.sleep(0.1)
        time.sleep(2.5)
        print("\n\n" + TiktokUsernameChecker.title + "\n\n")
        print("[1] Start the TikTok Username Checker\n[2] Username Generator\n[3] Clear 'usernames.txt' and cache\n[4] Exit\n")

        while True:
            event = keyboard.read_event(suppress=True)
            if event.name in ["1", "2", "3", "4"]:
                menu = int(event.name)
                break
            else:
                print(Fore.RED + "\nChoose either 1, 2, 3 or 4.\n")
                time.sleep(2.5)
                os.system("cls")
                break

        if event.name in ["1", "2", "3", "4"]:
            break

    if menu == 1:
        try:
            while True:
                time.sleep(0.1)
                print("How many threads do you want to use? (1-9)\n")
                TiktokUsernameChecker.threads = keyboard.read_event(suppress=True)
                if int(TiktokUsernameChecker.threads.name) > 0 and int(TiktokUsernameChecker.threads.name) <= 9:
                    TiktokUsernameChecker.threads = int(TiktokUsernameChecker.threads.name)
                    break
                elif int(TiktokUsernameChecker.threads.name) > 9:
                    print(Fore.RED + "\nYou can choose max 9 threads to prevent ratelimits.\n")
                elif int(TiktokUsernameChecker.threads.name) <= 0:
                    print(Fore.RED + "\nYou have to choose atleast 1 thread.\n")
        except ValueError:
            print(Fore.RED + "\nYou must choose an integer between 1-9.\n")
        checker_main()

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
    init(autoreset=True) # Initiate colorama in terminal

    latest_version = TiktokUsernameChecker.check_for_updates(update=False)
    if latest_version == TiktokUsernameChecker.version: # If user has the latest version - continue
        pass
    else:
        while True:
            update = input(f"You are using an outdated version!\nVersion installed: {TiktokUsernameChecker.version}\nLatest version: {latest_version}\n\nDo you want to update to the latest version? (yes/no)\n\nYour choice: ").lower()
            if update == "yes":
                latest_url = TiktokUsernameChecker.check_for_updates(update=True)
                print(Fore.GREEN + f"\nHere you can download the latest version: {latest_url}\n")
                input("Press enter to exit the program.")
                exit()
            elif update == "no":
                break
            else:
                print(Fore.RED + "\nYou must choose either yes or no.\n")
                time.sleep(2.5)

    while True:
        try:
            f = TiktokUsernameChecker.WriteOrRead("usernames.txt", "r")
            TiktokUsernameChecker.usernames = {line.strip() for line in f}
            f.close()
        except FileNotFoundError:
            f = TiktokUsernameChecker.WriteOrRead("usernames.txt", "x")
            f.close()

        main()