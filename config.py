import os, time, keyboard, requests, ctypes, string, random
from colorama import Fore, init


class TiktokUsernameChecker:
    available = 0
    unavailable = 0
    usernames = set()
    directory = os.path.dirname(os.path.abspath(__file__)) # Get directory path 
    endpoint = "https://www.tiktok.com/@"
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