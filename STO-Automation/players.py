from time import gmtime, strftime  # Display current time for logging.
import win32api  # Windows components.
import win32com.client  # Windows components.
import win32con  # Windows components.
import win32gui  # Windows components.
import pyautogui  # Graphic Automation.
import keyboard  # Keyboard Simulation.
import time  # Pause between actions, Mouse drag Duration time.
import os  # Get current logged in User and save log file in Documents.
import reputation  # Reputation module


# ------ Admiralty Vars ------ #
adm_folder_x, adm_folder_y = 510, 20
progress_x, progress_y = 85, 95

# Before Collection
adm_slot_1_x_static, adm_slot_1_y_static = 785, 155
adm_slot_2_x_static, adm_slot_2_y_static = 785, 295
adm_slot_3_x_static, adm_slot_3_y_static = 785, 430
adm_slot_4_x_static, adm_slot_4_y_static = 785, 570
adm_slot_5_x_static, adm_slot_5_y_static = 785, 705
adm_slot_6_x_static, adm_slot_6_y_static = 785, 840
adm_slot_7_x_static, adm_slot_7_y_static = 785, 985

# After Collection
adm_slot_1_x, adm_slot_1_y = 785, 155
adm_slot_2_x, adm_slot_2_y = 785, 275
adm_slot_3_x, adm_slot_3_y = 785, 385
adm_slot_4_x, adm_slot_4_y = 785, 495
adm_slot_5_x, adm_slot_5_y = 785, 620
adm_slot_6_x, adm_slot_6_y = 785, 745
adm_slot_7_x, adm_slot_7_y = 785, 895
adm_slot_8_x, adm_slot_8_y = 785, 995

# After Scrolling Down
adm_slot_8_x_static, adm_slot_8_y_static = 785, 885

topScroller_x, topScroller_y = 878, 360
bottomScroller_x, bottomScroller_y = 878, 565

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
upgrades_x, upgrades_y = 360, 530
upgrade_select_x, upgrade_select_y = 830, 530
fill_x, fill_y = 820, 1048
confirm_x, confirm_y = 955, 640

duff_pause = 1.5
pause = 0.2
dur = 0.2
log = f"c:\\Users\\{os.getlogin()}\\Documents\\STO-Log.txt"


class Player1:
    def __init__(self):
        # Reputation vars
        self.discovery_select_x, self.discovery_select_y = 815, 590
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

        # Duty Officers vars
        self.duff_folder_x, self.duff_folder_y = 410, 20
        self.completed_x, self.completed_y = 85, 235
        self.duff_1_x, self.duff_1_y = 795, 175

    # Run Reputation Automation
    def act_reputation(self):
        # Discovery Legends
        reputation.discovery_legends(self.discovery_select_x, self.discovery_select_y)
        time.sleep(pause)

        # Task Force Omega
        reputation.task_force_omega(self.omega_select_x, self.omega_select_y)
        time.sleep(pause)

        # Nukara Strikeforce
        reputation.nukara_strike_force(self.nukara_select_x, self.nukara_select_y)
        time.sleep(pause)

        # New Romulus
        reputation.new_romulus(self.romulus_select_x, self.romulus_select_y)
        time.sleep(pause)

        # Dyson Joint Command
        reputation.dyson_joint_command(self.dyson_select_x, self.dyson_select_y)
        time.sleep(pause)

        # 8472 Counter-Command
        reputation.counter_command(self.counter_command_select_x, self.counter_command_select_y)
        time.sleep(pause)

        # Delta Alliance
        reputation.delta_alliance(self.delta_select_x, self.delta_select_y)
        time.sleep(pause)

        # Iconian Resistance
        reputation.iconian_resistance(self.iconian_select_x, self.iconian_select_y)
        time.sleep(pause)

        # Terran Task Force
        reputation.terran_task_force(self.terran_select_x, self.terran_select_y)
        time.sleep(pause)

        # Temporal Defence Initiative
        reputation.temporal_defence_initiative(self.temporal_select_x, self.temporal_select_y)
        time.sleep(pause)

        # Lukari Task Force
        reputation.lukari_task_force(self.lukari_select_x, self.lukari_select_y)
        time.sleep(pause)

        # Competetive Wargames
        reputation.competetive_wargames(self.competetive_select_x, self.competetive_select_y)
        time.sleep(pause)

        # Gamma Task Force
        reputation.gamma_task_force(self.gamma_select_x, self.gamma_select_y)
        time.sleep(pause)

        # Return To Legends
        pyautogui.moveTo(reputation.discovery_tab_mouse_x, reputation.discovery_tab_mouse_y, duration=dur)
        time.sleep(pause)
        click(reputation.discovery_tab_mouse_x, reputation.discovery_tab_mouse_y)
        time.sleep(pause)

        return

    # Run Admiralty Automation
    def act_admiralty(self):
        # Open Admiralty Folder
        pyautogui.moveTo(adm_folder_x, adm_folder_y, duration=dur)
        time.sleep(pause)
        print("[i]Player 1: Clicking on Admiralty Folder")
        click(adm_folder_x, adm_folder_y)
        time.sleep(pause)

        # Open Progress Window
        pyautogui.moveTo(progress_x, progress_y, duration=dur)
        time.sleep(pause)
        print("[i]Clicking on Progress Tab")
        click(progress_x, progress_y)

        time.sleep(pause)

        # Slot 1
        pyautogui.moveTo(adm_slot_1_x, adm_slot_1_y, duration=dur)
        time.sleep(pause)
        print("[i]Clicking on Slot 1")
        click(adm_slot_1_x, adm_slot_1_y)
        time.sleep(pause)

        # Slot 2
        pyautogui.moveTo(adm_slot_2_x, adm_slot_2_y, duration=dur)
        time.sleep(pause)
        print("[i]Clicking on Slot 2")
        click(adm_slot_2_x, adm_slot_2_y)
        time.sleep(pause)

        # Slot 3
        pyautogui.moveTo(adm_slot_3_x, adm_slot_3_y, duration=dur)
        time.sleep(pause)
        print("[i]Clicking on Slot 3")
        click(adm_slot_3_x, adm_slot_3_y)
        time.sleep(pause)

        # Slot 4
        pyautogui.moveTo(adm_slot_4_x, adm_slot_4_y, duration=dur)
        time.sleep(pause)
        print("[i]Clicking on Slot 4")
        click(adm_slot_4_x, adm_slot_4_y)
        time.sleep(pause)

        # Slot 5
        pyautogui.moveTo(adm_slot_5_x, adm_slot_5_y, duration=dur)
        time.sleep(pause)
        print("[i]Clicking on Slot 5")
        click(adm_slot_5_x, adm_slot_5_y)
        time.sleep(pause)

        # Slot 6
        pyautogui.moveTo(adm_slot_6_x, adm_slot_6_y, duration=dur)
        time.sleep(pause)
        print("[i]Clicking on Slot 6")
        click(adm_slot_6_x, adm_slot_6_y)
        time.sleep(pause)

        # Slot 7
        pyautogui.moveTo(adm_slot_7_x, adm_slot_7_y, duration=dur)
        time.sleep(pause)
        print("[i]Clicking on Slot 7")
        click(adm_slot_7_x, adm_slot_7_y)
        time.sleep(pause)

        # Slot 8
        pyautogui.moveTo(adm_slot_8_x, adm_slot_8_y, duration=dur)
        time.sleep(pause)
        print("[i]Clicking on Slot 8")
        click(adm_slot_8_x, adm_slot_8_y)
        time.sleep(pause)

        return

    # Run Duty Officers Automation
    def act_dutyofficers(self):
        # Open Duty Officers Folder
        pyautogui.moveTo(self.duff_folder_x, self.duff_folder_y, duration=dur)
        time.sleep(pause)
        print("[i]Clicking on DutyOfficers Folder")
        click(self.duff_folder_x, self.duff_folder_y)
        time.sleep(pause)

        # Open Completed Window
        pyautogui.moveTo(self.completed_x, self.completed_y, duration=dur)
        time.sleep(pause)
        print("[i]Clicking on Completed")
        click(self.completed_x, self.completed_y)
        time.sleep(pause)

        # Collect Rewards
        pyautogui.moveTo(self.duff_1_x, self.duff_1_y, duration=dur)
        time.sleep(pause)
        for i in range(1, 22):
            print(f"[i]Player 1: Collecting reward #{i}...")
            click(self.duff_1_x, self.duff_1_y)
            time.sleep(0.4)
            print(f"[i]Player 1: reward #{i} collected.")

    # Set new DutyOfficers missions
    def duff_missions(self):
        # Open Duty Officers Folder
        pyautogui.moveTo(self.duff_folder_x, self.duff_folder_y, duration=dur)
        time.sleep(pause)
        print(f"[i]Player 1: Clicking on DutyOfficers Folder")
        click(self.duff_folder_x, self.duff_folder_y)
        time.sleep(pause)

        # Click on Personal
        pyautogui.moveTo(personal_x, personal_y, duration=dur)
        time.sleep(pause)
        print(f"[i]Player 1: Clicking on Personal")
        click(personal_x, personal_y)
        time.sleep(duff_pause)

        # Click on Filters
        pyautogui.moveTo(filters_x, filters_y, duration=dur)
        time.sleep(pause)
        print(f"[i]Player 1: Personal: Clicking Filters")
        click(filters_x, filters_y)
        time.sleep(duff_pause)

        # Click on Met Reqs
        pyautogui.moveTo(metReqs_x, metReqs_y, duration=dur)
        time.sleep(pause)
        print(f"[i]Player 1: Personal: Clicking on Met Reqs")
        click(metReqs_x, metReqs_y)
        time.sleep(duff_pause)
        click(metReqs_x, metReqs_y)
        pyautogui.doubleClick(metReqs_x, metReqs_y)
        time.sleep(duff_pause)

        # Start Planning & Executing for Personal Assignments
        self.planExecute()

        # Click on Engineering Assignments
        pyautogui.moveTo(engineering_x, engineering_y, duration=dur)
        time.sleep(pause)
        print(f"[i]Player 1: Clicking on Engineering")
        click(engineering_x, engineering_y)
        time.sleep(duff_pause)

        # Plan & Execute & Return to Department Heads
        self.planExecute()

        # Click on Science Assignments
        pyautogui.moveTo(science_x, science_y, duration=dur)
        time.sleep(pause)
        print("[i]Clicking on Science Assignment")
        click(science_x, science_y)
        time.sleep(duff_pause)

        # Plan & Execute & Return to Department Heads
        self.planExecute()

        # Click on Tactical Assignments
        pyautogui.moveTo(tactical_x, tactical_y, duration=dur)
        time.sleep(pause)
        print("[i]Clicking on Tactical Assignment")
        click(tactical_x, tactical_y)
        time.sleep(duff_pause)

        # Plan & Execute & Return to Department Heads
        self.planExecute()

        # Click on Security Assignments
        pyautogui.moveTo(security_x, security_y, duration=dur)
        time.sleep(pause)
        print("[i]Clicking on Security Assignment")
        click(security_x, security_y)
        time.sleep(duff_pause)

        # Plan & Execute & Return to Department Heads
        self.planExecute()

        # Click on Medical Assignments
        pyautogui.moveTo(medial_x, medical_y, duration=dur)
        time.sleep(pause)
        print("[i]Clicking on Medical Assignment")
        click(medial_x, medical_y)
        time.sleep(duff_pause)

        # Plan & Execute & Return to Department Heads
        self.planExecute()

        print("[i]Simulating keyboard for ']' key")
        keyboard.press_and_release("]")
        time.sleep(pause)

        return

    # General Plan & Begin
    def planExecute(self):
        # Plan & Begin
        for i in range(1, 6):
            # Plan
            print(f"[i]Player 1: Clicking on Plan #{i}")
            plan()
            time.sleep(pause)

            # Begin
            print(f"[i]Player 1: Clicking on Begin Assignment #{i}")
            begin()
            time.sleep(pause)

        # Return to Department Heads
        pyautogui.moveTo(department_x, department_y, duration=dur)
        time.sleep(pause)
        print("[i]Clicking on Department Heads")
        click(department_x, department_y)
        time.sleep(duff_pause)

        return


class Player2:
    def __init__(self):
        # Reputation vars
        self.discovery_select_x, self.discovery_select_y = 815, 600
        self.omega_select_x, self.omega_select_y = 815, 640
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

        # Duty Officers vars
        self.duff_folder_x, self.duff_folder_y = 410, 20
        self.completed_x, self.completed_y = 85, 235
        self.duff_1_x, self.duff_1_y = 785, 175

    # Run Reputation Automation
    def act_reputation(self):
        # Discovery Legends
        reputation.discovery_legends(self.discovery_select_x, self.discovery_select_y)
        time.sleep(pause)

        # Task Force Omega
        reputation.task_force_omega(self.omega_select_x, self.omega_select_y)
        time.sleep(pause)

        # Nukara Strikeforce
        reputation.nukara_strike_force(self.nukara_select_x, self.nukara_select_y)
        time.sleep(pause)

        # New Romulus
        reputation.new_romulus(self.romulus_select_x, self.romulus_select_y)
        time.sleep(pause)

        # Dyson Joint Command
        reputation.dyson_joint_command(self.dyson_select_x, self.dyson_select_y)
        time.sleep(pause)

        # 8472 Counter-Command
        reputation.counter_command(self.counter_command_select_x, self.counter_command_select_y)
        time.sleep(pause)

        # Delta Alliance
        reputation.delta_alliance(self.delta_select_x, self.delta_select_y)
        time.sleep(pause)

        # Iconian Resistance
        reputation.iconian_resistance(self.iconian_select_x, self.iconian_select_y)
        time.sleep(pause)

        # Terran Task Force
        reputation.terran_task_force(self.terran_select_x, self.terran_select_y)
        time.sleep(pause)

        # Temporal Defence Initiative
        reputation.temporal_defence_initiative(self.temporal_select_x, self.temporal_select_y)
        time.sleep(pause)

        # Lukari Task Force
        reputation.lukari_task_force(self.lukari_select_x, self.lukari_select_y)
        time.sleep(pause)

        # Competetive Wargames
        reputation.competetive_wargames(self.competetive_select_x, self.competetive_select_y)
        time.sleep(pause)

        # Gamma Task Force
        reputation.gamma_task_force(self.gamma_select_x, self.gamma_select_y)
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
        pyautogui.moveTo(adm_folder_x, adm_folder_y, duration=dur)
        time.sleep(pause)
        print("[i]Clicking on Admiralty Folder")
        click(adm_folder_x, adm_folder_y)
        time.sleep(pause)

        # Open Progress Window
        pyautogui.moveTo(progress_x, progress_y, duration=dur)
        time.sleep(pause)
        print("[i]Clicking on Progress Tab")
        click(progress_x, progress_y)
        time.sleep(pause)

        # Scroll Up
        print("[i]Scrolling up")
        pyautogui.moveTo(bottomScroller_x, bottomScroller_y, duration=dur)
        time.sleep(pause)
        pyautogui.dragTo(topScroller_x, topScroller_y, duration=dur)
        time.sleep(pause)

        # Slot 1
        pyautogui.moveTo(adm_slot_1_x, adm_slot_1_y, duration=dur)
        time.sleep(pause)
        print("[i]Clicking on Slot 1")
        click(adm_slot_1_x, adm_slot_1_y)
        time.sleep(pause)

        # Slot 2
        pyautogui.moveTo(adm_slot_2_x, adm_slot_2_y, duration=dur)
        time.sleep(pause)
        print("[i]Clicking on Slot 2")
        click(adm_slot_2_x, adm_slot_2_y)
        time.sleep(pause)

        # Slot 3
        pyautogui.moveTo(adm_slot_3_x, adm_slot_3_y, duration=dur)
        time.sleep(pause)
        print("[i]Clicking on Slot 3")
        click(adm_slot_3_x, adm_slot_3_y)
        time.sleep(pause)

        # Slot 4
        pyautogui.moveTo(adm_slot_4_x, adm_slot_4_y, duration=dur)
        time.sleep(pause)
        print("[i]Clicking on Slot 4")
        click(adm_slot_4_x, adm_slot_4_y)
        time.sleep(pause)

        # Slot 5
        pyautogui.moveTo(adm_slot_5_x, adm_slot_5_y, duration=dur)
        time.sleep(pause)
        print("[i]Clicking on Slot 5")
        click(adm_slot_5_x, adm_slot_5_y)
        time.sleep(pause)

        # Slot 6
        pyautogui.moveTo(adm_slot_6_x, adm_slot_6_y, duration=dur)
        time.sleep(pause)
        print("[i]Clicking on Slot 6")
        click(adm_slot_6_x, adm_slot_6_y)
        time.sleep(pause)

        # Slot 7
        pyautogui.moveTo(adm_slot_7_x, adm_slot_7_y, duration=dur)
        time.sleep(pause)
        print("[i]Clicking on Slot 7")
        click(adm_slot_7_x, adm_slot_7_y)
        time.sleep(pause)

        # Slot 8
        pyautogui.moveTo(adm_slot_8_x, adm_slot_8_y, duration=dur)
        time.sleep(pause)
        print("[i]Clicking on Slot 8")
        click(adm_slot_8_x, adm_slot_8_y)
        time.sleep(pause)

        return

    # Run Duty Officers Automation
    def act_dutyofficers(self):
        # Open Duty Officers Folder
        pyautogui.moveTo(self.duff_folder_x, self.duff_folder_y, duration=dur)
        time.sleep(pause)
        print("[i]Clicking on DutyOffices Folder")
        click(self.duff_folder_x, self.duff_folder_y)
        time.sleep(pause)

        # Open Completed Window
        pyautogui.moveTo(self.completed_x, self.completed_y, duration=dur)
        time.sleep(pause)
        print("[i]Clicking on Completed")
        click(self.completed_x, self.completed_y)
        time.sleep(pause)

        # Collect Rewards
        pyautogui.moveTo(self.duff_1_x, self.duff_1_y, duration=dur)
        time.sleep(pause)
        for i in range(1, 22):
            print(f"[i]Player 2: Collecting reward #{i}")
            click(self.duff_1_x, self.duff_1_y)
            time.sleep(0.4)
            print(f"[i]Player 2 : reward #{i} collected")

        return

    # Set new DutyOfficers missions

    def duff_missions(self):
        # Open Duty Officers Folder
        pyautogui.moveTo(self.duff_folder_x, self.duff_folder_y, duration=dur)
        time.sleep(pause)
        print(f"[i]Player 2: Clicking on DutyOfficers Folder")
        click(self.duff_folder_x, self.duff_folder_y)
        time.sleep(pause)

        # Click on Personal
        pyautogui.moveTo(personal_x, personal_y, duration=dur)
        time.sleep(pause)
        print(f"[i]Player 2: Clicking on Personal")
        click(personal_x, personal_y)
        time.sleep(duff_pause)

        # Click on Filters
        pyautogui.moveTo(filters_x, filters_y, duration=dur)
        time.sleep(pause)
        print(f"[i]Player 1: Personal: Clicking Filters")
        click(filters_x, filters_y)
        time.sleep(duff_pause)

        # Click on Met Reqs
        pyautogui.moveTo(metReqs_x, metReqs_y, duration=dur)
        time.sleep(pause)
        print(f"[i]Player 1: Personal: Clicking on Met Reqs")
        click(metReqs_x, metReqs_y)
        time.sleep(duff_pause)
        click(metReqs_x, metReqs_y)
        pyautogui.doubleClick(metReqs_x, metReqs_y, button='left')

        # Start Planning & Executing for Personal Assignments
        self.planExecute()

        # Click on Engineering Assignments
        pyautogui.moveTo(engineering_x, engineering_y, duration=dur)
        time.sleep(pause)
        print(f"[i]Player 1: Clicking on Engineering")
        click(engineering_x, engineering_y)
        time.sleep(duff_pause)

        # Plan & Execute & Return to Department Heads
        self.planExecute()

        # Click on Science Assignments
        pyautogui.moveTo(science_x, science_y, duration=dur)
        time.sleep(pause)
        print("[i]Clicking on Science Assignment")
        click(science_x, science_y)
        time.sleep(duff_pause)

        # Plan & Execute & Return to Department Heads
        self.planExecute()

        # Click on Tactical Assignments
        pyautogui.moveTo(tactical_x, tactical_y, duration=dur)
        time.sleep(pause)
        print("[i]Clicking on Tactical Assignment")
        click(tactical_x, tactical_y)
        time.sleep(duff_pause)

        # Plan & Execute & Return to Department Heads
        self.planExecute()

        # Click on Security Assignments
        pyautogui.moveTo(security_x, security_y, duration=dur)
        time.sleep(pause)
        print("[i]Clicking on Security Assignment")
        click(security_x, security_y)
        time.sleep(duff_pause)

        # Plan & Execute & Return to Department Heads
        self.planExecute()

        # Click on Medical Assignments
        pyautogui.moveTo(medial_x, medical_y, duration=dur)
        time.sleep(pause)
        print("[i]Clicking on Medical Assignment")
        click(medial_x, medical_y)
        time.sleep(duff_pause)

        # Plan & Execute & Return to Department Heads
        self.planExecute()

        print("[i]Simulating keyboard for ']' key")
        keyboard.press_and_release("]")
        time.sleep(pause)

        return

    # General Plan & Begin
    def planExecute(self):
        # Plan & Begin
        for i in range(1, 6):
            print(f"[i]Player 2: Clicking on Plan #{i}")
            plan()
            print(f"[i]Player 2: Clicking on Begin Assignment #{i}")
            begin()

        # Return to Department Heads
        pyautogui.moveTo(department_x, department_y, duration=dur)
        time.sleep(pause)
        print("[i]Clicking on Department Heads")
        click(department_x, department_y)
        time.sleep(duff_pause)

        return


# General Plan
def plan():
    pyautogui.moveTo(plan_x, plan_y, duration=dur)
    time.sleep(pause)
    click(plan_x, plan_y)
    time.sleep(pause)

    return


# General Begin Assignment
def begin():
    pyautogui.moveTo(begin_x, begin_y, duration=dur)
    time.sleep(pause)
    click(begin_x, begin_y)
    time.sleep(duff_pause)

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
