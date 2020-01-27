import cv2
import numpy

img = cv2.imread('F:/Codes/PythonCodes/Image Processing/OpenCV/Thresholding/data/data.jpg', 0)

ret, thres = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)
gauss = cv2.adaptiveThreshold(img, 200, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 2)

cv2.imshow('og', img)
cv2.imshow('gauss', gauss)

cv2.waitKey(0)
cv2.destroyAllWindows()