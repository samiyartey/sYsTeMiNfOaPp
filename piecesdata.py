import wikipedia
from customtkinter import *
from tkinter.messagebox import *
from PIL import Image
def picesfinder(piceses):
    return wikipedia.summary(piceses,"3")

wikipedia.set_lang("fa")

class pisecsdata:
    def __init__(self,root):
        self.root = root
"""class pisecsdata:
    def __init__(self,root):
        self.root = root
        lbl = CTkLabel(self.root,text="select a pieces")
        lbl.pack(fill="both")
        options = CTkComboBox(self.root,values=("GPU","RAM","CPU","wifi","hard"),state="readonly")
        options.pack(fill="both")
        def search():
            pic = Image.open(f"pics/{options.get()}.png")

            piclbl.configure(image=CTkImage(pic))
            showinfo(options.get(), picesfinder(options.get()))

        but = CTkButton(self.root,text="find data",command=search)
        but.pack(fill="both")
        frame = CTkFrame(self.root)
        frame.pack(fill='both',)
        piclbl = CTkLabel(frame,text="")
        piclbl.pack(fill='both')
if __name__=="__main__":
    root = CTk()
    object = pisecsdata(root)
    root.mainloop()
picesfinder("gpu")"""