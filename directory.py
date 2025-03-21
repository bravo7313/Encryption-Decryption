import os
from tkinter import *
from tkinter import messagebox as ms
from tkinter import filedialog as fd

def directory():
    a=fd.askopenfilename(
        title = "Select a Text File",
        filetype = [("Text File","*.txt")])
    return a;
def temp():
    target=open(r'C:\Users\athar\AppData\Local\Temp\temp.txt','w')
    target.write("temp")
    target.close()
def tempexit():
    target=open(r'C:\Users\athar\AppData\Local\Temp\temp.txt','w')
    target.write("temp")
    target.close()
    os.remove(r'C:\Users\athar\AppData\Local\Temp\temp.txt')
