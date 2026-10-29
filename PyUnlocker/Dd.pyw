import urllib.request
import os
import sys
import subprocess
import time
version_url = "https://github.com/Kostyanchik2/PyUnlocker/releases/latest/download/version1.txt"
url = "https://github.com/Kostyanchik2/PyUnlocker/releases/latest/download/PyUnlocker.Setup.exe"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
req2 = urllib.request.Request(version_url, headers={"User-Agent": "Mozilla/5.0"})
def update():
    global req
    try:
        with urllib.request.urlopen(req) as r, open("setup.exe", "wb") as f:
            f.write(r.read())
        subprocess.Popen(".\\udpate_wait.exe")
        subprocess.run('setup.exe /VERYSILENT /SUPPRESSMSGBOXES /DIR="."')
        os.remove("setup.exe")
        subprocess.run(["taskkill", "/F", "/IM", "udpate_wait.exe"], creationflags=0x080000000)
        subprocess.Popen([".\\d.exe"], creationflags=16)
    except Exception as e:
        subprocess.Popen([".\\d.exe"], creationflags=16)
def check():
    global req2
    with open("..\version1.txt", "r", encoding="utf-8") as v:
       version = f.read().strip()
       
    try:
        with urllib.request.urlopen(req2) as github:
            latest_version = github.read().decode("urf-8").strip()
        if version != latest_version:
            update()
        else:
            subprocess.Popen
    except Exception as er:
        subprocess.Popen(".\\d.exe")
