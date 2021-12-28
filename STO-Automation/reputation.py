import pyautogui
import time
from time import gmtime, strftime
import win32api
import win32com.client
import win32con
import win32gui
import os

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


def discovery_legends(x, y, player):
    # Open Discovery Tab
    print(f"[i] Player #{player}: Clicking on Discovery Tab")
    pyautogui.moveTo(discovery_tab_mouse_x, discovery_tab_mouse_y, duration=dur)
    time.sleep(pause)
    click(discovery_tab_mouse_x, discovery_tab_mouse_y)
    time.sleep(pause)

    # Project 1 Reward
    print(f"[i] Player #{player}: Clicking on Project 1 Reward")
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    click(project1_x, project1_y)
    time.sleep(pause)

    # Project 1
    print(f"[i] Player #{player}: Clicking on Project 1")
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    click(project1_x, project1_y)
    time.sleep(pause)

    # Click on Select Button
    print(f"[i] Player #{player}: Clicking on Select")
    pyautogui.moveTo(x, y, duration=dur)
    time.sleep(pause)
    click(x, y)
    time.sleep(pause)

    # Click on Fill All Button
    print(f"[i] Player #{player}: Clicking on Fill All")
    pyautogui.moveTo(fill_x, fill_y, duration=dur)
    time.sleep(pause)
    click(fill_x, fill_y)
    time.sleep(pause)

    # Click on Confirm Button
    print(f"[i] Player #{player}: Clicking on Confirm")
    pyautogui.moveTo(confirm_x, confirm_y, duration=dur)
    time.sleep(pause)
    click(confirm_x, confirm_y)
    time.sleep(pause)

    return


def task_force_omega(x, y, player):
    # Open Omega Tab
    print(f"[i] Player #{player}: Clicking on Omega Tab")
    pyautogui.moveTo(omega_tab_mouse_x, omega_tab_mouse_y, duration=dur)
    time.sleep(pause)
    click(omega_tab_mouse_x, omega_tab_mouse_y)
    time.sleep(pause)

    # Project 1 Reward
    print(f"[i] Player #{player}: Clicking on Project 1 Reward")
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    click(project1_x, project1_y)
    time.sleep(pause)

    # Project 1
    print(f"[i] Player #{player}: Clicking on Project 1")
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    click(project1_x, project1_y)
    time.sleep(pause)

    # Click on Select Button
    print(f"[i] Player #{player}: Clicking on Select")
    pyautogui.moveTo(x, y, duration=dur)
    time.sleep(pause)
    click(x, y)
    time.sleep(pause)

    # Click on Fill All Button
    print(f"[i] Player #{player}: Clicking on Fill All")
    pyautogui.moveTo(fill_x, fill_y, duration=dur)
    time.sleep(pause)
    click(fill_x, fill_y)
    time.sleep(pause)

    # Click on Confirm Button
    print(f"[i] Player #{player}: Clicking on Confirm")
    pyautogui.moveTo(confirm_x, confirm_y, duration=dur)
    time.sleep(pause)
    click(confirm_x, confirm_y)
    time.sleep(pause)

    return


def nukara_strike_force(x, y, player):
    # Open Nukara Tab
    print(f"[i] Player #{player}: Clicking on Nukara Tab")
    pyautogui.moveTo(nukara_tab_mouse_x, nukara_tab_mouse_y, duration=dur)
    time.sleep(pause)
    click(nukara_tab_mouse_x, nukara_tab_mouse_y)
    time.sleep(pause)

    # Project 1 Reward
    print(f"[i] Player #{player}: Clicking on Project 1 Reward")
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    click(project1_x, project1_y)
    time.sleep(pause)

    # Project 1
    print(f"[i] Player #{player}: Clicking on Project 1")
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    click(project1_x, project1_y)
    time.sleep(pause)

    # Click on Select Button
    print(f"[i] Player #{player}: Clicking on Select")
    pyautogui.moveTo(x, y, duration=dur)
    time.sleep(pause)
    click(x, y)
    time.sleep(pause)

    # Click on Fill All Button
    print(f"[i] Player #{player}: Clicking on Fill All")
    pyautogui.moveTo(fill_x, fill_y, duration=dur)
    time.sleep(pause)
    click(fill_x, fill_y)
    time.sleep(pause)

    # Click on Confirm Button
    print(f"[i] Player #{player}: Clicking on Confirm")
    pyautogui.moveTo(confirm_x, confirm_y, duration=dur)
    time.sleep(pause)
    click(confirm_x, confirm_y)
    time.sleep(pause)

    return


def new_romulus(x, y, player):
    # Open Romulus Tab
    print(f"[i] Player #{player}: Clicking on Romulus Tab")
    pyautogui.moveTo(romulus_tab_mouse_x, romulus_tab_mouse_y, duration=dur)
    time.sleep(pause)
    click(romulus_tab_mouse_x, romulus_tab_mouse_y)
    time.sleep(pause)

    # Project 1 Reward
    print(f"[i] Player #{player}: Clicking on Project 1 Reward")
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    click(project1_x, project1_y)
    time.sleep(pause)

    # Project 1
    print(f"[i] Player #{player}: Clicking on Project 1")
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    click(project1_x, project1_y)
    time.sleep(pause)

    # Click on Select Button
    print(f"[i] Player #{player}: Clicking on Select")
    pyautogui.moveTo(x, y, duration=dur)
    time.sleep(pause)
    click(x, y)
    time.sleep(pause)

    # Click on Fill All Button
    print(f"[i] Player #{player}: Clicking on Fill All")
    pyautogui.moveTo(fill_x, fill_y, duration=dur)
    time.sleep(pause)
    click(fill_x, fill_y)
    time.sleep(pause)

    # Click on Confirm Button
    print(f"[i] Player #{player}: Clicking on Confirm")
    pyautogui.moveTo(confirm_x, confirm_y, duration=dur)
    time.sleep(pause)
    click(confirm_x, confirm_y)
    time.sleep(pause)

    return


def dyson_joint_command(x, y, player):
    # Open Dyson Tab
    print(f"[i] Player #{player}: Clicking on Dyson Tab")
    pyautogui.moveTo(dyson_tab_mouse_x, dyson_tab_mouse_y, duration=dur)
    time.sleep(pause)
    click(dyson_tab_mouse_x, dyson_tab_mouse_y)
    time.sleep(pause)

    # Project 1 Reward
    print(f"[i] Player #{player}: Clicking on Project 1 Reward")
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    click(project1_x, project1_y)
    time.sleep(pause)

    # Project 1
    print(f"[i] Player #{player}: Clicking on Project 1")
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    click(project1_x, project1_y)
    time.sleep(pause)

    # Click on Select Button
    print(f"[i] Player #{player}: Clicking on Select")
    pyautogui.moveTo(x, y, duration=dur)
    time.sleep(pause)
    click(x, y)
    time.sleep(pause)

    # Click on Fill All Button
    print(f"[i] Player #{player}: Clicking on Fill All")
    pyautogui.moveTo(fill_x, fill_y, duration=dur)
    time.sleep(pause)
    click(fill_x, fill_y)
    time.sleep(pause)

    # Click on Confirm Button
    print(f"[i] Player #{player}: Clicking on Confirm")
    pyautogui.moveTo(confirm_x, confirm_y, duration=dur)
    time.sleep(pause)
    click(confirm_x, confirm_y)
    time.sleep(pause)

    return


def counter_command(x, y, player):
    # Open Counter-Command Tab
    print(f"[i] Player #{player}: Clicking on Counter-Command Tab")
    pyautogui.moveTo(counter_command_tab_mouse_x, counter_command_tab_mouse_y, duration=dur)
    time.sleep(pause)
    click(counter_command_tab_mouse_x, counter_command_tab_mouse_y)
    time.sleep(pause)

    # Project 1 Reward
    print(f"[i] Player #{player}: Clicking on Project 1 Reward")
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    click(project1_x, project1_y)
    time.sleep(pause)

    # Project 1
    print(f"[i] Player #{player}: Clicking on Project 1")
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    click(project1_x, project1_y)
    time.sleep(pause)

    # Click on Select Button
    print(f"[i] Player #{player}: Clicking on Select")
    pyautogui.moveTo(x, y, duration=dur)
    time.sleep(pause)
    click(x, y)
    time.sleep(pause)

    # Click on Fill All Button
    print(f"[i] Player #{player}: Clicking on Fill All")
    pyautogui.moveTo(fill_x, fill_y, duration=dur)
    time.sleep(pause)
    click(fill_x, fill_y)
    time.sleep(pause)

    # Click on Confirm Button
    print(f"[i] Player #{player}: Clicking on Confirm")
    pyautogui.moveTo(confirm_x, confirm_y, duration=dur)
    time.sleep(pause)
    click(confirm_x, confirm_y)
    time.sleep(pause)

    return


def delta_alliance(x, y, player):
    # Open Delta Tab
    print(f"[i] Player #{player}: Clicking on Delta Tab")
    pyautogui.moveTo(delta_tab_mouse_x, delta_tab_mouse_y, duration=dur)
    time.sleep(pause)
    click(delta_tab_mouse_x, delta_tab_mouse_y)
    time.sleep(pause)

    # Project 1 Reward
    print(f"[i] Player #{player}: Clicking on Project 1 Reward")
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    click(project1_x, project1_y)
    time.sleep(pause)

    # Project 1
    print(f"[i] Player #{player}: Clicking on Project 1")
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    click(project1_x, project1_y)
    time.sleep(pause)

    # Click on Select Button
    print(f"[i] Player #{player}: Clicking on Select")
    pyautogui.moveTo(x, y, duration=dur)
    time.sleep(pause)
    click(x, y)
    time.sleep(pause)

    # Click on Fill All Button
    print(f"[i] Player #{player}: Clicking on Fill All")
    pyautogui.moveTo(fill_x, fill_y, duration=dur)
    time.sleep(pause)
    click(fill_x, fill_y)
    time.sleep(pause)

    # Click on Confirm Button
    print(f"[i] Player #{player}: Clicking on Confirm")
    pyautogui.moveTo(confirm_x, confirm_y, duration=dur)
    time.sleep(pause)
    click(confirm_x, confirm_y)
    time.sleep(pause)

    return


def iconian_resistance(x, y, player):
    # Open Iconian Tab
    print(f"[i] Player #{player}: Clicking on Iconian Tab")
    pyautogui.moveTo(iconian_tab_mouse_x, iconian_tab_mouse_y, duration=dur)
    time.sleep(pause)
    click(iconian_tab_mouse_x, iconian_tab_mouse_y)
    time.sleep(pause)

    # Project 1 Reward
    print(f"[i] Player #{player}: Clicking on Project 1 Reward")
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    click(project1_x, project1_y)
    time.sleep(pause)

    # Project 1
    print(f"[i] Player #{player}: Clicking on Project 1")
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    click(project1_x, project1_y)
    time.sleep(pause)

    # Click on Select Button
    print(f"[i] Player #{player}: Clicking on Select")
    pyautogui.moveTo(x, y, duration=dur)
    time.sleep(pause)
    click(x, y)
    time.sleep(pause)

    # Click on Fill All Button
    print(f"[i] Player #{player}: Clicking on Fill All")
    pyautogui.moveTo(fill_x, fill_y, duration=dur)
    time.sleep(pause)
    click(fill_x, fill_y)
    time.sleep(pause)

    # Click on Confirm Button
    print(f"[i] Player #{player}: Clicking on Confirm")
    pyautogui.moveTo(confirm_x, confirm_y, duration=dur)
    time.sleep(pause)
    click(confirm_x, confirm_y)
    time.sleep(pause)

    return


def terran_task_force(x, y, player):
    # Open Terran Tab
    pyautogui.moveTo(terran_tab_mouse_x, terran_tab_mouse_y, duration=dur)
    time.sleep(pause)
    print(f"[i] Player #{player}: Clicking on Terran Tab")
    click(terran_tab_mouse_x, terran_tab_mouse_y)
    time.sleep(pause)

    # Project 1 Reward
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    print(f"[i] Player #{player}: Clicking on Project 1 Reward")
    click(project1_x, project1_y)
    time.sleep(pause)

    # Project 1
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    print(f"[i] Player #{player}: Clicking on Project 1")
    click(project1_x, project1_y)
    time.sleep(pause)

    # Click on Select Button
    pyautogui.moveTo(x, y, duration=dur)
    time.sleep(pause)
    print(f"[i] Player #{player}: Clicking on Select")
    click(x, y)
    time.sleep(pause)

    # Click on Fill All Button
    pyautogui.moveTo(fill_x, fill_y, duration=dur)
    time.sleep(pause)
    print(f"[i] Player #{player}: Clicking on Fill All")
    click(fill_x, fill_y)
    time.sleep(pause)

    # Click on Confirm Button
    pyautogui.moveTo(confirm_x, confirm_y, duration=dur)
    time.sleep(pause)
    print(f"[i] Player #{player}: Clicking on Confirm")
    click(confirm_x, confirm_y)
    time.sleep(pause)

    return


def temporal_defence_initiative(x, y, player):
    # Open Temporal Tab
    pyautogui.moveTo(temporal_tab_mouse_x, temporal_tab_mouse_y, duration=dur)
    time.sleep(pause)
    print(f"[i] Player #{player}: Clicking on Temporal Tab")
    click(temporal_tab_mouse_x, temporal_tab_mouse_y)
    time.sleep(pause)

    # Project 1 Reward
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    print(f"[i] Player #{player}: Clicking on Project 1 Reward")
    click(project1_x, project1_y)
    time.sleep(pause)

    # Project 1
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    print(f"[i] Player #{player}: Clicking on Project 1")
    click(project1_x, project1_y)
    time.sleep(pause)

    # Click on Select Button
    pyautogui.moveTo(x, y, duration=dur)
    time.sleep(pause)
    print(f"[i] Player #{player}: Clicking on Select")
    click(x, y)
    time.sleep(pause)

    # Click on Fill All Button
    pyautogui.moveTo(fill_x, fill_y, duration=dur)
    time.sleep(pause)
    print(f"[i] Player #{player}: Clicking on Fill All")
    click(fill_x, fill_y)
    time.sleep(pause)

    # Click on Confirm Button
    pyautogui.moveTo(confirm_x, confirm_y, duration=dur)
    time.sleep(pause)
    print(f"[i] Player #{player}: Clicking on Confirm")
    click(confirm_x, confirm_y)
    time.sleep(pause)

    return


def lukari_task_force(x, y, player):
    # Open Lukari Tab
    pyautogui.moveTo(lukari_tab_mouse_x, lukari_tab_mouse_y, duration=dur)
    time.sleep(pause)
    print(f"[i] Player #{player}: Clicking on Lukari Tab")
    click(lukari_tab_mouse_x, lukari_tab_mouse_y)
    time.sleep(pause)

    # Project 1 Reward
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    print(f"[i] Player #{player}: Clicking on Project 1 Reward")
    click(project1_x, project1_y)
    time.sleep(pause)

    # Project 1
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    print(f"[i] Player #{player}: Clicking on Project 1")
    click(project1_x, project1_y)
    time.sleep(pause)

    # Click on Select Button
    pyautogui.moveTo(x, y, duration=dur)
    time.sleep(pause)
    print(f"[i] Player #{player}: Clicking on Select")
    click(x, y)
    time.sleep(pause)

    # Click on Fill All Button
    pyautogui.moveTo(fill_x, fill_y, duration=dur)
    time.sleep(pause)
    print(f"[i] Player #{player}: Clicking on Fill All")
    click(fill_x, fill_y)
    time.sleep(pause)

    # Click on Confirm Button
    pyautogui.moveTo(confirm_x, confirm_y, duration=dur)
    time.sleep(pause)
    print(f"[i] Player #{player}: Clicking on Confirm")
    click(confirm_x, confirm_y)
    time.sleep(pause)

    return


def competetive_wargames(x, y, player):
    # Open Competetive Tab
    pyautogui.moveTo(competetive_tab_mouse_x, competetive_tab_mouse_y, duration=dur)
    time.sleep(pause)
    print(f"[i] Player #{player}: Clicking on Competetive Tab")
    click(competetive_tab_mouse_x, competetive_tab_mouse_y)
    time.sleep(pause)

    # Project 1 Reward
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    print(f"[i] Player #{player}: Clicking on Project 1 Reward")
    click(project1_x, project1_y)
    time.sleep(pause)

    # Project 1
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    print(f"[i] Player #{player}: Clicking on Project 1")
    click(project1_x, project1_y)
    time.sleep(pause)

    # Click on Select Button
    pyautogui.moveTo(x, y, duration=dur)
    time.sleep(pause)
    print(f"[i] Player #{player}: Clicking on Select")
    click(x, y)
    time.sleep(pause)

    # Click on Fill All Button
    pyautogui.moveTo(fill_x, fill_y, duration=dur)
    time.sleep(pause)
    print(f"[i] Player #{player}: Clicking on Fill All")
    click(fill_x, fill_y)
    time.sleep(pause)

    # Click on Confirm Button
    pyautogui.moveTo(confirm_x, confirm_y, duration=dur)
    time.sleep(pause)
    print(f"[i] Player #{player}: Clicking on Confirm")
    click(confirm_x, confirm_y)
    time.sleep(pause)

    return


def gamma_task_force(x, y, player):
    # Open Gamma Tab
    pyautogui.moveTo(gamma_tab_mouse_x, gamma_tab_mouse_y, duration=dur)
    time.sleep(pause)
    print(f"[i] Player #{player}: Clicking on Gamma Tab")
    click(gamma_tab_mouse_x, gamma_tab_mouse_y)
    time.sleep(pause)

    # Project 1 Reward
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    print(f"[i] Player #{player}: Clicking on Project 1 Reward")
    click(project1_x, project1_y)
    time.sleep(pause)

    # Project 1
    pyautogui.moveTo(project1_x, project1_y, duration=dur)
    time.sleep(pause)
    print(f"[i] Player #{player}: Clicking on Project 1")
    click(project1_x, project1_y)
    time.sleep(pause)

    # Click on Select Button
    pyautogui.moveTo(x, y, duration=dur)
    time.sleep(pause)
    print(f"[i] Player #{player}: Clicking on Select")
    click(x, y)
    time.sleep(pause)

    # Click on Fill All Button
    pyautogui.moveTo(fill_x, fill_y, duration=dur)
    time.sleep(pause)
    print(f"[i] Player #{player}: Clicking on Fill All")
    click(fill_x, fill_y)
    time.sleep(pause)

    # Click on Confirm Button
    pyautogui.moveTo(confirm_x, confirm_y, duration=dur)
    time.sleep(pause)
    print(f"[i] Player #{player}: Clicking on Confirm")
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
