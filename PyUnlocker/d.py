import os
import winreg
import subprocess
import sys
print("Windows check")
shoce = ""
def Vibor():
	global shoce
	shoce = input("1 - Check Winlogon, 2 - Settings: ")
Vibor()
if shoce == "1":
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows NT\CurrentVersion\Winlogon", 0, winreg.KEY_ALL_ACCESS)
    except PermissionError:
            print("[ERROR] Permission Error!")
            Vibor()
    Sheel_Value, _ = winreg.QueryValueEx(key, "Shell")
    if Sheel_Value == "explorer.exe":
        print("Vse chisto")
        Vibor()
    else:
        print("Obnaryhena_Podelka!")
        winreg.SetValueEx(key, "Shell", 0, winreg.REG_SZ, "explorer.exe")
        Vibor()
elif shoce == "2":
    key2 = winreg.CreateKeyEx(winreg.HKEY_CURRENT_USER, r"Software\PyUnlocker", 0, winreg.KEY_ALL_ACCESS)
    try:
            whitelist, _ = winreg.QueryValueEx(key2, "whitelist")
    except FileNotFoundError:
            winreg.SetValueEx(key2, "whitelist", 0, winreg.REG_MULTI_SZ, ["None"])
            Vibor()
    print("whitelist: " + ", ".join(whitelist))
    whitepath = input("Enter whitelist words in the Winlogon checker: ")
    whitelist = whitepath    
    winreg.SetValueEx(key2, "whitelist", 0, winreg.REG_MULTI_SZ, [", ".join(whitepath)])
    Vibor()                          
    
