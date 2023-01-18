import os
import pandas as pd
import numpy as np
import shutil


path = './GE_b/'

x = [item for item in os.listdir(path) if item.endswith('.png')] 


df = pd.read_csv('./cms.csv')


A = df['cms_subtype'].unique()

for i in range(len(A)):
    os.makedirs(path+A[i])

print(A)




for index, row in df.iterrows():
    for i in range(len(x)):
        try:
            if row['SS'] == x[i].split('.')[0]:
                print(row['cms_subtype'], x[i])
                #shutil.copy(source, destination)
                shutil.copy(path+x[i], path+row['cms_subtype']+'/'+x[i])
                    
        except:
            pass
            print('not found', x[i].replace('.csv',''))
    
