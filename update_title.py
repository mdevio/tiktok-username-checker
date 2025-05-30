# MADE BY @MDEVIO ON GITHUB
from config import ctypes
from config import TiktokUsernameChecker

def update_title(ttucmode):
    """
    Updates the console title with the current status of the TikTok Username Checker
    """
    TiktokUsernameChecker.remaining = len(TiktokUsernameChecker.usernames) - (TiktokUsernameChecker.available + TiktokUsernameChecker.unavailable) # Formula to calculate the remaining usernames to check
    if ttucmode == "checker":
        ctypes.windll.kernel32.SetConsoleTitleW(f"usernamechecker.online | TikTok Username Checker {TiktokUsernameChecker.version} | Available/Banned: {TiktokUsernameChecker.available} | Unavailable: {TiktokUsernameChecker.unavailable} | Remaining: {TiktokUsernameChecker.remaining} | Total checked: {TiktokUsernameChecker.available + TiktokUsernameChecker.unavailable} | Press SPACE to stop!")
    else:
        ctypes.windll.kernel32.SetConsoleTitleW(f"usernamechecker.online | TikTok Username Checker {TiktokUsernameChecker.version} | Available/Banned: {TiktokUsernameChecker.available} | Unavailable: {TiktokUsernameChecker.unavailable} | Remaining: {TiktokUsernameChecker.remaining} | Total checked: {TiktokUsernameChecker.available + TiktokUsernameChecker.unavailable}")