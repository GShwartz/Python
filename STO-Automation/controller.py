from ComputerVision import ComputerVision
from datetime import datetime
from PIL import ImageGrab
import win32com.client
import numpy as np
import reputation
import cv2 as cv
import pyautogui
import keyboard
import win32api
import win32con
import win32gui
import random
import time
import sys
import cv2
import os

menu_x, menu_y = 1905, 150
confirm_x, confirm_y = 955, 640
dur = 0.2
pause = 0.5
liveImage = 'Images/Anchors/live_sc.jpg'
logged_out = 'Images/Anchors/logged_out.JPG'
defaultEmpty = 'Images/Anchors/defaultEmpty.JPG'
defaultAlmostEmpty = 'Images/Anchors/defaultAlmostEmpty.JPG'
planButton = 'Images/Anchors/planButton.JPG'
completed = 'Images/Anchors/completed.JPG'
welcome = 'Images/Anchors/welcome.JPG'
collect = 'Images/Anchors/collect.JPG'
desktop = 'Images/Anchors/desktop.JPG'

# Duty Officers vars
personal_x, personal_y = 95, 125
filters_x, filters_y = 725, 55
metReqs_x, metReqs_y = 700, 102
department_x, department_y = 95, 165
engineering_x, engineering_y = 485, 385
science_x, science_y = 485, 485
tactical_x, tactical_y = 485, 590
security_x, security_y = 830, 590
medial_x, medical_y = 835, 485
plan_x, plan_y = 800, 260
begin_x, begin_y = 800, 1025
duff_folder_x, duff_folder_y = 410, 25
completed_x, completed_y = 95, 230
duffTopScroller_x, duffTopScroller_y = 878, 405
duffBottomScroller_x, duffBottomScroller_y = 878, 590
duff_pause = 1.5

# Change Character vars
changeButton_x, changeButton_y = 540, 385
changeConfirm_x, changeConfirm_y = 955, 570
charTopScroller_x, charTopScroller_y = 478, 375
charBottomScroller_x, charBottomScroller_y = 478, 535
lastChar_x, lastChar_y = 230, 740
play_x, play_y = 425, 875


class Controller:
    def __init__(self, logger, player, topTotals, totalsList, topAssignments,
                 rewards, personal, engineering,
                 science, tactical, security, medical, sleep):

        self.sleep = sleep

        self.top_windows = []
        self.results = []

        self.logger = logger
        self.player = player

        self.departments = ['Personal', 'Engineering', 'Science', 'Tactical', 'Security', 'Medical']
        self.rewardCollect = 0
        self.topTotals = topTotals
        self.totalsList = totalsList
        self.topAssignments = topAssignments
        self.rewards = rewards
        self.personalAss = personal
        self.engineeringAss = engineering
        self.scienceAss = science
        self.tacticalAss = tactical
        self.securityAss = security
        self.medicalAss = medical

    def init_automation(self):
        # Init Mouse Position
        pyautogui.FAILSAFE = False
        pyautogui.moveTo(120, 100, duration=dur)
        pyautogui.FAILSAFE = True
        time.sleep(pause)

    def duffWindow(self):
        # Open DutyOfficers/Admiralty Window
        keyboard.press_and_release("]")
        time.sleep(pause)

        return

    def duffFolder(self):
        time.sleep(pause)
        pyautogui.FAILSAFE = False
        pyautogui.moveTo(duff_folder_x, duff_folder_y, duration=dur)
        pyautogui.FAILSAFE = True
        time.sleep(pause)
        click(duff_folder_x, duff_folder_y)
        time.sleep(pause)

        return

    def completed(self):
        # Open Completed Window
        pyautogui.FAILSAFE = False
        pyautogui.moveTo(completed_x, completed_y, duration=dur)
        pyautogui.FAILSAFE = True
        time.sleep(pause)
        click(completed_x, completed_y)
        time.sleep(pause)

        return

    def collect(self):
        # Collect Rewards
        for i in range(1, 23):
            boxCollect = pyautogui.locateOnScreen(collect, grayscale=True, confidence=.7)
            try:
                if len(boxCollect):
                    duff_1_x, duff_1_y = random.randint(790, 799), random.randint(171, 186)

                    logIt(self.logger, debug=True, msg=f'Player #{self.player}: Found Rewards')
                    pyautogui.FAILSAFE = False
                    pyautogui.moveTo(duff_1_x, duff_1_y, duration=dur)
                    pyautogui.FAILSAFE = True
                    time.sleep(pause)
                    logIt(self.logger, write=False, debug=True,
                          msg=f'Player #{self.player}: Collecting Reward #{i}...')
                    click(duff_1_x, duff_1_y)
                    time.sleep(0.4)
                    logIt(self.logger, write=False, debug=True,
                          msg=f'Player #{self.player}: Collected Reward #{i}.')

                    self.rewardCollect += 1

            except TypeError:
                logIt(self.logger, debug=True, msg=f'Player #{self.player}: No Rewards Found')
                self.topAssignments['Rewards'] = self.rewardCollect
                break

        logIt(self.logger, debug=True, msg=f'Player #{self.player}: Updating rewards list')
        self.rewards.append(self.rewardCollect)
        logIt(self.logger, debug=True, msg=f'Player #{self.player}: Rewards collected: {self.rewardCollect}')

        return

    def personal(self):
        # Click on Personal
        pyautogui.FAILSAFE = False
        pyautogui.moveTo(personal_x, personal_y, duration=dur)
        pyautogui.FAILSAFE = True
        time.sleep(pause)
        click(personal_x, personal_y)
        time.sleep(duff_pause)

        return

    def filters(self):
        # Click on Filters
        pyautogui.FAILSAFE = False
        pyautogui.moveTo(filters_x, filters_y, duration=dur)
        pyautogui.FAILSAFE = True
        time.sleep(pause)
        click(filters_x, filters_y)
        time.sleep(duff_pause)

        # Click on Met Reqs
        pyautogui.moveTo(metReqs_x, metReqs_y, duration=dur)
        time.sleep(pause)
        logIt(self.logger, debug=True, msg=f'Player #{self.player}: Clicking on Met Reqs')
        click(metReqs_x, metReqs_y)
        time.sleep(duff_pause)
        click(metReqs_x, metReqs_y)
        pyautogui.doubleClick(metReqs_x, metReqs_y)
        time.sleep(duff_pause)

        return

    def scroller(self):
        # Move Scroller up
        pyautogui.FAILSAFE = False
        pyautogui.moveTo(duffBottomScroller_x, duffBottomScroller_y, duration=dur)
        pyautogui.FAILSAFE = True
        time.sleep(pause)
        pyautogui.dragTo(duffTopScroller_x, duffTopScroller_y, duration=dur)
        time.sleep(pause)

        return

    def engineering(self):
        # Click on Engineering Assignments
        pyautogui.FAILSAFE = False
        pyautogui.moveTo(engineering_x, engineering_y, duration=dur)
        pyautogui.FAILSAFE = True
        time.sleep(pause)
        click(engineering_x, engineering_y)
        time.sleep(duff_pause)

        return

    def science(self):
        # Click on Science Assignments
        pyautogui.FAILSAFE = False
        pyautogui.moveTo(science_x, science_y, duration=dur)
        pyautogui.FAILSAFE = True
        time.sleep(pause)
        click(science_x, science_y)
        time.sleep(duff_pause)

        return

    def tactical(self):
        # Click on Tactical Assignments
        pyautogui.FAILSAFE = False
        pyautogui.moveTo(tactical_x, tactical_y, duration=dur)
        pyautogui.FAILSAFE = True
        time.sleep(pause)
        click(tactical_x, tactical_y)
        time.sleep(duff_pause)

        return

    def security(self):
        # Click on Security Assignments
        pyautogui.FAILSAFE = False
        pyautogui.moveTo(security_x, security_y, duration=dur)
        pyautogui.FAILSAFE = True
        time.sleep(pause)
        click(security_x, security_y)
        time.sleep(duff_pause)

        return

    def medical(self):
        # Click on Medical Assignments
        pyautogui.FAILSAFE = False
        pyautogui.moveTo(medial_x, medical_y, duration=dur)
        pyautogui.FAILSAFE = True
        time.sleep(pause)
        click(medial_x, medical_y)
        time.sleep(duff_pause)

        return

    def closeDuff(self):
        # Close Admiralty/DutyOfficers Window
        keyboard.press_and_release("]")
        time.sleep(pause)

        return

    def menu(self):
        # Open Main Menu
        pyautogui.FAILSAFE = False
        pyautogui.moveTo(menu_x, menu_y, duration=dur)
        pyautogui.FAILSAFE = True
        time.sleep(pause)
        click(menu_x, menu_y)
        time.sleep(duff_pause)

        return

    def change(self):
        time.sleep(pause)
        # Click on Change Character
        pyautogui.FAILSAFE = False
        pyautogui.moveTo(changeButton_x, changeButton_y, duration=dur)
        pyautogui.FAILSAFE = True
        time.sleep(pause)
        click(changeButton_x, changeButton_y)
        time.sleep(1)

        return

    def confirm(self):
        time.sleep(1)
        # Confirm character Change
        pyautogui.FAILSAFE = False
        pyautogui.moveTo(changeConfirm_x, changeConfirm_y, duration=dur)
        pyautogui.FAILSAFE = True
        time.sleep(pause)
        click(changeConfirm_x, changeConfirm_y)
        time.sleep(duff_pause)

        return

    def moveCharScroller(self):
        time.sleep(pause)
        pyautogui.FAILSAFE = False
        pyautogui.moveTo(charTopScroller_x, charTopScroller_y, duration=dur)
        pyautogui.FAILSAFE = True
        time.sleep(pause)
        pyautogui.FAILSAFE = False
        pyautogui.dragTo(charBottomScroller_x, charBottomScroller_y, duration=dur)
        pyautogui.FAILSAFE = True
        time.sleep(pause)
        click(charBottomScroller_x, charBottomScroller_y)

        return

    def choose(self):
        # Choose the middle character
        time.sleep(pause)
        pyautogui.FAILSAFE = False
        pyautogui.moveTo(lastChar_x, lastChar_y, duration=dur)
        pyautogui.FAILSAFE = True
        time.sleep(pause)
        click(lastChar_x, lastChar_y)
        time.sleep(duff_pause)

        return

    def play(self):
        # Click the Play button
        pyautogui.FAILSAFE = False
        pyautogui.moveTo(play_x, play_y, duration=dur)
        pyautogui.FAILSAFE = True
        time.sleep(pause)
        click(play_x, play_y)

        return

    def closeChar(self):
        time.sleep(pause)
        keyboard.press_and_release("esc")

    def plan(self, department=None):
        planned = 0

        for i in range(1, 6):
            boxPlan = pyautogui.locateOnScreen(planButton, grayscale=True, confidence=.8)
            try:
                if len(boxPlan):
                    logIt(self.logger, debug=True, msg=f'Player #{self.player}: Found Missions')
                    # Plan
                    logIt(self.logger, debug=True, msg=f'Player #{self.player}: Clicking on Plan #{i}')
                    pyautogui.FAILSAFE = False
                    pyautogui.moveTo(plan_x, plan_y, duration=dur)
                    pyautogui.FAILSAFE = True
                    time.sleep(pause)
                    click(plan_x, plan_y)
                    time.sleep(pause)

                    # Begin
                    logIt(self.logger, debug=True, msg=f'Player #{self.player}: Clicking on Begin #{i}')
                    pyautogui.FAILSAFE = False
                    pyautogui.moveTo(begin_x, begin_y, duration=dur)
                    pyautogui.FAILSAFE = True
                    time.sleep(pause)
                    click(begin_x, begin_y)
                    time.sleep(duff_pause)

                    planned += 1

            except TypeError:
                logIt(self.logger, debug=True, msg=f'Player #{self.player}: No Missions Found.')
                break

            if department == 'Personal':
                self.personalAss.append(planned)
                self.topAssignments['Personal'] = self.personalAss[-1]

            elif department == 'Engineering':
                self.engineeringAss.append(planned)
                self.topAssignments['Engineering'] = self.engineeringAss[-1]

            elif department == 'Science':
                self.scienceAss.append(planned)
                self.topAssignments['Science'] = self.scienceAss[-1]

            elif department == 'Tactical':
                self.tacticalAss.append(planned)
                self.topAssignments['Tactical'] = self.tacticalAss[-1]

            elif department == 'Security':
                self.securityAss.append(planned)
                self.topAssignments['Security'] = self.securityAss[-1]

            elif department == 'Medical':
                self.medicalAss.append(planned)
                self.topAssignments['Medical'] = self.medicalAss[-1]

        self.topTotals[f'player {self.player}'] = self.topAssignments
        logIt(self.logger, debug=True, msg=f'Player {self.player}: Planned Assignments for {department}: {planned}')
        logIt(self.logger, debug=True, msg=f'{self.topTotals}')

        return

    def back(self):
        # Return to Department Heads
        pyautogui.FAILSAFE = False
        pyautogui.moveTo(department_x, department_y, duration=dur)
        pyautogui.FAILSAFE = True
        time.sleep(pause)
        click(department_x, department_y)
        time.sleep(duff_pause)

        return

    def sleeper(self):
        # sleeptime = random.randint(300, 720)    # Between 5 and 12 minutes.
        # sleeptime = random.randint(5, 10)
        logIt(self.logger, debug=True, msg=f'Sleeper set for {self.sleep} seconds. ({round(self.sleep / 60)} minutes)')

        for x in range(self.sleep, 0, -1):
            sys.stdout.write("\r[i]Sleeping for " + str(x) + " seconds...")
            time.sleep(1)

        # Capture Screenshot
        logIt(self.logger, debug=True, msg=f'Updating Screenshot')
        self.main_window()

        # Compare screenshots and verify the connection to the server.
        logIt(self.logger, debug=True, msg=f'Initializing Computer Vision Class...')
        logIt(self.logger, debug=True, msg=f'Comparing Screenshot to Logged Out & Desktop')
        visionConn = ComputerVision(cv.imread(liveImage, cv.IMREAD_UNCHANGED),
                                    cv.imread(logged_out, cv.IMREAD_UNCHANGED),
                                    threshold=0.5)
        visionDesktop = ComputerVision(cv.imread(liveImage, cv.IMREAD_UNCHANGED),
                                       cv.imread(desktop, cv.IMREAD_UNCHANGED),
                                       threshold=0.5)

        if not visionConn.compare() and not visionDesktop.compare():
            logIt(self.logger, debug=True, msg=f'Connection Is Stable')

            # Simulate character movement
            logIt(self.logger, debug=True, msg=f'Simulating Character Look Left')
            keyboard.press('a')
            time.sleep(0.3)
            keyboard.release('a')
            logIt(self.logger, debug=True, msg=f'Simulating Character Look Right')
            keyboard.press('d')
            time.sleep(0.3)
            keyboard.release('d')

        else:
            logIt(self.logger, debug=True, msg=f'Disconnected from Server. Stopping Script.')
            quit()

        return self.sleep

    def main_window(self):
        # Switch to STO Window
        for i in self.top_windows:
            if "star trek online" in f"{i[1]}".lower():
                logIt(self.logger, write=False, debug=True, msg=f'Switching to STO...')
                win32gui.ShowWindow(i[0], 5)
                win32gui.SetForegroundWindow(i[0])
                logIt(self.logger, write=False, debug=True, msg=f'Taking Screenshot')
                liveSC = pyautogui.screenshot()
                liveSC.save(liveImage)
                logIt(self.logger, write=False, debug=True, msg=f'Screenshot Saved')


def logIt(logfile, write=True, debug=False, msg=''):
    if debug:
        print(f"{datetime.today().replace(microsecond=0)}: {msg}")

    if write:
        with open(logfile, 'a') as lf:
            lf.write(f"{datetime.today().replace(microsecond=0)}: {msg}\n")


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def window_enumeration_handler(hwnd, top_windows):
    # Add windows to list
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))
