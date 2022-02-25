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
    def __init__(self, log, resultsLog):
        self.assignments = ["Engineering", "Science", "Tactical", "Security", "Medical"]
        self.resultsLog = resultsLog    # A File that will store only the final summarization for each round.
        self.logger = log               # Log file.
        self.pause = 0.5                # Pause between actions.
        self.dur = 0.2                  # Mouse movement duration.
        self.playerChanges = 0          # Number of player changes made.
        self.rounds = 1                 # Number of Total Rounds.

        self.topTotals = {}             # Will store Rewards and Assignments for each character.
        self.topAssignments = {}        # Will store each character's collected/planned missions.
        self.totalsList = []            # Will store a list of all missions assigned to all characters.
        self.totalRounds = {}           # Will store the round number and all missions assigned/collected.
        self.totalSleep = 0             # Total sleep time for all rounds.

        self.rewards = []               # Total rewards for each character.
        self.personalAss = []           # Will store all Personal Assignments.
        self.tempAssignments = []       # Will store temporary departments for each character.
        self.engineeringAss = []        # Will store all Engineering Assignments.
        self.scienceAss = []            # Will store all Science Assignments.
        self.tacticalAss = []           # Will store all Tactical Assignments.
        self.securityAss = []           # Will store all Security Assignments.
        self.medicalAss = []            # Will store all Medical Assignments.

    def check_process(self, task):
        crashes = 0     # Number of times the game process was not found.
        quickLaunch_x, quickLaunch_y = 155, 445     # Epic Games STO Quick Launch Button
        engage_x, engage_y = 1255, 700              # Launcher Engage Button

        # Check if game is running and restart if not.
        proc = subprocess.check_output('tasklist', shell=True)
        if str(task) in str(proc):
            logIt(self.logger, debug=True, msg=f'Game is running')

            return

        if crashes == 3:
            logIt(self.logger, debug=True, msg=f'Game crashed 3 times. stopping script.')
            exit()

        logIt(self.logger, debug=True, msg=f'Game is not running. restarting.')
        logIt(self.logger, debug=True, msg=f'Starting Epic Games Launcher...')
        subprocess.run(
            r'c:/Program Files (x86)/Epic Games/Launcher/Portal/Binaries/Win32/EpicGamesLauncher.exe')
        timer(30)

        logIt(self.logger, debug=True, msg=f'Clicking on Quick Launch')
        pyautogui.moveTo(quickLaunch_x, quickLaunch_y, duration=0.3)
        time.sleep(1)
        click(quickLaunch_x, quickLaunch_y)
        time.sleep(30)
        logIt(self.logger, debug=True, msg=f'Clicking on Engage')
        pyautogui.moveTo(engage_x, engage_y, duration=0.3)
        click(engage_x, engage_y)
        timer(120)
        logIt(self.logger, debug=True, msg=f'Moving character scroller...')
        self.pA.moveCharScroller()
        logIt(self.logger, debug=True, msg=f'Choose last character')
        self.pA.choose()
        timer(10)
        logIt(self.logger, debug=True, msg=f'Clicking on Play')
        self.pA.play()
        timer(60)
        logIt(self.logger, debug=True, msg=f'Closing Welcome Window')
        self.pA.closeChar()
        time.sleep(3)

        crashes += 1

        return

    def duff(self, player):
        # Start Duty Officers Automation
        logIt(self.logger, debug=True, msg=f'Player #{player}: Initializing mouse position')
        self.pA.init_automation()
        logIt(self.logger, debug=True, msg=f'Player #{player}: Opening Duty Officers Window')
        self.pA.duffWindow()
        logIt(self.logger, debug=True, msg=f'Player #{player}: Clicking on Duty Officers Folder')
        self.pA.duffFolder()
        logIt(self.logger, debug=True, msg=f'Player #{player}: Clicking on Completed')
        self.pA.completed()
        logIt(self.logger, debug=True, msg=f'Player #{player}: Taking Screenshot')
        self.pA.main_window()
        logIt(self.logger, debug=True, msg=f'Player #{player}: Collecting Rewards...')
        self.pA.collect()
        logIt(self.logger, debug=True, msg=f'Player #{player}: Clicking on Personal')
        self.pA.personal()
        logIt(self.logger, debug=True, msg=f'Player #{player}: Clicking on Filters')
        self.pA.filters()

        logIt(self.logger, debug=True, msg=f'Player #{player}: Detecting Scroller...')
        personalBox = pyautogui.locateOnScreen(planButton, grayscale=True, confidence=.8)
        try:
            if len(personalBox):
                logIt(self.logger, debug=True, msg=f'Player #{player}: Moving Mission scroller')
                self.pA.scroller()

        except TypeError:
            logIt(self.logger, debug=True, msg=f'Player #{player}: No Personal Missions Found')

        logIt(self.logger, debug=True, msg=f'Player #{player}: Planning Personal missions...')
        self.pA.plan(department='Personal')
        logIt(self.logger, debug=True, msg=f'Player #{player}: Clicking on Department Heads')
        self.pA.back()

        for i in range(len(self.assignments)):
            logIt(self.logger, debug=True, msg=f'Player #{player}: Selecting department...')
            department = random.choice(self.assignments)
            logIt(self.logger, debug=True, msg=f'Player #{player}: Department selected: {department}')
            if department not in self.tempAssignments:
                self.tempAssignments.append(department)
                logIt(self.logger, write=False, debug=True, msg=f'DEBUG Temp Assignments: {self.tempAssignments}')

                if department == "Engineering":
                    logIt(self.logger, debug=True, msg=f'Player #{player}: Planning Engineering Missions...')
                    self.pA.engineering()
                    self.pA.plan(department='Engineering')
                    self.pA.back()

                elif department == "Science":
                    logIt(self.logger, debug=True, msg=f'Player #{player}: Planning Science Missions...')
                    self.pA.science()
                    self.pA.plan(department='Science')
                    self.pA.back()

                elif department == "Tactical":
                    logIt(self.logger, debug=True, msg=f'Player #{player}: Planning Tactical Missions...')
                    self.pA.tactical()
                    self.pA.plan(department='Tactical')
                    self.pA.back()

                elif department == "Security":
                    logIt(self.logger, debug=True, msg=f'Player #{player}: Planning Security Missions...')
                    self.pA.security()
                    self.pA.plan(department='Security')
                    self.pA.back()

                elif department == "Medical":
                    logIt(self.logger, debug=True, msg=f'Player #{player}: Planning Medical Missions...')
                    self.pA.medical()
                    self.pA.plan(department='Medical')
                    self.pA.back()

        logIt(self.logger, debug=True, msg=f'Player #{player}: Closing Duty Officers window')
        self.pA.closeDuff()

        return

    def change_character(self, player):
        # Change Characters
        logIt(self.logger, debug=True, msg=f'Changing Character')
        logIt(self.logger, debug=True, msg=f'Clicking on Menu')
        self.pA.menu()
        logIt(self.logger, debug=True, msg=f'Clicking on Change Character')
        self.pA.change()
        logIt(self.logger, debug=True, msg=f'Clicking on Confirm')
        self.pA.confirm()
        timer(10)       # Wait for the game to load the characters screen
        logIt(self.logger, debug=True, msg=f'Moving Characters scroller')
        self.pA.moveCharScroller()
        logIt(self.logger, debug=True, msg=f'Clicking on Last Character')
        self.pA.choose()
        timer(30)       # Wait for the game to load the character's team screen
        logIt(self.logger, debug=True, msg=f'Checking if the game is running...')
        self.check_process('GameClient.exe')
        logIt(self.logger, debug=True, msg=f'Clicking on Play')
        self.pA.play()
        timer(10)
        # timer(120)      # Wait for the game to load the character
        logIt(self.logger, debug=True, msg=f'Closing Welcome Window')
        self.pA.closeChar()

        return

    def main(self, characters):
        for character in range(1, characters + 1):
            # Set sleep time
            # sleeptime = random.randint(300, 720)  # Between 5 and 12 minutes.
            sleeptime = random.randint(5, 10)

            # Initialize Controller
            self.pA = Controller(self.logger, character, self.topTotals, self.totalsList, self.topAssignments,
                                 self.rewards, self.personalAss, self.engineeringAss,
                                 self.scienceAss, self.tacticalAss, self.securityAss, self.medicalAss, sleeptime)

            # Start Duff Section
            logIt(self.logger, debug=True, msg=f'Starting automation round: '
                                               f'{self.rounds} for player {character}...')
            self.duff(character)
            logIt(self.logger, debug=True, msg=f'Player #{character}: DutyOfficers automation completed.')
            self.topTotals = {f'Player #{character}': self.topAssignments}
            self.totalRounds[f'Round #{self.rounds}'] = self.topTotals
            self.totalsList.append([self.topTotals])
            logIt(self.logger, msg=f'\n========= Totals for Player #{character}: '
                                   f'{self.topTotals}=========\n')

            logIt(self.logger, debug=True, msg=f'Resetting lists')
            self.topTotals = {}
            self.topAssignments = {}
            self.tempAssignments = []

            # Change Character
            logIt(self.logger, debug=True, msg=f'Starting Character change automation')
            self.change_character(character)
            logIt(self.logger, debug=True, msg=f'Character change automation completed')
            self.playerChanges += 1

            # Check if game is running
            logIt(self.logger, debug=True, msg=f'Checking if the game is running...')
            self.check_process('GameClient.exe')

            # Start sleeper if each player had an automation round.
            if self.playerChanges >= characters:
                logIt(self.logger, msg=f'**** {self.topTotals} ****')
                with open(self.resultsLog, 'a') as sumlog:
                    print(f"Total Rounds: {self.totalRounds}")
                    logIt(self.logger, debug=True, msg=f'Updating results log...')
                    sumlog.write(f"===============================================\n" 
                                 f"{datetime.today().replace(microsecond=0)}\n"
                                 f"#### Summarization ####\n"
                                 f"* Rounds: {self.rounds}\n"
                                 f"* Rewards: {sum(self.rewards)} collected.\n"
                                 f"* Personal: {sum(self.personalAss)}.\n"
                                 f"* Engineering: {sum(self.engineeringAss)}.\n"
                                 f"* Science: {sum(self.scienceAss)}.\n"
                                 f"* Tactical: {sum(self.tacticalAss)}.\n"
                                 f"* Security: {sum(self.securityAss)}.\n"
                                 f"* Medical: {sum(self.medicalAss)}.\n\n"

                                 f"#### Detailed ####\n"
                                 f"* Total time slept: {self.totalSleep} seconds.\n")

                    for k, v in self.totalRounds.items():
                        sumlog.write(f"{k}: {v}\n")

                    sumlog.write("===============================================\n\n\n")
                    logIt(self.logger, debug=True, msg=f'Results log updated.')

                self.totalsList = []
                logIt(self.logger, msg=f'Rounds: {self.rounds}')

                # Check if game is running
                logIt(self.logger, debug=True, msg=f'Checking if the game is running...')
                self.check_process('GameClient.exe')

                # Start Sleeper
                logIt(self.logger, debug=True, msg=f'Starting Sleeper')
                self.pA.sleeper()
                logIt(self.logger, debug=True, msg=f'Sleeper finished')
                logIt(self.logger, debug=True, msg=f'Time Slept: {sleeptime}')

                # Updating Total Sleeptime
                self.totalSleep += sleeptime

                # Update Counters
                logIt(self.logger, debug=True, msg=f'Updating Counters')
                self.playerChanges = 0
                self.rounds += 1


def logIt(logfile, write=True, debug=False, msg=''):
    if debug:
        print(f"{datetime.today().replace(microsecond=0)}: {msg}")

    if not write:
        return

    with open(logfile, 'a') as lf:
        lf.write(f"{datetime.today().replace(microsecond=0)}: {msg}\n")


def timer(t):
    for x in range(t, 0, -1):
        sys.stdout.write(f"\rWaiting for {str(x)} seconds...")
        time.sleep(1)

    return print("\n")


def fore_window():
    top_windows = []
    results = []

    # Enumerate opened OS windows
    win32gui.EnumWindows(window_enumeration_handler, top_windows)

    # Switch to STO Window
    for i in top_windows:
        if "star trek online" in f"{i[1]}".lower():
            logIt(log, write=False, debug=True, msg=f'Switching to STO...')
            win32gui.ShowWindow(i[0], 5)
            win32gui.SetForegroundWindow(i[0])
            logIt(log, write=False, debug=True, msg=f'Taking Screenshot')
            liveSC = pyautogui.screenshot()
            liveSC.save(liveImage)
            logIt(log, write=False, debug=True, msg=f'Screenshot Saved')
            break

    time.sleep(0.8)


def window_enumeration_handler(hwnd, top_windows):
    # Add windows to list
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))


# For Debugging
def show_mouse_pos():
    while True:
        print(pyautogui.position())


def check_connection(address):
    print(f"checking connection to {address}...")
    response = os.system(f"ping -c 1 {address}")

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
    resultLog = f"c:\\Users\\{os.getlogin()}\\Documents\\STO-Results.log"

    display = False
    charas = 9

    parse = argparse.ArgumentParser()
    parse.add_argument("-d", "--display", help="Display and Record", required=False, action='store_true')
    parse.add_argument("-c", "--chars", type=int, help="Sleep every (num) of characters", required=False, default=8)
    args = parse.parse_args()
    if args.display:
        display = True

    if 1 <= args.chars <= charas:
        charas = args.chars

    elif int(args.chars) > charas:
        print("Error, max is 8.\n")
        quit()

    elif type(args.chars) != int:
        print("Only Numbers")
        quit()

    else:
        print(f"Running default {charas} characters...")

    top_windows = []
    results = []

    # Show Mouse Position for Debugging
    global_thread = threading.Thread(target=show_mouse_pos, name="Global Conf")
    # global_thread.daemon = True
    # global_thread.start()

    # Bring Game screen to front and take a screenshot.
    fore_window()

    # Initialize Game Class
    game = Game(log, resultLog)
    game.check_process("GameClient.exe")

    while True:
        if display:
            startThread = threading.Thread(target=game.main, args=(charas,), name="Main Thread")
            startThread.daemon = True
            startThread.start()

            # Display and Record screen capture
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
