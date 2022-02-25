from pytesseract import pytesseract
from PIL import ImageChops
from PIL import ImageGrab
from PIL import Image
import numpy as np
import cv2 as cv
import pyautogui
import win32con
import win32gui
import win32com
import win32api
import keyboard
import time
import os


class ComputerVision:
    # Parameters
    rectangles = []
    points = []
    top_windows = []
    results = []
    pytesser_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    liveImage = 'Images/Anchors/live_sc.jpg'

    def __init__(self, screenshot, button, threshold):
        self.screen_img = screenshot
        self.button_img = button
        self.threshold = threshold
        self.button_w = self.button_img.shape[1]
        self.button_h = self.button_img.shape[0]
        self.method = cv.TM_CCOEFF_NORMED
        self.result = cv.matchTemplate(self.screen_img, self.button_img, self.method)
        self.min_val, self.max_val, self.min_loc, self.max_loc = cv.minMaxLoc(self.result)

    def compare(self, threshold=0.5):
        locations = np.where(self.result >= threshold)
        locations = list(zip(*locations[::-1]))
        if len(locations) == 0:
            print("\n**** UNMATCHED! ****")
            return False

        else:
            print("\n **** MATCH-FOUND! ****")
            return True

    def process(self, debug_mode='rectangles'):
        locations = np.where(self.result >= self.threshold)
        locations = list(zip(*locations[::-1]))
        for loc in locations:
            rect = [int(loc[0]), int(loc[1]), self.button_w, self.button_h]
            self.rectangles.append(rect)

        self.rectangles, weight = cv.groupRectangles(self.rectangles, groupThreshold=1, eps=0.5)

        if len(self.rectangles):
            print(f"[i]Buttons Found!")
            line_color = (0, 255, 0)
            line_type = cv.LINE_4
            marker_color = (0, 0, 255)
            marker_type = cv.MORPH_CROSS

            for (x, y, w, h) in self.rectangles:
                center_x = x + int(w / 2)
                center_y = y + int(h / 2)
                if len(self.points) > 12:
                    break

                self.points.append((center_x, center_y))

                if debug_mode == 'rectangles':
                    top_left = (x, y)
                    bottom_right = (x + w, y + h)

                    cv.rectangle(self.screen_img, top_left, bottom_right, color=line_color, lineType=line_type, thickness=2)

                elif debug_mode == 'points':
                    cv.drawMarker(self.screen_img, (center_x, center_y),
                                  color=marker_color, markerType=marker_type,
                                  markerSize=40, thickness=2)

            if debug_mode:
                cv.imshow('Matches', self.screen_img)
                cv.waitKey()

                return

        else:
            print("[!]Button Not Found!")
            exit()

    def text_from_image(self, image):
        pytesseract.tesseract_cmd = pytesser_path

        text = pytesseract.image_to_string(image)

        return text

    def screen_capture(self):
        # Switch to STO Window
        for i in self.top_windows:
            if "star trek online" in f"{i[1]}".lower():
                print("[i]Switching to STO...")
                win32gui.ShowWindow(i[0], 5)
                win32gui.SetForegroundWindow(i[0])
                pos = win32gui.GetWindowRect(i[0])
                print(f"[i] Window Size: {pos}")
                print("[i] Taking Screenshot.")
                self.liveSC = pyautogui.screenshot()
                self.liveSC.save(self.liveImage)
                print("[i] Screenshot Saved.")

    def window_enumeration_handler(self, hwnd, top_windows):
        # Add windows to list
        top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

    def click(self, x, y):
        # Clear Mouse Status
        win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE, x, y, 0, 0)

        # Set Mouse Position
        win32api.SetCursorPos((x, y))

        # Commence Mouse Click
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

        # Clear Mouse Status
        win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE, x, y, 0, 0)


class WindowCapture:
    def __init__(self):
        self.codec = cv.VideoWriter_fourcc(*"mp4v")
        self.out = cv.VideoWriter("Automator.avi", self.codec, 60, (1920, 1080))
        cv.namedWindow("STO-Automator", cv.WINDOW_NORMAL)
        cv.resizeWindow("STO-Automator", 1024, 768)

    def capture(self):
        while True:
            img = pyautogui.screenshot()
            frame = np.array(img)
            frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            # self.out.write(frame)
            cv.imshow('STO-Automator', frame)

            if (cv.waitKey(1) & 0xFF) == ord('/'):
                cv.destroyAllWindows()
                break
