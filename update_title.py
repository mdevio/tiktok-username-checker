from config import ctypes
from config import usernames, available, unavailable, duplicates

def update_title():
    remaining = len(usernames) - (available + unavailable) # Formula to calculate the remaining usernames to check
    ctypes.windll.kernel32.SetConsoleTitleW(f"Username Checker for TikTok | Available/Banned: {available} | Unavailable: {unavailable} | Duplicates: {duplicates} | Remaining: {remaining} | Total checked: {available + unavailable}")
