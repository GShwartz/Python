from datetime import datetime
from termcolor import colored
from threading import Thread
from colorama import init
from decouple import config
import subprocess
import pwinput
import os.path
import socket
import psutil
import shutil
import time
import sys

# Local Modules
import validation
from screenshot import Screenshot
from tasks import Tasks
from vital_signs import Vitals
from sysinfo import Sysinfo
from freestyle import Freestyle

# TODO: Finish logger

init()


class Server:
    clients = {}
    connections = {}
    connHistory = []
    ips = []
    targets = []
    threads = []
    tmp_availables = []

    def __init__(self, serverIP, serverPort, ttl, path, log_path):
        self.serverIp = serverIP
        self.serverPort = serverPort
        self.ttl = ttl
        self.path = path
        self.log_path = log_path
        self.server = socket.socket()
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((self.serverIp, self.serverPort))
        self.server.listen(5)

        if not os.path.exists(self.path):
            os.makedirs(self.path)

    def get_date(self):
        d = datetime.now().replace(microsecond=0)
        dt = str(d.strftime("%b %d %Y %I.%M.%S %p"))

        return dt

    def logIt(self, logfile=None, debug=False, msg=''):
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

    def run(self):
        self.logIt_thread(self.log_path, debug=False, msg=f'Running run()...')
        self.logIt_thread(self.log_path, debug=False, msg=f'Calling connect() in new thread...')
        self.connectThread = Thread(target=self.connect, daemon=True, name=f"Connect Thread").start()
        self.logIt_thread(self.log_path, debug=False, msg=f'Adding thread to threads list...')
        self.threads.append(self.connectThread)
        self.logIt_thread(self.log_path, debug=False, msg=f'Thread added to threads list.')

    def connect(self):
        self.logIt_thread(self.log_path, debug=False, msg=f'Running connect()...')
        while True:
            self.logIt_thread(self.log_path, debug=False, msg=f'Accepting connections...')
            self.conn, (self.ip, self.port) = self.server.accept()
            self.logIt_thread(self.log_path, debug=False, msg=f'Connection from {self.ip} accepted.')

            try:
                # Get Remote Computer's Name
                self.logIt_thread(self.log_path, debug=False, msg=f'Waiting for remote station name...')
                self.ident = self.conn.recv(1024).decode()
                self.logIt_thread(self.log_path, debug=False, msg=f'Remote station name: {self.ident}')

                # Get Current User:
                self.logIt_thread(self.log_path, debug=False, msg=f'Waiting for remote station current logged user...')
                self.user = self.conn.recv(1024).decode()
                self.logIt_thread(self.log_path, debug=False, msg=f'Remote station user: {self.user}')

            except (WindowsError, socket.error) as e:
                self.logIt_thread(self.log_path, debug=False, msg=f'Connection Error: {e}')
                return  # Restart The Loop

            # Update Thread Dict and Connection Lists
            if self.conn not in self.targets and self.ip not in self.ips:
                self.logIt_thread(self.log_path, debug=False, msg=f'New Connection!')

                # Add Socket Connection To Targets list
                self.logIt_thread(self.log_path, debug=False,
                                  msg=f'Adding {self.conn} to targets list...')
                self.targets.append(self.conn)
                self.logIt_thread(self.log_path, debug=False, msg=f'targets list updated.')

                # Add IP Address Connection To IPs list
                self.logIt_thread(self.log_path, debug=False, msg=f'Adding {self.ip} to ips list...')
                self.ips.append(self.ip)
                self.logIt_thread(self.log_path, debug=False, msg=f'ips list updated.')

                # Set Temp Dict To Update Live Connections List
                self.logIt_thread(self.log_path, debug=False,
                                  msg=f'Adding {self.conn} | {self.ip} to temp live connections dict...')
                self.temp_connection = {self.conn: self.ip}
                self.logIt_thread(self.log_path, debug=False, msg=f'Temp connections dict updated.')

                # Add Temp Dict To Connections List
                self.logIt_thread(self.log_path, debug=False, msg=f'Updating connections list...')
                self.connections.update(self.temp_connection)
                self.logIt_thread(self.log_path, debug=False, msg=f'Connections list updated.')

                # Set Temp Idents Dict For Idents
                self.logIt_thread(self.log_path, debug=False, msg=f'Creating dict to hold ident details...')
                self.temp_ident = {self.conn: {self.ip: {self.ident: self.user}}}
                self.logIt_thread(self.log_path, debug=False, msg=f'Dict created: {self.temp_ident}')

                # Add Temp Idents Dict To Idents Dict
                self.logIt_thread(self.log_path, debug=False, msg=f'Updating live clients list...')
                self.clients.update(self.temp_ident)
                self.logIt_thread(self.log_path, debug=False, msg=f'Live clients list updated.')

            # Create a Dict of Connection, IP, Computer Name, Date & Time
            self.logIt_thread(self.log_path, debug=False, msg=f'Fetching current date & time...')
            dt = get_date()
            self.logIt_thread(self.log_path, debug=False, msg=f'Creating a connection dict...')
            self.temp_connection_record = {self.conn: {self.ip: {self.ident: {self.user: dt}}}}
            self.logIt_thread(self.log_path, debug=False, msg=f'Connection dict created: {self.temp_connection_record}')

            # Add Connection to Connection History
            self.logIt_thread(self.log_path, debug=False, msg=f'Adding connection to connection history...')
            self.connHistory.append(self.temp_connection_record)
            self.logIt_thread(self.log_path, debug=False, msg=f'Connection added to connection history.')

            self.logIt_thread(self.log_path, debug=False, msg=f'Calling self.welcome_message() condition...')
            if self.welcome_message():
                continue

    def welcome_message(self):
        self.logIt_thread(self.log_path, debug=False, msg=f'Running welcome_message()...')

        # Send Welcome Message
        try:
            self.welcome = "Connection Established!"
            self.logIt_thread(self.log_path, debug=False, msg=f'Sending welcome message...')
            self.conn.send(f"@Server: {self.welcome}".encode())
            self.logIt_thread(self.log_path, debug=False, msg=f'{self.welcome} sent to {self.ident}.')

            return True

        except (WindowsError, socket.error) as e:
            self.logIt_thread(self.log_path, debug=False, msg=f'Connection Error: {e}')
            if self.conn in self.targets and self.ip in self.ips:
                self.logIt_thread(self.log_path, debug=False, msg=f'Removing {self.conn} from self.targets...')
                self.targets.remove(self.conn)

                self.logIt_thread(self.log_path, debug=False, msg=f'Removing {self.ip} from self.ips list...')
                self.ips.remove(self.ip)

                self.logIt_thread(self.log_path, debug=False, msg=f'Deleting {self.conn} from self.connections.')
                del self.connections[self.conn]

                self.logIt_thread(self.log_path, debug=False, msg=f'Deleting {self.conn} from self.clients...')
                del self.clients[self.conn]

                self.logIt_thread(self.log_path, debug=False, msg=f'[V]Connection removed from lists.')

                return False

    def connection_history(self):
        self.logIt_thread(self.log_path, debug=False, msg=f'Running connection_history()...')
        print(f"{colored('=', 'blue')}=>{colored('Connection History', 'red')}<={colored('=', 'blue')}")

        self.logIt_thread(self.log_path, debug=False, msg=f'Check if connection history list is empty...')
        if len(self.connHistory) == 0:
            self.logIt_thread(self.log_path, debug=False, msg=f'List is empty.')
            print(f"[{colored('*', 'cyan')}]List is empty.")
            return

        c = 1  # Initiate Counter for Connection Number
        try:
            # Iterate Through Connection History List Items
            self.logIt_thread(self.log_path, debug=False, msg=f'Iterating self.connHistory...')
            for connection in self.connHistory:
                for conKey, ipValue in connection.items():
                    for ipKey, identValue in ipValue.items():
                        for identKey, userValue in identValue.items():
                            for userKey, timeValue in userValue.items():
                                print(
                                    f"[{colored(str(c), 'green')}]{colored('IP', 'cyan')}: {ipKey} | "
                                    f"{colored('Station Name', 'cyan')}: {identKey} | "
                                    f"{colored('User', 'cyan')}: {userKey} | "
                                    f"{colored('Time', 'cyan')}: {timeValue}")
                    c += 1
            return

        # Break If Client Lost Connection
        except (KeyError, socket.error, ConnectionResetError) as e:
            self.logIt_thread(self.log_path, debug=False, msg=f'Iteration Error: {e}')
            return

    def vital_signs(self):
        self.logIt_thread(self.log_path, debug=False, msg=f'Running vital_signs()...')

        if len(self.targets) == 0:
            self.logIt_thread(self.log_path, debug=False, msg=f'No connected stations.')
            print(f"[{colored('*', 'cyan')}]No connected stations.\n")
            return False

        self.logIt_thread(self.log_path, debug=False, msg=f'Init class: vitals({self.targets, self.ips, self.clients, self.connections, self.log_path})...')
        vitals = Vitals(self.targets, self.ips, self.clients,
                        self.connections, self.log_path, self.ident)
        if vitals.vitals_input():
            vitals.vital_signs()
            return True

        else:
            self.logIt_thread(self.log_path, debug=False, msg=f'Closing vital_signs()...')
            return False

    def show_available_connections(self):
        self.logIt_thread(self.log_path, debug=False, msg=f'Running show_available_connections()...')
        if len(self.ips) == 0:
            self.logIt_thread(self.log_path, debug=False, msg=f'No connected Stations')
            print(f"[{colored('*', 'cyan')}]No connected stations.\n")
            return

        try:
            print(f"[{colored('*', 'cyan')}] {colored('Available Connections', 'green')} [{colored('*', 'cyan')}]")
            print(f"{colored('=', 'yellow') * 29}")

            self.logIt_thread(self.log_path, debug=False, msg=f'Creating available list...')
            count = 0
            for conKey, ipValue in self.clients.items():
                for ipKey, identValue in ipValue.items():
                    for con, ip in self.connections.items():
                        if ip == ipKey:
                            for identKey, userValue in identValue.items():
                                if (count, ipKey, identKey, userValue) in self.tmp_availables:
                                    continue

                                self.tmp_availables.append((count, ipKey, identKey, userValue))
                count += 1

            self.logIt_thread(self.log_path, debug=False, msg=f'Available list created.')

            self.logIt_thread(self.log_path, debug=False,
                              msg=f'Extracting: Session | Station IP | Station Name | Logged User from clients list...')
            for item in self.tmp_availables:
                for conKey, ipValue in self.clients.items():
                    for ipKey in ipValue.keys():
                        if item[1] == ipKey:
                            print(f"Session [{colored(f'{item[0]}', 'cyan')}] | "
                                  f"Station IP: {colored(f'{item[1]}', 'green')} | "
                                  f"Station Name: {colored(f'{item[2]}', 'green')} | "
                                  f"Logged User: {colored(f'{item[3]}', 'green')}")

            print(f"\n[{colored('[Q/q]', 'cyan')}]Back")
            self.logIt_thread(self.log_path, debug=False, msg=f'Extraction completed.')
            return True

        except (WindowsError, socket.error) as e:
            self.logIt_thread(self.log_path, debug=False, msg=f'Connection Error: {e}')
            print(f"[{colored('*', 'red')}]Connection terminated by the client.")

            self.logIt_thread(self.log_path, debug=False, msg=f'Removing connection from available list...')
            self.remove_lost_connection(con, ip)
            self.logIt_thread(self.log_path, debug=False, msg=f'Available list updated.')

            self.logIt_thread(self.log_path, debug=False, msg=f'=== End of show_available_connections ===')

    def get_station_number(self):
        self.logIt_thread(self.log_path, debug=False, msg=f'Running get_station_number()...')
        if len(self.tmp_availables) == 0:
            self.logIt_thread(self.log_path, debug=False, msg=f'No available connections.')
            print(f"[{colored('*', 'cyan')}]No available connections.\n")
            return

        tries = 1
        while True:
            self.logIt_thread(self.log_path, debug=False, msg=f'Waiting for station number...')
            station_num = input(f"\n@Session #>> ")
            self.logIt_thread(self.log_path, debug=False, msg=f'Station number: {station_num}')
            if str(station_num).lower() == 'q':
                self.logIt_thread(self.log_path, debug=False, msg=f'Station number: {station_num} | moving back...')
                return False

            try:
                self.logIt_thread(self.log_path, debug=False, msg=f'Running input validation on {station_num}')
                val = int(station_num)
                if int(station_num) <= 0 or int(station_num) <= (len(self.tmp_availables)):
                    tarnum = self.targets[int(station_num)]
                    ipnum = self.ips[int(station_num)]
                    self.logIt_thread(log_path, debug=False, msg=f'=== End of get_station_number() ===')
                    return int(station_num), tarnum, ipnum

                else:
                    self.logIt_thread(log_path, debug=False, msg=f'Wrong input detected.')
                    print(f"[{colored('*', 'red')}]Wrong Number. Choose between [1 - {len(self.tmp_availables)}].\n"
                          f"[Try {colored(f'{tries}', 'yellow')}/{colored('3', 'yellow')}]")

                    if tries == 3:
                        print("U obviously don't know what you're doing. goodbye.")
                        self.logIt_thread(self.log_path, debug=False, msg=f'Tries: 3 | Ending program...')
                        if len(server.targets) > 0:
                            self.logIt_thread(self.log_path, debug=False, msg=f'Closing live connections...')
                            for t in server.targets:
                                t.send('exit'.encode())
                                t.shutdown(socket.SHUT_RDWR)
                                t.close()

                            self.logIt_thread(self.log_path, debug=False, msg=f'Live connections closed.')

                        self.logIt_thread(self.log_path, debug=False, msg=f'Exiting app...')
                        sys.exit()

                    tries += 1

            except (TypeError, ValueError, IndexError):
                self.logIt_thread(self.log_path, debug=False, msg=f'Wrong input detected.')
                print(f"[{colored('*', 'red')}]Numbers only. Choose between [1 - {len(self.tmp_availables)}].\n"
                      f"[Try {colored(f'{tries}', 'yellow')}/{colored('3', 'yellow')}]")
                if tries == 3:
                    dt = get_date()
                    if len(server.targets) > 0:
                        self.logIt_thread(self.log_path, debug=False, msg=f'Closing live connections...')
                        for t in server.targets:
                            t.send('exit'.encode())
                            t.shutdown(socket.SHUT_RDWR)
                            t.close()

                        self.logIt_thread(self.log_path, debug=False, msg=f'Live connections closed.')

                    print("U obviously don't know what you're doing. goodbye.")
                    self.logIt_thread(self.log_path, debug=False, msg=f'Exiting app...')
                    sys.exit()

                tries += 1

    def show_shell_commands(self, ip):
        self.logIt_thread(self.log_path, debug=False, msg=f'Running show_shell_commands()...')
        self.logIt_thread(self.log_path, debug=False, msg=f'Displaying headline...')
        print("\t\t" + f"{colored('=', 'blue')}" * 20, f"=> {colored('REMOTE CONTROL', 'red')} <=",
              f"{colored('=', 'blue')}" * 20)

        self.logIt_thread(self.log_path, debug=False,
                          msg=f'Displaying Station IP | Station Name | Logged User in headline...')
        for conKey, ipValue in self.clients.items():
            for ipKey, userValue in ipValue.items():
                if ipKey == ip:
                    for identKey, timeValue in userValue.items():
                        print("\t\t" + f"Station IP: {colored(f'{ipKey}', 'green')} | "
                                       f"Station Name: {colored(f'{identKey}', 'green')} | "
                                       f"Logged User: {colored(f'{timeValue}', 'green')}")

        print("\t\t" + f"{colored('=', 'yellow')}" * 62 + "\n")

        self.logIt_thread(self.log_path, debug=False, msg=f'Displaying shell commands menu...')
        print(f"\t\t[{colored('1', 'cyan')}]Screenshot          \t\t---------------> "
              f"Capture screenshot.")
        print(f"\t\t[{colored('2', 'cyan')}]System Info         \t\t---------------> "
              f"Show Station's System Information")
        print(f"\t\t[{colored('3', 'cyan')}]Last Restart Time   \t\t---------------> "
              f"Show remote station's last restart time")
        print(f"\t\t[{colored('4', 'cyan')}]Anydesk             \t\t---------------> "
              f"Start Anydesk")
        print(f"\t\t[{colored('5', 'cyan')}]Tasks               \t\t---------------> "
              f"Show remote station's running tasks")
        print(f"\t\t[{colored('6', 'cyan')}]Restart             \t\t---------------> "
              f"Restart remote station")
        print(f"\t\t[{colored('7', 'cyan')}]CLS                 \t\t---------------> "
              f"Clear Screen")
        print(f"\t\t[{colored('8', 'cyan')}]Back                \t\t---------------> "
              f"Back to Control Center \n")

        self.logIt_thread(self.log_path, debug=False, msg=f'=== End of show_shell_commands() ===')

    def confirm_restart(self, con):
        self.logIt_thread(self.log_path, debug=False, msg=f'Running confirm_restart()...')
        tries = 0
        while True:
            try:
                self.logIt_thread(self.log_path, debug=False, msg=f'Running input validation on {self.sure}...')
                str(self.sure)

            except TypeError:
                self.logIt_thread(self.log_path, debug=False, msg=f'Wrong input detected.')
                print(f"[{colored('*', 'red')}]Wrong Input. [({colored('Y/y', 'yellow')}) | "
                      f"({colored('N/n', 'yellow')})]")

                if tries == 3:
                    self.logIt_thread(self.log_path, debug=False, msg=f'Tries: 3')
                    print("U obviously don't know what you're doing. goodbye.")
                    if len(server.targets) > 0:
                        self.logIt_thread(self.log_path, debug=False, msg=f'Closing live connections...')
                        for t in server.targets:
                            t.send('exit'.encode())
                            t.shutdown(socket.SHUT_RDWR)
                            t.close()

                        self.logIt_thread(self.log_path, debug=False, msg=f'Live connections closed.')

                    self.logIt_thread(self.log_path, debug=False, msg=f'Exiting app with code 1...')
                    sys.exit(1)

                tries += 1

            if str(self.sure).lower() == "y":
                self.logIt_thread(self.log_path, debug=False, msg=f'User input: {self.sure} | Returning TRUE...')
                return True

            elif str(self.sure).lower() == "n":
                self.logIt_thread(self.log_path, debug=False, msg=f'User input: {self.sure} | Returning FALSE...')
                con.send('n'.encode())
                break

            else:
                self.logIt_thread(self.log_path, debug=False, msg=f'Wrong input detected.')
                print(f"[{colored('*', 'red')}]Wrong Input. [({colored('Y/y', 'yellow')}) | "
                      f"({colored('N/n', 'yellow')})]")

                if tries == 3:
                    self.logIt_thread(self.log_path, debug=False, msg=f'Tries: 3')
                    print("U obviously don't know what you're doing. goodbye.")
                    if len(server.targets) > 0:
                        self.logIt_thread(self.log_path, debug=False, msg=f'Closing live connections...')
                        dt = get_date()
                        for t in server.targets:
                            t.send('exit'.encode())
                            t.shutdown(socket.SHUT_RDWR)
                            t.close()

                        self.logIt_thread(self.log_path, debug=False, msg=f'Live connections closed.')

                    self.logIt_thread(self.log_path, debug=False, msg=f'Exiting app with code 1...')
                    sys.exit(1)

                tries += 1

    def restart(self, con, ip):
        self.logIt_thread(self.log_path, debug=False, msg=f'Running restart({con}, {ip})...')
        errCount = 3
        self.sure = input("Are you sure you want to restart [Y/n]?")
        if self.confirm_restart(con):
            try:
                self.logIt_thread(self.log_path, debug=False, msg=f'Sending restart command to client...')
                con.send('restart'.encode())
                try:
                    self.logIt_thread(self.log_path, debug=False,
                                      msg=f'Calling self.remove_lost_connection({con}, {ip})...')
                    self.remove_lost_connection(con, ip)
                    return False

                except RuntimeError as e:
                    self.logIt_thread(self.log_path, debug=False, msg=f'Runtime Error: {e}')
                    return False

            except (WindowsError, socket.error) as e:
                self.logIt_thread(self.log_path, debug=False, msg=f'Connection Error: {e}')
                print(f"[{colored('!', 'red')}]Client lost connection.")

                self.logIt_thread(self.log_path, debug=False,
                                  msg=f'Calling self.remove_lost_connection({con}, {ip})...')
                self.remove_lost_connection(con, ip)

        else:
            return False

    def bytes_to_number(self, b):
        self.logIt_thread(self.log_path, msg=f'Running bytes_to_number({b})...')
        dt = get_date()
        res = 0
        for i in range(4):
            res += b[i] << (i * 8)
        return res

    def shell(self, con, ip):
        self.logIt_thread(self.log_path, debug=False, msg=f'Running shell({con}, {ip})...')
        errCount = 0
        while True:
            self.logIt_thread(self.log_path, debug=False, msg=f'Calling self.show_shell_commands({ip})...')
            self.show_shell_commands(ip)

            # Wait for User Input
            self.logIt_thread(self.log_path, debug=False, msg=f'Waiting for user input...')
            cmd = input(f"COMMAND@{ip}> ")

            # Input Validation
            try:
                self.logIt_thread(self.log_path, debug=False,
                                  msg=f'Performing input validation on user input: {cmd}...')
                val = int(cmd)

            except (TypeError, ValueError):
                self.logIt_thread(self.log_path, debug=False, msg=f'Wrong input detected.')
                print(f"[{colored('*', 'red')}]Numbers Only [{colored('1', 'yellow')} - {colored('8', 'yellow')}]!")
                errCount += 1
                if errCount == 3:
                    self.logIt_thread(self.log_path, debug=False, msg=f'Tries: 3')
                    print("U obviously don't know what you're doing. goodbye.")

                    self.logIt_thread(self.log_path, debug=False, msg=f'Sending exit command to {ip}...')
                    con.send("exit".encode())
                    self.logIt_thread(self.log_path, debug=False, msg=f'Send Completed.')

                    self.logIt_thread(self.log_path, debug=False, msg=f'Closing connections...')
                    con.shutdown(socket.SHUT_RDWR)
                    con.close()
                    self.logIt_thread(self.log_path, debug=False, msg=f'Connections closed.')

                    self.logIt_thread(self.log_path, debug=False, msg=f'Exiting app with code 1...')
                    sys.exit(1)

                continue

            # Run Custom Command
            if int(cmd) == 100:
                self.logIt_thread(self.log_path, debug=False, msg=f'Command: 100')
                try:
                    self.logIt_thread(self.log_path, debug=False, msg=f'Send freestyle command...')
                    con.send("freestyle".encode())
                    self.logIt_thread(self.log_path, debug=False, msg=f'Send Completed.')

                except (WindowsError, socket.error) as e:
                    self.logIt_thread(self.log_path, debug=False, msg=f'Connection Error: {e}')
                    break

                self.logIt_thread(self.log_path, debug=False, msg=f'Initializing Freestyle Module...')
                free = Freestyle(con, path, self.tmp_availables, self.clients, self.targets, log_path)

                self.logIt_thread(self.log_path, debug=False, msg=f'Calling freestyle module...')
                free.freestyle()

                continue

            # Create INT Zone Condition
            self.logIt_thread(self.log_path, debug=False, msg=f'Creating user input zone from 1-8...')
            if int(cmd) <= 0 or int(cmd) > 8:
                errCount += 1
                if errCount == 3:
                    self.logIt_thread(self.log_path, debug=False, msg=f'Tries: 3')
                    print("U obviously don't know what you're doing. goodbye.")

                    self.logIt_thread(self.log_path, debug=False, msg=f'Sending exit command to {ip}...')
                    con.send("exit".encode())
                    self.logIt_thread(self.log_path, debug=False, msg=f'Send Completed.')

                    self.logIt_thread(self.log_path, debug=False, msg=f'Closing connections...')
                    con.close()
                    self.logIt_thread(self.log_path, debug=False, msg=f'Connections closed.')

                    self.logIt_thread(self.log_path, debug=False, msg=f'Exiting app with code 1...')
                    sys.exit(1)

                self.logIt_thread(self.log_path, debug=False, msg=f'Wrong input detected.')
                print(f"[{colored('*', 'red')}]{cmd} not in the menu."
                      f"[try {colored(errCount, 'yellow')} of {colored('3', 'yellow')}]\n")

            # Screenshot
            if int(cmd) == 1:
                self.logIt_thread(self.log_path, debug=False, msg=f'Running screenshot condition...')
                errCount = 0
                if len(self.targets) == 0:
                    self.logIt_thread(self.log_path, debug=False, msg=f'No available connections.')
                    print(f"[{colored('*', 'red')}]No connected stations.")
                    break

                try:
                    print(f"[{colored('*', 'cyan')}]Fetching screenshot...")
                    self.logIt_thread(self.log_path, debug=False, msg=f'Sending screen command to client...')
                    con.send('screen'.encode())
                    self.logIt_thread(self.log_path, debug=False, msg=f'Send Completed.')

                    self.logIt_thread(self.log_path, debug=False,
                                      msg=f'Calling Module: '
                                          f'screenshot({con, path, self.tmp_availables, self.clients})...')
                    screenshot = Screenshot(con, path, self.tmp_availables, self.clients, self.log_path)

                    self.logIt_thread(self.log_path, debug=False, msg=f'Calling screenshot.recv_file()...')
                    screenshot.recv_file()

                except (WindowsError, socket.error, ConnectionResetError) as e:
                    self.logIt_thread(self.log_path, debug=False, msg=f'Connection Error: {e}')
                    print(f"[{colored('!', 'red')}]Client lost connection.")

                    self.logIt_thread(self.log_path, debug=False,
                                      msg=f'Calling self.remove_lost_connection({con}, {ip}...)')
                    self.remove_lost_connection(con, ip)
                    break

            # System Information
            elif int(cmd) == 2:
                self.logIt_thread(self.log_path, debug=False, msg=f'Running system information condition...')
                errCount = 0
                if len(self.targets) == 0:
                    self.logIt_thread(self.log_path, debug=False, msg=f'No available connections.')
                    print(f"[{colored('*', 'red')}]No connected stations.")
                    break

                try:
                    self.logIt_thread(self.log_path, debug=False, msg=f'Initializing Module: sysinfo...')
                    sysinfo = Sysinfo(con, self.ttl, path, self.tmp_availables, self.clients, self.log_path)

                    print(f"[{colored('*', 'cyan')}]Fetching system information, please wait... ")
                    self.logIt_thread(self.log_path, debug=False, msg=f'Calling sysinfo.run()...')
                    sysinfo.recv_file(text=True)

                except (WindowsError, socket.error, ConnectionResetError) as e:
                    self.logIt_thread(self.log_path, debug=True, msg=f'Connection Error: {e}.')
                    # print(f"[{colored('!', 'red')}]Client lost connection.")
                    try:
                        self.logIt_thread(self.log_path, debug=False,
                                          msg=f'Calling self.remove_lost_connection({con}, {ip})...')
                        self.remove_lost_connection(con, ip)
                        return

                    except RuntimeError:
                        return

            # Last Restart Time
            elif int(cmd) == 3:
                self.logIt_thread(self.log_path, debug=False, msg=f'Running last restart condition...')
                errCount = 0
                if len(self.targets) == 0:
                    self.logIt_thread(self.log_path, debug=False, msg=f'No available connections.')
                    print(f"[{colored('*', 'red')}]No connected stations.")
                    break

                try:
                    self.logIt_thread(self.log_path, debug=False, msg=f'Sending lr command to client...')
                    con.send('lr'.encode())
                    self.logIt_thread(self.log_path, debug=False, msg=f'Send Completed.')

                    self.logIt_thread(self.log_path, debug=False, msg=f'Waiting for response from client...')
                    msg = con.recv(4096).decode()
                    self.logIt_thread(self.log_path, debug=False, msg=f'Client response: {msg}')
                    print(f"[{colored('@', 'green')}]{msg}")

                except (WindowsError, socket.error, ConnectionResetError) as e:
                    self.logIt_thread(self.log_path, debug=False, msg=f'Connection Error: {e}.')
                    print(f"[{colored('!', 'red')}]Client lost connection.")
                    try:
                        self.logIt_thread(self.log_path, debug=False,
                                          msg=f'Calling self.remove_lost_connection({con}, {ip})...')
                        self.remove_lost_connection(con, ip)
                        break

                    except RuntimeError as e:
                        self.logIt_thread(self.log_path, debug=True, msg=f'Runtime Error: {e}.')
                        return

            # Anydesk
            elif int(cmd) == 4:
                self.logIt_thread(self.log_path, debug=False, msg=f'Running anydesk condition...')

                errCount = 0
                print(f"[{colored('*', 'magenta')}]Starting AnyDesk...\n")
                if len(self.targets) == 0:
                    self.logIt_thread(self.log_path, debug=False, msg=f'No available connections.')
                    print(f"[{colored('*', 'red')}]No connected stations.")
                    break

                try:
                    self.logIt_thread(self.log_path, debug=False, msg=f'Sending anydesk command to {con}...')
                    con.send('anydesk'.encode())
                    self.logIt_thread(self.log_path, debug=False, msg=f'Send Completed.')

                    self.logIt_thread(self.log_path, debug=False, msg=f'Waiting for response from client...')
                    msg = con.recv(1024).decode()
                    self.logIt_thread(self.log_path, debug=False, msg=f'Client response: {msg}.')

                    if "OK" not in msg:
                        self.logIt_thread(self.log_path, debug=False, msg=f'Printing msg from client...')
                        print(msg)

                except (WindowsError, ConnectionError, socket.error) as e:
                    self.logIt_thread(self.log_path, debug=False, msg=f'Connection Error: {e}.')
                    print(f"[{colored('!', 'red')}]Client lost connection.")
                    try:
                        self.logIt_thread(self.log_path, debug=False,
                                          msg=f'Calling self.remove_lost_connection({con}, {ip})...')
                        self.remove_lost_connection(con, ip)
                        break

                    except RuntimeError as e:
                        self.logIt_thread(self.log_path, debug=True, msg=f'Runtime Error: {e}.')
                        return

            # Tasks
            elif int(cmd) == 5:
                self.logIt_thread(self.log_path, debug=False, msg=f'Running tasks condition...')
                errCount = 0
                if len(self.targets) == 0:
                    self.logIt_thread(self.log_path, debug=False, msg=f'No available connections.')
                    print(f"[{colored('*', 'red')}]No connected stations.")
                    break

                self.logIt_thread(self.log_path, debug=False, msg=f'Initializing Module: tasks...')
                tasks = Tasks(con, ip, ttl, self.clients, self.connections,
                              self.targets, self.ips, self.tmp_availables, path)

                # tasks.run()
                self.logIt_thread(self.log_path, debug=False, msg=f'Calling tasks.tasks()...')
                if not tasks.tasks():
                    self.logIt_thread(self.log_path, debug=False, msg=f'Tasks: False. returning False...')
                    return False

                self.logIt_thread(self.log_path, debug=False, msg=f'Calling tasks.kill_tasks()...')
                task = tasks.kill_tasks()
                if task is None:
                    continue

                try:
                    self.logIt_thread(self.log_path, debug=False, msg=f'Calling tasks.task_to_kill()...')
                    tasks.task_to_kill()
                    return True

                except (WindowsError, socket.error, ConnectionResetError, ConnectionError) as e:
                    self.logIt_thread(self.log_path, debug=False, msg=f'Connection Error: {e}')
                    print(f"[{colored('!', 'red')}]Client lost connection.")
                    try:
                        self.logIt_thread(self.log_path, debug=False,
                                          msg=f'Calling self.remove_lost_connection({con}, {ip})...')
                        self.remove_lost_connection(con, ip)

                    except RuntimeError as e:
                        self.logIt_thread(self.log_path, debug=False, msg=f'Runtime Error: {e}.')
                        return False

            # Restart
            elif int(cmd) == 6:
                self.logIt_thread(self.log_path, debug=False, msg=f'Running restart condition...')
                self.logIt_thread(self.log_path, debug=False, msg=f'Calling self.restart({con}, {ip})...')
                self.restart(con, ip)

            # Clear Screen
            elif int(cmd) == 7:
                self.logIt_thread(self.log_path, debug=False, msg=f'Running clear screen condition...')
                self.logIt_thread(self.log_path, debug=False, msg=f'Clearing screen...')
                os.system('cls')
                self.logIt_thread(self.log_path, debug=False, msg=f'Screen cleared.')
                continue

            # Back
            elif int(cmd) == 8:
                self.logIt_thread(self.log_path, debug=False, msg=f'Running back condition...')
                self.logIt_thread(self.log_path, debug=False, msg=f'Breaking shell loop...')
                break

        self.logIt_thread(self.log_path, debug=False, msg=f'=== End of shell() ===')
        return

    def remove_lost_connection(self, con, ip):
        self.logIt_thread(self.log_path, debug=False, msg=f'Running remove_lost_connection({con}, {ip})...')
        try:
            self.logIt_thread(self.log_path, debug=False, msg=f'Removing connections...')
            for conKey, ipValue in self.clients.items():
                if conKey == con:
                    for ipKey, identValue in ipValue.items():
                        if ipKey == ip:
                            for identKey, userValue in identValue.items():
                                self.targets.remove(con)
                                self.ips.remove(ip)

                                del self.connections[con]
                                del self.clients[con]
                                print(f"[{colored('*', 'red')}]{colored(f'{ip}', 'yellow')} | "
                                      f"{colored(f'{identKey}', 'yellow')} | "
                                      f"{colored(f'{userValue}', 'yellow')} "
                                      f"Removed from Availables list.\n")

            self.logIt_thread(self.log_path, debug=False, msg=f'Connections removed.')
            return True

        except RuntimeError as e:
            self.logIt_thread(self.log_path, debug=True, msg=f'Runtime Error: {e}.')
            return False


def headline():
    server.logIt_thread(log_path, debug=False, msg=f'Running headline()...')
    print(f"\t\t\t\t{colored('==+-+-+-+-+-+-++-0-+-+-0++-+-+-+-+-+-+-+-+-++', 'red')}\n"
          f"\t\t\t\t{colored('|W|e|l|c|o|m|e', 'yellow')} {colored('|0|T|o|0|', 'green')} "
          f"{colored('M|e|k|i|f|A|d|m|i|n', 'yellow')}\n"
          f"\t\t\t\t{colored('==+-+-+-+-+-+-++-0-+-+-0++-+-+-+-+-+-+-+-+-++', 'red')}")
    print(f""
          f"\t\t\t\t{colored('By Gil Shwartz', 'green')} {colored('@2022', 'yellow')}\n")
    print(f"\t\t({colored('1', 'yellow')})Remote Control          ---------------> "
          f"Show Remote Commands")
    print(f"\t\t({colored('2', 'yellow')})Connection History      ---------------> "
          f"Show connection history.")
    print(f"\t\t({colored('3', 'yellow')})Show Connected Stations ---------------> "
          f"Display Current connected stations")
    print(f"\t\t({colored('4', 'yellow')})CLS                     ---------------> "
          f"Clear Local Screen")
    print(f"\t\t({colored('5', 'yellow')})Server Info             ---------------> "
          f"Show Server Information")
    print(f"\n\t\t({colored('6', 'red')})Exit                    ---------------> "
          f"Close connections and exit program.\n")

    server.logIt_thread(log_path, debug=False, msg=f'=== End of headline() ===')


def get_date():
    d = datetime.now().replace(microsecond=0)
    dt = str(d.strftime("%b %d %Y | %I-%M-%S"))

    return dt


def main():
    def validate():
        while True:
            server.logIt_thread(log_path, debug=False, msg=f'Waiting for user input...')
            command = input("CONTROL@> ")
            server.logIt_thread(log_path, debug=False, msg=f'User input: {command}.')

            try:
                server.logIt_thread(log_path, debug=False, msg=f'Performing input validation on {command}...')
                int(command)

                return command

            except ValueError:
                server.logIt_thread(log_path, debug=False, msg=f'Wrong input detected.')
                print(
                    f"[{colored('*', 'red')}]Numbers only. Choose between "
                    f"[{colored('1', 'yellow')} - {colored('5', 'yellow')}].\n")

    def remote_shell():
        server.logIt_thread(log_path, debug=False, msg=f'Running remote shell commands condition...')
        if len(server.clients) != 0:
            print(f"{colored('=', 'blue')}=>{colored('Remote Shell', 'red')}<={colored('=', 'blue')}")

            # Show Available Connections
            server.logIt_thread(log_path, debug=False, msg=f'Calling server.show_available_connections()...')
            server.show_available_connections()

            # Get Number from User and start Remote Shell
            server.logIt_thread(log_path, debug=False, msg=f'Calling server.get_station_number()...')
            station = server.get_station_number()
            if station:
                server.logIt_thread(log_path, debug=False, msg=f'Calling server.shell({station[1]}, {station[2]})...')
                server.shell(station[1], station[2])
                return

        else:
            server.logIt_thread(log_path, debug=False, msg=f'No available connections.')
            print(f"[{colored('*', 'cyan')}]No available connections.")

        return

    def choices():
        server.logIt_thread(log_path, debug=False, msg=f'Validating input number is in the menu...')
        if int(command) <= 0 or int(command) > 6:
            print(f"[{colored('*', 'red')}]Wrong Number. [{colored('1', 'yellow')} - {colored('5', 'yellow')}]!")
            return False

        # Remote Shell Commands
        if int(command) == 1:
            remote_shell()

        # Connection History
        elif int(command) == 2:
            server.logIt_thread(log_path, debug=False, msg=f'Calling server.connection_history()...')
            server.connection_history()
            return

        # Vital Signs - Show Connected Stations
        elif int(command) == 3:
            server.logIt_thread(log_path, debug=False, msg=f'Running show connected stations condition...')
            if len(server.ips) == 0:
                server.logIt_thread(log_path, debug=False, msg=f'No available connections.')
                print(f"[{colored('*', 'yellow')}]No connected stations.")
                return

            print(f"{colored('=', 'blue')}=>{colored('Vital Signs', 'red')}<={colored('=', 'blue')}")
            print(f"[{colored('1', 'green')}]Start | "
                  f"[{colored('2', 'cyan')}]Back\n")

            server.logIt_thread(log_path, debug=False, msg=f'Calling server.vital_signs()...')
            server.vital_signs()

        # Clear Screen
        elif int(command) == 4:
            server.logIt_thread(log_path, debug=False, msg=f'Running clear screen...')
            server.logIt_thread(log_path, debug=False, msg=f'Calling headline()...')
            os.system('cls')

        # Show Server's Information
        elif int(command) == 5:
            server.logIt_thread(log_path, debug=False, msg=f'Running show server information...')
            last_reboot = psutil.boot_time()
            print(f"\n[{colored('*', 'cyan')}]Server running on IP: {server.serverIp} | Port: {server.serverPort}")
            print(f"[{colored('*', 'cyan')}]Server's last restart: "
                  f"{datetime.fromtimestamp(last_reboot).replace(microsecond=0)}")
            print(f"[{colored('*', 'cyan')}]Connected Stations: {len(server.clients)}\n")

        # Exit Program
        elif int(command) == 6:
            server.logIt_thread(log_path, debug=False, msg=f'User input: 6 | Exiting app...')

            if len(server.targets) > 0:
                try:
                    for t in server.targets:
                        server.logIt_thread(log_path, debug=False, msg=f'Sending exit command to connected stations...')
                        t.send('exit'.encode())
                        server.logIt_thread(log_path, debug=False, msg=f'Send completed.')

                        server.logIt_thread(log_path, debug=False, msg=f'Closing socket connections...')
                        t.close()
                        server.logIt_thread(log_path, debug=False, msg=f'Socket connections closed.')

                except ConnectionResetError as e:
                    server.logIt_thread(log_path, debug=True, msg=f'Connection Error: {e}.')
                    print(f"[{colored('X', 'red')}]Connection Reset by client.")

                    server.logIt_thread(log_path, debug=True, msg=f'Exiting app with code 1...')
                    sys.exit(1)

            server.logIt_thread(log_path, debug=False, msg=f'Exiting app with code 0...')
            sys.exit(0)

        return

    server.logIt_thread(log_path, debug=False, msg=f'Running main()...')
    server.logIt_thread(log_path, debug=False, msg=f'Calling headline()...')
    headline()

    server.logIt_thread(log_path, debug=False, msg=f'Calling validate()...')
    command = validate()
    server.logIt_thread(log_path, debug=False, msg=f'Validated command: {command}')

    server.logIt_thread(log_path, debug=False, msg=f'Calling choices()...')
    choices()


if __name__ == '__main__':
    port = 55400
    ttl = 5
    hostname = socket.gethostname()
    serverIP = str(socket.gethostbyname(hostname))
    path = r'c:\MekifRemoteAdmin'
    log_path = r'c:\MekifRemoteAdmin\server_log.txt'

    # Run User Validation
    # validation.validation()

    # Initialize Server Class
    server = Server(serverIP, port, ttl, path, log_path)
    server.logIt_thread(log_path, debug=False, msg=f'Server class initiated!')

    server.logIt_thread(log_path, debug=False, msg=f'Calling server.run()...')
    server.run()

    while True:
        main()
