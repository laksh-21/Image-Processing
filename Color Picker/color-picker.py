import cv2
import numpy as np

img = cv2.imread(filename='data/colors.png')


def color(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # creates a 1x1 array with three channels technically a single pixel image
        bgr = np.ndarray(shape=(1, 1, 3), dtype=np.uint8)
        # assigns b, g, r values to the three channels
        bgr[0, 0] = img[y, x]
        # covert it to hsv values
        bgr = cv2.cvtColor(src=bgr, code=cv2.COLOR_BGR2HSV)
        print(bgr)

cv2.namedWindow('color', cv2.WINDOW_FREERATIO)
cv2.setMouseCallback('color', color)


while True:
    cv2.imshow('color', img)
    if cv2.waitKey(20) == ord('q'):
        break

cv2.destroyAllWindows()
