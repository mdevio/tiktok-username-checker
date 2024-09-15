# MADE BY @MDEVIO ON GITHUB
from config import time, os, string, random
from config import Fore
from config import TiktokUsernameChecker

def username_generator():
    while True:
        try:
            amount_of_usernames = int(input("\nHow many usernames do you want to generate? (Max 10K)\n\nYour choice: "))

            if amount_of_usernames <= 10000 and amount_of_usernames > 0:
                break
            elif amount_of_usernames > 10000 or amount_of_usernames <= 0:
                print(Fore.RED + "Amount of usernames to generate may only be between 1-10000.")
        except ValueError:
            print(Fore.RED + "Please enter only integers.")

    while True:
        try:
            amount_of_characters = int(input("\nHow many characters would you want the generated usernames to have? (2-24)\n\nYour choice: "))

            if amount_of_characters >= 2 and amount_of_characters <= 24:
                break
            elif amount_of_characters < 2 or amount_of_characters > 24:
                print(Fore.RED + "Username has to be between 2 and 24 characters.")
        except ValueError:
            print(Fore.RED + "Please enter only integers.")

    generated_usernames = set()
    characters = string.ascii_lowercase + string.digits + "_."

    if amount_of_characters == 2 and amount_of_usernames > 1344: # 1344 is the maximum amount of combinations of 2 characters
        amount_of_usernames = 1344
        print("Maximum of combinations for 2 character names are 1344.")


    while len(generated_usernames) < amount_of_usernames:
        _ = ''.join(random.choice(characters) for _ in range(amount_of_characters))
        if _ not in generated_usernames:
            generated_usernames.add(_)
            
    f = TiktokUsernameChecker.WriteOrRead("usernames.txt", "a")
    for _ in generated_usernames:
        f.write(_ + "\n")
    f.close()
    
    print(Fore.GREEN + f"\nSuccessfully generated {amount_of_usernames} usernames with {amount_of_characters} characters each.")
    time.sleep(3)
    os.system("cls")
