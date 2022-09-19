from datetime import datetime
from termcolor import colored
import ntpath
import time


def bytes_to_number(b):
    # if Python2.x
    # b = map(ord, b)
    res = 0
    for i in range(4):
        res += b[i] << (i * 8)
    return res


def screenshot(con):
    d = datetime.now().replace(microsecond=0)
    dt = str(d.strftime("%b %d %Y | %I-%M-%S"))
    print(f"working...")
    con.send('screen'.encode())
    filenameRecv = con.recv(1024)
    con.send("OK filename".encode())
    time.sleep(0.1)
    name = ntpath.basename(str(filenameRecv).encode())
    size = con.recv(4)
    size = bytes_to_number(size)
    current_size = 0
    buffer = b""

    with open(filenameRecv, 'wb') as screenshotFile:
        while current_size < size:
            data = con.recv(1024)
            if not data:
                break

            if len(data) + current_size > size:
                data = data[:size - current_size]

            buffer += data
            current_size += len(data)
            screenshotFile.write(data)

    print(f"[{colored('*', 'green')}]Received: {name[:-1]} \n")
    con.send(f"Received file: {name[:-1]}\n".encode())

    return
