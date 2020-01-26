import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

#import image
pic = Image.open("E:\Index.jpg")

#convert into array
pic_arr = np.asarray(pic)

#create a copy of image 
img_red = pic_arr.copy()

#set R and B values of all pixels to 0
img_red[:, :, 0] = 0
img_red[:, :, 2] = 0

#show image
plt.imshow(img_red)
plt.show()