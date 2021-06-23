import os
import cv2
import time
import math
import shutil

filename = 'Large3.JPG'
subsize = 512



time_start = time.time()
img = cv2.imread(filename)
[h, w, d] = img.shape

# Split All
# h_n = math.ceil(h/subsize)
# w_n = math.ceil(w/subsize)

# Split Same Size Image
h_n = math.floor(h/subsize)
w_n = math.floor(w/subsize)
####################################################
cv2.waitKey(0)
cv2.destroyAllWindows()
currentPath = os.getcwd()
tempImgPath = str(currentPath)+'\\tempImg'

# For Spliting Same Size Image
h = subsize*h_n
w = subsize*w_n

if os.path.isdir(tempImgPath):
    shutil.rmtree(tempImgPath)
os.makedirs(tempImgPath)

if os.path.isdir(currentPath+'\\SplitInfo.txt'):
    shutil.rmtree(currentPath+'\\SplitInfo.txt')


for i in range(h_n):
      for j in range(w_n):
          temp = img[i*subsize:subsize*(i+1), j*subsize:subsize*(j+1)]
          if i==1 & j==1:
              firstTemp = temp
          cv2.imwrite(tempImgPath+'\\'+filename[:-4]+'_result_h_'+ str(i) + '_w_' + str(j) + '.jpg', temp)
          
f = open(currentPath+'\\SplitInfo.txt', 'w')
time_end = time.time()
SplitInfo = ['Filename: ',filename,'\nh = ', str(h), '\nw = ', str(w),'\nSubset Size = ', str(subsize),\
             '\nNumber of h = ', str(h_n), '\nNumber of w = ', str(w_n),\
             '\nTime Spent: ',str(time_end - time_start)]
f.writelines(SplitInfo)
f.close()
print('done')
cv2.imshow('result',firstTemp)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
Created on Tue Jun  8 16:41:41 2021

@author: roman
"""

