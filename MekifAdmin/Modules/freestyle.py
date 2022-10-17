import os
import time
import socket
import shutil
from termcolor import colored
from threading import Thread
from datetime import datetime

# TODO: FINISHED: logging.


class Freestyle:
    def __init__(self, con, root, tmp_availables, clients, targets, logpath, ident):
        self.ident = ident
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

    def make_dir(self):
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

    def freestyle(self):
        ipval, host, user, path = self.make_dir()
        self.cmd_log = rf'C:\Peach\{host}\cmd_log.txt'

        while True:
            try:
                self.logIt_thread(self.log_path, debug=False, msg=f'Waiting for user input...')
                cmd = input(f"{host}♦CMD>")
                self.logIt_thread(self.log_path, debug=False, msg=f'User input: {cmd}')

                if str(cmd).lower()[:4] == "back":
                    self.logIt_thread(self.log_path, debug=False, msg=f'Sending {cmd} command to client...')
                    self.con.send("back".encode())
                    self.logIt_thread(self.log_path, debug=False, msg=f'Send completed.')
                    break

                self.logIt_thread(self.log_path, debug=False, msg=f'Sending {cmd} to client...')
                self.con.send(cmd.encode())
                self.logIt_thread(self.log_path, debug=False, msg=f'Send completed.')

                result = self.con.recv(4096).decode()
                print(result)

                if not os.path.exists(self.cmd_log):
                    with open(self.cmd_log, 'w') as log:
                        log.write(f"Command: {cmd}\n")
                        log.write(f"{result}\n")

                else:
                    with open(self.cmd_log, 'a') as log:
                        log.write(f"Command: {cmd}\n")
                        log.write(f"{result}\n")

            except (WindowsError, socket.error) as e:
                self.logIt_thread(self.log_path, debug=True, msg=f'Error: {e}')
                return False

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
        return
