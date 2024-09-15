# MADE BY @MDEVIO ON GITHUB
import os, time, keyboard, requests, ctypes, string, random, shutil, platform, threading
from colorama import Fore, init
from concurrent.futures import ThreadPoolExecutor, as_completed


class TiktokUsernameChecker:
    version = "v1.5.1"
    available = 0
    unavailable = 0
    threads = 5
    lock = threading.Lock()
    stop_event = threading.Event()
    usernames = set()
    remaining = 0
    directory = os.path.dirname(os.path.abspath(__file__)) # Get directory path 
    endpoint = "https://www.tiktok.com/@"
    githubapi_endpoint = "https://api.github.com/repos/mdevio/tiktok-username-checker/releases/latest"
    pycache_dir = rf"{directory}\__pycache__"
    available_usernames = set()
    tried_usernames = set()
    title = r"""
    $$$$$$$$\ $$$$$$$$\ $$\   $$\  $$$$$$\  
    \__$$  __|\__$$  __|$$ |  $$ |$$  __$$\ 
       $$ |      $$ |   $$ |  $$ |$$ /  \__|
       $$ |      $$ |   $$ |  $$ |$$ |      
       $$ |      $$ |   $$ |  $$ |$$ |      
       $$ |      $$ |   $$ |  $$ |$$ |  $$\ 
       $$ |      $$ |   \$$$$$$  |\$$$$$$  |
       \__|      \__|    \______/  \______/ """
    

    def WriteOrRead(file, mode):
        f = open(rf"{TiktokUsernameChecker.directory}\output\{file}", f"{mode}")
        return f
    
    def check_for_updates(update):
        request = requests.get(TiktokUsernameChecker.githubapi_endpoint)
        if request.status_code == 200:
            latest_version = request.json()
            if update == False:
                return latest_version['tag_name']
            elif update == True:
                latest_url = latest_version['html_url']
                return latest_url
        else:
            raise Exception(f'Failed to fetch release info: {request.status_code}')