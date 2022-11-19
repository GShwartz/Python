import sys
from datetime import datetime
from threading import Thread
import subprocess
import time
import wget
import os


def process_exists(process_name):
    call = 'TASKLIST', '/FI', f'imagename eq {process_name}'
    output = subprocess.check_output(call).decode()
    last_process_line = output.strip().split('\r\n')[-1]
    return last_process_line.lower().startswith(process_name.lower())


def get_date():
    d = datetime.now().replace(microsecond=0)
    dt = str(d.strftime("%b %d %Y %I.%M.%S %p"))

    return dt


def logIt(logfile=None, debug=None, msg=''):
    dt = get_date()
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


def logIt_thread(log_path=None, debug=False, msg=''):
    logit_thread = Thread(target=logIt, args=(log_path, debug, msg), name="Log Thread")
    logit_thread.start()
    return


def download(url, destination):
    logIt_thread(log_path, msg='Downloading new client.exe file...')
    wget.download(url, destination)
    logIt_thread(log_path, msg='Download complete.')
    return True


def restart_client():
    logIt_thread(log_path, msg='Running client.vbs...')
    p = subprocess.call([r'wscript', r'C:\HandsOff\client.vbs'])

    logIt_thread(log_path, msg='Waiting 5 seconds for process restart...')
    time.sleep(5)
    if process_exists(task):
        logIt_thread(log_path, msg='\n\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'
                                   '\n********** End of Updater **********\n\n')
        return True

    else:
        return False


def main():
    logIt_thread(log_path, msg=f'Calling process_exists({task})...')
    if process_exists(task):
        logIt_thread(log_path, msg='Killing client.exe process...')
        os.system(f'taskkill /IM {task} /F')
        time.sleep(2)

    # Delete current client.exe file
    if os.path.exists(client_file):
        logIt_thread(log_path, msg=f'Removing {client_file}...')
        os.remove(client_file)
        time.sleep(5)

    # Download new client file
    download(url, destination)

    while True:
        if not restart_client():
            if not os.path.exists(client_file):
                download(url, destination)
                if not process_exists(task):
                    time.sleep(1)
                    restart_client()

            else:
                os.remove(client_file)
                time.sleep(2)
                download(url, destination)
                time.sleep(1)
                restart_client()

        else:
            sys.exit(0)


if __name__ == '__main__':
    task = 'client.exe'
    client_path = r'c:\HandsOff'
    client_file = r'c:\HandsOff\client.exe'
    url = 'https://github.com/GShwartz/Python/raw/main/Peach/Client/Setup/client.exe'
    destination = r'C:\HandsOff\client.exe'
    log_path = r'c:\HandsOff\client_log.txt'

    logIt_thread(log_path, msg='\n\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'
                               '\n********** Starting Updater **********')

    main()


