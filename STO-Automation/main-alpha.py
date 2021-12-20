from time import gmtime, strftime   # Display current time for logging.
import pyautogui    # Graphic Automation.
import keyboard     # Keyboard Simulation.
import win32api             # Windows components.
import win32com.client      # Windows components.
import win32con             # Windows components.
import win32gui             # Windows components.
import threading    # For mouse position display.
import random       # Random number for Sleeper's timer.
import ctypes       # For Keyboard language validation.
import time         # Pause between actions, Mouse drag Duration time.
import sys          # Display counter while sleeper in action
import os           # Get current logged in User and save log file in Documents.


class Player1:
    def __init__(self):
        # Reputation vars
        self.discovery_select_x, self.discovery_select_y = 815, 600
        self.omega_select_x, self.omega_select_y = 815, 645
        self.nukara_select_x, self.nukara_select_y = 815, 635
        self.romulus_select_x, self.romulus_select_y = 815, 600
        self.dyson_select_x, self.dyson_select_y = 815, 600
        self.counter_command_select_x, self.counter_command_select_y = 815, 625
        self.delta_select_x, self.delta_select_y = 815, 580
        self.iconian_select_x, self.iconian_select_y = 815, 615
        self.terran_select_x, self.terran_select_y = 815, 595
        self.temporal_select_x, self.temporal_select_y = 815, 615
        self.lukari_select_x, self.lukari_select_y = 815, 630
        self.competetive_select_x, self.competetive_select_y = 815, 610
        self.gamma_select_x, self.gamma_select_y = 815, 600

        # Admiralty Vars
        self.adm_folder_x, self.adm_folder_y = 510, 20
        self.progress_x, self.progress_y = 85, 95
        self.adm_slot_1_x, self.adm_slot_1_y = 940, 155
        self.adm_slot_2_x, self.adm_slot_2_y = 940, 275
        self.adm_slot_3_x, self.adm_slot_3_y = 940, 395
        self.adm_slot_4_x, self.adm_slot_4_y = 940, 505
        self.adm_slot_5_x, self.adm_slot_5_y = 940, 620
        self.adm_slot_6_x, self.adm_slot_6_y = 940, 735
        self.adm_slot_7_x, self.adm_slot_7_y = 940, 865
        self.adm_slot_8_x, self.adm_slot_8_y = 940, 1000

        # Duty Officers vars
        self.duff_folder_x, self.duff_folder_y = 410, 20
        self.completed_x, self.completed_y = 85, 235
        self.duff_1_x, self.duff_1_y = 935, 175

    # Run Reputation Automation
    def act_reputation(self):
        # Discovery Legends
        discovery_legends(self.discovery_select_x, self.discovery_select_y)
        time.sleep(pause)

        # Task Force Omega
        task_force_omega(self.omega_select_x, self.omega_select_y)
        time.sleep(pause)

        # Nukara Strikeforce
        nukara_strike_force(self.nukara_select_x, self.nukara_select_y)
        time.sleep(pause)

        # New Romulus
        new_romulus(self.romulus_select_x, self.romulus_select_y)
        time.sleep(pause)

        # Dyson Joint Command
        dyson_joint_command(self.dyson_select_x, self.dyson_select_y)
        time.sleep(pause)

        # 8472 Counter-Command
        counter_command(self.counter_command_select_x, self.counter_command_select_y)
        time.sleep(pause)

        # Delta Alliance
        delta_alliance(self.delta_select_x, self.delta_select_y)
        time.sleep(pause)

        # Iconian Resistance
        iconian_resistance(self.iconian_select_x, self.iconian_select_y)
        time.sleep(pause)

        # Terran Task Force
        terran_task_force(self.terran_select_x, self.terran_select_y)
        time.sleep(pause)

        # Temporal Defence Initiative
        temporal_defence_initiative(self.temporal_select_x, self.temporal_select_y)
        time.sleep(pause)

        # Lukari Task Force
        lukari_task_force(self.lukari_select_x, self.lukari_select_y)
        time.sleep(pause)

        # Competetive Wargames
        competetive_wargames(self.competetive_select_x, self.competetive_select_y)
        time.sleep(pause)

        # Gamma Task Force
        gamma_task_force(self.gamma_select_x, self.gamma_select_y)
        time.sleep(pause)

        # Return To Legends
        pyautogui.moveTo(discovery_tab_mouse_x, discovery_tab_mouse_y, duration=dur)
        time.sleep(pause)
        click(discovery_tab_mouse_x, discovery_tab_mouse_y)
        time.sleep(pause)

        return

    # Run Admiralty Automation
    def act_admiralty(self):
        # Open Admiralty Folder
        pyautogui.moveTo(self.adm_folder_x, self.adm_folder_y, duration=dur)
        time.sleep(pause)
        click(self.adm_folder_x, self.adm_folder_y)
        time.sleep(pause)

        # Open Progress Window
        pyautogui.moveTo(self.progress_x, self.progress_y, duration=dur)
        time.sleep(pause)
        click(self.progress_x, self.progress_y)
        time.sleep(pause)

        # Slot 1
        pyautogui.moveTo(self.adm_slot_1_x, self.adm_slot_1_y, duration=dur)
        time.sleep(pause)
        click(self.adm_slot_1_x, self.adm_slot_1_y)
        time.sleep(pause)

        # Slot 2
        pyautogui.moveTo(self.adm_slot_2_x, self.adm_slot_2_y, duration=dur)
        time.sleep(pause)
        click(self.adm_slot_2_x, self.adm_slot_2_y)
        time.sleep(pause)

        # Slot 3
        pyautogui.moveTo(self.adm_slot_3_x, self.adm_slot_3_y, duration=dur)
        time.sleep(pause)
        click(self.adm_slot_3_x, self.adm_slot_3_y)
        time.sleep(pause)

        # Slot 4
        pyautogui.moveTo(self.adm_slot_4_x, self.adm_slot_4_y, duration=dur)
        time.sleep(pause)
        click(self.adm_slot_4_x, self.adm_slot_4_y)
        time.sleep(pause)

        # Slot 5
        pyautogui.moveTo(self.adm_slot_5_x, self.adm_slot_5_y, duration=dur)
        time.sleep(pause)
        click(self.adm_slot_5_x, self.adm_slot_5_y)
        time.sleep(pause)

        # Slot 6
        pyautogui.moveTo(self.adm_slot_6_x, self.adm_slot_6_y, duration=dur)
        time.sleep(pause)
        click(self.adm_slot_6_x, self.adm_slot_6_y)
        time.sleep(pause)

        # Slot 7
        pyautogui.moveTo(self.adm_slot_7_x, self.adm_slot_7_y, duration=dur)
        time.sleep(pause)
        click(self.adm_slot_7_x, self.adm_slot_7_y)
        time.sleep(pause)

        # Slot 8
        pyautogui.moveTo(self.adm_slot_8_x, self.adm_slot_8_y, duration=dur)
        time.sleep(pause)
        click(self.adm_slot_8_x, self.adm_slot_8_y)
        time.sleep(pause)

        return

    # Run Duty Officers Automation
    def act_dutyofficers(self):
        # Open Duty Officers Folder
        pyautogui.moveTo(self.duff_folder_x, self.duff_folder_y, duration=dur)
        time.sleep(pause)
        click(self.duff_folder_x, self.duff_folder_y)
        time.sleep(pause)

        # Open Completed Window
        pyautogui.moveTo(self.completed_x, self.completed_y, duration=dur)
        time.sleep(pause)
        click(self.completed_x, self.completed_y)
        time.sleep(pause)

        # Collect Rewards
        pyautogui.moveTo(self.duff_1_x, self.duff_1_y, duration=dur)
        time.sleep(pause)
        for i in range(1, 22):
            print(f"[i]Player 1: Collecting reward #{i}...\n")
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())} : Player 1: Collecting reward...\n")
            click(self.duff_1_x, self.duff_1_y)
            time.sleep(0.8)
            print(f"[i]Player 1: reward #{i} collected.")
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())} : Player 1: Reward collected.\n")


class Player2:
    def __init__(self):
        # Reputation vars
        self.discovery_select_x, self.discovery_select_y = 815, 600
        self.omega_select_x, self.omega_select_y = 815, 630
        self.nukara_select_x, self.nukara_select_y = 815, 610
        self.romulus_select_x, self.romulus_select_y = 815, 595
        self.dyson_select_x, self.dyson_select_y = 815, 595
        self.counter_command_select_x, self.counter_command_select_y = 815, 605
        self.delta_select_x, self.delta_select_y = 815, 595
        self.iconian_select_x, self.iconian_select_y = 815, 595
        self.terran_select_x, self.terran_select_y = 815, 590
        self.temporal_select_x, self.temporal_select_y = 815, 605
        self.lukari_select_x, self.lukari_select_y = 815, 625
        self.competetive_select_x, self.competetive_select_y = 815, 605
        self.gamma_select_x, self.gamma_select_y = 815, 600

        # Admiralty Vars
        self.adm_folder_x, self.adm_folder_y = 510, 20
        self.progress_x, self.progress_y = 85, 95
        self.adm_slot_1_x, self.adm_slot_1_y = 945, 155
        self.adm_slot_2_x, self.adm_slot_2_y = 945, 275
        self.adm_slot_3_x, self.adm_slot_3_y = 945, 390
        self.adm_slot_4_x, self.adm_slot_4_y = 945, 500
        self.adm_slot_5_x, self.adm_slot_5_y = 945, 620
        self.adm_slot_6_x, self.adm_slot_6_y = 945, 735
        self.adm_slot_7_x, self.adm_slot_7_y = 945, 865
        self.adm_slot_8_x, self.adm_slot_8_y = 945, 1000

        # Duty Officers vars
        self.duff_folder_x, self.duff_folder_y = 410, 20
        self.completed_x, self.completed_y = 85, 235
        self.duff_1_x, self.duff_1_y = 935, 175

    # Run Reputation Automation
    def act_reputation(self):
        # Discovery Legends
        discovery_legends(self.discovery_select_x, self.discovery_select_y)
        time.sleep(pause)

        # Task Force Omega
        task_force_omega(self.omega_select_x, self.omega_select_y)
        time.sleep(pause)

        # Nukara Strikeforce
        nukara_strike_force(self.nukara_select_x, self.nukara_select_y)
        time.sleep(pause)

        # New Romulus
        new_romulus(self.romulus_select_x, self.romulus_select_y)
        time.sleep(pause)

        # Dyson Joint Command
        dyson_joint_command(self.dyson_select_x, self.dyson_select_y)
        time.sleep(pause)

        # 8472 Counter-Command
        counter_command(self.counter_command_select_x, self.counter_command_select_y)
        time.sleep(pause)

        # Delta Alliance
        delta_alliance(self.delta_select_x, self.delta_select_y)
        time.sleep(pause)

        # Iconian Resistance
        iconian_resistance(self.iconian_select_x, self.iconian_select_y)
        time.sleep(pause)

        # Terran Task Force
        terran_task_force(self.terran_select_x, self.terran_select_y)
        time.sleep(pause)

        # Temporal Defence Initiative
        temporal_defence_initiative(self.temporal_select_x, self.temporal_select_y)
        time.sleep(pause)

        # Lukari Task Force
        lukari_task_force(self.lukari_select_x, self.lukari_select_y)
        time.sleep(pause)

        # Competetive Wargames
        competetive_wargames(self.competetive_select_x, self.competetive_select_y)
        time.sleep(pause)

        # Gamma Task Force
        gamma_task_force(self.gamma_select_x, self.gamma_select_y)
        time.sleep(pause)

        # # Return To Legends
        # pyautogui.moveTo(discovery_tab_mouse_x, discovery_tab_mouse_y, duration=dur)
        # time.sleep(pause)
        # click(discovery_tab_mouse_x, discovery_tab_mouse_y)
        # time.sleep(pause)

        return

    # Run Admiralty Automation
    def act_admiralty(self):
        # Open Admiralty Folder
        pyautogui.moveTo(self.adm_folder_x, self.adm_folder_y, duration=dur)
        time.sleep(pause)
        click(self.adm_folder_x, self.adm_folder_y)
        time.sleep(pause)

        # Open Progress Window
        pyautogui.moveTo(self.progress_x, self.progress_y, duration=dur)
        time.sleep(pause)
        click(self.progress_x, self.progress_y)
        time.sleep(pause)

        # Slot 1
        pyautogui.moveTo(self.adm_slot_1_x, self.adm_slot_1_y, duration=dur)
        time.sleep(pause)
        click(self.adm_slot_1_x, self.adm_slot_1_y)
        time.sleep(pause)

        # Slot 2
        pyautogui.moveTo(self.adm_slot_2_x, self.adm_slot_2_y, duration=dur)
        time.sleep(pause)
        click(self.adm_slot_2_x, self.adm_slot_2_y)
        time.sleep(pause)

        # Slot 3
        pyautogui.moveTo(self.adm_slot_3_x, self.adm_slot_3_y, duration=dur)
        time.sleep(pause)
        click(self.adm_slot_3_x, self.adm_slot_3_y)
        time.sleep(pause)

        # Slot 4
        pyautogui.moveTo(self.adm_slot_4_x, self.adm_slot_4_y, duration=dur)
        time.sleep(pause)
        click(self.adm_slot_4_x, self.adm_slot_4_y)
        time.sleep(pause)

        # Slot 5
        pyautogui.moveTo(self.adm_slot_5_x, self.adm_slot_5_y, duration=dur)
        time.sleep(pause)
        click(self.adm_slot_5_x, self.adm_slot_5_y)
        time.sleep(pause)

        # Slot 6
        pyautogui.moveTo(self.adm_slot_6_x, self.adm_slot_6_y, duration=dur)
        time.sleep(pause)
        click(self.adm_slot_6_x, self.adm_slot_6_y)
        time.sleep(pause)

        # Slot 7
        pyautogui.moveTo(self.adm_slot_7_x, self.adm_slot_7_y, duration=dur)
        time.sleep(pause)
        click(self.adm_slot_7_x, self.adm_slot_7_y)
        time.sleep(pause)

        # Slot 8
        pyautogui.moveTo(self.adm_slot_8_x, self.adm_slot_8_y, duration=dur)
        time.sleep(pause)
        click(self.adm_slot_8_x, self.adm_slot_8_y)
        time.sleep(pause)

        return

    # Run Duty Officers Automation
    def act_dutyofficers(self):
        # Open Duty Officers Folder
        pyautogui.moveTo(self.duff_folder_x, self.duff_folder_y, duration=dur)
        time.sleep(pause)
        click(self.duff_folder_x, self.duff_folder_y)
        time.sleep(pause)

        # Open Completed Window
        pyautogui.moveTo(self.completed_x, self.completed_y, duration=dur)
        time.sleep(pause)
        click(self.completed_x, self.completed_y)
        time.sleep(pause)

        # Collect Rewards
        pyautogui.moveTo(self.duff_1_x, self.duff_1_y, duration=dur)
        time.sleep(pause)
        for i in range(1, 22):
            print(f"[i]Player 2: Collecting reward #{i}")
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())} : Player 2: Collecting reward.\n")
            click(self.duff_1_x, self.duff_1_y)
            time.sleep(1)
            print(f"[i]Player 2 : reward #{i} collected")
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())} : Player 2: Reward collected.\n")


class DilRefine:
    def __init__(self):
        self.assets_x, self.assets_y = 1685, 635
        self.top_scroller_x, self.top_scroller_y = 1897, 700
        self.bottom_scroller_x, self.bottom_scroller_y = 1897, 950
        self.refine_button_x, self.refine_button_y = 1765, 810

    def act(self):
        pyautogui.moveTo(self.assets_x, self.assets_y, duration=dur)
        time.sleep(pause)
        click(self.assets_x, self.assets_y)
        time.sleep(pause)
        pyautogui.moveTo(self.top_scroller_x, self.top_scroller_y, duration=dur)
        time.sleep(pause)
        pyautogui.dragTo(self.bottom_scroller_x, self.bottom_scroller_y, duration=dur)
        time.sleep(pause)
        pyautogui.moveTo(self.refine_button_x, self.refine_button_y, duration=dur)
        time.sleep(pause)
        click(self.refine_button_x, self.refine_button_y)
        time.sleep(pause)

        return


class Character:
    def __init__(self):
        self.changeButton_x, self.changeButton_y = 540, 390
        self.changeConfirm_x, self.changeConfirm_y = 955, 570
        self.middleCharacter_x, self.middleCharacter_y = 245, 390
        self.play_x, self.play_y = 425, 875

    def act(self):
        # Click the Change Character button
        pyautogui.moveTo(self.changeButton_x, self.changeButton_y, duration=dur)
        time.sleep(pause)
        click(self.changeButton_x, self.changeButton_y)
        time.sleep(pause)

        # Confirm character Change
        pyautogui.moveTo(self.changeConfirm_x, self.changeConfirm_y, duration=dur)
        time.sleep(pause)
        click(self.changeConfirm_x, self.changeConfirm_y)
        time.sleep(5)

        # Choose the middle character
        pyautogui.moveTo(self.middleCharacter_x, self.middleCharacter_y, duration=dur)
        time.sleep(pause)
        click(self.middleCharacter_x, self.middleCharacter_y)
        time.sleep(5)

        # Click the Play button
        pyautogui.moveTo(self.play_x, self.play_y, duration=dur)
        time.sleep(pause)
        click(self.play_x, self.play_y)
        time.sleep(10)

        # Close the welcome window
        keyboard.press_and_release("esc")

        return


def discovery_legends(x, y):
    # Open Discovery Tab
    pyautogui.moveTo(discovery_tab_mouse_x, discovery_tab_mouse_y, duration=dur)
    time.sleep(pause)
    click(discovery_tab_mouse_x, discovery_tab_mouse_y)
    time.sleep(pause)

    # Project 1 Reward
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    click(project1_x, project1_y)
    time.sleep(pause)

    # Project 1
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    click(project1_x, project1_y)
    time.sleep(pause)

    # Click on Select Button
    pyautogui.moveTo(x, y, duration=dur)
    time.sleep(pause)
    click(x, y)
    time.sleep(pause)

    # Click on Fill All Button
    pyautogui.moveTo(fill_x, fill_y, duration=dur)
    time.sleep(pause)
    click(fill_x, fill_y)
    time.sleep(pause)

    # Click on Confirm Button
    pyautogui.moveTo(confirm_x, confirm_y, duration=dur)
    time.sleep(pause)
    click(confirm_x, confirm_y)
    time.sleep(pause)

    return


def task_force_omega(x, y):
    # Open Omega Tab
    pyautogui.moveTo(omega_tab_mouse_x, omega_tab_mouse_y, duration=dur)
    time.sleep(pause)
    click(omega_tab_mouse_x, omega_tab_mouse_y)
    time.sleep(pause)

    # Project 1 Reward
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    click(project1_x, project1_y)
    time.sleep(pause)

    # Project 1
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    click(project1_x, project1_y)
    time.sleep(pause)

    # Click on Select Button
    pyautogui.moveTo(x, y, duration=dur)
    time.sleep(pause)
    click(x, y)
    time.sleep(pause)

    # Click on Fill All Button
    pyautogui.moveTo(fill_x, fill_y, duration=dur)
    time.sleep(pause)
    click(fill_x, fill_y)
    time.sleep(pause)

    # Click on Confirm Button
    pyautogui.moveTo(confirm_x, confirm_y, duration=dur)
    time.sleep(pause)
    click(confirm_x, confirm_y)
    time.sleep(pause)


def nukara_strike_force(x, y):
    # Open Nukara Tab
    pyautogui.moveTo(nukara_tab_mouse_x, nukara_tab_mouse_y, duration=dur)
    time.sleep(pause)
    click(nukara_tab_mouse_x, nukara_tab_mouse_y)
    time.sleep(pause)

    # Project 1 Reward
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    click(project1_x, project1_y)
    time.sleep(pause)

    # Project 1
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    click(project1_x, project1_y)
    time.sleep(pause)

    # Click on Select Button
    pyautogui.moveTo(x, y, duration=dur)
    time.sleep(pause)
    click(x, y)
    time.sleep(pause)

    # Click on Fill All Button
    pyautogui.moveTo(fill_x, fill_y, duration=dur)
    time.sleep(pause)
    click(fill_x, fill_y)
    time.sleep(pause)

    # Click on Confirm Button
    pyautogui.moveTo(confirm_x, confirm_y, duration=dur)
    time.sleep(pause)
    click(confirm_x, confirm_y)
    time.sleep(pause)

    return


def new_romulus(x, y):
    # Open Romulus Tab
    pyautogui.moveTo(romulus_tab_mouse_x, romulus_tab_mouse_y, duration=dur)
    time.sleep(pause)
    click(romulus_tab_mouse_x, romulus_tab_mouse_y)
    time.sleep(pause)

    # Project 1 Reward
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    click(project1_x, project1_y)
    time.sleep(pause)

    # Project 1
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    click(project1_x, project1_y)
    time.sleep(pause)

    # Click on Select Button
    pyautogui.moveTo(x, y, duration=dur)
    time.sleep(pause)
    click(x, y)
    time.sleep(pause)

    # Click on Fill All Button
    pyautogui.moveTo(fill_x, fill_y, duration=dur)
    time.sleep(pause)
    click(fill_x, fill_y)
    time.sleep(pause)

    # Click on Confirm Button
    pyautogui.moveTo(confirm_x, confirm_y, duration=dur)
    time.sleep(pause)
    click(confirm_x, confirm_y)
    time.sleep(pause)

    return


def dyson_joint_command(x, y):
    # Open Dyson Tab
    pyautogui.moveTo(dyson_tab_mouse_x, dyson_tab_mouse_y, duration=dur)
    time.sleep(pause)
    click(dyson_tab_mouse_x, dyson_tab_mouse_y)
    time.sleep(pause)

    # Project 1 Reward
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    click(project1_x, project1_y)
    time.sleep(pause)

    # Project 1
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    click(project1_x, project1_y)
    time.sleep(pause)

    # Click on Select Button
    pyautogui.moveTo(x, y, duration=dur)
    time.sleep(pause)
    click(x, y)
    time.sleep(pause)

    # Click on Fill All Button
    pyautogui.moveTo(fill_x, fill_y, duration=dur)
    time.sleep(pause)
    click(fill_x, fill_y)
    time.sleep(pause)

    # Click on Confirm Button
    pyautogui.moveTo(confirm_x, confirm_y, duration=dur)
    time.sleep(pause)
    click(confirm_x, confirm_y)
    time.sleep(pause)

    return


def counter_command(x, y):
    # Open Counter-Command Tab
    pyautogui.moveTo(counter_command_tab_mouse_x, counter_command_tab_mouse_y, duration=dur)
    time.sleep(pause)
    click(counter_command_tab_mouse_x, counter_command_tab_mouse_y)
    time.sleep(pause)

    # Project 1 Reward
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    click(project1_x, project1_y)
    time.sleep(pause)

    # Project 1
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    click(project1_x, project1_y)
    time.sleep(pause)

    # Click on Select Button
    pyautogui.moveTo(x, y, duration=dur)
    time.sleep(pause)
    click(x, y)
    time.sleep(pause)

    # Click on Fill All Button
    pyautogui.moveTo(fill_x, fill_y, duration=dur)
    time.sleep(pause)
    click(fill_x, fill_y)
    time.sleep(pause)

    # Click on Confirm Button
    pyautogui.moveTo(confirm_x, confirm_y, duration=dur)
    time.sleep(pause)
    click(confirm_x, confirm_y)
    time.sleep(pause)

    return


def delta_alliance(x, y):
    # Open Delta Tab
    pyautogui.moveTo(delta_tab_mouse_x, delta_tab_mouse_y, duration=dur)
    time.sleep(pause)
    click(delta_tab_mouse_x, delta_tab_mouse_y)
    time.sleep(pause)

    # Project 1 Reward
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    click(project1_x, project1_y)
    time.sleep(pause)

    # Project 1
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    click(project1_x, project1_y)
    time.sleep(pause)

    # Click on Select Button
    pyautogui.moveTo(x, y, duration=dur)
    time.sleep(pause)
    click(x, y)
    time.sleep(pause)

    # Click on Fill All Button
    pyautogui.moveTo(fill_x, fill_y, duration=dur)
    time.sleep(pause)
    click(fill_x, fill_y)
    time.sleep(pause)

    # Click on Confirm Button
    pyautogui.moveTo(confirm_x, confirm_y, duration=dur)
    time.sleep(pause)
    click(confirm_x, confirm_y)
    time.sleep(pause)

    return


def iconian_resistance(x, y):
    # Open Iconian Tab
    pyautogui.moveTo(iconian_tab_mouse_x, iconian_tab_mouse_y, duration=dur)
    time.sleep(pause)
    click(iconian_tab_mouse_x, iconian_tab_mouse_y)
    time.sleep(pause)

    # Project 1 Reward
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    click(project1_x, project1_y)
    time.sleep(pause)

    # Project 1
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    click(project1_x, project1_y)
    time.sleep(pause)

    # Click on Select Button
    pyautogui.moveTo(x, y, duration=dur)
    time.sleep(pause)
    click(x, y)
    time.sleep(pause)

    # Click on Fill All Button
    pyautogui.moveTo(fill_x, fill_y, duration=dur)
    time.sleep(pause)
    click(fill_x, fill_y)
    time.sleep(pause)

    # Click on Confirm Button
    pyautogui.moveTo(confirm_x, confirm_y, duration=dur)
    time.sleep(pause)
    click(confirm_x, confirm_y)
    time.sleep(pause)

    return


def terran_task_force(x, y):
    # Open Terran Tab
    pyautogui.moveTo(terran_tab_mouse_x, terran_tab_mouse_y, duration=dur)
    time.sleep(pause)
    click(terran_tab_mouse_x, terran_tab_mouse_y)
    time.sleep(pause)

    # Project 1 Reward
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    click(project1_x, project1_y)
    time.sleep(pause)

    # Project 1
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    click(project1_x, project1_y)
    time.sleep(pause)

    # Click on Select Button
    pyautogui.moveTo(x, y, duration=dur)
    time.sleep(pause)
    click(x, y)
    time.sleep(pause)

    # Click on Fill All Button
    pyautogui.moveTo(fill_x, fill_y, duration=dur)
    time.sleep(pause)
    click(fill_x, fill_y)
    time.sleep(pause)

    # Click on Confirm Button
    pyautogui.moveTo(confirm_x, confirm_y, duration=dur)
    time.sleep(pause)
    click(confirm_x, confirm_y)
    time.sleep(pause)

    return


def temporal_defence_initiative(x, y):
    # Open Temporal Tab
    pyautogui.moveTo(temporal_tab_mouse_x, temporal_tab_mouse_y, duration=dur)
    time.sleep(pause)
    click(temporal_tab_mouse_x, temporal_tab_mouse_y)
    time.sleep(pause)

    # Project 1 Reward
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    click(project1_x, project1_y)
    time.sleep(pause)

    # Project 1
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    click(project1_x, project1_y)
    time.sleep(pause)

    # Click on Select Button
    pyautogui.moveTo(x, y, duration=dur)
    time.sleep(pause)
    click(x, y)
    time.sleep(pause)

    # Click on Fill All Button
    pyautogui.moveTo(fill_x, fill_y, duration=dur)
    time.sleep(pause)
    click(fill_x, fill_y)
    time.sleep(pause)

    # Click on Confirm Button
    pyautogui.moveTo(confirm_x, confirm_y, duration=dur)
    time.sleep(pause)
    click(confirm_x, confirm_y)
    time.sleep(pause)

    return


def lukari_task_force(x, y):
    # Open Lukari Tab
    pyautogui.moveTo(lukari_tab_mouse_x, lukari_tab_mouse_y, duration=dur)
    time.sleep(pause)
    click(lukari_tab_mouse_x, lukari_tab_mouse_y)
    time.sleep(pause)

    # Project 1 Reward
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    click(project1_x, project1_y)
    time.sleep(pause)

    # Project 1
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    click(project1_x, project1_y)
    time.sleep(pause)

    # Click on Select Button
    pyautogui.moveTo(x, y, duration=dur)
    time.sleep(pause)
    click(x, y)
    time.sleep(pause)

    # Click on Fill All Button
    pyautogui.moveTo(fill_x, fill_y, duration=dur)
    time.sleep(pause)
    click(fill_x, fill_y)
    time.sleep(pause)

    # Click on Confirm Button
    pyautogui.moveTo(confirm_x, confirm_y, duration=dur)
    time.sleep(pause)
    click(confirm_x, confirm_y)
    time.sleep(pause)

    return


def competetive_wargames(x, y):
    # Open Competetive Tab
    pyautogui.moveTo(competetive_tab_mouse_x, competetive_tab_mouse_y, duration=dur)
    time.sleep(pause)
    click(competetive_tab_mouse_x, competetive_tab_mouse_y)
    time.sleep(pause)

    # Project 1 Reward
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    click(project1_x, project1_y)
    time.sleep(pause)

    # Project 1
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    click(project1_x, project1_y)
    time.sleep(pause)

    # Click on Select Button
    pyautogui.moveTo(x, y, duration=dur)
    time.sleep(pause)
    click(x, y)
    time.sleep(pause)

    # Click on Fill All Button
    pyautogui.moveTo(fill_x, fill_y, duration=dur)
    time.sleep(pause)
    click(fill_x, fill_y)
    time.sleep(pause)

    # Click on Confirm Button
    pyautogui.moveTo(confirm_x, confirm_y, duration=dur)
    time.sleep(pause)
    click(confirm_x, confirm_y)
    time.sleep(pause)

    return


def gamma_task_force(x, y):
    # Open Gamma Tab
    pyautogui.moveTo(gamma_tab_mouse_x, gamma_tab_mouse_y, duration=dur)
    time.sleep(pause)
    click(gamma_tab_mouse_x, gamma_tab_mouse_y)
    time.sleep(pause)

    # Project 1 Reward
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    click(project1_x, project1_y)
    time.sleep(pause)

    # Project 1
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    click(project1_x, project1_y)
    time.sleep(pause)

    # Click on Select Button
    pyautogui.moveTo(x, y, duration=dur)
    time.sleep(pause)
    click(x, y)
    time.sleep(pause)

    # Click on Fill All Button
    pyautogui.moveTo(fill_x, fill_y, duration=dur)
    time.sleep(pause)
    click(fill_x, fill_y)
    time.sleep(pause)

    # Click on Confirm Button
    pyautogui.moveTo(confirm_x, confirm_y, duration=dur)
    time.sleep(pause)
    click(confirm_x, confirm_y)
    time.sleep(pause)

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
    logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())} : Changing Character\n")
    pyautogui.moveTo(menu_x, menu_y, duration=dur)
    time.sleep(pause)
    click(menu_x, menu_y)
    time.sleep(pause)
    Character().act()
    time.sleep(pause)
    print("[i]Finished Character change.")
    logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())} : Character changed.\n")

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
    keyboard.press_and_release("[")
    time.sleep(pause)
    print("[i]Player 1: Running Reputation automation...")
    logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())} : Player 1: Running Reputation automation.\n")
    Player1().act_reputation()
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


def get_keyboard_language():
    languages = {'0x436': "Afrikaans - South Africa", '0x041c': "Albanian - Albania", '0x045e': "Amharic - Ethiopia",
                 '0x401': "Arabic - Saudi Arabia",
                 '0x1401': "Arabic - Algeria", '0x3c01': "Arabic - Bahrain", '0x0c01': "Arabic - Egypt",
                 '0x801': "Arabic - Iraq", '0x2c01': "Arabic - Jordan",
                 '0x3401': "Arabic - Kuwait", '0x3001': "Arabic - Lebanon", '0x1001': "Arabic - Libya",
                 '0x1801': "Arabic - Morocco", '0x2001': "Arabic - Oman",
                 '0x4001': "Arabic - Qatar", '0x2801': "Arabic - Syria", '0x1c01': "Arabic - Tunisia",
                 '0x3801': "Arabic - U.A.E.", '0x2401': "Arabic - Yemen",
                 '0x042b': "Armenian - Armenia", '0x044d': "Assamese", '0x082c': "Azeri (Cyrillic)",
                 '0x042c': "Azeri (Latin)", '0x042d': "Basque",
                 '0x423': "Belarusian", '0x445': "Bengali (India)", '0x845': "Bengali (Bangladesh)",
                 '0x141A': "Bosnian (Bosnia/Herzegovina)", '0x402': "Bulgarian",
                 '0x455': "Burmese", '0x403': "Catalan", '0x045c': "Cherokee - United States",
                 '0x804': "Chinese - People's Republic of China",
                 '0x1004': "Chinese - Singapore", '0x404': "Chinese - Taiwan", '0x0c04': "Chinese - Hong Kong SAR",
                 '0x1404': "Chinese - Macao SAR", '0x041a': "Croatian",
                 '0x101a': "Croatian (Bosnia/Herzegovina)", '0x405': "Czech", '0x406': "Danish", '0x465': "Divehi",
                 '0x413': "Dutch - Netherlands", '0x813': "Dutch - Belgium",
                 '0x466': "Edo", '0x409': "English - United States", '0x809': "English - United Kingdom",
                 '0x0c09': "English - Australia", '0x2809': "English - Belize",
                 '0x1009': "English - Canada", '0x2409': "English - Caribbean", '0x3c09': "English - Hong Kong SAR",
                 '0x4009': "English - India", '0x3809': "English - Indonesia",
                 '0x1809': "English - Ireland", '0x2009': "English - Jamaica", '0x4409': "English - Malaysia",
                 '0x1409': "English - New Zealand", '0x3409': "English - Philippines",
                 '0x4809': "English - Singapore", '0x1c09': "English - South Africa", '0x2c09': "English - Trinidad",
                 '0x3009': "English - Zimbabwe", '0x425': "Estonian",
                 '0x438': "Faroese", '0x429': "Farsi", '0x464': "Filipino", '0x040b': "Finnish",
                 '0x040c': "French - France", '0x080c': "French - Belgium",
                 '0x2c0c': "French - Cameroon", '0x0c0c': "French - Canada",
                 '0x240c': "French - Democratic Rep. of Congo", '0x300c': "French - Cote d'Ivoire",
                 '0x3c0c': "French - Haiti", '0x140c': "French - Luxembourg", '0x340c': "French - Mali",
                 '0x180c': "French - Monaco", '0x380c': "French - Morocco",
                 '0xe40c': "French - North Africa", '0x200c': "French - Reunion", '0x280c': "French - Senegal",
                 '0x100c': "French - Switzerland",
                 '0x1c0c': "French - West Indies", '0x462': "Frisian - Netherlands", '0x467': "Fulfulde - Nigeria",
                 '0x042f': "FYRO Macedonian", '0x083c': "Gaelic (Ireland)",
                 '0x043c': "Gaelic (Scotland)", '0x456': "Galician", '0x437': "Georgian", '0x407': "German - Germany",
                 '0x0c07': "German - Austria", '0x1407': "German - Liechtenstein",
                 '0x1007': "German - Luxembourg", '0x807': "German - Switzerland", '0x408': "Greek",
                 '0x474': "Guarani - Paraguay", '0x447': "Gujarati", '0x468': "Hausa - Nigeria",
                 '0x475': "Hawaiian - United States", '0x040d': "Hebrew", '0x439': "Hindi", '0x040e': "Hungarian",
                 '0x469': "Ibibio - Nigeria", '0x040f': "Icelandic",
                 '0x470': "Igbo - Nigeria", '0x421': "Indonesian", '0x045d': "Inuktitut", '0x410': "Italian - Italy",
                 '0x810': "Italian - Switzerland", '0x411': "Japanese",
                 '0x044b': "Kannada", '0x471': "Kanuri - Nigeria", '0x860': "Kashmiri", '0x460': "Kashmiri (Arabic)",
                 '0x043f': "Kazakh", '0x453': "Khmer", '0x457': "Konkani",
                 '0x412': "Korean", '0x440': "Kyrgyz (Cyrillic)", '0x454': "Lao", '0x476': "Latin", '0x426': "Latvian",
                 '0x427': "Lithuanian", '0x043e': "Malay - Malaysia",
                 '0x083e': "Malay - Brunei Darussalam", '0x044c': "Malayalam", '0x043a': "Maltese", '0x458': "Manipuri",
                 '0x481': "Maori - New Zealand", '0x044e': "Marathi",
                 '0x450': "Mongolian (Cyrillic)", '0x850': "Mongolian (Mongolian)", '0x461': "Nepali",
                 '0x861': "Nepali - India", '0x414': "Norwegian (Bokmål)",
                 '0x814': "Norwegian (Nynorsk)", '0x448': "Oriya", '0x472': "Oromo", '0x479': "Papiamentu",
                 '0x463': "Pashto", '0x415': "Polish", '0x416': "Portuguese - Brazil",
                 '0x816': "Portuguese - Portugal", '0x446': "Punjabi", '0x846': "Punjabi (Pakistan)",
                 '0x046B': "Quecha - Bolivia", '0x086B': "Quecha - Ecuador",
                 '0x0C6B': "Quecha - Peru", '0x417': "Rhaeto-Romanic", '0x418': "Romanian",
                 '0x818': "Romanian - Moldava", '0x419': "Russian", '0x819': "Russian - Moldava",
                 '0x043b': "Sami (Lappish)", '0x044f': "Sanskrit", '0x046c': "Sepedi", '0x0c1a': "Serbian (Cyrillic)",
                 '0x081a': "Serbian (Latin)", '0x459': "Sindhi - India",
                 '0x859': "Sindhi - Pakistan", '0x045b': "Sinhalese - Sri Lanka", '0x041b': "Slovak",
                 '0x424': "Slovenian", '0x477': "Somali", '0x042e': "Sorbian",
                 '0x0c0a': "Spanish - Spain (Modern Sort)", '0x040a': "Spanish - Spain (Traditional Sort)",
                 '0x2c0a': "Spanish - Argentina", '0x400a': "Spanish - Bolivia",
                 '0x340a': "Spanish - Chile", '0x240a': "Spanish - Colombia", '0x140a': "Spanish - Costa Rica",
                 '0x1c0a': "Spanish - Dominican Republic",
                 '0x300a': "Spanish - Ecuador", '0x440a': "Spanish - El Salvador", '0x100a': "Spanish - Guatemala",
                 '0x480a': "Spanish - Honduras", '0xe40a': "Spanish - Latin America",
                 '0x080a': "Spanish - Mexico", '0x4c0a': "Spanish - Nicaragua", '0x180a': "Spanish - Panama",
                 '0x3c0a': "Spanish - Paraguay", '0x280a': "Spanish - Peru",
                 '0x500a': "Spanish - Puerto Rico", '0x540a': "Spanish - United States", '0x380a': "Spanish - Uruguay",
                 '0x200a': "Spanish - Venezuela", '0x430': "Sutu",
                 '0x441': "Swahili", '0x041d': "Swedish", '0x081d': "Swedish - Finland", '0x045a': "Syriac",
                 '0x428': "Tajik", '0x045f': "Tamazight (Arabic)",
                 '0x085f': "Tamazight (Latin)", '0x449': "Tamil", '0x444': "Tatar", '0x044a': "Telugu",
                 '0x041e': "Thai", '0x851': "Tibetan - Bhutan",
                 '0x451': "Tibetan - People's Republic of China", '0x873': "Tigrigna - Eritrea",
                 '0x473': "Tigrigna - Ethiopia", '0x431': "Tsonga", '0x432': "Tswana",
                 '0x041f': "Turkish", '0x442': "Turkmen", '0x480': "Uighur - China", '0x422': "Ukrainian",
                 '0x420': "Urdu", '0x820': "Urdu - India", '0x843': "Uzbek (Cyrillic)",
                 '0x443': "Uzbek (Latin)", '0x433': "Venda", '0x042a': "Vietnamese", '0x452': "Welsh", '0x434': "Xhosa",
                 '0x478': "Yi", '0x043d': "Yiddish", '0x046a': "Yoruba",
                 '0x435': "Zulu", '0x04ff': "HID (Human Interface Device)"
                 }
    user32 = ctypes.WinDLL('user32', use_last_error=True)

    # Get the current active window handle
    handle = user32.GetForegroundWindow()

    # Get the thread id from that window handle
    threadid = user32.GetWindowThreadProcessId(handle, 0)

    # Get the keyboard layout id from the threadid
    layout_id = user32.GetKeyboardLayout(threadid)

    # Extract the keyboard language id from the keyboard layout id
    language_id = layout_id & (2 ** 16 - 1)

    # Convert the keyboard language id from decimal to hexadecimal
    language_id_hex = hex(language_id)

    # Check if the hex value is in the dictionary.
    if language_id_hex in languages.keys():
        return languages[language_id_hex]
    else:
        # Return language id hexadecimal value if not found.
        return str(language_id_hex)


if __name__ == "__main__":
    # Reputation vars
    discovery_tab_mouse_x, discovery_tab_mouse_y = 100, 100
    omega_tab_mouse_x, omega_tab_mouse_y = 100, 145
    nukara_tab_mouse_x, nukara_tab_mouse_y = 100, 195
    romulus_tab_mouse_x, romulus_tab_mouse_y = 100, 240
    dyson_tab_mouse_x, dyson_tab_mouse_y = 100, 285
    counter_command_tab_mouse_x, counter_command_tab_mouse_y = 100, 330
    delta_tab_mouse_x, delta_tab_mouse_y = 100, 375
    iconian_tab_mouse_x, iconian_tab_mouse_y = 100, 425
    terran_tab_mouse_x, terran_tab_mouse_y = 100, 470
    temporal_tab_mouse_x, temporal_tab_mouse_y = 100, 515
    lukari_tab_mouse_x, lukari_tab_mouse_y = 100, 565
    competetive_tab_mouse_x, competetive_tab_mouse_y = 100, 610
    gamma_tab_mouse_x, gamma_tab_mouse_y = 100, 660
    project1_x, project1_y = 355, 350
    fill_x, fill_y = 820, 1048
    confirm_x, confirm_y = 955, 640
    menu_x, menu_y = 1905, 150

    # General Vars
    time_slept = 0
    player1_round = 1
    player2_round = 1
    rounds = 1
    player_changes = 1
    pause = 0.3
    dur = 0.2
    log = f"c:\\Users\\{os.getlogin()}\\Documents\\STO-Log.txt"

    # Change keyboard language to English
    win32api.LoadKeyboardLayout('00000409', 1)
    print(f"Keyboard Language changed to: {get_keyboard_language()}")

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
            start = time.time()

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

                end = time.time()
                print(f"Time elapsed: {end - start}")
                logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())} : Time elapsed: {end - start}.\n")
