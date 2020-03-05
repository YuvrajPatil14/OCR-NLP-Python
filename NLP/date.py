# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 16:32:52 2020

@author: Yuvraj
Simple program to find date in a text file using datefinder
Usage : python date.py
"""

import datefinder

def findDateNLP(input_string):
    matches = list(datefinder.find_dates(input_string))
    if len(matches) > 0:
    # date returned will be a datetime.datetime object. here we are only using the first match.
        date = matches[0]
        print(date)
        return
    else:
        print('No dates found')

file1 = open('file.txt','r+') #path of text file and mode of file opening
inputString = file1.read()
print(findDateNLP(inputString))