import cv2
import numpy as np

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    cap.open()

#img = cv2.imread("C:\\Users\\HP\\Desktop\\Aly\\C.jpg", cv2.IMREAD_GRAYSCALE)
while(1):
    ret, frame = cap.read()

    if not ret:
        print("Could not get frame")

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    green_lower = np.array([50, 50, 50])
    green_upper = np.array([70, 255, 255])

    # green_lower = np.array([255, 40, 255])
    # green_upper = np.array([255, 255, 255])

    mask = cv2.inRange(hsv_frame, green_lower, green_upper)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('original', frame)
    #cv2.imshow('masked', mask)
    cv2.imshow('res', res)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

