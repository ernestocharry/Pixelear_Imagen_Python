
from PIL import Image
import os
import cv2
import numpy as np
from matplotlib import pyplot as plt


print(os.getcwd())

file_name = 'DSC_0054.jpg'
#-------------------------------------------------------------------------------
img = cv2.imread(file_name)
color = ('b','g','r')
plt.figure()
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()
#-------------------------------------------------------------------------------
img = cv2.imread(file_name)

def rgb_exclusion(image, channel):
    out = image
    if channel == 'R':
        out[:, :, 0] = 0
    elif channel == 'G':
        out[:, :, 1] = 0
    elif channel == 'B':
        out[:, :, 2] = 0
    return out

without_red = rgb_exclusion(img, 'R')
without_blue = rgb_exclusion(img, 'B')
without_green = rgb_exclusion(img, 'G')

plt.imshow(without_blue)
plt.axis('off')
plt.show()

import imageio
import matplotlib.pyplot as plt
import numpy as np
im = imageio.imread('DSC_0054.jpg')
im_r = np.zeros(np.shape(im))
im_r[:, :, 0] = im[:, :, 0]