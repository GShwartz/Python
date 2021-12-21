from time import gmtime, strftime   # Display current time for logging.
from players import Player1, Player2    # Current Characters
import reputation   # Reputation module
import pyautogui    # Graphic Automation.
import keyboard     # Keyboard Simulation.
import win32api             # Windows components.
import win32com.client      # Windows components.
import win32con             # Windows components.
import win32gui             # Windows components.
import threading    # For mouse position display.
import datetime     # For Elapsed Time calculation.
import random       # Random number for Sleeper's timer.
import ctypes       # For Keyboard language validation.
import time         # Pause between actions, Mouse drag Duration time.
import sys          # Display counter while sleeper in action
import os           # Get current logged in User and save log file in Documents.


class DilRefine:
    def __init__(self):
        self.assets_x, self.assets_y = 1685, 635
        self.top_scroller_x, self.top_scroller_y = 1897, 700
        self.bottom_scroller_x, self.bottom_scroller_y = 1897, 950
        self.refine_button_x, self.refine_button_y = 1765, 810

    def act(self):
        pyautogui.moveTo(self.assets_x, self.assets_y, duration=dur)
        time.sleep(pause)
        print("[i]Clicking on Assets")
        click(self.assets_x, self.assets_y)
        logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : Clicked on Assets.\n")
        time.sleep(pause)
        pyautogui.moveTo(self.top_scroller_x, self.top_scroller_y, duration=dur)
        time.sleep(pause)
        print("[i]Scrolling Down")
        pyautogui.dragTo(self.bottom_scroller_x, self.bottom_scroller_y, duration=dur)
        logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : Scrolled Down.\n")
        time.sleep(pause)
        pyautogui.moveTo(self.refine_button_x, self.refine_button_y, duration=dur)
        time.sleep(pause)
        print("[i]Clicking on Refine Dilithium")
        click(self.refine_button_x, self.refine_button_y)
        logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : Clicked on Refine Dilithium.\n")
        time.sleep(pause)

        return


class Character:
    def __init__(self):
        self.changeButton_x, self.changeButton_y = 540, 390
        self.changeConfirm_x, self.changeConfirm_y = 955, 570
        self.middleCharacter_x, self.middleCharacter_y = 245, 390
        self.play_x, self.play_y = 425, 875

    def act(self):
        with open(log, 'a+') as logger:
            # Click the Change Character button
            pyautogui.moveTo(self.changeButton_x, self.changeButton_y, duration=dur)
            time.sleep(pause)
            print("[i]Clicking on Change Character")
            click(self.changeButton_x, self.changeButton_y)
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : Clicked on Change Character.\n")
            time.sleep(pause)

            # Confirm character Change
            pyautogui.moveTo(self.changeConfirm_x, self.changeConfirm_y, duration=dur)
            time.sleep(pause)
            print("[i]Clicking on Confirm")
            click(self.changeConfirm_x, self.changeConfirm_y)
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : Clicked on Confirm.\n")
            time.sleep(5)

            # Choose the middle character
            pyautogui.moveTo(self.middleCharacter_x, self.middleCharacter_y, duration=dur)
            time.sleep(pause)
            print("[i]Clicking on the Middle Character")
            click(self.middleCharacter_x, self.middleCharacter_y)
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : Clicked on the Middle Character.\n")
            time.sleep(5)

            # Click the Play button
            pyautogui.moveTo(self.play_x, self.play_y, duration=dur)
            time.sleep(pause)
            print("[i]Clicking on Play")
            click(self.play_x, self.play_y)
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : Clicked on Play.\n")
            time.sleep(10)

            # Close the welcome window
            print("[i]Closing Welcome Window")
            keyboard.press_and_release("esc")
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : Keyboard Press ESC\n")

            return


def click(x, y):
    # Clear Mouse Status
    win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE, x, y, 0, 0)

    # Set Mouse Position
    win32api.SetCursorPos((x, y))

    # Commence Mouse Click
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

    # Clear Mouse Status
    win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE, x, y, 0, 0)


def sleeper(timeslept):
    # sleeptime = random.randint(480, 2400)
    sleeptime = random.randint(5, 10)
    print(f"[i]Sleeper set for {sleeptime} seconds.")
    logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())} : Sleeper set for {sleeptime} seconds.\n")
    for x in range(sleeptime, 0, -1):
        sys.stdout.write("\r[i]Sleeping for " + str(x) + " seconds...")
        time.sleep(1)

    timeslept = timeslept + sleeptime

    return timeslept


def change_player():
    # Change Character
    print("[i]Changing character...")
    logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())} : ==== Changing Character ==== \n")
    pyautogui.moveTo(menu_x, menu_y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Menu")
    click(menu_x, menu_y)
    time.sleep(pause)
    Character().act()
    time.sleep(pause)
    print("[i]Finished Character change.")
    logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())} : ==== Character changed. ====\n")

    return


def window_enumeration_handler(hwnd, top_windows):
    # Add windows to list
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))


def show_mouse_pos():
    while True:
        print(pyautogui.position())


def player1_automation():
    global player1_round

    # Start Reputation Automation
    print(f"[i]Starting automation for Player 1")
    logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())} : Starting automation for Player 1\n")
    pyautogui.moveTo(100, 100, duration=dur)
    time.sleep(pause)
    print("[i]Opening Reputation Window")
    keyboard.press_and_release("[")
    logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())} : Opening Reputation Window\n")
    time.sleep(pause)
    print("[i]Player 1: Running Reputation automation.")
    logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())} : Player 1: Running Reputation automation.\n")
    Player1().act_reputation()
    time.sleep(pause)
    print("[i]Running DuFF missions.")
    # Player1().duff_missions()
    time.sleep(pause)
    keyboard.press_and_release("[")
    time.sleep(pause)
    keyboard.press_and_release("]")
    time.sleep(pause)
    print("Player 1: Reputation automation completed.")
    logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())} : Player 1: Reputation automation completed.\n")

    # Start Admiralty Automation
    print("[i]Running Admiralty automation.")
    logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())} : Player 1: Running Admiralty automation. \n")
    Player1().act_admiralty()
    print("[i]Player 1: Admiralty automation completed.")
    logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())} : Player 1: Admiralty Automation completed.\n")
    time.sleep(pause)

    # Start Duty Officers Automation
    print("[i]Player 1: Starting DutyOfficers automation.")
    logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())} : Player 1: Running DutyOfficers automation.\n")
    Player1().act_dutyofficers()
    time.sleep(pause)
    keyboard.press_and_release("]")
    time.sleep(pause)
    print("[i]Player 1: DutyOfficers automation completed.")
    logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())} : Player 1: DutyOfficers automation completed.\n")

    # Start Refining Automation
    print("[i]Player 1: Running Refining automation.")
    logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())} : Player 1: Running Refining automation.\n")
    keyboard.press_and_release("i")
    time.sleep(pause)
    DilRefine().act()
    time.sleep(pause)
    keyboard.press_and_release("i")
    print("[i]Player 1: Finished Refining automation.")
    logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())} : Player 1: Refining automation completed.\n")
    time.sleep(pause)

    player1_round += 1

    return


def player2_automation():
    global player2_round

    # Start Reputation Automation Character 2
    print(f"[i]Running automation for character 2...")
    logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())} : Running automation for Player 2\n")
    pyautogui.moveTo(100, 100, duration=dur)
    time.sleep(pause)
    keyboard.press_and_release("[")
    time.sleep(pause)
    print("[i]Player 2: Running Reputation automation...")
    logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())} : Player 2: Running Reputation automation.\n")
    Player2().act_reputation()
    time.sleep(pause)
    keyboard.press_and_release("[")
    time.sleep(pause)
    print("[i]Player 2: Reputation automation completed.")
    logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())} : Player 2: Reputation automation completed.\n")
    keyboard.press_and_release("]")
    time.sleep(pause)

    # Start Admiralty Automation
    print("[i]Running Admiralty automation.")
    logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())} : Player 2: Running Admiralty automation.\n")
    Player2().act_admiralty()
    print("[i]Player 2: Admiralty automation completed.")
    logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())} : Player 2: Admiralty automation completed.\n")
    time.sleep(pause)

    # Start Duty Officers Automation
    print("[i]Player 2: Starting DutyOfficers automation.")
    logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())} : Player 2: Running DutyOfficers automation.\n")
    Player2().act_dutyofficers()
    time.sleep(pause)
    keyboard.press_and_release("]")
    time.sleep(pause)
    print("[i]Player 2: DutyOfficers automation completed.")
    logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())} : Player 2: DutyOfficers automation completed.\n")

    # Start Refining Automation
    print("[i]Player 2: Starting Refining trainer...")
    logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())} : Player 2: Running Refining automation.\n")
    keyboard.press_and_release("i")
    time.sleep(pause)
    DilRefine().act()
    time.sleep(pause)
    keyboard.press_and_release("i")
    print("[i]Player 2: Finished Refining trainer.")
    logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())} : Player 2: Refining automation completed.\n")
    time.sleep(pause)

    player2_round += 1

    return


if __name__ == "__main__":
    confirm_x, confirm_y = 955, 640
    menu_x, menu_y = 1905, 150

    # General Vars
    dt = datetime.datetime.now()
    time_slept = 0
    player1_round = 1
    player2_round = 1
    rounds = 1
    player_changes = 1
    pause = 0.3
    dur = 0.2
    log = f"c:\\Users\\{os.getlogin()}\\Documents\\STO-Log.txt"

    # Change keyboard language to English
    keyboard_language = win32api.LoadKeyboardLayout('00000409', 1)
    print(f"Keyboard Language changed to: English - United States")

    # Show Mouse Position
    global_thread = threading.Thread(target=show_mouse_pos, name="Global Conf")
    # global_thread.daemon = True
    # global_thread.start()

    # Initialize OS's open windows
    results = []
    top_windows = []

    # Enumerate opened OS windows
    win32gui.EnumWindows(window_enumeration_handler, top_windows)

    # Start logger
    with open(log, 'a+') as logger:
        logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : Switch to STO Window.\n")

        # Switch to STO Window
        for i in top_windows:
            if "star trek online" in f"{i[1]}".lower():
                print("[i]Switching to STO...")
                win32gui.ShowWindow(i[0], 5)
                win32gui.SetForegroundWindow(i[0])
                break
        time.sleep(0.5)

        while True:
            # Initialize timer
            start - dt.replace(microsecond=0)

            # Start automation
            player1_automation()
            change_player()
            time.sleep(pause)
            player2_automation()
            change_player()
            time.sleep(pause)

            # Start sleeper if each player had an automation round.
            player_changes += 1
            if player_changes >= 2:
                rounds += 1
                player1_round = 1
                player2_round = 1

                # Start Sleeper
                time_slept = sleeper(time_slept)
                print("\n[i]Sleeper finished.")
                logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())}"
                             f" : Sleeper finished.\n")
                print(f"[i]Total time slept: {time_slept} seconds.")
                logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())}"
                             f" : Total time slept: {time_slept} seconds.\n")
                print(f"[i]Total rounds: {rounds}")
                logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())}"
                             f" : Total rounds: {rounds}\n")

                player_changes = 1

                end = dt.replace(microsecond=0)
                print(f"Time elapsed: {end - start}")
                logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())} : Time elapsed: {end - start}.\n")
