import cv2
import numpy as np
import matplotlib.pyplot as plt

#create an empty black image
PICTURE = np.ones((700, 700, 3), dtype=np.int16)

#rectangle
cv2.rectangle(PICTURE, (100, 100), (412, 300), (255, 0, 255), 1)

#circle
cv2.circle(PICTURE, (500, 500), 60, (0, 255, 255), 3)

#line
cv2.line(PICTURE, (23, 80), (600, 560), (255, 255, 255), thickness=3)

#font
FONT = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(PICTURE, "Heyy", (300, 300), FONT, 4, (120, 34, 200), 2)

#display image
plt.imshow(PICTURE)
plt.show()