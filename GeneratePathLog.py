import os

currentPath = os.getcwd()
subImgPath = currentPath + '\\tempImg\\'
files = os.listdir(subImgPath)
if os.path.isdir('D:\\DeepCrack-master-for-River\\codes\\data\\test_example.txt'):
    shutil.rmtree('D:\\DeepCrack-master-for-River\\codes\\data\\test_example.txt')
#fop = open('D:\\DeepCrack-master\\DeepCrack-master-Trying-to-solve-test\\codes\\data\\val_example.txt', 'w')
fop = open('D:\\DeepCrack-master-for-River\\codes\\data\\test_example.txt', 'w')
for f in files:
    fop.write('D:\DeepCrack-master-for-River\codes\data\INPUT\\'+f+' '+\
              'D:\DeepCrack-master-for-River\codes\data\INPUT\\'+f+'\n')
fop.close()
    # -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 15:46:54 2021

@author: alisha
"""

