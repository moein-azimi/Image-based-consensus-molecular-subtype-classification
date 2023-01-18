import os
import pandas as pd
import numpy as np
import cv2
import shutil


path = 'E:/GE/Image-based consensus molecular subtype/test/CMS4tiles/'


x = [item for item in os.listdir(path) if item.endswith('.png')]  

def histogram_equalization(img):
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    img2[:, :, 0] = cv2.equalizeHist(img2[:, :, 0])
    img3 = cv2.cvtColor(img2, cv2.COLOR_YCrCb2BGR)
    return img3
    
    
for i in range (len(x)):
    img = cv2.imread(path+x[i])
    img = histogram_equalization(img)
    #resized = cv2.resize(img, (224,224), interpolation = cv2.INTER_AREA)
    cv2.imwrite(path+x[i], img)