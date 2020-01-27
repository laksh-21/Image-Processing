import cv2
import numpy
from os.path import abspath, dirname

BASE_PATH = abspath(dirname(__file__))
DATA_PATH = BASE_PATH + '/data/'
IMG_PATH = DATA_PATH + 'data.jpg'
img = cv2.imread(IMG_PATH, 0)

ret, thres = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)
gauss = cv2.adaptiveThreshold(img, 200, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 2)

cv2.imshow('og', img)
cv2.imshow('gauss', gauss)

cv2.waitKey(0)
cv2.destroyAllWindows()