from engine import CharAutomation, Character, DilRefine
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


class Controller:
    def __init__(self):
        self.top_windows = []
        self.results = []
        self.change_time = 0
        self.confirm_x, self.confirm_y = 955, 640
        self.menu_x, self.menu_y = 1905, 150
        self.player1_round = 0
        self.player2_round = 0
        self.player2_time = 0
        self.dur = 0.2
        self.pause = 0.5
        self.liveImage = 'live_sc.jpg'
        self.logged_out = 'logged_out.JPG'

    def player_automation(self, player):
        # Open Reputation Window
        print(f"[i] Player #{player}: Opening Reputation Window")
        keyboard.press_and_release("[")
        time.sleep(self.pause)

        # Start Reputation Automation
        print(f"[i] Player #{player}: Starting automation for Player 1")

        # Init Mouse Position
        pyautogui.moveTo(100, 100, duration=self.dur)
        time.sleep(self.pause)

        # Running Reputation automation
        print(f"[i] Player #{player}: Running Reputation automation.")
        CharAutomation(player).act_reputation()
        time.sleep(self.pause)

        # Close Reputation Window
        print(f"[i] Player #{player}: Reputation Window")
        keyboard.press_and_release('[')
        time.sleep(self.pause)

        # Open DutyOfficers/Admiralty Window
        print(f"[i] Player #{player}: Opening Admiralty Window")
        keyboard.press_and_release("]")
        time.sleep(self.pause)

        # Start Admiralty Automation
        print(f"[i] Player #{player}: Running Admiralty automation.")
        # CharAutomation().act_admiralty()
        print(f"[i] Player #{player}: Admiralty automation completed.")
        time.sleep(self.pause)

        # Start Duty Officers Automation
        print(f"[i] Player #{player}: Starting DutyOfficers automation.")
        CharAutomation(player).act_dutyofficers()
        time.sleep(self.pause)
        print(f"[i] Player #{player}: DutyOfficers automation completed.")

        # Start DutyOfficers Mission Assignments
        print(f"[i] Player #{player}: Running DuFF missions.")
        CharAutomation(player).duff_missions()
        time.sleep(self.pause)

        # Close Admiralty/DutyOfficers Window
        print(f"[i] Player #{player}: Closing DutyOfficers/Admiralty Window")
        keyboard.press_and_release("]")
        time.sleep(self.pause)

        # Start Refining Automation
        print(f"[i] Player #{player}: Running Refining automation.")

        # Open Refining Window
        print(f"[i] Player #{player}: Opening Refining Window")
        keyboard.press_and_release("i")
        time.sleep(self.pause)

        # Run Automation
        print(f"[i] Player #{player}: Running Refining Automation")
        DilRefine(player).act()
        time.sleep(self.pause)

        # Close Refining window
        print(f"[i] Player #{player}: Closing Refining Window")
        keyboard.press_and_release("i")
        print(f"[i] Player #{player}: Finished Refining automation.")
        time.sleep(self.pause)

    def change_player(self, player):
        change_start = time.time()

        # Change Character
        print(f"[i] Player #{player}: Changing character...")

        # Open Main Menu
        print(f"[i] Player #{player}: Opening Main Menu")
        pyautogui.moveTo(self.menu_x, self.menu_y, duration=self.dur)
        time.sleep(self.pause)
        print(f"[i] Player #{player}: Clicking on Menu")
        click(self.menu_x, self.menu_y)
        time.sleep(self.pause)
        Character(player).act()
        time.sleep(self.pause)
        print(f"[i] Player #{player}: Finished Character change.")

        change_end = time.time()
        self.change_time = change_end - change_start

        return

    def sleeper(self):
        # sleeptime = random.randint(300, 720)    # Between 5 and 12 minutes.
        sleeptime = random.randint(5, 10)
        print(f"[i] Sleeper set for {sleeptime} seconds.")
        for x in range(sleeptime, 0, -1):
            sys.stdout.write("\r[i]Sleeping for " + str(x) + " seconds...")
            time.sleep(1)

        # Capture Screenshot
        self.main_window()

        # Compare screenshots and verify the connection to the server.
        if not ComputerVision(cv.imread(self.liveImage, cv.IMREAD_UNCHANGED),
                              cv.imread(self.logged_out, cv.IMREAD_UNCHANGED),
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

    def main_window(self):
        # Switch to STO Window
        for i in self.top_windows:
            if "star trek online" in f"{i[1]}".lower():
                print("[i]Switching to STO...")
                win32gui.ShowWindow(i[0], 5)
                win32gui.SetForegroundWindow(i[0])
                print("[i] Taking Screenshot.")
                liveSC = pyautogui.screenshot()
                liveSC.save(self.liveImage)
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
