import cv2
import matplotlib.pyplot as plt
import numpy as np

# image to put logo on
img = cv2.imread(filename='F:/Codes/PythonCodes/Image Processing/OpenCV/Overlay/data/hedgie.jpg')
img = cv2.resize(src=img, dsize=(600, 600))
imgf = img
cv2.imshow('og', img)
# image of logo
logo = cv2.imread(filename='F:/Codes/PythonCodes/Image Processing/OpenCV/Overlay/data/yeet.jpg')
logo = cv2.resize(src=logo, dsize=(300, 300))
# create ROI

cols, rows, channels = logo.shape
roi = img[0:cols, 0:rows]

# create mask
logo_gray = cv2.cvtColor(src=logo, code=cv2.COLOR_BGR2GRAY)
ret, msk = cv2.threshold(src=logo_gray, thresh=150, maxval=255, type=cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(src=msk)

# blackout all the parts in ROI except the logo
bg = cv2.bitwise_and(roi, roi, mask=msk)

# put the original logo over the whited out area
fg = cv2.bitwise_and(logo, logo, mask=mask_inv)

# add both background and foreground
final = cv2.add(bg, fg)

# overlay it on the original image
imgf[0:logo.shape[1], 0:logo.shape[0]] = final

# show both the final result and original image
cv2.imshow(winname='Overlayed', mat=imgf)
cv2.waitKey(0)
cv2.destroyAllWindows()