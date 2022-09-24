from datetime import datetime
from termcolor import colored
import socket
import shutil
import time
import os


class Sysinfo:
    def __init__(self, con, ttl, root, tmp_availables, clients):
        self.con = con
        self.ttl = ttl
        self.root = root
        self.tmp_availables = tmp_availables
        self.clients = clients

    def make_dir(self):
        # Create a directory with host's name if not already exists.
        for item in self.tmp_availables:
            for conKey, ipValue in self.clients.items():
                for ipKey in ipValue.keys():
                    if item[1] == ipKey:
                        ipval = item[1]
                        host = item[2]
                        user = item[3]
                        self.path = os.path.join(self.root, host)
                        try:
                            os.makedirs(self.path)

                        except FileExistsError:
                            pass

    def send_cmd(self):
        # Send Systeminfo command to client
        try:
            self.con.send('si'.encode())

        except (WindowsError, socket.error):
            return False

    def get_filename(self):
        # Get systeminfo filename
        try:
            self.filenameRecv = self.con.recv(1024)
            return self.filenameRecv

        except (WindowsError, socket.error):
            return False

    def get_file_size(self):
        # Get file size in bytes
        try:
            self.size = self.con.recv(4)
            self.size = self.bytes_to_number(self.size)
            return self.size

        except (WindowsError, socket.error):
            return False

    def bytes_to_number(self, b):
        res = 0
        for i in range(4):
            res += b[i] << (i * 8)
        return res

    def get_file_content(self):
        try:
            with open(self.filenameRecv, 'wb') as file:
                while self.current_size < self.size:
                    data = self.con.recv(1024)
                    if not data:
                        break

                    if len(data) + self.current_size > self.size:
                        data = data[:self.size - self.current_size]

                    self.buffer += data
                    self.current_size += len(data)
                    file.write(data)

        except socket.error as e:
            print(f"[{colored('*', 'red')}]{e}\n")
            return False

        except (ConnectionResetError, ConnectionError,
                ConnectionRefusedError, ConnectionAbortedError) as c:
            print(f"[{colored('*', 'red')}]{c}\n")
            return False

    def output(self):
        with open(self.filenameRecv, 'r') as file:
            data = file.read()
            print(data)

    def confirm(self):
        print(f"[{colored('V', 'green')}]Received: {self.filenameRecv} \n")
        self.con.send(f"Received file: {self.filenameRecv}\n".encode())
        msg = self.con.recv(1024).decode()

    def move(self):
        self.filenameRecv = str(self.filenameRecv).strip("b'")
        src = os.path.abspath(self.filenameRecv)
        dst = fr"{self.path}"
        shutil.move(src, dst)

    def run(self):
        # Init current size & buffer
        self.current_size = 0
        self.buffer = b""

        self.make_dir()
        self.send_cmd()
        self.get_filename()
        self.size = self.get_file_size()
        self.get_file_content()
        self.output()
        self.confirm()
        self.move()
