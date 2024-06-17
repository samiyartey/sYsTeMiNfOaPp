import platform
import PIL
from customtkinter import *
from webbrowser import open_new
sticker = PIL.Image.open("STICKER.png")

class osinfo:
    def __init__(self,osinforoot,osdoc):
        self.osinforoot = osinforoot
        infolbl = CTkLabel(self.osinforoot, text=f"OS : {osdoc.system} {osdoc.release} \n System name: {osdoc.node} \n os version : {osdoc.version} ")
        infolbl.pack()
        stickerlbl = CTkButton(osinforoot,image=CTkImage(sticker),fg_color="transparent",text="OPEN MY GITHUB",command=lambda:open_new('https://github.com/samiyartey/sYsTeMiNfOaPp')).pack(fill="x")