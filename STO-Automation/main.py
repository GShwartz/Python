from controllerC import Controller
from datetime import datetime
from PIL import ImageGrab
import numpy as np
import subprocess
import threading
import pyautogui
import keyboard
import win32gui
import win32api
import win32con
import argparse
import random
import time
import cv2
import sys
import os


class Game:
    def __init__(self, log, sleep):
        self.sleep = sleep
        self.logger = log
        self.pause = 0.5
        self.dur = 0.2
        self.playerChanges = 0
        self.rounds = 0

        self.topTotals = {}
        self.topAssignments = {}
        self.totalsList = []
        self.totalRounds = {}

        self.rewards = []
        self.personalAss = []
        self.assignments = ["Engineering", "Science", "Tactical", "Security", "Medical"]
        self.tempAssignments = []
        self.engineeringAss = []
        self.scienceAss = []
        self.tacticalAss = []
        self.securityAss = []
        self.medicalAss = []

    def check_process(self, task):
        quickLaunch_x, quickLaunch_y = 155, 445
        engage_x, engage_y = 1255, 700

        # Check if game is running and restart if not.
        proc = subprocess.check_output('tasklist', shell=True)
        if str(task) in str(proc):
            print("Game is running.")

            return

        print("Game is not running. restarting...")
        subprocess.run(
            r'c:/Program Files (x86)/Epic Games/Launcher/Portal/Binaries/Win32/EpicGamesLauncher.exe')
        time.sleep(30)
        pyautogui.moveTo(quickLaunch_x, quickLaunch_y, duration=0.3)
        time.sleep(1)
        click(quickLaunch_x, quickLaunch_y)
        time.sleep(30)
        pyautogui.moveTo(engage_x, engage_y, duration=0.3)
        click(engage_x, engage_y)
        timer(120)
        self.pA.moveCharScroller()
        self.pA.choose()
        time.sleep(6)
        self.pA.play()
        timer(60)
        self.pA.closeChar()

        return

    def main(self, characters):
        while True:
            # Capture Initial Screenshot
            self.logger.write(f"{datetime.today().replace(microsecond=0)}: Taking Screenshot\n")
            for character in range(1, characters + 1):
                # Start automation
                self.pA = Controller(self.logger, character, self.topTotals, self.totalsList, self.topAssignments,
                                     self.rewards, self.personalAss, self.engineeringAss,
                                     self.scienceAss, self.tacticalAss, self.securityAss, self.medicalAss, self.sleep)

                # Set Round Number
                if self.rounds == 0:
                    self.totalRounds[f'Round {self.rounds + 1}'] = self.topTotals
                    print(f"Starting automation round: {self.rounds + 1} for player {character}...")
                    self.logger.write(f"{datetime.today().replace(microsecond=0)}: "
                                      f"Starting automation round: {self.rounds + 1} for player {character}...\n")

                # Check if Game is running
                self.check_process('GameClient.exe')

                # Start Duty Officers Automation
                print(f"[i] Player #{character}: Starting DutyOfficers automation.")
                self.pA.player_automation()
                self.pA.duffWindow()
                self.pA.duffFolder()
                self.pA.completed()
                self.pA.main_window()
                self.pA.collect()
                self.pA.personal()
                self.pA.filters()

                personalBox = pyautogui.locateOnScreen(planButton, grayscale=True, confidence=.8)
                try:
                    if len(personalBox):
                        self.pA.scroller()

                except TypeError:
                    print("No Personal Missions Found.")

                # pA.scroller()
                self.pA.plan(department='Personal')
                self.pA.back()

                for i in range(len(self.assignments)):
                    self.check_process('GameClient.exe')
                    department = random.choice(self.assignments)
                    print(f"Debug ASSIGNMENTS: Department: {department} | Assignment #{i + 1}")
                    if department not in self.tempAssignments:
                        self.tempAssignments.append(department)
                        print(f"DEBUG Temp Assignments: {self.tempAssignments}")

                        if department == "Engineering":
                            self.pA.engineering()
                            self.pA.plan(department='Engineering')
                            self.pA.back()

                        elif department == "Science":
                            self.pA.science()
                            self.pA.plan(department='Science')
                            self.pA.back()

                        elif department == "Tactical":
                            self.pA.tactical()
                            self.pA.plan(department='Tactical')
                            self.pA.back()

                        elif department == "Security":
                            self.pA.security()
                            self.pA.plan(department='Security')
                            self.pA.back()

                        elif department == "Medical":
                            self.pA.medical()
                            self.pA.plan(department='Medical')
                            self.pA.back()

                self.pA.closeDuff()

                self.topTotals = {f'Player {character}': self.topAssignments}
                self.totalsList.append(self.topTotals)
                self.logger.write(f"{datetime.today().replace(microsecond=0)}: "
                                  f"\n============= Totals for Player {character}: "
                                  f"{self.topTotals}\n=============\n")

                self.topTotals = {}
                self.topAssignments = {}
                self.tempAssignments = []

                # print(f"Top Totals Dict: {self.topTotals}")
                # print(f"Top Totals List: {self.totalsList}")
                # print(f"Temp Assignment List: {self.tempAssignments}")
                # time.sleep(10)  # For DEBUG

                print(f"[i] Player #{character}: DutyOfficers automation completed.")

                # Change Characters
                self.logger.write(f"{datetime.today().replace(microsecond=0)}: Changing Character\n")
                self.pA.change_player()
                self.pA.change()
                self.pA.confirm()
                time.sleep(5)
                self.pA.moveCharScroller()
                self.pA.choose()
                time.sleep(6)
                self.check_process('GameClient.exe')
                self.pA.play()
                timer(60)
                self.pA.closeChar()

                print(f"[i] Player #{character}: Finished Character change.")
                self.playerChanges += 1

                # Start sleeper if each player had an automation round.
                if self.playerChanges >= characters:
                    self.logger.write(f"{datetime.today().replace(microsecond=0)}: Player #{character}: "
                                      f"**** {self.totalsList} ****\n")
                    self.logger.write(f"{datetime.today().replace(microsecond=0)}:\n"
                                      f"#### Total Missions planned ####\n"
                                      f"Rewards: {sum(self.rewards)} collected.\n"
                                      f"Personal: {sum(self.personalAss)}.\n"
                                      f"Engineering: {sum(self.engineeringAss)}.\n"
                                      f"Science: {sum(self.scienceAss)}.\n"
                                      f"Tactical: {sum(self.tacticalAss)}.\n"
                                      f"Security: {sum(self.securityAss)}.\n"
                                      f"Medical: {sum(self.medicalAss)}.\n"
                                      f"####\n")

                    self.totalRounds[f"Round {self.rounds}"] = self.totalsList
                    print(f"Total Rounds: {self.totalRounds}")
                    self.totalsList = []
                    self.logger.write(f"{datetime.today().replace(microsecond=0)}:\nRounds: {self.totalRounds}\n")

                    self.check_process('GameClient.exe')

                    # Start Sleeper
                    self.pA.sleeper()
                    self.logger.write(f"{datetime.today().replace(microsecond=0)}: Starting Sleeper\n\n")
                    print("[i]Sleeper finished.")
                    print(f"[i]Time Slept: {self.time_slept}")

                    # Update Counters
                    self.playerChanges = 0
                    self.rounds += 1


def timer(t):
    for x in range(t, 0, -1):
        sys.stdout.write(f"\rWaiting for {str(x)} seconds...")
        time.sleep(1)

    return


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
            liveSC = pyautogui.screenshot()
            liveSC.save(liveImage)
            print(f"Screenshot Saved to: \n{liveImage}")
            break

    time.sleep(0.8)


def window_enumeration_handler(hwnd, top_windows):
    # Add windows to list
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))


# For Debugging
def show_mouse_pos():
    while True:
        print(pyautogui.position())


def check_connection():
    host = '208.95.184.200'
    print(f"checking connection to {host}...")
    response = os.system(f"ping -c 1 {host}")

    return response


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    liveImage = 'Images/Anchors/live_sc.jpg'
    planButton = 'Images/Anchors/planButton.JPG'
    log = f"c:\\Users\\{os.getlogin()}\\Documents\\STO-Log.log"
    # sleeptime = random.randint(300, 720)  # Between 5 and 12 minutes.
    sleeptime = random.randint(5, 10)

    display = False
    charas = 8

    parse = argparse.ArgumentParser()
    parse.add_argument("-d", "--display", help="Display and Record", required=False, action='store_true')
    parse.add_argument("-c", "--chars", type=int, help="Number of characters", required=False, default=8)
    args = parse.parse_args()
    if args.display:
        display = True

    if 1 <= args.chars < 8:
        charas = args.chars

    elif int(args.chars) > 8:
        print("Error, max is 8.\n")
        quit()

    elif type(args.chars) != int:
        print("Only Numbers")
        quit()

    else:
        charas = 8

    top_windows = []
    results = []

    # Show Mouse Position for Debugging
    global_thread = threading.Thread(target=show_mouse_pos, name="Global Conf")
    # global_thread.daemon = True
    # global_thread.start()

    fore_window()
    # Start main loop
    with open(log, 'a') as logger:
        logger.write(f"{datetime.today().replace(microsecond=0)}: Starting Main\n")
        game = Game(logger, sleeptime)

        if display:
            startThread = threading.Thread(target=game.main, args=(charas,), name="Main Thread")
            startThread.daemon = True
            startThread.start()

            while True:
                pyautogui.FAILSAFE = False
                imgScreen = np.array(ImageGrab.grab(bbox=(0, 0, 1920, 1080)))
                # frame = cv2.cvtColor(imgScreen, cv2.COLOR_BGR2GRAY)
                frame = cv2.cvtColor(imgScreen, cv2.COLOR_BGR2RGB)
                width = 1280
                height = 1024
                dim = (width, height)
                resized = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

                cv2.imshow('LIVE', frame)
                if cv2.waitKey(1) == ord('q'):
                    cv2.destroyAllWindows()

        start = game.main(characters=int(charas))
