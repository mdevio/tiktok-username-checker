import time, os, string, random

from config import directory, Fore

def username_generator():
    try:
        while True:
            amount_of_usernames = int(input("\nHow many usernames do you want to generate? (Max 10K)\n\nYour choice: "))

            if amount_of_usernames <= 10000 and amount_of_usernames > 0:
                break
            elif amount_of_usernames > 10000 or amount_of_usernames <= 0:
                print(Fore.RED + "Amount of usernames to generate may only be between 1-10000.")
        
        while True:
            amount_of_characters = int(input("\nHow many characters would you want the generated usernames to have? (2-24)\n\nYour choice: "))

            if amount_of_characters >= 2 and amount_of_characters <= 24:
                break
            elif amount_of_characters < 2 or amount_of_characters > 24:
                print(Fore.RED + "Username has to be between 2 and 24 characters.")

    except ValueError:
        print(Fore.RED + "Please enter only integers.")

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
        with open(rf"{directory}\output\usernames.txt", "a") as f:
            f.write(_ + "\n")
    
    print(Fore.GREEN + f"\nSuccessfully generated {amount_of_usernames} usernames with {amount_of_characters} characters each.")
    time.sleep(3)
    os.system("cls")