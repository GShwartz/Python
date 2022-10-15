from datetime import datetime
from threading import Thread
import subprocess
import os


class Freestyle:
    def __init__(self, soc, log, hostname, localIP):
        self.soc = soc
        self.log_path = log
        self.hostname = hostname
        self.localIP = localIP

    def get_date(self):
        d = datetime.now().replace(microsecond=0)
        dt = str(d.strftime("%b %d %Y %I.%M.%S %p"))

        return dt

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
        return

    def convert_to_bytes(self, no):
        result = bytearray()
        result.append(no & 255)
        for i in range(3):
            no = no >> 8
            result.append(no & 255)

        return result

    def send_file(self, filename):
        def send_file_name():
            try:
                self.logIt_thread(self.log_path, msg='Sending file name...')
                self.soc.send(filename.encode())
                self.logIt_thread(self.log_path, msg=f'Send Completed.')

                self.logIt_thread(self.log_path, msg='Waiting for confirmation from server...')
                msg = self.soc.recv(1024).decode()
                self.logIt_thread(self.log_path, msg=f'Server Message: {msg}')

                return True

            except (WindowsError, socket.error):
                self.logIt_thread(self.log_path, msg='Connection Error')
                return False

        def send_file_size():
            self.logIt_thread(self.log_path, msg='Getting file size...')
            length = os.path.getsize(filename)
            self.logIt_thread(self.log_path, msg=f'File Size: {length}.')
            try:
                self.logIt_thread(self.log_path, msg=f'Sending file size: {length}...')
                self.soc.send(self.convert_to_bytes(length))
                self.logIt_thread(self.log_path, msg=f'Send Completed.')

                return length

            except (WindowsError, socket.error) as e:
                self.logIt_thread(self.log_path, msg=f'Connection Error: {e}')
                return False

        def send_file_content():
            try:
                self.logIt_thread(self.log_path, msg=f'Opening {filename} with ReadBytes permissions...')
                with open(filename, 'rb') as file:
                    self.logIt_thread(self.log_path, msg='Reading file content...')
                    data = file.read(1024)
                    self.logIt_thread(self.log_path, msg='Sending file content...')
                    while data:
                        self.soc.send(data)
                        if not data:
                            break

                        data = file.read(1024)

                self.logIt_thread(self.log_path, msg=f'Send Completed.')

            except (FileNotFoundError, FileExistsError) as e:
                self.logIt_thread(self.log_path, msg=f'File Error: {e}')
                return False

        self.logIt_thread(self.log_path, msg=f'Running send_file({filename})...')
        self.logIt_thread(self.log_path, msg='Calling send_file_name()...')
        send_file_name()
        self.logIt_thread(self.log_path, msg='Calling send_file_size()...')
        send_file_size()
        self.logIt_thread(self.log_path, msg='Calling send_file_content()...')
        send_file_content()

        self.logIt_thread(self.log_path, msg=f'=== End of send_file({filename}) ===')

    def run_command(self):
        self.logIt_thread(self.log_path, msg='Defining file name...')
        dt = self.get_date()
        self.filename = rf"c:\MekifRemoteAdmin\{self.plat} {self.hostname} {str(self.localIP)} {dt}.txt"
        self.logIt_thread(self.log_path, msg=f'File name: {self.filename}')

        if str(self.plat) == "ps":
            powershell = r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"
            try:
                self.logIt_thread(self.log_path, msg=f'Opening {self.filename}...')
                with open(self.filename, 'w') as file:
                    self.logIt_thread(self.log_path, msg=f'Running PS command: {self.cmd} to {self.filename}...')
                    p = subprocess.run([f'{powershell}', f'{self.cmd}'], stdout=file, shell=True)

            except FileExistsError as e:
                self.logIt_thread(self.log_path, msg=f'Passing File Error: {e}...')
                pass

        elif str(self.plat) == "cmd":
            try:
                self.logIt_thread(self.log_path, msg=f'Opening {self.filename}...')
                with open(self.filename, 'w') as file:
                    self.logIt_thread(self.log_path, msg=f'Running CMD command: {self.cmd} to {self.filename}...')
                    p = subprocess.run(self.cmd, stdout=file, shell=True)

                self.logIt_thread(self.log_path, msg=f'Write to file Completed.')

            except (FileExistsError, IndexError):
                self.logIt_thread(self.log_path, msg=f'Passing File Error: {e}...')
                pass

    def confirm(self):
        try:
            self.logIt_thread(self.log_path, msg=f'Waiting for msg from server...')
            msg = self.soc.recv(1024).decode()
            self.logIt_thread(self.log_path, msg=f'Server Message: {msg}')

            self.logIt_thread(self.log_path, msg=f'Sending confirmation to server...')
            self.soc.send(f"{self.hostname} | {self.localIP}: Command: {self.cmd} Completed.\n".encode())
            self.logIt_thread(self.log_path, msg=f'Send Completed.')

        except (WindowsError, socket.error) as e:
            self.logIt_thread(self.log_path, msg=f'Connection Error: {e}')
            return False

    def run(self):
        self.logIt_thread(self.log_path, msg=f'Calling self.send_file({self.filename})...')
        self.send_file(self.filename)

        self.logIt_thread(self.log_path, msg='Calling confirm()...')
        self.confirm()

        self.logIt_thread(self.log_path, msg=f'Removing {self.filename}...')
        os.remove(self.filename)

        self.logIt_thread(self.log_path, msg=f'=== End of execute({self.plat}, {self.cmd}) ===')

    def free_style(self):
        while True:
            try:
                self.logIt_thread(self.log_path, msg='Waiting for platform...')
                self.plat = self.soc.recv(1024).decode()
                self.logIt_thread(self.log_path, msg=f'Received {self.plat}')

                if str(self.plat).lower()[:2] == "ps":
                    while True:
                        self.logIt_thread(self.log_path, msg=f'Waiting for command...')
                        self.cmd = self.soc.recv(1024).decode()
                        self.logIt_thread(self.log_path, msg=f'Command: {self.cmd}')

                        if self.cmd == "back":
                            self.soc.send("OK".encode())
                            return

                        self.logIt_thread(self.log_path, msg=f'Calling self.execute({self.plat}, {self.cmd})...')
                        self.run_command()
                        self.run()

                elif str(self.plat).lower()[:3] == "cmd":
                    while True:
                        self.logIt_thread(self.log_path, msg=f'Waiting for command...')
                        self.cmd = self.soc.recv(1024).decode()
                        self.logIt_thread(self.log_path, msg=f'Command: {self.cmd}')

                        if self.cmd == "back":
                            self.soc.send("OK".encode())
                            return

                        self.logIt_thread(self.log_path, msg=f'Calling self.execute({self.plat}, {self.cmd})...')
                        self.run_command()
                        self.run()

                elif str(plat).lower() == "back":
                    msg = "back".encode()
                    self.logIt_thread(self.log_path, msg=f'Sending back message to server...')
                    self.soc.send(msg)
                    self.logIt_thread(self.log_path, msg=f'Send Completed.')
                    break

            except (WindowsError, socket.error) as e:
                self.logIt_thread(self.log_path, msg=f'Connection Error: {e}')
                print(e)
                break
