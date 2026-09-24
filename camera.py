import cv2
import numpy as np

camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, frame = camera.read()
    frame = cv2.flip(frame, 1)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0, 100, 100])
    upper_red = np.array([5, 255, 255])

    mask = cv2.inRange(hsv, lower_red, upper_red)

    countours_red, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    detected_red = False

    for countour in countours_red:
        if cv2.contourArea(countour) > 500:

            detected_red = True

            x, y, w, h = cv2.boundingRect(countour)

            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

            cv2.putText(
                frame,
                "Merah",
                (x, y-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                2
            )

    lower_blue = np.array([100, 150, 0])
    upper_blue = np.array([140, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    countours_blue, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    detected_blue = False

    for countour in countours_blue:
        if cv2.contourArea(countour) > 500:

            detected_blue = True

            x, y, w, h = cv2.boundingRect(countour)

            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            cv2.putText(
                frame,
                "Biru",
                (x, y-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 0, 0),
                2
            )

    lower_yellow = np.array([20, 90, 100])
    upper_yellow = np.array([40, 255, 255])

    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    countours_yellow, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    detected_yellow = False

    for countour in countours_yellow:
        if cv2.contourArea(countour) > 500:

            detected_yellow = True

            x, y, w, h = cv2.boundingRect(countour)

            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)

            cv2.putText(
                frame,
                "Kuning",
                (x, y-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 255),
                2
            )

    if ret: 
        cv2.imshow("camera open", frame)

    if cv2.waitKey(1) == ord('f'):
        break

camera.release()
arduino.close()
cv2.destroyAllWindows()