from cv2 import cv2
import numpy as np

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("output.avi", fourcc, 20.0, (640, 480))

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # gray video frame
    out.write(frame)  # storing original video
    cv2.imshow("frame", frame)

    cv2.imshow("gray", gray)
    # cv2.waitKey(0)

    # The function waitKey waits for a
    # key event infinitely or for delay . milliseconds, when it is positive.
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
