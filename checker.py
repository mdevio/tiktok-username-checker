# MADE BY @MDEVIO ON GITHUB
from config import os, keyboard, Fore, cloudscraper, time, threading, ThreadPoolExecutor, as_completed, random
from update_title import update_title
from config import TiktokUsernameChecker

def checker_main():
    """
    Main function for the Checker
    """
    global executor, scraper, headers_list
    if TiktokUsernameChecker.usernames:
        os.system("cls")
        spacebar_thread = threading.Thread(target=monitor_spacebar) # spacebar thread
        spacebar_thread.start() # start spacebar thread
        scraper = cloudscraper.create_scraper()

        headers_list = [
            {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"},
            {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"},
            {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}
        ]

        with ThreadPoolExecutor(max_workers=int(TiktokUsernameChecker.threads)) as executor:
            futures = [executor.submit(checker, username) for username in TiktokUsernameChecker.usernames]
            spacebar_thread.join() # join
            for future in as_completed(futures):
                future.result()

        for username in TiktokUsernameChecker.tried_usernames: # Remove all tried usernames from usernames
            TiktokUsernameChecker.usernames.remove(username)

        TiktokUsernameChecker.tried_usernames = set() # Reset tried_usernames variable

        try:
            f = TiktokUsernameChecker.WriteOrRead("available_usernames.txt", "x")
        except FileExistsError:
            f = TiktokUsernameChecker.WriteOrRead("available_usernames.txt", "a")
        finally:
            for username in TiktokUsernameChecker.available_usernames:
                f.write(username + "\n")
            f.close()
                
        print(f"\nYou have checked {TiktokUsernameChecker.available+TiktokUsernameChecker.unavailable} usernames. The results are the following:\n\nAvailable/Banned: {TiktokUsernameChecker.available}\nUnavailable: {TiktokUsernameChecker.unavailable}\n\nAll of the available usernames has been saved in a file named 'available_usernames.txt' in the output folder.")
        input("\nPress enter to continue.")
        os.system("cls")
        TiktokUsernameChecker.available = 0
        TiktokUsernameChecker.unavailable = 0
        TiktokUsernameChecker.lock = threading.Lock()
        TiktokUsernameChecker.stop_event = threading.Event()
        keyboard.read_event(suppress=True)
    else:
        print(Fore.RED + "The file 'usernames.txt' is empty. Please generate usernames via the menu or input usernames in the file.")
        time.sleep(3)
        os.system("cls")

def monitor_spacebar():
    """
    Monitors the spacebar key to stop the TikTok Username Checker
    """
    while not TiktokUsernameChecker.stop_event.is_set():
        if keyboard.is_pressed('space'):
            TiktokUsernameChecker.stop_event.set()
            break

def checker(username):
    """
    Checks the availability of a TikTok username
    """
    try:
        if TiktokUsernameChecker.stop_event.is_set():
            return
        TiktokUsernameChecker.tried_usernames.add(username)
        if len(TiktokUsernameChecker.usernames) == len(TiktokUsernameChecker.tried_usernames):
            TiktokUsernameChecker.stop_event.set()

        if not username.isdigit():
            request = scraper.get(TiktokUsernameChecker.endpoint + username, headers=random.choice(headers_list))
            while len(request.text) < 200000:
                request = scraper.get(TiktokUsernameChecker.endpoint + username, headers=random.choice(headers_list))

            if request.status_code == 200:
                if "followingcount" in request.text.lower():
                    with TiktokUsernameChecker.lock:
                        TiktokUsernameChecker.unavailable += 1
                        print(Fore.RED + "[Unavailable]      " + request.url)
                elif "followingcount" not in request.text.lower():
                    with TiktokUsernameChecker.lock:
                        TiktokUsernameChecker.available += 1
                        TiktokUsernameChecker.available_usernames.add(username)
                        print(Fore.GREEN + "[Available/Banned] " + request.url)
            else:
                with TiktokUsernameChecker.lock:
                    print("Ratelimited!")
        else:
            with TiktokUsernameChecker.lock:
                TiktokUsernameChecker.unavailable += 1
                print(Fore.RED + "[Unavailable]      " + request.url)
        update_title("checker")
    except Exception as e:
        with TiktokUsernameChecker.lock:
            print(Fore.YELLOW + f"[Error] {username}: {e}")