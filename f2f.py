'''
import os
l=os.listdir(".")
for i in l:
    i.endswith('.ini')
    print(i)
'''

import glob,os

def getfiles():
    return glob.glob("*.py"),glob.glob1(".","*.ini")
print(getfiles())
'''Autohot key--'''