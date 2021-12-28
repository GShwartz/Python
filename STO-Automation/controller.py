from engine import Player1, Player2, Character, DilRefine
from ComputerVision import ComputerVision
import win32com.client
import reputation
import pyautogui
import cv2 as cv
import keyboard
import win32api
import win32con
import win32gui
import random
import engine
import time
import sys
import os

top_windows = []
results = []
change_time = 0
confirm_x, confirm_y = 955, 640
menu_x, menu_y = 1905, 150
player1_round = 0
player2_round = 0
player2_time = 0
dur = 0.2
pause = 0.5
liveImage = r'G:\School\Python - Homework\Projects\STO-Automation\live_sc.jpg'
logged_out = r'G:\School\Python - Homework\Projects\STO-Automation\logged_out.JPG'


def player_automation(player):
    # Open Reputation Window
    print(f"[i] Player #{player}: Opening Reputation Window")
    keyboard.press_and_release("[")
    time.sleep(pause)

    # Start Reputation Automation
    print(f"[i] Player #{player}: Starting automation for Player 1")

    # Init Mouse Position
    pyautogui.moveTo(100, 100, duration=dur)
    time.sleep(pause)

    # Running Reputation automation
    print(f"[i] Player #{player}: Running Reputation automation.")
    Player1(player).act_reputation()
    time.sleep(pause)

    # Close Reputation Window
    print(f"[i] Player #{player}: Reputation Window")
    keyboard.press_and_release('[')
    time.sleep(pause)

    # Open DutyOfficers/Admiralty Window
    print(f"[i] Player #{player}: Opening Admiralty Window")
    keyboard.press_and_release("]")
    time.sleep(pause)

    # Start Admiralty Automation
    print(f"[i] Player #{player}: Running Admiralty automation.")
    # Player1().act_admiralty()
    print(f"[i] Player #{player}: Admiralty automation completed.")
    time.sleep(pause)

    # Start Duty Officers Automation
    print(f"[i] Player #{player}: Starting DutyOfficers automation.")
    Player1(player).act_dutyofficers()
    time.sleep(pause)
    print(f"[i] Player #{player}: DutyOfficers automation completed.")

    # Start DutyOfficers Mission Assignments
    print(f"[i] Player #{player}: Running DuFF missions.")
    Player1(player).duff_missions()
    time.sleep(pause)

    # Close Admiralty/DutyOfficers Window
    print(f"[i] Player #{player}: Closing DutyOfficers/Admiralty Window")
    keyboard.press_and_release("]")
    time.sleep(pause)

    # Start Refining Automation
    print(f"[i] Player #{player}: Running Refining automation.")

    # Open Refining Window
    print(f"[i] Player #{player}: Opening Refining Window")
    keyboard.press_and_release("i")
    time.sleep(pause)

    # Run Automation
    print(f"[i] Player #{player}: Running Refining Automation")
    DilRefine(player).act()
    time.sleep(pause)

    # Close Refining window
    print(f"[i] Player #{player}: Closing Refining Window")
    keyboard.press_and_release("i")
    print(f"[i] Player #{player}: Finished Refining automation.")
    time.sleep(pause)


def change_player(player):
    global change_time
    change_start = time.time()

    # Change Character
    print(f"[i] Player #{player}: Changing character...")

    # Open Main Menu
    print(f"[i] Player #{player}: Opening Main Menu")
    pyautogui.moveTo(menu_x, menu_y, duration=dur)
    time.sleep(pause)
    print(f"[i] Player #{player}: Clicking on Menu")
    click(menu_x, menu_y)
    time.sleep(pause)
    Character(player).act()
    time.sleep(pause)
    print(f"[i] Player #{player}: Finished Character change.")

    change_end = time.time()
    change_time = change_end - change_start

    return


def sleeper():
    # sleeptime = random.randint(300, 720)    # Between 5 and 12 minutes.
    sleeptime = random.randint(5, 10)
    print(f"[i] Sleeper set for {sleeptime} seconds.")
    for x in range(sleeptime, 0, -1):
        sys.stdout.write("\r[i]Sleeping for " + str(x) + " seconds...")
        time.sleep(1)

    # Capture Screenshot
    main_window()

    # Compare screenshots and verify the connection to the server.
    if not ComputerVision(cv.imread(liveImage, cv.IMREAD_UNCHANGED),
                          cv.imread(logged_out, cv.IMREAD_UNCHANGED),
                          threshold=0.5).compare():

        # Simulate character movement
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

    return


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
