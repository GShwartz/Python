from tkinter import filedialog
from threading import Thread
from datetime import date
import tkinter as tk
import datetime
import time
import cv2
import os


class VideoStreamWidget:
    def __init__(self, src):
        self.src = src
        self.capture = cv2.VideoCapture(self.src, cv2.CAP_DSHOW)
        self.detection = False
        self.timer_started = False
        self.frame_size = (int(self.capture.get(3)), int(self.capture.get(4)))
        self.detection_stopped_time = None

        self.thread = Thread(target=self.update, name="Update Thread")
        self.thread.daemon = True
        self.thread.start()

    def update(self):
        while True:
            if self.capture.isOpened():
                self.status, self.frame = self.capture.read()
                self.gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
                self.faces = face_cascade.detectMultiScale(self.gray, 1.3, 5)

                if len(self.faces) > 0:
                    if self.detection:
                        self.timer_started = False

                    else:
                        self.detection = True
                        self.current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H.%M.%S")
                        self.out = cv2.VideoWriter(
                            fr"{recording_dir}/{self.current_time}.mp4", video_code, 20.0, self.frame_size)
                        print("Recording started!")

                if self.detection:
                    if self.timer_started:
                        if (time.time() - self.detection_stopped_time) >= sec_to_rec_dectection:
                            self.detection = False
                            self.timer_started = False
                            self.out.release()
                            self.out.write(self.frame)
                            print("Recording Stopped!")
                    else:
                        self.timer_started = True
                        self.detection_stopped_time = time.time()

                if self.detection:
                    self.out.write(self.frame)

            time.sleep(.01)

    def show_datetime(self):
        date_font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
        dt = str(datetime.datetime.today().replace(microsecond=0))

        dt_frame = cv2.putText(self.frame, dt, (0, 470), date_font, 1, (255, 255, 255), 2, cv2.LINE_4)

    def show_frame(self):
        self.date_thread = Thread(target=self.show_datetime, name="Date Thread")
        self.date_thread.daemon = True
        self.date_thread.start()

        for (x, y, width, height) in self.faces:
            cv2.rectangle(self.frame, (x, y), (x + width, y + height), (0, 255, 255), 2)
            font = cv2.FONT_HERSHEY_PLAIN
            cv2.putText(self.frame, "Detector", ((x - width) + height, (y + height) - (width + 3)),
                        font, 0.7, (255, 255, 255), 1)

        cv2.imshow(f'Camera: {self.src}', self.frame)
        key = cv2.waitKey(1)

        if key == ord('q'):
            self.out.release()
            self.capture.release()
            print("User Exit!")
            cv2.destroyAllWindows()
            exit()

        elif key == ord("c"):
            current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H.%M.%S")
            imgname = os.path.join(fr"{recording_dir}", fr"{current_time}.jpg")
            cv2.imwrite(imgname, self.frame)
            print(f"Captured {imgname}.")


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    print("Choose video files location...")
    recording_dir = filedialog.askdirectory()
    if len(recording_dir) == 0:
        print("User cancelled, quitting...")
        exit()

    try:
        os.makedirs(recording_dir)

    except Exception as err:
        pass

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    video_code = cv2.VideoWriter_fourcc(*"mp4v")
    sec_to_rec_dectection = 30

    video_stream_widget = VideoStreamWidget(src=0)
    print("Starting camera...")
    time.sleep(1)

    while True:
        try:
            video_stream_widget.show_frame()
        except AttributeError:
            pass
