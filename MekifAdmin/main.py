from datetime import datetime
from termcolor import colored
from threading import Thread
from colorama import init
import subprocess
import threading
import argparse
import pwinput
import os.path
import ntpath
import select
import random
import socket
import psutil
import time
import sys

init()


class Client:
    def __init__(self, clients):
        self.clients = clients
        self.d = datetime.now().replace(microsecond=0)
        self.dt = str(self.d.strftime("%b %d %Y | %I-%M-%S"))

    def shell(self, conn, ip, clients):
        errCount = 0
        while True:
            show_shell_commands()

            # Wait for User Input
            cmd = input(f"COMMAND@{ip}> ")
            # Input Validation
            try:
                val = float(cmd)

            except ValueError:
                print(f"[{colored('*', 'red')}]Numbers Only.")
                errCount += 1
                if errCount == 3:
                    print("U obviously don't know what you're doing. goodbye.")
                    conn.send("exit".encode())
                    conn.shutdown(socket.SHUT_RDWR)
                    conn.close()
                    sys.exit()

                continue

            if int(cmd) <= 0 or int(cmd) > 8:
                errCount += 1
                if errCount == 3:
                    print("U obviously don't know what you're doing. goodbye.")
                    conn.send("exit".encode())
                    conn.shutdown(socket.SHUT_RDWR)
                    conn.close()
                    sys.exit()

                print(f"[{colored('*', 'red')}]{cmd} not in the menu."
                      f"[try {colored(errCount, 'yellow')} of {colored('3', 'yellow')}]\n")

                continue

            # Screenshot
            if int(cmd) == 1:
                errCount = 0
                if len(targets) == 0:
                    print(f"[{colored('*', 'red')}]No connected stations.")
                    break

                d = datetime.now().replace(microsecond=0)
                dt = str(d.strftime("%b %d %Y | %I-%M-%S"))
                chunk = 1000000
                print(f"working...")
                conn.send('screen'.encode())
                filenameRecv = conn.recv(1024)
                conn.send("OK filename".encode())
                name = ntpath.basename(str(filenameRecv))
                print(name)
                with open(filenameRecv, 'wb') as file:
                    try:
                        fileRecv = conn.recv(chunk)
                        file.write(fileRecv)

                    except len(fileRecv) == 0:
                        return

                # print(f"[{colored('*', 'green')}]Received: {name[:-2]} \n")
                conn.send(f"Received file: {name[:-1]}\n".encode())
                msg = conn.recv(1024).decode()
                print(f"{msg}")
                continue

            # System Information
            elif int(cmd) == 2:
                errCount = 0
                if len(targets) == 0:
                    print(f"[{colored('*', 'red')}]No connected stations.")
                    break

                d = datetime.now().replace(microsecond=0)
                dt = str(d.strftime("%b %d %Y | %I-%M-%S"))
                print(f"working...")
                conn.send('si'.encode())
                filenameRecv = conn.recv(1024)
                time.sleep(10)
                fileRecv = conn.recv(4096).decode()
                print(fileRecv)

                with open(filenameRecv, 'w') as file:
                    file.write(fileRecv)

                name = ntpath.basename(str(filenameRecv))
                print(f"[{colored('*', 'green')}]Received: {name} \n")
                conn.send(f"Received file: {name}\n".encode())
                msg = conn.recv(1024).decode()
                print(f"{msg}")

                continue

            # Show Current Logged On User
            elif int(cmd) == 3:
                errCount = 0
                if len(targets) == 0:
                    print(f"[{colored('*', 'red')}]No connected stations.")
                    break

                conn.send('user'.encode())
                msg = conn.recv(1024)
                print(msg.decode())
                continue

            # Last Restart Time
            elif int(cmd) == 4:
                errCount = 0
                if len(targets) == 0:
                    print(f"[{colored('*', 'red')}]No connected stations.")
                    break

                d = datetime.now().replace(microsecond=0)
                dt = str(d.strftime("%b %d %Y | %I-%M-%S"))
                conn.send('lr'.encode())
                msg = conn.recv(1024)
                print(msg.decode())

                continue

            # Anydesk
            elif int(cmd) == 5:
                errCount = 0
                if len(targets) == 0:
                    print(f"[{colored('*', 'red')}]No connected stations.")
                    break

                d = datetime.now().replace(microsecond=0)
                dt = str(d.strftime("%b %d %Y | %I-%M-%S"))
                conn.send('anydesk'.encode())
                continue

            # Tasks
            elif int(cmd) == 6:
                errCount = 0
                if len(targets) == 0:
                    print(f"[{colored('*', 'red')}]No connected stations.")
                    break

                chunk = 1000000
                d = datetime.now().replace(microsecond=0)
                dt = str(d.strftime("%b %d %Y | %I-%M-%S"))
                print(f"working...")
                conn.send('tasks'.encode())
                filenameRecv = conn.recv(1024)
                time.sleep(10)
                fileRecv = conn.recv(chunk)
                print(fileRecv.decode())

                with open(filenameRecv, 'w') as file:
                    file.write(fileRecv.decode())

                name = ntpath.basename(str(filenameRecv))
                print(f"[{colored('*', 'green')}]Received: {name} \n")
                conn.send(f"Received file: {name}\n".encode())
                msg = conn.recv(1024).decode()
                print(f"{msg}")

                while True:
                    try:
                        choose_task = input(f"Would you like to kill a task [Y/n]? ")

                    except ValueError:
                        print(f"[{colored('*', 'red')}]Choose [Y] or [N].")

                    if choose_task.lower() == 'y':
                        while True:
                            task_to_kill = input("Task filename: ")
                            try:
                                confirm_kill = input(f"Are you sure you want to kill {task_to_kill} [Y/n]? ")

                            except ValueError:
                                print(f"[{colored('*', 'red')}]Choose [Y] or [N].")

                            if confirm_kill.lower() == "y":
                                conn.send('kill'.encode())
                                conn.send(task_to_kill.encode())
                                msg = conn.recv(1024).decode()
                                print(msg)
                                break

                            elif confirm_kill.lower() == "n":
                                conn.send('pass'.encode())
                                break

                            else:
                                break

                        break

                    elif choose_task.lower() == 'n':
                        conn.send('pass'.encode())
                        break

                    else:
                        print(f"[{colored('*', 'red')}]Choose [Y] or [N]\n")
                        continue

                continue

            # Restart
            elif int(cmd) == 7:
                errCount = 0
                if len(targets) == 0:
                    print(f"[{colored('*', 'red')}]No connected stations.")
                    break

                d = datetime.now().replace(microsecond=0)
                dt = str(d.strftime("%b %d %Y | %I-%M-%S"))
                sure = input("Are you sure you want to restart [Y/n]?")
                while True:
                    try:
                        if str(sure).lower() == "y":
                            conn.send('restart'.encode())
                            targets.remove(conn)
                            ips.remove(ip)
                            clients -= 1
                            break

                        elif str(sure).lower() == "n":
                            break

                    except TypeError:
                        print("Wrong Input")
                return

            # Back
            elif int(cmd) == 8:
                d = datetime.now().replace(microsecond=0)
                dt = str(d.strftime("%b %d %Y | %I-%M-%S"))
                conn.send('exit'.encode())
                targets.remove(conn)
                ips.remove(ip)
                self.clients -= 1
                break

        return


def welcome_menu():
    try:
        print(f"\n\t\t[{colored('*', 'green')}]Connection from: IP: {colored(ip, 'green')} | "
              f"Port: {colored(port, 'green')} | Name: {colored(ident, 'green')}")

    except ValueError:
        pass

    print("\t\t" + f"{colored('=', 'blue')}" * 20, f"=> {colored('Welcome to Mekif Remote Admin!', 'red')} <=",
          f"{colored('=', 'blue')}" * 20)
    print("\t\t" + f"{colored('=', 'blue')}" * 20, f"=>      {colored('By Gil Shwartz @2022', 'red')}      <=",
          f"{colored('=', 'blue')}" * 20)
    print("\t\t" + f"{colored('=', 'yellow')}" * 78 + "\n")
    print(f"\t\t[{colored('1', 'yellow')}]Remote Control          ---------------> "
          f"Show Remote Commands")
    print(f"\t\t[{colored('2', 'yellow')}]Connection History      ---------------> "
          f"Show connection history.")
    print(f"\t\t[{colored('3', 'yellow')}]Close                   ---------------> "
          f"Close current session.")
    print(f"\t\t[{colored('4', 'yellow')}]Exit                    ---------------> "
          f"Close connections and exit program.\n")


def show_shell_commands():
    print("\t\t\t" + f"{colored('=', 'blue')}" * 20, f"=> {colored('REMOTE CONTROL', 'red')} <=",
          f"{colored('=', 'blue')}" * 20)
    print(f"\t\t[{colored('1', 'cyan')}]Screenshot          \t\t---------------> "
          f"Capture screenshot.")
    print(f"\t\t[{colored('2', 'cyan')}]System Info         \t\t---------------> "
          f"Show Station's System Information")
    print(f"\t\t[{colored('3', 'cyan')}]Current User        \t\t---------------> "
          f"Show current logged on user")
    print(f"\t\t[{colored('4', 'cyan')}]Last Restart Time   \t\t---------------> "
          f"Show remote station's last restart time")
    print(f"\t\t[{colored('5', 'cyan')}]Anydesk             \t\t---------------> "
          f"Start Anydesk")
    print(f"\t\t[{colored('6', 'cyan')}]Tasks               \t\t---------------> "
          f"Show remote station's running tasks")
    print(f"\t\t[{colored('7', 'cyan')}]Restart             \t\t---------------> "
          f"Restart remote station")
    print(f"\t\t[{colored('8', 'cyan')}]Back                \t\t---------------> "
          f"Back to Control Center\n")


def create_socket(ip):
    listener = socket.socket()
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listener.bind((ip, port))

    return listener


def accept():
    while True:
        (conn, (ip, port)) = listener.accept()
        return conn, (ip, port)


def validation(users):
    phrase = ' '
    tries = 0
    while True:
        user = input("Username: ")
        validate = pwinput.pwinput(prompt="Password: ", mask='*')
        if str(validate) == str(phrase) and user in users:
            tries = 0
            return

        else:
            tries += 1
            print(f"Wrong password! [{tries} of 3]")
            if int(tries) >= 3:
                print("Exiting.")
                sys.exit()


if __name__ == '__main__':
    users = ['g', 'r', 'o', 'i']
    noping_live_connections = {}
    connections = {}
    sconnections = [{}]
    noping_targets = []
    noping_ips = []
    ips = []
    targets = []
    clients = 0
    listeners = []
    threads = []
    port = 55400
    last_reboot = psutil.boot_time()
    hostname = socket.gethostname()
    serverIP = str(socket.gethostbyname(hostname))

    # Run User Validation
    # validation(users)

    print(f"[{colored('*', 'cyan')}]Starting Server on IP: {serverIP} | Port: {port}")
    print(f"[{colored('*', 'cyan')}]Server's Last Restart: "
          f"{datetime.fromtimestamp(last_reboot).replace(microsecond=0)}\n")
    print(f"[{colored('*', 'magenta')}]Listening...")

    # Create Sockets
    listener = create_socket(serverIP)
    listeners.append(listener)
    listener.listen(5)

    while True:
        # Accept New Connections
        conn, (ip, port) = accept()

        # Capture Date & Time with an AM PM
        d = datetime.now().replace(microsecond=0)
        dt = str(d.strftime("%b %d %Y %I:%M:%S %p"))

        try:
            # Get Remote Computer's Name
            ident = conn.recv(1024).decode()

        except (ConnectionResetError, ConnectionError, ConnectionAbortedError, ConnectionRefusedError):
            print("Lost Connection")
            continue

        # Update Connection Lists
        if conn not in targets:
            targets.append(conn)
            ips.append(ip)

        connections[conn] = ip
        temp_connection_record = {f'IP: {ip} | Name: {ident}': dt}
        sconnections.append(temp_connection_record)
        clients += 1

        # Initialize Client Class
        client = Client(clients)

        while True:
            # Send Welcome Message
            try:
                welcome = "Connection Established!"
                conn.send(f"@Server: {welcome}".encode())

            except (ConnectionResetError, ConnectionError, ConnectionAbortedError):
                print(
                    f"[{colored('*', 'red')}]Check client's connection. use the {colored('Close', 'yellow')} option.")
                if conn in targets:
                    targets.remove(conn)
                    ips.remove(ip)
                    clients -= 1

            welcome_menu()

            # Wait For User Commands
            command = input(f"CONTROL@{ip}> ")
            try:
                # Remote Shell Commands
                if command.lower() == "shell" or int(command) == 1:
                    if conn not in targets:
                        break

                    d = datetime.now().replace(microsecond=0)
                    dt = str(d.strftime("%b %d %Y %I:%M:%S %p"))
                    while True:
                        if len(targets) > 0:
                            try:
                                client.shell(conn, ip, clients)
                                break

                            except (ValueError, IndexError):
                                if conn in targets:
                                    targets.remove(conn)

                                if ip in ips:
                                    ips.remove(ip)

                        else:
                            raise ValueError("f[{colored('*', 'red')}]No available stations.")

                # Connection History
                elif command.lower() == "history" or int(command) == 2:
                    d = datetime.now().replace(microsecond=0)
                    dt = str(d.strftime("%b %d %Y %I:%M:%S %p"))
                    c = 1
                    for connection in sconnections:
                        for k, v in connection.items():
                            print(
                                f"[{colored(str(c), 'cyan')}]{k} | {colored('Time', 'cyan')}: {v}")
                            c += 1

                # Close Current Connection
                elif command == "close" or int(command) == 3:
                    d = datetime.now().replace(microsecond=0)
                    dt = str(d.strftime("%b %d %Y %I:%M:%S %p"))
                    if len(targets) > 0:
                        for t in targets:
                            t.close()

                        targets.remove(conn)
                        ips.remove(ip)
                        clients -= 1
                        break

                    else:
                        print(f"[{colored('*', 'magenta')}]Listening...")

                    break

                # Exit Program
                elif command == "break" or int(command) == 4:
                    d = datetime.now().replace(microsecond=0)
                    dt = str(d.strftime("%b %d %Y %I:%M:%S %p"))
                    conn.shutdown(socket.SHUT_RDWR)
                    conn.close()
                    sys.exit()

            except (ValueError, ConnectionError, ConnectionAbortedError, ConnectionResetError, ConnectionRefusedError):
                print(f"[{colored('*', 'red')}]Check client's connection. use the {colored('Close', 'yellow')} option.")
                continue

            else:
                continue
