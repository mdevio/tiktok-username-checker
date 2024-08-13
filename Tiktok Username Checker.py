try:
    import requests, ctypes, os, time, random, string
    from colorama import Fore
except ImportError as package_not_installed:
    input(f"Package {package_not_installed} is not installed.\nPress enter to exit the program.")

def update_title():
    remaining = len(usernames) - (available + unavailable)
    ctypes.windll.kernel32.SetConsoleTitleW(f"Username Checker for TikTok | Available: {available} | Unavailable: {unavailable} | Remaining: {remaining} | Total: {available + unavailable}")

directory = os.path.dirname(os.path.abspath(__file__)) # Get directory path
usernames = []


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
    with open(rf"{directory}\main\usernames.txt", "r") as f:
        lines = f.readlines()
        for username in lines:
            username = username.rstrip()
            usernames.append(username)
    available_usernames = []
    available = 0
    unavailable = 0
    update_title()
    print("\n" + title)
    menu = int(input("[1] Start the TikTok Username Checker\n[2] Username Generator\n[3] Exit\n\nYour choice: "))

    if menu == 1:
        for _ in usernames:
            request = requests.get(f"https://www.tiktok.com/@{_}")

            if "followingcount" not in request.text.lower():
                available += 1
                available_usernames.append(_)
                update_title()
                print(Fore.GREEN + request.url + Fore.RESET)
            elif "followingcount" in request.text.lower():
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
        while True:
            amount_of_usernames = int(input("How many usernames do you want to generate? (Max 10K)\n\nYour choice: "))

            if amount_of_usernames <= 10000:
                break
            else:
                print(Fore.RED + "Max 10K usernames!" + Fore.RESET)
            
        while True:
            amount_of_characters = int(input("How many characters would you want the generated usernames to have? (2-24)\n\nYour choice: "))

            if amount_of_characters >= 2 and amount_of_characters <= 24:
                break
            else:
                print(Fore.RED + "Username has to be between 2 and 24 characters." + Fore.RESET)

        generated_usernames = []
        characters = string.ascii_letters + string.digits + "_."

        for i in range(amount_of_usernames):
            temp_username = ""
            for index in range(amount_of_characters):
                random_char = random.choice(characters)
                temp_username += random_char
            generated_usernames.append(temp_username)
                
        for generated_username in generated_usernames:
            with open(rf"{directory}\main\usernames.txt", "a") as f:
                f.write(generated_username + "\n")

    elif menu == 3:
        break
    else:
        print("Choose either 1, 2 or 3.")
