import cv2
import keyboard
import controller
from controller import Controller
import pyautogui
import threading
import win32gui
import time
import os
import numpy as np
from datetime import datetime
from PIL import ImageGrab


class Game:
    def __init__(self, log):
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
        self.engineeringAss = []
        self.scienceAss = []
        self.tacticalAss = []
        self.securityAss = []
        self.medicalAss = []

    def main(self, characters):
        while True:
            # Capture Initial Screenshot
            self.logger.write(f"{datetime.today().replace(microsecond=0)}: Taking Screenshot\n")
            for character in range(1, characters + 1):
                if self.rounds == 0:
                    self.totalRounds[f'Round {self.rounds + 1}'] = self.topTotals
                    print(f"Starting automation round: {self.rounds + 1} for player {character}...")
                    self.logger.write(f"{datetime.today().replace(microsecond=0)}: "
                                      f"Starting automation round: {self.rounds + 1} for player {character}...\n")
                else:
                    self.totalRounds[f'Round {self.rounds}'] = self.topTotals
                    print(f"Starting automation round: {self.rounds} for player {character}...")
                    self.logger.write(f"{datetime.today().replace(microsecond=0)}: "
                                      f"Starting automation round: {self.rounds} for player {character}...\n")

                # Start automation
                pA = Controller(self.logger, character, self.topTotals, self.totalsList, self.topAssignments,
                                self.rewards, self.personalAss, self.engineeringAss,
                                self.scienceAss, self.tacticalAss, self.securityAss, self.medicalAss)

                # Start Duty Officers Automation
                print(f"[i] Player #{character}: Starting DutyOfficers automation.")
                pA.player_automation()
                pA.duffWindow()
                pA.duffFolder()
                pA.completed()
                pA.main_window()
                pA.collect()
                pA.personal()
                pA.filters()
                pA.scroller()
                pA.plan(department='Personal')
                pA.back()
                pA.engineering()
                pA.plan(department='Engineering')
                pA.back()
                pA.science()
                pA.plan(department='Science')
                pA.back()
                pA.tactical()
                pA.plan(department='Tactical')
                pA.back()
                pA.security()
                pA.plan(department='Security')
                pA.back()
                pA.medical()
                pA.plan(department='Medical')
                pA.back()
                pA.closeDuff()

                self.topTotals = {f'Player {character}': self.topAssignments}
                self.totalsList.append(self.topTotals)
                self.logger.write(f"{datetime.today().replace(microsecond=0)}: "
                                  f"\n============= Totals for Player {character}: "
                                  f"{self.topTotals}\n=============\n")
                
                self.topTotals = {}
                self.topAssignments = {}
                print(f"Top Totals Dict: {self.topTotals}")
                print(f"Top Totals List: {self.totalsList}")
                time.sleep(10)  # For DEBUG

                print(f"[i] Player #{character}: DutyOfficers automation completed.")

                # Change Characters
                self.logger.write(f"{datetime.today().replace(microsecond=0)}: Changing Character\n")
                pA.change_player()
                pA.change()
                pA.confirm()
                time.sleep(5)
                pA.choose()
                time.sleep(6)
                pA.play()
                pA.closeChar()

                print(f"[i] Player #{character}: Finished Character change.")
                self.playerChanges += 1

                # Start sleeper if each player had an automation round.
                if self.playerChanges >= characters:
                    self.logger.write(f"{datetime.today().replace(microsecond=0)}: Player #{self.player}: "
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
                    self.totalsList = []
                    # Start Sleeper
                    self.logger.write(f"{datetime.today().replace(microsecond=0)}: Starting Sleeper\n")
                    self.time_slept = pA.sleeper()
                    print("\n[i]Sleeper finished.")
                    print(f"[i]Time Slept: {self.time_slept}")
                    self.playerChanges = 0
                    self.rounds += 1


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


if __name__ == "__main__":
    top_windows = []
    results = []
    liveImage = r'G:\School\Python - Homework\Projects\STO-Automation\live_sc.jpg'
    log = f"c:\\Users\\{os.getlogin()}\\Documents\\STO-Log.log"

    # Show Mouse Position for Debugging
    global_thread = threading.Thread(target=show_mouse_pos, name="Global Conf")
    # global_thread.daemon = True
    # global_thread.start()

    fore_window()
    # Start main loop
    with open(log, 'a') as logger:
        logger.write(f"{datetime.today().replace(microsecond=0)}: Starting Main\n")
        game = Game(logger)
        start = game.main(characters=8)
