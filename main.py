#--imports--
import os
import random
import s
import windowinfo
import platform
from osinfor import *
from customtkinter import *
from PIL import Image
import piecesdata as pd
def p():
    pass
#--clases---
sticker = Image.open("STICKER.png")
osdoc = platform.uname()
class dashboard:
    def __init__(self,window):
        def lightdarkk():
            ld = get_appearance_mode()
            if ld == "Dark":
                set_appearance_mode("light")
            if ld == "Light":
                set_appearance_mode("dark")
        #--setup graphic--
        self.window = window
        self.window.title("system info app")
        self.window.geometry("705x385")
        set_default_color_theme("green")
        pages = CTkTabview(self.window)
        pages.pack(fill="both")
        windowspage =  pages.add("window's info")
        ospage = pages.add("os info")
        ghataattab = pages.add("picses info")
        ghataatdatatab = pages.add("picses data")
        #--create grpahic--
        windowinfo.windowsinfo(windowspage)
        osinfo(ospage,osdoc)
        s.docs(ghataattab,osdoc)
        pd.pisecsdata(ghataatdatatab)
#--rn--
if __name__=="__main__":
    root = CTk()
    object = dashboard(root)
    root.mainloop()