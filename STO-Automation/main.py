from ComputerVision import ComputerVision
from controller import Controller
from engine import Player1, Player2, Character, DilRefine
import win32com.client
import reputation
import threading
import cv2 as cv
import pyautogui
import win32api
import win32con
import win32gui
import engine
import time
import os


def screenshot():
    global liveImage
    print("[i] Taking Screenshot.")
    liveSC = pyautogui.screenshot()
    liveSC.save(liveImage)
    print("[i] Screenshot Saved.")


def fore_window():
    top_windows = []
    results = []

    # Enumerate opened OS windows
    win32gui.EnumWindows(window_enumeration_handler, top_windows)

    # Switch to STO Window
    for i in top_windows:
        if "star trek online" in f"{i[1]}".lower():
            print("[i]Switching to STO...")
            win32gui.ShowWindow(i[0], 5)
            win32gui.SetForegroundWindow(i[0])
            break

    time.sleep(0.8)


def window_enumeration_handler(hwnd, top_windows):
    # Add windows to list
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))


# For Debugging
def show_mouse_pos():
    while True:
        print(pyautogui.position())


def main(time_slept, characters):
    player_changes = 0
    while True:
        # Capture Initial Screenshot
        fore_window()
        screenshot()

        for character in range(1, characters + 1):
            # Start automation
            Controller(character).characterAutomation()

            # Change Characters
            Controller(character).change_player()
            player_changes += 1

            # Start sleeper if each player had an automation round.
            if player_changes >= characters:
                # Start Sleeper
                time_slept = Controller(character).sleeper()
                print("\n[i]Sleeper finished.")
                print(f"[i]Time Slept: {time_slept}")
                player_changes = 0


if __name__ == "__main__":
    time_slept = 0
    pause = 0.5
    dur = 0.2
    log = f"c:\\Users\\{os.getlogin()}\\Documents\\STO-Log.log"
    liveImage = r'G:\School\Python - Homework\Projects\STO-Automation\live_sc.jpg'
    logged_out = r'G:\School\Python - Homework\Projects\STO-Automation\logged_out.JPG'

    # Show Mouse Position for Debugging
    global_thread = threading.Thread(target=show_mouse_pos, name="Global Conf")
    # global_thread.daemon = True
    # global_thread.start()

    # Start main loop
    main(time_slept, characters=2)
