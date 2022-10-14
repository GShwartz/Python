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


if __name__ == '__main__':

    task = 'client.exe'
    client_file = r'c:\peach\client.exe'
    url = 'https://github.com/GShwartz/Python/raw/main/MekifAdmin/Setup/client.exe'
    destination = r'C:\Peach\client.exe'
    log_path = r'c:\Peach\client_log.txt'

    logIt_thread(log_path, msg='\n\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'
                               '\n********** Starting Updater **********')

    logIt_thread(log_path, msg=f'Calling process_exists({task})...')
    if process_exists(task):
        # Kill running client
        logIt_thread(log_path, msg='Killing client.exe process...')
        os.system(f'taskkill /IM {task} /F')

    # Delete current client.exe file
    if os.path.exists(client_file):
        logIt_thread(log_path, msg=f'Removing {client_file}...')
        os.remove(client_file)

    logIt_thread(log_path, msg='Sleeping for 1 second...')
    time.sleep(1)

    # Download new client file
    logIt_thread(log_path, msg='Downloading new client.exe file...')
    wget.download(url, destination)
    logIt_thread(log_path, msg='Download complete.')

    # Restart client
    logIt_thread(log_path, msg='Running run.bat...')
    p = subprocess.call([r'wscript', r'C:\Peach\run.vbs'])

    logIt_thread(log_path, msg='Waiting 5 seconds for process restart...')
    time.sleep(5)

    if process_exists(task):
        logIt_thread(log_path, msg='\n\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'
                                   '\n********** End of Updater **********\n\n')

    else:
        logIt_thread(log_path, msg='Error!')
        sys.exit(1)
