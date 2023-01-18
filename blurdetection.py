import os
import pandas as pd
import numpy as np
import cv2
import shutil


path = './GE_b/CMS2/CMS2tiles/'
path2 = './GE_b/CMS2/blur/'

x = [item for item in os.listdir(path) if item.endswith('.png')]  


def blackandwhite(im, thresh = 200):

    im_bw = cv2.threshold(im, thresh, 255, cv2.THRESH_BINARY)[1]
    return im_bw

A = []
B = []
C = []
for i in range(len(x)):
    image = cv2.imread(path+x[i])
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    bw = blackandwhite(gray)
    n_white_pix = np.sum(bw == 255)
    scorebw = 100*n_white_pix/(image.shape[0]*image.shape[1])
    blur_map = cv2.Laplacian(gray, cv2.CV_64F)
    scoreblur = np.var(blur_map)
    A.append(x[i])
    B.append(scorebw)
    C.append(scoreblur)
    if scorebw > 80:
        shutil.move(path+x[i], path2+x[i])
    elif scoreblur < 40:
        shutil.move(path+x[i], path2+x[i])

'''
D = {'title': A, 'white':B, 'bluriness': C}
df = pd.DataFrame(D)
df.to_csv('1.csv')
'''
'''
for i in range(len(x)):
    img = cv2.imread(path+x[i])
    avgR = np.mean(img[:,:,2])
    avgG = np.mean(img[:,:,1])
    avgB = np.mean(img[:,:,0])
    print(i, '   ', avgR, avgG, avgB)
'''

