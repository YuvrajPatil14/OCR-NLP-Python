"""
Created on Tue Mar  4 2020

@author: Yuvraj
 
store string to a text file in new folder
and rewrite if path exists
Usage: python toTxt.py
"""

import os

#second argument 'i' is passed to create a new folder with same image
def toTxt(instring,i): 
    file_name='converted' + str(i) 
    output_path = os.path.join('', file_name)
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    save_path = os.path.join(output_path, file_name+"_filter_.txt")
    file = open(save_path, "w")
    file.write(instring)
    file.close()
