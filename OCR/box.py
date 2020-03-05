"""
Created on Tue Mar  3 16:32:52 2020

@author: Namita
Simple program to detect text and boxing it using pytessersct

Usage : python box.py
"""

import cv2
import pytesseract
from pytesseract import Output

img_cv = cv2.imread('image.jpg') # read image using image path
img = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB) # Because pytesseract works good on grayscale
d = pytesseract.image_to_data(img, output_type=Output.DICT) #convert image to data object
# print(pytesseract.image_to_boxes(img))
# print(d['text'])
n_boxes = len(d['text'])
for i in range(n_boxes):
    if int(d['conf'][i]) > 60:
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow('IMG.png', img)#display image
cv2.waitKey(0)#wait key zero means manual closing the window, You can add time in mils