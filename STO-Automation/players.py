from time import gmtime, strftime   # Display current time for logging.
import win32api             # Windows components.
import win32com.client      # Windows components.
import win32con             # Windows components.
import win32gui             # Windows components.
import pyautogui            # Graphic Automation.
import keyboard             # Keyboard Simulation.
import time                 # Pause between actions, Mouse drag Duration time.
import os                   # Get current logged in User and save log file in Documents.
import reputation           # Reputation module


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

        # self.filters_x, self.filters_y = 880, 50
        # self.metReqs_x, self.metReqs_y = 862, 99
        # self.personal_x, self.personal_y = 70, 130
        # self.department_x, self.department_y = 90, 165
        # self.engineering_x, self.engineering_y = 485, 360
        # self.operations_x, self.operations_y = 835, 360
        # self.science_x, self.science_y = 485, 465
        # self.science_plan_x, self.science_plan_y = 965, 265
        # self.medial_x, self.medical_y = 835, 465
        # self.tactical_x, self.tactical_y = 485, 570
        # self.security_x, self.security_y = 835, 570
        # self.plan_x, self.plan_y = 965, 255
        # self.begin_x, self.begin_y = 955, 1025

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
        with open(log, 'a+') as logger:
            # Open Admiralty Folder
            pyautogui.moveTo(self.adm_folder_x, self.adm_folder_y, duration=dur)
            time.sleep(pause)
            print("[i]Player 1: Clicking on Admiralty Folder")
            click(self.adm_folder_x, self.adm_folder_y)
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : "
                         f"Player 1: Clicked on Admiralty Folder.\n")
            time.sleep(pause)

            # Open Progress Window
            pyautogui.moveTo(self.progress_x, self.progress_y, duration=dur)
            time.sleep(pause)
            print("[i]Clicking on Progress Tab")
            click(self.progress_x, self.progress_y)
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : Player 1: Clicked on Progress Tab.\n")
            time.sleep(pause)

            # Slot 1
            pyautogui.moveTo(self.adm_slot_1_x, self.adm_slot_1_y, duration=dur)
            time.sleep(pause)
            print("[i]Clicking on Slot 1")
            click(self.adm_slot_1_x, self.adm_slot_1_y)
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : Player 1: Clicked on Slot 1.\n")
            time.sleep(pause)

            # Slot 2
            pyautogui.moveTo(self.adm_slot_2_x, self.adm_slot_2_y, duration=dur)
            time.sleep(pause)
            print("[i]Clicking on Slot 2")
            click(self.adm_slot_2_x, self.adm_slot_2_y)
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : Player 1: Clicked on Slot 2.\n")
            time.sleep(pause)

            # Slot 3
            pyautogui.moveTo(self.adm_slot_3_x, self.adm_slot_3_y, duration=dur)
            time.sleep(pause)
            print("[i]Clicking on Slot 3")
            click(self.adm_slot_3_x, self.adm_slot_3_y)
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : Player 1: Clicked on Slot 3.\n")
            time.sleep(pause)

            # Slot 4
            pyautogui.moveTo(self.adm_slot_4_x, self.adm_slot_4_y, duration=dur)
            time.sleep(pause)
            print("[i]Clicking on Slot 4")
            click(self.adm_slot_4_x, self.adm_slot_4_y)
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : Player 1: Clicked on Slot 4.\n")
            time.sleep(pause)

            # Slot 5
            pyautogui.moveTo(self.adm_slot_5_x, self.adm_slot_5_y, duration=dur)
            time.sleep(pause)
            print("[i]Clicking on Slot 5")
            click(self.adm_slot_5_x, self.adm_slot_5_y)
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : Player 1: Clicked on Slot 5.\n")
            time.sleep(pause)

            # Slot 6
            pyautogui.moveTo(self.adm_slot_6_x, self.adm_slot_6_y, duration=dur)
            time.sleep(pause)
            print("[i]Clicking on Slot 6")
            click(self.adm_slot_6_x, self.adm_slot_6_y)
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : Player 1: Clicked on Slot 6.\n")
            time.sleep(pause)

            # Slot 7
            pyautogui.moveTo(self.adm_slot_7_x, self.adm_slot_7_y, duration=dur)
            time.sleep(pause)
            print("[i]Clicking on Slot 7")
            click(self.adm_slot_7_x, self.adm_slot_7_y)
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : Player 1: Clicked on Slot 7.\n")
            time.sleep(pause)

            # Slot 8
            pyautogui.moveTo(self.adm_slot_8_x, self.adm_slot_8_y, duration=dur)
            time.sleep(pause)
            print("[i]Clicking on Slot 8")
            click(self.adm_slot_8_x, self.adm_slot_8_y)
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : Player 1:  Clicked on Slot 8.\n")
            time.sleep(pause)

            return

    # Run Duty Officers Automation
    def act_dutyofficers(self):
        with open(log, 'a+') as logger:
            # Open Duty Officers Folder
            pyautogui.moveTo(self.duff_folder_x, self.duff_folder_y, duration=dur)
            time.sleep(pause)
            print("[i]Clicking on DutyOfficers Folder")
            click(self.duff_folder_x, self.duff_folder_y)
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : "
                         f"Player 1: Clicked on DutyOfficers Folder.\n")
            time.sleep(pause)

            # Open Completed Window
            pyautogui.moveTo(self.completed_x, self.completed_y, duration=dur)
            time.sleep(pause)
            print("[i]Clicking on Completed")
            click(self.completed_x, self.completed_y)
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : "
                         f"Player 1: Clicked on Completed Tab.\n")
            time.sleep(pause)

            # Collect Rewards
            pyautogui.moveTo(self.duff_1_x, self.duff_1_y, duration=dur)
            time.sleep(pause)
            for i in range(1, 22):
                print(f"[i]Player 1: Collecting reward #{i}...")
                logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())} : "
                             f"Player 1: Collecting reward #{i}...\n")
                click(self.duff_1_x, self.duff_1_y)
                time.sleep(0.4)
                print(f"[i]Player 1: reward #{i} collected.")
                logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())} : "
                             f"Player 1: Collected Reward #{i}.\n")

    # Set new DutyOfficers missions
    def duff_missions(self):
        with open(log, 'a+') as logger:
            # Open Duty Officers Folder
            pyautogui.moveTo(self.duff_folder_x, self.duff_folder_y, duration=dur)
            time.sleep(pause)
            print(f"[i]Player 1: Clicking on DutyOfficers Folder")
            click(self.duff_folder_x, self.duff_folder_y)
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : "
                         f"Player 1: Clicked on DutyOfficers Folder.\n")
            time.sleep(pause)

            # Click on Personal
            pyautogui.moveTo(personal_x, personal_y, duration=dur)
            time.sleep(pause)
            print(f"[i]Player 1: Clicking on Personal")
            click(personal_x, personal_y)
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : "
                         f"Player 1: Clicked on Personal.\n")
            time.sleep(duff_pause)

            # Click on Filters
            pyautogui.moveTo(filters_x, filters_y, duration=dur)
            time.sleep(pause)
            print(f"[i]Player 1: Personal: Clicking Filters")
            click(filters_x, filters_y)
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : "
                         f"Player 1: Clicked on Filters.\n")
            time.sleep(duff_pause)

            # Click on Met Reqs
            pyautogui.moveTo(metReqs_x, metReqs_y, duration=dur)
            time.sleep(pause)
            print(f"[i]Player 1: Personal: Clicking on Met Reqs")
            click(metReqs_x, metReqs_y)
            time.sleep(duff_pause)
            click(metReqs_x, metReqs_y)
            pyautogui.doubleClick(metReqs_x, metReqs_y, button='left')
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : "
                         f"Player 1: Clicked on Met Reqs.\n")
            time.sleep(duff_pause)

            # Start Planning & Executing for Personal Assignments
            self.planExecute()

            # Click on Engineering Assignments
            pyautogui.moveTo(engineering_x, engineering_y, duration=dur)
            time.sleep(pause)
            print(f"[i]Player 1: Clicking on Engineering")
            click(engineering_x, engineering_y)
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : "
                         f"Player 1: Clicked on Engineering.\n")
            time.sleep(duff_pause)

            # Plan & Execute & Return to Department Heads
            self.planExecute()

            # Click on Science Assignments
            pyautogui.moveTo(science_x, science_y, duration=dur)
            time.sleep(pause)
            print("[i]Clicking on Science Assignment")
            click(science_x, science_y)
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : "
                         f"Player 1: Clicked on Science Assignments.\n")
            time.sleep(duff_pause)

            # Plan & Execute & Return to Department Heads
            self.planExecute()

            # Click on Tactical Assignments
            pyautogui.moveTo(tactical_x, tactical_y, duration=dur)
            time.sleep(pause)
            print("[i]Clicking on Tactical Assignment")
            click(tactical_x, tactical_y)
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : "
                         f"Player 1: Clicked on Tactical Assignments.\n")
            time.sleep(duff_pause)

            # Plan & Execute & Return to Department Heads
            self.planExecute()

            # Click on Security Assignments
            pyautogui.moveTo(security_x, security_y, duration=dur)
            time.sleep(pause)
            print("[i]Clicking on Security Assignment")
            click(security_x, security_y)
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : "
                         f"Player 1: Clicked on Security Assignments.\n")
            time.sleep(duff_pause)

            # Plan & Execute & Return to Department Heads
            self.planExecute()

            # Click on Medical Assignments
            pyautogui.moveTo(medial_x, medical_y, duration=dur)
            time.sleep(pause)
            print("[i]Clicking on Medical Assignment")
            click(medial_x, medical_y)
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : "
                         f"Player 1: Clicked on Medical Assignments.\n")
            time.sleep(duff_pause)

            # Plan & Execute & Return to Department Heads
            self.planExecute()

            print("[i]Simulating keyboard for ']' key")
            keyboard.press_and_release("]")
            time.sleep(pause)

            return

    # General Plan & Begin
    def planExecute(self):
        with open(log, 'a+') as logger:
            # Plan & Begin
            for i in range(1, 6):
                # Plan
                print(f"[i]Player 1: Clicking on Plan #{i}")
                self.plan()

                # Begin
                print(f"[i]Player 1: Personal: Clicking on Begin Assignment #{i}")
                self.begin()

            # Return to Department Heads
            pyautogui.moveTo(department_x, department_y, duration=dur)
            time.sleep(pause)
            print("[i]Clicking on Department Heads")
            click(department_x, department_y)
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : "
                         f"Player 1: Clicked on Department Heads.\n")
            time.sleep(duff_pause)

        return

    # General Plan
    def plan(self):
        with open(log, 'a+') as logger:
            pyautogui.moveTo(plan_x, plan_y, duration=dur)
            time.sleep(pause)
            click(plan_x, plan_y)
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : "
                         f"Player 1: Clicked on Plan.\n")
            time.sleep(pause)

        return

    # General Begin Assignment
    def begin(self):
        with open(log, 'a+') as logger:
            pyautogui.moveTo(begin_x, begin_y, duration=dur)
            time.sleep(pause)
            click(begin_x, begin_y)
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : "
                         f"Player 1: Clicked on Begin Assignment.\n")
            time.sleep(duff_pause)

        return


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
        self.top_scroller_x, self.top_scroller_y = 1040, 320
        self.bottom_scroller_x, self.bottom_scroller_y = 1040, 655

        # Duty Officers vars
        self.duff_folder_x, self.duff_folder_y = 410, 20
        self.completed_x, self.completed_y = 85, 235
        self.duff_1_x, self.duff_1_y = 935, 175

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
        with open(log, 'a+') as logger:
            # Open Admiralty Folder
            pyautogui.moveTo(self.adm_folder_x, self.adm_folder_y, duration=dur)
            time.sleep(pause)
            print("[i]Clicking on Admiralty Folder")
            click(self.adm_folder_x, self.adm_folder_y)
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : "
                         f"Player 2:  Clicked on Admiralty Folder.\n")
            time.sleep(pause)

            # Open Progress Window
            pyautogui.moveTo(self.progress_x, self.progress_y, duration=dur)
            time.sleep(pause)
            print("[i]Clicking on Progress Tab")
            click(self.progress_x, self.progress_y)
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : "
                         f"Player 2:  Clicked on Progress Tab.\n")
            time.sleep(pause)

            # Scroll Up
            print("[i]Scrolling up")
            pyautogui.moveTo(self.bottom_scroller_x, self.bottom_scroller_y, duration=dur)
            time.sleep(pause)
            pyautogui.dragTo(self.top_scroller_x, self.top_scroller_y, duration=dur)
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : "
                         f"Player 2:  Scrolling Up.\n")
            time.sleep(pause)

            # Slot 1
            pyautogui.moveTo(self.adm_slot_1_x, self.adm_slot_1_y, duration=dur)
            time.sleep(pause)
            print("[i]Clicking on Slot 1")
            click(self.adm_slot_1_x, self.adm_slot_1_y)
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : "
                         f"Player 2:  Clicked on Slot 1.\n")
            time.sleep(pause)

            # Slot 2
            pyautogui.moveTo(self.adm_slot_2_x, self.adm_slot_2_y, duration=dur)
            time.sleep(pause)
            print("[i]Clicking on Slot 2")
            click(self.adm_slot_2_x, self.adm_slot_2_y)
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : "
                         f"Player 2:  Clicked on Slot 2.\n")
            time.sleep(pause)

            # Slot 3
            pyautogui.moveTo(self.adm_slot_3_x, self.adm_slot_3_y, duration=dur)
            time.sleep(pause)
            print("[i]Clicking on Slot 3")
            click(self.adm_slot_3_x, self.adm_slot_3_y)
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : "
                         f"Player 2:  Clicked on Slot 3.\n")
            time.sleep(pause)

            # Slot 4
            pyautogui.moveTo(self.adm_slot_4_x, self.adm_slot_4_y, duration=dur)
            time.sleep(pause)
            print("[i]Clicking on Slot 4")
            click(self.adm_slot_4_x, self.adm_slot_4_y)
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : "
                         f"Player 2:  Clicked on Slot 4.\n")
            time.sleep(pause)

            # Slot 5
            pyautogui.moveTo(self.adm_slot_5_x, self.adm_slot_5_y, duration=dur)
            time.sleep(pause)
            print("[i]Clicking on Slot 5")
            click(self.adm_slot_5_x, self.adm_slot_5_y)
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : "
                         f"Player 2:  Clicked on Slot 5.\n")
            time.sleep(pause)

            # Slot 6
            pyautogui.moveTo(self.adm_slot_6_x, self.adm_slot_6_y, duration=dur)
            time.sleep(pause)
            print("[i]Clicking on Slot 6")
            click(self.adm_slot_6_x, self.adm_slot_6_y)
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : "
                         f"Player 2:  Clicked on Slot 6.\n")
            time.sleep(pause)

            # Slot 7
            pyautogui.moveTo(self.adm_slot_7_x, self.adm_slot_7_y, duration=dur)
            time.sleep(pause)
            print("[i]Clicking on Slot 7")
            click(self.adm_slot_7_x, self.adm_slot_7_y)
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : "
                         f"Player 2:  Clicked on Slot 7.\n")
            time.sleep(pause)

            # Slot 8
            pyautogui.moveTo(self.adm_slot_8_x, self.adm_slot_8_y, duration=dur)
            time.sleep(pause)
            print("[i]Clicking on Slot 8")
            click(self.adm_slot_8_x, self.adm_slot_8_y)
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : "
                         f"Player 2:  Clicked on Slot 8.\n")
            time.sleep(pause)

            return

    # Run Duty Officers Automation
    def act_dutyofficers(self):
        with open(log, 'a+') as logger:
            # Open Duty Officers Folder
            pyautogui.moveTo(self.duff_folder_x, self.duff_folder_y, duration=dur)
            time.sleep(pause)
            print("[i]Clicking on DutyOffices Folder")
            click(self.duff_folder_x, self.duff_folder_y)
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} :Player 2:  Open DutyOfficers Folder.\n")
            time.sleep(pause)

            # Open Completed Window
            pyautogui.moveTo(self.completed_x, self.completed_y, duration=dur)
            time.sleep(pause)
            print("[i]Clicking on Completed")
            click(self.completed_x, self.completed_y)
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} :Player 2:  Clicked on Completed.\n")
            time.sleep(pause)

            # Collect Rewards
            pyautogui.moveTo(self.duff_1_x, self.duff_1_y, duration=dur)
            time.sleep(pause)
            for i in range(1, 22):
                print(f"[i]Player 2: Collecting reward #{i}")
                logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())} : Player 2: Collecting reward.\n")
                click(self.duff_1_x, self.duff_1_y)
                time.sleep(0.4)
                print(f"[i]Player 2 : reward #{i} collected")
                logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', gmtime())} : Player 2: Reward collected.\n")

    # Set new DutyOfficers missions
    def duff_missions(self):
        with open(log, 'a+') as logger:
            # Open Duty Officers Folder
            pyautogui.moveTo(self.duff_folder_x, self.duff_folder_y, duration=dur)
            time.sleep(pause)
            print(f"[i]Player 1: Clicking on DutyOfficers Folder")
            click(self.duff_folder_x, self.duff_folder_y)
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : "
                         f"Player 1: Clicked on DutyOfficers Folder.\n")
            time.sleep(pause)

            # Click on Personal
            pyautogui.moveTo(personal_x, personal_y, duration=dur)
            time.sleep(pause)
            print(f"[i]Player 1: Clicking on Personal")
            click(personal_x, personal_y)
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : "
                         f"Player 1: Clicked on Personal.\n")
            time.sleep(duff_pause)

            # Click on Filters
            pyautogui.moveTo(filters_x, filters_y, duration=dur)
            time.sleep(pause)
            print(f"[i]Player 1: Personal: Clicking Filters")
            click(filters_x, filters_y)
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : "
                         f"Player 1: Clicked on Filters.\n")
            time.sleep(duff_pause)

            # Click on Met Reqs
            pyautogui.moveTo(metReqs_x, metReqs_y, duration=dur)
            time.sleep(pause)
            print(f"[i]Player 1: Personal: Clicking on Met Reqs")
            click(metReqs_x, metReqs_y)
            time.sleep(duff_pause)
            click(metReqs_x, metReqs_y)
            pyautogui.doubleClick(metReqs_x, metReqs_y, button='left')
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : "
                         f"Player 1: Clicked on Met Reqs.\n")

            # Clear Mouse Status
            win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE, metReqs_x, metReqs_y, 0, 0)
            time.sleep(duff_pause)

            # Start Planning & Executing for Personal Assignments
            self.planExecute()

            # Click on Engineering Assignments
            pyautogui.moveTo(engineering_x, engineering_y, duration=dur)
            time.sleep(pause)
            print(f"[i]Player 1: Clicking on Engineering")
            click(engineering_x, engineering_y)
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : "
                         f"Player 1: Clicked on Engineering.\n")
            time.sleep(duff_pause)

            # Plan & Execute & Return to Department Heads
            self.planExecute()

            # Click on Science Assignments
            pyautogui.moveTo(science_x, science_y, duration=dur)
            time.sleep(pause)
            print("[i]Clicking on Science Assignment")
            click(science_x, science_y)
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : "
                         f"Player 1: Clicked on Science Assignments.\n")
            time.sleep(duff_pause)

            # Plan & Execute & Return to Department Heads
            self.planExecute()

            # Click on Tactical Assignments
            pyautogui.moveTo(tactical_x, tactical_y, duration=dur)
            time.sleep(pause)
            print("[i]Clicking on Tactical Assignment")
            click(tactical_x, tactical_y)
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : "
                         f"Player 1: Clicked on Tactical Assignments.\n")
            time.sleep(duff_pause)

            # Plan & Execute & Return to Department Heads
            self.planExecute()

            # Click on Security Assignments
            pyautogui.moveTo(security_x, security_y, duration=dur)
            time.sleep(pause)
            print("[i]Clicking on Security Assignment")
            click(security_x, security_y)
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : "
                         f"Player 1: Clicked on Security Assignments.\n")
            time.sleep(duff_pause)

            # Plan & Execute & Return to Department Heads
            self.planExecute()

            # Click on Medical Assignments
            pyautogui.moveTo(medial_x, medical_y, duration=dur)
            time.sleep(pause)
            print("[i]Clicking on Medical Assignment")
            click(medial_x, medical_y)
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : "
                         f"Player 1: Clicked on Medical Assignments.\n")
            time.sleep(duff_pause)

            # Plan & Execute & Return to Department Heads
            self.planExecute()

            print("[i]Simulating keyboard for ']' key")
            keyboard.press_and_release("]")
            time.sleep(pause)

            return

    # General Plan & Begin
    def planExecute(self):
        with open(log, 'a+') as logger:
            # Plan & Begin
            for i in range(1, 6):
                # Plan
                print(f"[i]Player 1: Clicking on Plan #{i}")
                self.plan()

                # Begin
                print(f"[i]Player 1: Personal: Clicking on Begin Assignment #{i}")
                self.begin()

            # Return to Department Heads
            pyautogui.moveTo(department_x, department_y, duration=dur)
            time.sleep(pause)
            print("[i]Clicking on Department Heads")
            click(department_x, department_y)
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : "
                         f"Player 1: Clicked on Department Heads.\n")
            time.sleep(duff_pause)

        return

    # General Plan
    def plan(self):
        with open(log, 'a+') as logger:
            pyautogui.moveTo(plan_x, plan_y, duration=dur)
            time.sleep(pause)
            click(plan_x, plan_y)
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : "
                         f"Player 1: Clicked on Plan.\n")
            # time.sleep(pause)

        return

    # General Begin Assignment
    def begin(self):
        with open(log, 'a+') as logger:
            pyautogui.moveTo(begin_x, begin_y, duration=dur)
            time.sleep(pause)
            click(begin_x, begin_y)
            logger.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : "
                         f"Player 1: Clicked on Begin Assignment.\n")
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


# Setup Assignments Coordinates
department_x, department_y = 90, 165
filters_x, filters_y = 880, 50
metReqs_x, metReqs_y = 862, 99
personal_x, personal_y = 70, 130
engineering_x, engineering_y = 485, 360
operations_x, operations_y = 835, 360
science_x, science_y = 485, 465
science_plan_x, science_plan_y = 965, 265
medial_x, medical_y = 835, 465
tactical_x, tactical_y = 485, 570
security_x, security_y = 835, 570
plan_x, plan_y = 965, 255
begin_x, begin_y = 955, 1025

duff_pause = 1.5
pause = 0.2
dur = 0.2
log = f"c:\\Users\\{os.getlogin()}\\Documents\\STO-Log.txt"