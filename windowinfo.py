import pyautogui as pag
from customtkinter import *
from time import sleep
import PIL
from webbrowser import open_new
sticker = PIL.Image.open("STICKER.png")
multi = PIL.Image.open("multi window.png")
one = PIL.Image.open("one.png")

def p():
    pass
class windowsinfo:
    def __init__(self,root):
        self.root = root
        loganswer = CTkLabel(root,text="logs show here")
        loganswer.pack(fill="x")

        def getactive():
            sleep(5)
            loganswer.configure(text=pag.getActiveWindowTitle())
        logactivewindow = CTkButton(self.root,text="log active windows",command=getactive,corner_radius=32,fg_color="transparent",image=CTkImage(one))
        logactivewindow.pack(fill="x")
        logallwindow = CTkButton(self.root, text="log all windows",command=lambda:loganswer.configure(text=pag.getAllTitles().strip("{}"), font=("Corbel", 20)),corner_radius=32,fg_color="transparent",image=CTkImage(multi))
        logallwindow.pack(fill="x")
        stickerlbl = CTkButton(root,image=CTkImage(sticker),fg_color="transparent",text="OPEN MY GITHUB",command=lambda:open_new('https://github.com/samiyartey/sYsTeMiNfOaPp')).pack(fill="x")