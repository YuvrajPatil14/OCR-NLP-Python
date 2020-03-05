"""
Created on Tue Mar  3 16:32:52 2020

@author: Yuvarj
USing python OCR and cv2 with redular expressions to detect date pattern.
Usage : python date.py
"""


import cv2
import re
import numpy 
import pytesseract
from pytesseract import Output
from toTxt import toTxt



img_cv = cv2.imread('image.jpg')
img = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
d = pytesseract.image_to_data(img, output_type=Output.DICT)
d1 = pytesseract.image_to_string(img)
toTxt(d1,1) #save text in the new text file
keys = list(d.keys())
# re patterns to detect date
patt = '^((0?[13578]|10|12)(-|\/)(([1-9])|(0[1-9])|([12])([0-9]?)|(3[01]?))(-|\/)((19)([2-9])(\d{1})|(20)([01])(\d{1})|([8901])(\d{1}))|(0?[2469]|11)(-|\/)(([1-9])|(0[1-9])|([12])([0-9]?)|(3[0]?))(-|\/)((19)([2-9])(\d{1})|(20)([01])(\d{1})|([8901])(\d{1})))$'
n_boxes = len(d['text'])
text = d['text']
#print(text)
for i in range(len(text)):
    #print(text[i])
    m = re.search(patt,text[i])
    if m:
        print(d['text'][i])
        (x, y, w, h) = (d['left'][i], d['top']
                        [i], d['width'][i], d['height'][i]) # segmentation in image
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    if text[i].lower == 'date':
        print(text[i],text[i+1]) #hardcoding is not good
    if d['text'][i].lower =='total':
        print(d['text'][i],d['text'][i+1]) #again its not good

cv2.imshow('img', img)
cv2.waitKey(0)
