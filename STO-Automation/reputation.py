import pyautogui
import time
from time import gmtime, strftime
import win32api
import win32com.client
import win32con
import win32gui
import os

log = f"c:\\Users\\{os.getlogin()}\\Documents\\STO-Log.txt"
pause = 0.3
dur = 0.2

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


def discovery_legends(x, y):
    # Open Discovery Tab
    pyautogui.moveTo(discovery_tab_mouse_x, discovery_tab_mouse_y, duration=dur)
    time.sleep(pause)
    print("[i]========= Clicking on Discovery Tab =========")
    click(discovery_tab_mouse_x, discovery_tab_mouse_y)
    time.sleep(pause)

    # Project 1 Reward
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Project 1 Reward")
    click(project1_x, project1_y)
    time.sleep(pause)

    # Project 1
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Project 1")
    click(project1_x, project1_y)
    time.sleep(pause)

    # Click on Select Button
    pyautogui.moveTo(x, y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Select")
    click(x, y)
    time.sleep(pause)

    # Click on Fill All Button
    pyautogui.moveTo(fill_x, fill_y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Fill All")
    click(fill_x, fill_y)
    time.sleep(pause)

    # Click on Confirm Button
    pyautogui.moveTo(confirm_x, confirm_y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Confirm")
    click(confirm_x, confirm_y)
    time.sleep(pause)

    return


def task_force_omega(x, y):
    # Open Omega Tab
    pyautogui.moveTo(omega_tab_mouse_x, omega_tab_mouse_y, duration=dur)
    time.sleep(pause)
    print("[i]========= Clicking on Omega Tab =========")
    click(omega_tab_mouse_x, omega_tab_mouse_y)
    time.sleep(pause)

    # Project 1 Reward
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Project 1 Reward")
    click(project1_x, project1_y)
    time.sleep(pause)

    # Project 1
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Project 1")
    click(project1_x, project1_y)
    time.sleep(pause)

    # Click on Select Button
    pyautogui.moveTo(x, y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Select")
    click(x, y)
    time.sleep(pause)

    # Click on Fill All Button
    pyautogui.moveTo(fill_x, fill_y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Fill All")
    click(fill_x, fill_y)
    time.sleep(pause)

    # Click on Confirm Button
    pyautogui.moveTo(confirm_x, confirm_y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Confirm")
    click(confirm_x, confirm_y)
    time.sleep(pause)

    return


def nukara_strike_force(x, y):
    # Open Nukara Tab
    pyautogui.moveTo(nukara_tab_mouse_x, nukara_tab_mouse_y, duration=dur)
    time.sleep(pause)
    print("[i]========= Clicking on Nukara Tab =========")
    click(nukara_tab_mouse_x, nukara_tab_mouse_y)
    time.sleep(pause)

    # Project 1 Reward
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Project 1 Reward")
    click(project1_x, project1_y)
    time.sleep(pause)

    # Project 1
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Project 1")
    click(project1_x, project1_y)
    time.sleep(pause)

    # Click on Select Button
    pyautogui.moveTo(x, y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Select")
    click(x, y)
    time.sleep(pause)

    # Click on Fill All Button
    pyautogui.moveTo(fill_x, fill_y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Fill All")
    click(fill_x, fill_y)
    time.sleep(pause)

    # Click on Confirm Button
    pyautogui.moveTo(confirm_x, confirm_y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Confirm")
    click(confirm_x, confirm_y)
    time.sleep(pause)

    return


def new_romulus(x, y):
    # Open Romulus Tab
    pyautogui.moveTo(romulus_tab_mouse_x, romulus_tab_mouse_y, duration=dur)
    time.sleep(pause)
    print("[i]========= Clicking on Romulus Tab =========")
    click(romulus_tab_mouse_x, romulus_tab_mouse_y)
    time.sleep(pause)

    # Project 1 Reward
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Project 1 Reward")
    click(project1_x, project1_y)
    time.sleep(pause)

    # Project 1
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Project 1")
    click(project1_x, project1_y)
    time.sleep(pause)

    # Click on Select Button
    pyautogui.moveTo(x, y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Select")
    click(x, y)
    time.sleep(pause)

    # Click on Fill All Button
    pyautogui.moveTo(fill_x, fill_y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Fill All")
    click(fill_x, fill_y)
    time.sleep(pause)

    # Click on Confirm Button
    pyautogui.moveTo(confirm_x, confirm_y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Confirm")
    click(confirm_x, confirm_y)
    time.sleep(pause)

    return


def dyson_joint_command(x, y):
    # Open Dyson Tab
    pyautogui.moveTo(dyson_tab_mouse_x, dyson_tab_mouse_y, duration=dur)
    time.sleep(pause)
    print("[i]========= Clicking on Dyson Tab =========")
    click(dyson_tab_mouse_x, dyson_tab_mouse_y)
    time.sleep(pause)

    # Project 1 Reward
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Project 1 Reward")
    click(project1_x, project1_y)
    time.sleep(pause)

    # Project 1
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Project 1")
    click(project1_x, project1_y)
    time.sleep(pause)

    # Click on Select Button
    pyautogui.moveTo(x, y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Select")
    click(x, y)
    time.sleep(pause)

    # Click on Fill All Button
    pyautogui.moveTo(fill_x, fill_y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Fill All")
    click(fill_x, fill_y)
    time.sleep(pause)

    # Click on Confirm Button
    pyautogui.moveTo(confirm_x, confirm_y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Confirm")
    click(confirm_x, confirm_y)
    time.sleep(pause)

    return


def counter_command(x, y):
    # Open Counter-Command Tab
    pyautogui.moveTo(counter_command_tab_mouse_x, counter_command_tab_mouse_y, duration=dur)
    time.sleep(pause)
    print("[i]========= Clicking on Counter-Command Tab =========")
    click(counter_command_tab_mouse_x, counter_command_tab_mouse_y)
    time.sleep(pause)

    # Project 1 Reward
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Project 1 Reward")
    click(project1_x, project1_y)
    time.sleep(pause)

    # Project 1
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Project 1")
    click(project1_x, project1_y)
    time.sleep(pause)

    # Click on Select Button
    pyautogui.moveTo(x, y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Select")
    click(x, y)
    time.sleep(pause)

    # Click on Fill All Button
    pyautogui.moveTo(fill_x, fill_y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Fill All")
    click(fill_x, fill_y)
    time.sleep(pause)

    # Click on Confirm Button
    pyautogui.moveTo(confirm_x, confirm_y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Confirm")
    click(confirm_x, confirm_y)
    time.sleep(pause)

    return


def delta_alliance(x, y):
    # Open Delta Tab
    pyautogui.moveTo(delta_tab_mouse_x, delta_tab_mouse_y, duration=dur)
    time.sleep(pause)
    print("[i]========= Clicking on Delta Tab =========")
    click(delta_tab_mouse_x, delta_tab_mouse_y)
    time.sleep(pause)

    # Project 1 Reward
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Project 1 Reward")
    click(project1_x, project1_y)
    time.sleep(pause)

    # Project 1
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Project 1")
    click(project1_x, project1_y)
    time.sleep(pause)

    # Click on Select Button
    pyautogui.moveTo(x, y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Select")
    click(x, y)
    time.sleep(pause)

    # Click on Fill All Button
    pyautogui.moveTo(fill_x, fill_y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Fill All")
    click(fill_x, fill_y)
    time.sleep(pause)

    # Click on Confirm Button
    pyautogui.moveTo(confirm_x, confirm_y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Confirm")
    click(confirm_x, confirm_y)
    time.sleep(pause)

    return


def iconian_resistance(x, y):
    # Open Iconian Tab
    pyautogui.moveTo(iconian_tab_mouse_x, iconian_tab_mouse_y, duration=dur)
    time.sleep(pause)
    print("[i]========= Clicking on Iconian Tab =========")
    click(iconian_tab_mouse_x, iconian_tab_mouse_y)
    time.sleep(pause)

    # Project 1 Reward
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Project 1 Reward")
    click(project1_x, project1_y)
    time.sleep(pause)

    # Project 1
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Project 1")
    click(project1_x, project1_y)
    time.sleep(pause)

    # Click on Select Button
    pyautogui.moveTo(x, y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Select")
    click(x, y)
    time.sleep(pause)

    # Click on Fill All Button
    pyautogui.moveTo(fill_x, fill_y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Fill All")
    click(fill_x, fill_y)
    time.sleep(pause)

    # Click on Confirm Button
    pyautogui.moveTo(confirm_x, confirm_y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Confirm")
    click(confirm_x, confirm_y)
    time.sleep(pause)

    return


def terran_task_force(x, y):
    # Open Terran Tab
    pyautogui.moveTo(terran_tab_mouse_x, terran_tab_mouse_y, duration=dur)
    time.sleep(pause)
    print("[i]========= Clicking on Terran Tab =========")
    click(terran_tab_mouse_x, terran_tab_mouse_y)
    time.sleep(pause)

    # Project 1 Reward
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Project 1 Reward")
    click(project1_x, project1_y)
    time.sleep(pause)

    # Project 1
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Project 1")
    click(project1_x, project1_y)
    time.sleep(pause)

    # Click on Select Button
    pyautogui.moveTo(x, y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Select")
    click(x, y)
    time.sleep(pause)

    # Click on Fill All Button
    pyautogui.moveTo(fill_x, fill_y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Fill All")
    click(fill_x, fill_y)
    time.sleep(pause)

    # Click on Confirm Button
    pyautogui.moveTo(confirm_x, confirm_y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Confirm")
    click(confirm_x, confirm_y)
    time.sleep(pause)

    return


def temporal_defence_initiative(x, y):
    # Open Temporal Tab
    pyautogui.moveTo(temporal_tab_mouse_x, temporal_tab_mouse_y, duration=dur)
    time.sleep(pause)
    print("[i]========= Clicking on Temporal Tab =========")
    click(temporal_tab_mouse_x, temporal_tab_mouse_y)
    time.sleep(pause)

    # Project 1 Reward
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Project 1 Reward")
    click(project1_x, project1_y)
    time.sleep(pause)

    # Project 1
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Project 1")
    click(project1_x, project1_y)
    time.sleep(pause)

    # Click on Select Button
    pyautogui.moveTo(x, y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Select")
    click(x, y)
    time.sleep(pause)

    # Click on Fill All Button
    pyautogui.moveTo(fill_x, fill_y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Fill All")
    click(fill_x, fill_y)
    time.sleep(pause)

    # Click on Confirm Button
    pyautogui.moveTo(confirm_x, confirm_y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Confirm")
    click(confirm_x, confirm_y)
    time.sleep(pause)

    return


def lukari_task_force(x, y):
    # Open Lukari Tab
    pyautogui.moveTo(lukari_tab_mouse_x, lukari_tab_mouse_y, duration=dur)
    time.sleep(pause)
    print("[i]========= Clicking on Lukari Tab =========")
    click(lukari_tab_mouse_x, lukari_tab_mouse_y)
    time.sleep(pause)

    # Project 1 Reward
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Project 1 Reward")
    click(project1_x, project1_y)
    time.sleep(pause)

    # Project 1
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Project 1")
    click(project1_x, project1_y)
    time.sleep(pause)

    # Click on Select Button
    pyautogui.moveTo(x, y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Select")
    click(x, y)
    time.sleep(pause)

    # Click on Fill All Button
    pyautogui.moveTo(fill_x, fill_y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Fill All")
    click(fill_x, fill_y)
    time.sleep(pause)

    # Click on Confirm Button
    pyautogui.moveTo(confirm_x, confirm_y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Confirm")
    click(confirm_x, confirm_y)
    time.sleep(pause)

    return


def competetive_wargames(x, y):
    # Open Competetive Tab
    pyautogui.moveTo(competetive_tab_mouse_x, competetive_tab_mouse_y, duration=dur)
    time.sleep(pause)
    print("[i]========= Clicking on Competetive Tab =========")
    click(competetive_tab_mouse_x, competetive_tab_mouse_y)
    time.sleep(pause)

    # Project 1 Reward
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Project 1 Reward")
    click(project1_x, project1_y)
    time.sleep(pause)

    # Project 1
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Project 1")
    click(project1_x, project1_y)
    time.sleep(pause)

    # Click on Select Button
    pyautogui.moveTo(x, y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Select")
    click(x, y)
    time.sleep(pause)

    # Click on Fill All Button
    pyautogui.moveTo(fill_x, fill_y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Fill All")
    click(fill_x, fill_y)
    time.sleep(pause)

    # Click on Confirm Button
    pyautogui.moveTo(confirm_x, confirm_y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Confirm")
    click(confirm_x, confirm_y)
    time.sleep(pause)

    return


def gamma_task_force(x, y):
    # Open Gamma Tab
    pyautogui.moveTo(gamma_tab_mouse_x, gamma_tab_mouse_y, duration=dur)
    time.sleep(pause)
    print("[i]========= Clicking on Gamma Tab =========")
    click(gamma_tab_mouse_x, gamma_tab_mouse_y)
    time.sleep(pause)

    # Project 1 Reward
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Project 1 Reward")
    click(project1_x, project1_y)
    time.sleep(pause)

    # Project 1
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Project 1")
    click(project1_x, project1_y)
    time.sleep(pause)

    # Click on Select Button
    pyautogui.moveTo(x, y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Select")
    click(x, y)
    time.sleep(pause)

    # Click on Fill All Button
    pyautogui.moveTo(fill_x, fill_y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Fill All")
    click(fill_x, fill_y)
    time.sleep(pause)

    # Click on Confirm Button
    pyautogui.moveTo(confirm_x, confirm_y, duration=dur)
    time.sleep(pause)
    print("[i]Clicking on Confirm")
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
