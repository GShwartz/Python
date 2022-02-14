import cv2
import numpy as np
from datetime import datetime
from PIL import ImageGrab
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
import time
import sys
import os
from collections import defaultdict


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
personal_x, personal_y = 70, 130
filters_x, filters_y = 718, 50
metReqs_x, metReqs_y = 700, 98
department_x, department_y = 90, 165
engineering_x, engineering_y = 485, 375
operations_x, operations_y = 835, 375
science_x, science_y = 485, 480
medial_x, medical_y = 835, 480
tactical_x, tactical_y = 475, 585
security_x, security_y = 830, 585
plan_x, plan_y = 800, 260
begin_x, begin_y = 800, 1025
duff_folder_x, duff_folder_y = 410, 20
completed_x, completed_y = 85, 235
duff_1_x, duff_1_y = random.randint(790, 799), random.randint(182, 187)
duffTopScroller_x, duffTopScroller_y = 878, 405
duffBottomScroller_x, duffBottomScroller_y = 878, 570
duff_pause = 1.5

# Change Character vars
changeScrollerTop_x, changeScrollerTop_y = 478, 285
changeScrollerBottom_x, changeScrollerBottom_y = 478, 370
changeButton_x, changeButton_y = 540, 385
changeConfirm_x, changeConfirm_y = 955, 570
lastChar_x, lastChar_y = 230, 810
play_x, play_y = 425, 875


class Controller:
    def __init__(self, logger, player, topTotals, totalsList, topAssignments,
                 rewards, personal, engineering,
                 science, tactical, security, medical):

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

    def player_automation(self):
        self.logger.write(f"{datetime.today().replace(microsecond=0)}: Automating Character #{self.player}\n")

        # Init Mouse Position
        pyautogui.moveTo(120, 100, duration=dur)
        time.sleep(pause)

    def duffWindow(self):
        # Open DutyOfficers/Admiralty Window
        self.logger.write(f"{datetime.today().replace(microsecond=0)}: Player #{self.player}: Opening Duff Window\n")
        print(f"[i] Player #{self.player}: Opening Admiralty Window")
        keyboard.press_and_release("]")
        time.sleep(pause)

        return

    def duffFolder(self):
        self.logger.write(
            f"{datetime.today().replace(microsecond=0)}: Player #{self.player}: Clicking on Duff Ticket\n")
        print(f"Player {self.player}: Clicking on Duff Ticket")
        pyautogui.moveTo(duff_folder_x, duff_folder_y)
        time.sleep(pause)
        click(duff_folder_x, duff_folder_y)
        time.sleep(pause)

        return

    def completed(self):
        # Open Completed Window
        pyautogui.moveTo(completed_x, completed_y, duration=dur)
        time.sleep(pause)
        self.logger.write(f"{datetime.today().replace(microsecond=0)}: Player #{self.player}: Clicking on Complete\n")
        print(f"[i]Player {self.player}: Clicking on Completed")
        click(completed_x, completed_y)
        time.sleep(pause)

        return

    def collect(self):
        # Collect Rewards
        pyautogui.moveTo(duff_1_x, duff_1_y, duration=dur)
        time.sleep(pause)
        for i in range(1, 23):
            boxCollect = pyautogui.locateOnScreen(collect, grayscale=True, confidence=.7)
            try:
                if len(boxCollect):
                    print("Found Missions.")
                    print(f"[i]Player {self.player}: Collecting reward #{i}...")
                    click(random.randint(790, 799), random.randint(182, 187))
                    time.sleep(0.4)
                    print(f"[i]Player {self.player}: reward #{i} collected.")
                    self.logger.write(f"{datetime.today().replace(microsecond=0)}: Player #{self.player}: "
                                      f"Collected reward #{i}\n")
                    self.rewardCollect += 1

            except TypeError:
                print("No Missions Found.")
                self.topAssignments['Rewards'] = self.rewardCollect
                break

        self.rewards.append(self.rewardCollect)
        print(f"Rewards Collected: {self.rewardCollect}")
        self.logger.write(f"{datetime.today().replace(microsecond=0)}: Player #{self.player}: "
                          f"Rewards collected:{self.rewardCollect}\n")

        return

    def personal(self):
        # Click on Personal
        pyautogui.moveTo(personal_x, personal_y, duration=dur)
        time.sleep(pause)
        self.logger.write(f"{datetime.today().replace(microsecond=0)}: Player #{self.player}: Clicking on Personal\n")
        print(f"[i]Player {self.player}: Clicking on Personal")
        click(personal_x, personal_y)
        time.sleep(duff_pause)

        return

    def filters(self):
        # Click on Filters
        pyautogui.moveTo(filters_x, filters_y, duration=dur)
        time.sleep(pause)
        self.logger.write(f"{datetime.today().replace(microsecond=0)}: Player #{self.player}: Clicking on Filters\n")
        print(f"[i]Player {self.player}: Clicking on Filters")
        click(filters_x, filters_y)
        time.sleep(duff_pause)

        # Click on Met Reqs
        pyautogui.moveTo(metReqs_x, metReqs_y, duration=dur)
        time.sleep(pause)
        self.logger.write(f"{datetime.today().replace(microsecond=0)}: Player #{self.player}: Clicking on Met Reqs\n")
        print(f"[i]Player {self.player}: Clicking on Met Reqs")
        click(metReqs_x, metReqs_y)
        time.sleep(duff_pause)
        click(metReqs_x, metReqs_y)
        pyautogui.doubleClick(metReqs_x, metReqs_y)
        time.sleep(duff_pause)

        return

    def scroller(self):
        self.logger.write(f"{datetime.today().replace(microsecond=0)}: Player #{self.player}: Moving Scroller\n")
        # Move Scroller up
        pyautogui.moveTo(duffBottomScroller_x, duffBottomScroller_y, duration=dur)
        time.sleep(pause)
        pyautogui.dragTo(duffTopScroller_x, duffTopScroller_y, duration=dur)
        time.sleep(pause)

        return

    def engineering(self):
        # Click on Engineering Assignments
        pyautogui.moveTo(engineering_x, engineering_y, duration=dur)
        time.sleep(pause)
        self.logger.write(
            f"{datetime.today().replace(microsecond=0)}: Player #{self.player}: Clicking on Engineering\n")
        print(f"[i]Player {self.player}: Clicking on Engineering")
        click(engineering_x, engineering_y)
        time.sleep(duff_pause)

        return

    def science(self):
        # Click on Science Assignments
        pyautogui.moveTo(science_x, science_y, duration=dur)
        time.sleep(pause)
        self.logger.write(f"{datetime.today().replace(microsecond=0)}: Player #{self.player}: Clicking on Science\n")
        print(f"[i]Player {self.player}: Clicking on Science Assignment")
        click(science_x, science_y)
        time.sleep(duff_pause)

        return

    def tactical(self):
        # Click on Tactical Assignments
        pyautogui.moveTo(tactical_x, tactical_y, duration=dur)
        time.sleep(pause)
        self.logger.write(f"{datetime.today().replace(microsecond=0)}: Player #{self.player}: Clicking on Tactical\n")
        print(f"[i]Player {self.player}: Clicking on Tactical Assignment")
        click(tactical_x, tactical_y)
        time.sleep(duff_pause)

        return

    def security(self):
        # Click on Security Assignments
        pyautogui.moveTo(security_x, security_y, duration=dur)
        time.sleep(pause)
        self.logger.write(f"{datetime.today().replace(microsecond=0)}: Player #{self.player}: Clicking on Security\n")
        print(f"[i]Player {self.player}: Clicking on Security Assignment")
        click(security_x, security_y)
        time.sleep(duff_pause)

        return

    def medical(self):
        # Click on Medical Assignments
        pyautogui.moveTo(medial_x, medical_y, duration=dur)
        time.sleep(pause)
        self.logger.write(f"{datetime.today().replace(microsecond=0)}: Player #{self.player}: Clicking on Medical\n")
        print(f"[i]Player {self.player}: Clicking on Medical Assignment")
        click(medial_x, medical_y)
        time.sleep(duff_pause)

        return

    def closeDuff(self):
        # Close Admiralty/DutyOfficers Window
        self.logger.write(f"{datetime.today().replace(microsecond=0)}: Player #{self.player}: Closing Duff Window\n")
        print(f"[i] Player #{self.player}: Closing DutyOfficers/Admiralty Window")
        keyboard.press_and_release("]")
        time.sleep(pause)

        return

    def change_player(self):
        self.logger.write(
            f"{datetime.today().replace(microsecond=0)}: ==== Player #{self.player}: Changing Character... ====\n")
        print(f"[i] Player #{self.player}: Changing character...")

        # Open Main Menu
        self.logger.write(f"{datetime.today().replace(microsecond=0)}: Player #{self.player}: Clicking on Menu\n")
        print(f"[i] Player #{self.player}: Opening Main Menu")
        pyautogui.moveTo(menu_x, menu_y, duration=dur)
        time.sleep(pause)
        click(menu_x, menu_y)
        time.sleep(duff_pause)

        return

    def change(self):
        time.sleep(pause)
        # Click on Change Character
        pyautogui.moveTo(changeButton_x, changeButton_y, duration=dur)
        time.sleep(pause)
        self.logger.write(
            f"{datetime.today().replace(microsecond=0)}: Player #{self.player}: Clicking on Change Character\n")
        print(f"[i]Player #{self.player}: Clicking on Change Character")
        click(changeButton_x, changeButton_y)
        time.sleep(1)

        return

    def confirm(self):
        time.sleep(1)
        # Confirm character Change
        pyautogui.moveTo(changeConfirm_x, changeConfirm_y, duration=dur)
        time.sleep(pause)
        self.logger.write(f"{datetime.today().replace(microsecond=0)}: Player #{self.player}: Clicking on Confirm\n")
        print(f"[i]Player #{self.player}: Clicking on Confirm")
        click(changeConfirm_x, changeConfirm_y)
        time.sleep(duff_pause)

        return

    def choose(self):
        # Choose the middle character
        time.sleep(pause)
        pyautogui.moveTo(lastChar_x, lastChar_y, duration=dur)
        time.sleep(pause)
        self.logger.write(
            f"{datetime.today().replace(microsecond=0)}: Player #{self.player}: Clicking on Last Character\n")
        print(f"[i]Player #{self.player}: Clicking on the Last Character")
        click(lastChar_x, lastChar_y)
        time.sleep(duff_pause)

        return

    def play(self):
        # Click the Play button
        pyautogui.moveTo(play_x, play_y, duration=dur)
        time.sleep(pause)
        self.logger.write(f"{datetime.today().replace(microsecond=0)}: Player #{self.player}: Clicking on Play\n")
        print(f"[i]Player #{self.player}: Clicking on Play")
        click(play_x, play_y)
        time.sleep(15)

        return

    def closeChar(self):
        print(f"[i]Player #{self.player}: Closing Welcome Window")
        self.logger.write(
            f"{datetime.today().replace(microsecond=0)}: Player #{self.player}: Closing Welcome Window.\n")
        time.sleep(5)
        keyboard.press_and_release("esc")

    def plan(self, department=None):
        planned = 0

        for i in range(1, 6):
            boxPlan = pyautogui.locateOnScreen(planButton, grayscale=True, confidence=.8)
            try:
                if len(boxPlan):
                    print("Found Missions.")
                    # Plan
                    self.logger.write(
                        f"{datetime.today().replace(microsecond=0)}: Player #{self.player}: Clicking on Plan\n")
                    print(f"[i]Player {self.player}: Clicking on Plan #{i}")
                    pyautogui.moveTo(plan_x, plan_y, duration=dur)
                    time.sleep(pause)
                    click(plan_x, plan_y)
                    time.sleep(pause)

                    # Begin
                    self.logger.write(
                        f"{datetime.today().replace(microsecond=0)}: Player #{self.player}: Clicking on Begin\n")
                    print(f"[i]Player {self.player}: Clicking on Begin Assignment #{i}")
                    pyautogui.moveTo(begin_x, begin_y, duration=dur)
                    time.sleep(pause)
                    click(begin_x, begin_y)
                    time.sleep(duff_pause)

                    planned += 1

            except TypeError:
                print("No Missions Found.")
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
        print(f"DEBUG: UPDATED TOTALS: {self.topTotals}")
        print(f"Planned Assignments for {department}: {planned}")
        self.logger.write(f"{datetime.today().replace(microsecond=0)}: Player #{self.player}: "
                          f"Planned Assignments for {department}: {planned}\n")
        self.logger.write(f"{datetime.today().replace(microsecond=0)}: Player #{self.player}: \n"
                          f"{self.topTotals}\n")

        return

    def back(self):
        # Return to Department Heads
        pyautogui.moveTo(department_x, department_y, duration=dur)
        time.sleep(pause)
        self.logger.write(
            f"{datetime.today().replace(microsecond=0)}: Player #{self.player}: Clicking on Department Heads\n")
        print(f"[i]Player {self.player}: Clicking on Department Heads")
        click(department_x, department_y)
        time.sleep(duff_pause)

        return

    def sleeper(self):
        # sleeptime = random.randint(300, 720)    # Between 5 and 12 minutes.
        sleeptime = random.randint(5, 10)
        print(f"[i] Sleeper set for {sleeptime} seconds.")
        self.logger.write(f"{datetime.today().replace(microsecond=0)}: Sleeper set for {sleeptime} seconds.\n")

        for x in range(sleeptime, 0, -1):
            sys.stdout.write("\r[i]Sleeping for " + str(x) + " seconds...")
            time.sleep(1)

        # Capture Screenshot
        self.main_window()

        # Compare screenshots and verify the connection to the server.
        if not ComputerVision(cv.imread(liveImage, cv.IMREAD_UNCHANGED),
                              cv.imread(logged_out, cv.IMREAD_UNCHANGED),
                              threshold=0.5).compare() and \
                not ComputerVision(cv.imread(liveImage, cv.IMREAD_UNCHANGED),
                                   cv.imread(desktop, cv.IMREAD_UNCHANGED),
                                   threshold=0.5).compare():
            print("Connection is Stable.")

            # Simulate character movement
            print("Simulating Character Look Left")
            keyboard.press('a')
            time.sleep(0.3)
            keyboard.release('a')
            print("Simulating Character Look Right")
            keyboard.press('d')
            time.sleep(0.3)
            keyboard.release('d')

        else:
            print("[!] Disconnected from Server. Stopping Script. [!]")
            quit()

        return sleeptime

    def main_window(self):
        # Switch to STO Window
        for i in self.top_windows:
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


def screenshot():
    global liveImage
    print("[i] Taking Screenshot.")
    liveSC = pyautogui.screenshot()
    liveSC.save(liveImage)
    print("[i] Screenshot Saved.")

    return liveSC


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
