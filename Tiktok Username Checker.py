# MADE BY @MDEVIO ON GITHUB

try: # Trying to import the required packages
    import requests, ctypes, os, time, random, string, keyboard
    from colorama import Fore, init
except ImportError as package_not_installed: # If ImportError is raised, error message is sent.
    input(f"Package {package_not_installed} is not installed. Please follow the instructions on github.\nPress enter to exit the program.")
    exit()

def update_title():
    global usernames, available, unavailable, duplicates
    
    remaining = len(usernames) - (available + unavailable) # Formula to calculate the remaining usernames to check
    ctypes.windll.kernel32.SetConsoleTitleW(f"Username Checker for TikTok | Available/Banned: {available} | Unavailable: {unavailable} | Duplicates: {duplicates} | Remaining: {remaining} | Total checked: {available + unavailable}")


def checker():
    global available, unavailable, duplicates, directory

    os.system("cls")
    if usernames:
        for username in usernames:
            if keyboard.is_pressed("space"):
                os.system("cls")
                print(Fore.RED + "Stopping the TikTok Username Checker!" + Fore.RESET)
                break
            if username in tried_usernames:
                duplicates += 1
                update_title()
                print(Fore.YELLOW + "[Duplicate] " + f"https://www.tiktok.com/@{username}" + Fore.RESET)
            elif username not in tried_usernames:
                request = requests.get(f"https://www.tiktok.com/@{username}")
                tried_usernames.add(username)

                if "followingcount" not in request.text.lower():
                    available += 1
                    available_usernames.add(username)
                    update_title()
                    print(Fore.GREEN + "[Available/Banned] " + request.url + Fore.RESET)
                elif "followingcount" in request.text.lower() or username.isdigit():
                    unavailable += 1
                    update_title()
                    print(Fore.RED + "[Unavailable]      " + request.url + Fore.RESET)
                elif request.status_code != 200:
                    print("Ratelimited!")
                else:
                    print("Error!")

        try:
            with open(rf"{directory}\main\Available Usernames.txt", "x") as f:
                for username in available_usernames:
                    f.write(username + "\n")
        except FileExistsError:
            with open(rf"{directory}\main\Available Usernames.txt", "w") as f:
                for username in available_usernames:
                    f.write(username + "\n")
                
        print(f"\nAll of the {available+unavailable} usernames were checked. The results are the following:\n\nAvailable: {available}\nUnavailable: {unavailable}\nDuplicates: {duplicates}\n\nAll of the available names were saved in a txt file called 'Available Usernames.txt' in the main folder in the same directory as the python file.")
        input("Press enter to continue.")
        os.system("cls")
    else:
        print(Fore.RED + "The file 'usernames.txt' is empty. Please generate usernames via the main menu or input usernames in the file." + Fore.RESET)
        time.sleep(3)


def username_generator():
    try:
        while True:
            amount_of_usernames = int(input("\nHow many usernames do you want to generate? (Max 10K)\n\nYour choice: "))

            if amount_of_usernames <= 10000 and amount_of_usernames > 0:
                break
            elif amount_of_usernames > 10000 or amount_of_usernames <= 0:
                print(Fore.RED + "Amount of usernames to generate may only be between 1-10000." + Fore.RESET)
        
        while True:
            amount_of_characters = int(input("\nHow many characters would you want the generated usernames to have? (2-24)\n\nYour choice: "))

            if amount_of_characters >= 2 and amount_of_characters <= 24:
                break
            elif amount_of_characters < 2 or amount_of_characters > 24:
                print(Fore.RED + "Username has to be between 2 and 24 characters." + Fore.RESET)

    except ValueError:
        print(Fore.RED + "Please enter only integers." + Fore.RESET)

    generated_usernames = set()
    characters = string.ascii_letters + string.digits + "_."

    if amount_of_characters == 2 and amount_of_usernames > 4096: # 4096 is the maximum amount of combinations of 2 characters
        amount_of_usernames = 4096
        print("Maximum of combinations for 2 character names are 4096.")

    temp_username = ""

    while len(generated_usernames) < amount_of_usernames:
        temp_username = ''.join(random.choice(characters) for _ in range(amount_of_characters))
        if temp_username not in generated_usernames:
            generated_usernames.add(temp_username)
            
    for _ in generated_usernames:
        with open(rf"{directory}\main\usernames.txt", "a") as f:
            f.write(_ + "\n")
    
    print(Fore.GREEN + f"\nSuccessfully generated {amount_of_usernames} usernames with {amount_of_characters} characters each." + Fore.RESET)
    time.sleep(3)
    os.system("cls")


def clear_usernames():
    global usernames, directory

    if usernames:
        usernames = set()
        with open(rf"{directory}\main\usernames.txt", "w"):
            pass
        print(Fore.GREEN + "\nSuccessfully cleared the usernames.\n" + Fore.RESET)
        time.sleep(2.5)
        os.system("cls")
    else:
        print(Fore.RED + "The file 'usernames.txt' is already empty, cannot clear it." + Fore.RESET)
        time.sleep(2.5)
        os.system("cls")


directory = os.path.dirname(os.path.abspath(__file__)) # Get directory path
usernames = set()
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
    init() # Initiate colorama in terminal
    try:
        with open(rf"{directory}\main\usernames.txt", "r") as f:
            lines = f.readlines()
            for username in lines:
                username = username.rstrip()
                usernames.add(username)
    except FileNotFoundError:
        with open(rf"{directory}\main\usernames.txt", "x") as f:
            pass
    available_usernames = set()
    tried_usernames = set()
    available = 0
    unavailable = 0
    duplicates = 0
    while True:
        try:
            update_title()
            print("\n" + title)
            menu = int(input("[1] Start the TikTok Username Checker\n[2] Username Generator\n[3] Clear 'usernames.txt'\n[4] Exit\n\nYour choice: "))
            break
        except ValueError:
            print(Fore.RED + "\nChoose either 1, 2, 3 or 4.\n" + Fore.RESET)
            time.sleep(2.5)
            os.system("cls")

    if menu == 1:
        checker()
    elif menu == 2:
        username_generator()
    elif menu == 3:
        clear_usernames()
    elif menu == 4:
        break
    else:
        print(Fore.RED + "\nChoose either 1, 2, 3 or 4.\n" + Fore.RESET)
        time.sleep(2.5)
        os.system("cls")
