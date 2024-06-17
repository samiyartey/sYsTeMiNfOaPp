import platform
import sqlite3

from customtkinter import *
import psutil as pcdata
import PIL
from webbrowser import open_new
sticker = PIL.Image.open("STICKER.png")
memorydata = pcdata.virtual_memory()

# get the memory details
class docs:
    def __init__(self,docsroot,cpuinfo):
        self.docsroot = docsroot
        docs = CTkLabel(self.docsroot, text=f" ________________________________________________________________________\n processor model  : {cpuinfo.processor}\n CPU architecture :{cpuinfo.machine}\n\n _____________________________________________________________________________________ \n amount of memory :{memorydata.total} bytes")
        docs.pack()
        stickerlbl = CTkButton(docsroot,image=CTkImage(sticker),fg_color="transparent",text="OPEN MY GITHUB",command=lambda:open_new('https://github.com/samiyartey/sYsTeMiNfOaPp')).pack(fill="x")

con = sqlite3.connect(database=r'database.db')
cur = con.cursor()
"""cur.execute("CREATE TABLE cpu(name, architecture)")
cur.execute("CREATE TABLE memory(byte)")"""