#MENU
import tkinter as tk

from tkinter import *
from os.path import basename, splitext

root = Tk()
hlavniMenu = Menu(root)


def bod1():
    class Application(tk.Tk):
        name = basename(splitext(basename(__file__.capitalize()))[0])
        name = "bod1"

        def __init__(self):
            super().__init__(className=self.name)
            self.var_entryF = tk.IntVar()
            self.title(self.name)
            self.bind("<Escape>", self.quit)

    app = Application()
    mainloop()



def bod2():
    class Application(tk.Tk):
        name = basename(splitext(basename(__file__.capitalize()))[0])
        name = "bod2"

        def __init__(self):
            super().__init__(className=self.name)
            self.var_entryF = tk.IntVar()
            self.title(self.name)
            self.bind("<Escape>", self.quit)

    app = Application()
    mainloop()
        
        


#1.bod zadání
hlavniMenu.add_cascade(label="1.bod zadání", command=bod1)
#2.bod zadání
hlavniMenu.add_cascade(label="2.bod zadání", command=bod2)
#plocha
frame = Frame(root, width=169, height=50)
frame.pack()






root.config(menu=hlavniMenu)
mainloop()

