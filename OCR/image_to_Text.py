"""
Created on Tue Mar  4 2020

@author: Namita
Code to cobert image into text file.
Works well given a bird eye view of image but not so good with shadows

Usage : python image_to_Text.py
ref : https://nanonets.com/blog/ocr-with-tesseract/#ocrwithpytesseractandopencv
    : https://nanonets.com/blog/deep-learning-ocr/
"""



import cv2
import pytesseract
from pytesseract import Output
import os
import numpy as np
from toTxt import toTxt #user defined function to convert image to text file

def get_string(img_path):
    # Read image using opencv
    img = cv2.imread(img_path)

    # Extract the file name without the file extension
    file_name = os.path.basename(img_path).split('.')[0]
    file_name = file_name.split()[0]

    # Create a directory for outputs
    output_path = os.path.join('', file_name)
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    img = cv2.resize(img, None, fx=2.5, fy=2.5, interpolation=cv2.INTER_CUBIC)
    # img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)#fast but low quality
    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((2, 2), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    # Apply blur to smooth out the edges
    img = cv2.GaussianBlur(img, (5, 5), 0)
    img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    #img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 25, 2)
    # Save the filtered image in the output directory
    # Apply dilation and erosion to remove some noise

    
    save_path = os.path.join(output_path, file_name + "_filter_" + 'l' + ".jpg")
    cv2.imwrite(save_path, img)

    # Recognize text with tesseract for python
    #result = pytesseract.image_to_string(img, lang="eng")
    result = pytesseract.image_to_data(img, output_type=Output.DICT)
    cv2.imshow('frame', img)
    cv2.waitKey(0)
    return result['text']

# for i in range(1,7):
#     toTxt(get_string("IMG0"+str(i)+".jpg"),i)

#toTxt(get_string('IMG_2.jpg'),0)
lists = get_string('IMG_2.jpg')
liststring = ' '.join(map(str,lists))
print(liststring)
