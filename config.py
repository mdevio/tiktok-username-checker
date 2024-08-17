import os, time, keyboard, requests, ctypes, string, random
from colorama import Fore, init


class TiktokUsernameChecker:
    version = "v1.3.3"
    available = 0
    unavailable = 0
    usernames = set()
    directory = os.path.dirname(os.path.abspath(__file__)) # Get directory path 
    endpoint = "https://www.tiktok.com/@"
    githubapi_endpoint = "https://api.github.com/repos/mdevio/tiktok-username-checker/releases/latest"
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