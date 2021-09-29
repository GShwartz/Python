import os
import cv2
import time
import datetime

dr = f"C:\\Users\\{os.getlogin()}\\Desktop\\"
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
detection = False
detection_stopped_time = None
timer_started = False
sec_to_rec_dectection = 30
frame_size = (int(cap.get(3)), int(cap.get(4)))
video_code = cv2.VideoWriter_fourcc(*"mp4v")

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 6)

    if len(faces) > 0:
        if detection:
            timer_started = False

        else:
            detection = True
            current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H.%M.%S")
            out = cv2.VideoWriter(
                f"{dr}{current_time}.mp4", video_code, 20.0, frame_size)
            print("Recording started!")

    elif detection:
        if timer_started:
            if time.time() - detection_stopped_time >= sec_to_rec_dectection:
                detection = False
                timer_started = False
                out.release()
                print("Recording stopped!")
        else:
            timer_started = True
            detection_stopped_time = time.time()

    if detection:
        out.write(frame)

    for (x, y, width, height) in faces:
        cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 255), 2)

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) == ord('q'):
        break

out.release()
cap.release()
cv2.destroyAllWindows()
