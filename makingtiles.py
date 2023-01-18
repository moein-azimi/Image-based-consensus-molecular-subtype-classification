import cv2
import os
import numpy as np 
path = './GE/'
path2 = './GE_b/'

x = [item for item in os.listdir(path) if item.endswith('.png')]
print(x)

'''
def histogram_equalization(img):
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    img2[:, :, 0] = cv2.equalizeHist(img2[:, :, 0])
    img3 = cv2.cvtColor(img2, cv2.COLOR_YCrCb2BGR)
    return img3
'''

'''
for i in range (len(x)):
    img = cv2.imread(path+x[i])
    #img = histogram_equalization(img)
    numrows, numcols = 7, 7
    height = int(img.shape[0] / numrows)
    width = int(img.shape[1] / numcols)
    for row in range(numrows):
        for col in range(numcols):
            y0 = row * height
            y1 = y0 + height
            x0 = col * width
            x1 = x0 + width
            img1 = img[y0:y1, x0:x1]
            resized = cv2.resize(img1, (224,224), interpolation = cv2.INTER_AREA)
            cv2.imwrite(path2+f'{x[i]}'+'-'+f'{row}'+'-'+f'{col}'+'.png', resized)
'''          
         

for m in range(2):
    for i in range (len(x)):
        img = cv2.imread(path+x[i])
        img = img[m*100:,m*100:]
        h,w = img.shape[:2]
        row = int(h/512)
        col = int(w/512)
        #print(row, col)
        for j in range(row):
            #print(h*j)
            for k in range(col):
                #print(k*w)
                blank_image = np.zeros((512,512,3), np.uint8)
                blank_image[0:512,0:512] = img[512*j:512*(j+1),512*k:512*(k+1)]
                #resized = cv2.resize(blank_image, (224,224), interpolation = cv2.INTER_AREA)
                cv2.imwrite(path2+f'{x[i]}'+'-'+f'{j}'+'-'+f'{k}'+'-'+f'{m}'+'.png', resized)                
