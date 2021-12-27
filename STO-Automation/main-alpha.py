from ComputerVision import ComputerVision   # Image Compare
from players import Player1, Player2  # Current Characters
from time import gmtime, strftime  # Display current time for logging.
import reputation  # Reputation module
import cv2 as cv    # Computer Vision
import pyautogui  # Graphic Automation.
import keyboard  # Keyboard Simulation.
import win32api  # Windows components.
import win32com.client  # Windows components.
import win32con  # Windows components.
import win32gui  # Windows components.
import threading  # For mouse position display.
import datetime  # For Elapsed Time calculation.
import random  # Random number for Sleeper's timer.
import ctypes  # For Keyboard language validation.
import time  # Pause between actions, Mouse drag Duration time.
import sys  # Display counter while sleeper in action
import os  # Get current logged in User and save log file in Documents.


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


def player1_automation():
    global player1_round
    global player1_time
    player1_round_start_time = time.time()

    # Start Reputation Automation
    print(f"[i]Starting automation for Player 1")
    logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())} : Starting automation for Player 1\n")
    pyautogui.moveTo(100, 100, duration=dur)
    time.sleep(pause)

    # Open Reputation Window
    print("[i]Opening Reputation Window")
    keyboard.press_and_release("[")
    logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())} : Opening Reputation Window\n")
    time.sleep(pause)

    # Running Reputation automation
    print("[i]Player 1: Running Reputation automation.")
    logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())} : Player 1: Running Reputation automation.\n")
    Player1().act_reputation()
    time.sleep(pause)

    # Close Reputation Window
    keyboard.press_and_release("[")
    time.sleep(pause)
    print("Player 1: Reputation automation completed.")
    logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())} : Player 1: Reputation automation completed.\n")

    # Open Admiralty Window
    print("[i]Opening Admiralty Window")
    keyboard.press_and_release("]")
    time.sleep(pause)

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

    print("[i]Player 1: DutyOfficers automation completed.")
    logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())} : Player 1: DutyOfficers automation completed.\n")

    # Start DutyOfficers Mission Assignments
    print("[i]Running DuFF missions.")
    Player1().duff_missions()
    time.sleep(pause)

    # keyboard.press_and_release("]")
    # time.sleep(pause)

    # Start Refining Automation
    print("[i]Player 1: Running Refining automation.")
    logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())} : Player 1: Running Refining automation.\n")

    # Open Refining Window
    keyboard.press_and_release("i")
    time.sleep(pause)

    # Run Automation
    DilRefine().act()
    time.sleep(pause)

    # Close Refining window
    keyboard.press_and_release("i")
    print("[i]Player 1: Finished Refining automation.")
    logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())} : Player 1: Refining automation completed.\n")
    time.sleep(pause)

    player1_round += 1
    player1_round_end_time = time.time()
    player1_time = player1_round_end_time - player1_round_start_time

    return


def player2_automation():
    global player2_round
    global player2_time
    player2_round_start_time = time.time()

    # Start Reputation Automation Character 2
    print(f"[i]Running automation for character 2...")
    logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())} : Running automation for Player 2\n")
    pyautogui.moveTo(100, 100, duration=dur)
    time.sleep(pause)

    # Open Reputation Window
    keyboard.press_and_release("[")
    print("[i]Player 2: Running Reputation automation...")
    logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())} : Player 2: Running Reputation automation.\n")
    time.sleep(pause)

    # Run Reputation Automation
    Player2().act_reputation()
    time.sleep(pause)

    # Close Reputation Window
    keyboard.press_and_release("[")
    time.sleep(pause)
    print("[i]Player 2: Reputation automation completed.")
    logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())} : Player 2: Reputation automation completed.\n")

    # Open Admiralty Window
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

    # Start DutyOfficers Mission Assignments
    print("[i]Running DuFF missions.")
    Player2().duff_missions()
    time.sleep(pause)

    print("[i]Player 2: DutyOfficers automation completed.")
    logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())} : Player 2: DutyOfficers automation completed.\n")

    # Start Refining Automation
    print("[i]Player 2: Starting Refining Automation.")
    logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())} : Player 2: Running Refining automation.\n")

    # Open Refining Window
    keyboard.press_and_release("i")
    time.sleep(pause)

    # Run Refining Automation
    DilRefine().act()
    time.sleep(pause)

    # Close Refining Window
    keyboard.press_and_release("i")
    print("[i]Player 2: Finished Refining trainer.")
    logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())} : Player 2: Refining automation completed.\n")
    time.sleep(pause)

    player2_round += 1
    player2_round_end_time = time.time()
    player2_time = player2_round_end_time - player2_round_start_time

    return


def change_player():
    global change_time
    change_start = time.time()

    # Change Character
    print("[i]Changing character...")
    logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())} : ==== Changing Character ==== \n")

    # Open Main Menu
    print("[i]Opening Main Menu")
    pyautogui.moveTo(menu_x, menu_y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Menu")
    click(menu_x, menu_y)
    time.sleep(pause)
    Character().act()
    time.sleep(pause)
    print("[i]Finished Character change.")
    logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())} : ==== Character changed. ====\n")

    change_end = time.time()
    change_time = change_end - change_start

    return


def sleeper(timeslept):
    # sleeptime = random.randint(300, 720)    # Between 5 and 12 minutes.
    sleeptime = random.randint(5, 10)
    print(f"[i]Sleeper set for {sleeptime} seconds.")
    for x in range(sleeptime, 0, -1):
        sys.stdout.write("\r[i]Sleeping for " + str(x) + " seconds...")
        time.sleep(1)

    timeslept = (timeslept + sleeptime)

    # Capture Screenshot
    main_window()

    # Compare screenshots and verify the connection to the server.
    # If Server is connected then simulate character movement.
    # If connection is lost then end the script.
    if not compare():
        print("Simulating Character Look Left")
        keyboard.press('a')
        time.sleep(0.2)
        keyboard.release('a')
        print("Simulating Character Look Right")
        keyboard.press('d')
        time.sleep(0.2)
        keyboard.release('d')

    else:
        print("[!] Disconnected from Server. Stopping Script. [!]")
        exit()

    return timeslept


def compare():
    if not ComputerVision(cv.imread(liveImage, cv.IMREAD_UNCHANGED),
                          cv.imread(logged_out, cv.IMREAD_UNCHANGED),
                          threshold=0.5).compare():
        return False

    else:
        return True


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


def main_window():
    global top_windows, results, liveImage

    # Switch to STO Window
    for i in top_windows:
        if "star trek online" in f"{i[1]}".lower():
            print("[i]Switching to STO...")
            win32gui.ShowWindow(i[0], 5)
            win32gui.SetForegroundWindow(i[0])
            print("[i] Taking Screenshot.")
            liveSC = pyautogui.screenshot()
            liveSC.save(liveImage)
            print("[i] Screenshot Saved.")


def window_enumeration_handler(hwnd, top_windows):
    # Add windows to list
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))


def show_mouse_pos():
    while True:
        print(pyautogui.position())


if __name__ == "__main__":
    top_windows = []
    results = []
    confirm_x, confirm_y = 955, 640
    menu_x, menu_y = 1905, 150

    # General Vars
    total_time = 0
    time_slept = 0
    player1_round = 0
    player1_time = 0
    player2_round = 0
    player2_time = 0
    rounds = 0
    player_changes = 0
    change_time = 0
    pause = 0.5
    dur = 0.2
    log = f"c:\\Users\\{os.getlogin()}\\Documents\\STO-Log.txt"
    liveImage = r'G:\School\Python - Homework\Projects\STO-Automation\live_sc.jpg'
    logged_out = r'G:\School\Python - Homework\Projects\STO-Automation\logged_out.JPG'

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
        logger.write(f"===============    {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())}    ===============\n")
        logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : Switch to STO Window.\n")

        # Switch to STO Window
        for i in top_windows:
            if "star trek online" in f"{i[1]}".lower():
                print("[i]Switching to STO...")
                win32gui.ShowWindow(i[0], 5)
                win32gui.SetForegroundWindow(i[0])
                break

        time.sleep(0.8)
        while True:
            # Initialize timer
            start = time.time()

            # Start automation
            player1_automation()
            print(f"[i]Player 1 Round Time: {player1_time} seconds.")
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : "
                         f"Player 1 Round Time: {player1_time} seconds.\n")

            # Switch Characters
            change_player()
            print(f"[i]Change Players Time: {change_time} seconds.")
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : "
                         f"Change Players Time: {change_time} seconds.\n")
            time.sleep(pause)

            player2_automation()
            print(f"[i]Player 2 Round Time: {player2_time} seconds.")
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : "
                         f"Player 1 Round Time: {player2_time} seconds.\n")

            change_player()
            time.sleep(pause)

            # Start sleeper if each character had an automation round.
            player_changes += 1
            if player_changes >= 1:
                rounds += 1
                player1_round = 1
                player2_round = 1

                # Start Sleeper
                time_slept = sleeper(time_slept)
                print("\n[i]Sleeper finished.")
                logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())}"
                             f" : Sleeper finished.\n")
                print(f"[i]Total time slept: {round(time_slept)} seconds.")
                logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())}"
                             f" : Total time slept: {round(time_slept)} seconds.\n")
                print(f"[i]Total rounds: {rounds}")
                logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())}"
                             f" : Total rounds: {rounds}\n")

                player_changes = 1

                end = time.time()
                total_t = end - start
                print(f"Time elapsed: {total_t} seconds.")
                logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())} : "
                             f"Time elapsed: {total_t} seconds.\n")
                total_time += total_t
                print(f"[i]Total Time: {round(total_time / 60)} minutes.")
                logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())} : "
                             f"Total Time: {round(total_time / 60)} minutes.\n")
