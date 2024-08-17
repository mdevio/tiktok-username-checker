from config import ctypes
from config import TiktokUsernameChecker

def update_title(ttucmode):
    remaining = len(TiktokUsernameChecker.usernames) - (TiktokUsernameChecker.available + TiktokUsernameChecker.unavailable) # Formula to calculate the remaining usernames to check
    if ttucmode == "checker":
        ctypes.windll.kernel32.SetConsoleTitleW(f"TikTok Username Checker | Available/Banned: {TiktokUsernameChecker.available} | Unavailable: {TiktokUsernameChecker.unavailable} | Duplicates: {TiktokUsernameChecker.duplicates} | Remaining: {remaining} | Total checked: {TiktokUsernameChecker.available + TiktokUsernameChecker.unavailable} | Press SPACE to stop!")
    else:
        ctypes.windll.kernel32.SetConsoleTitleW(f"TikTok Username Checker | Available/Banned: {TiktokUsernameChecker.available} | Unavailable: {TiktokUsernameChecker.unavailable} | Duplicates: {TiktokUsernameChecker.duplicates} | Remaining: {remaining} | Total checked: {TiktokUsernameChecker.available + TiktokUsernameChecker.unavailable}")