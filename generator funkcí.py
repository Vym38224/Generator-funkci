
#!/usr/bin/env python3

import pylab as plt
import tkinter as tk

from pylab import linspace, pi, plot,sin,cos, show,grid,legend
from os.path import basename, splitext
from tkinter import *

class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Generování průběhu"

    def __init__(self):
        super().__init__(className=self.name)
        self.var_entryS = tk.IntVar()
        self.var_entryF = tk.IntVar()
        self.var_entryA = tk.IntVar()
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.lbl1 = tk.Label(self, text="", font=7)
        self.lbl1.pack()  
        self.lblF = tk.Label(self, text=u"Frekvence:")
        self.lblF.pack(anchor=W)
        self.entryF  = tk.Entry(self, textvariable = self.var_entryF, width = 15, justify=CENTER)
        self.entryF.pack()
        self.lblA = tk.Label(self, text=u"Amplituda:")
        self.lblA.pack(anchor=W)
        self.entryA  = tk.Entry(self, textvariable = self.var_entryA, width = 15, justify=CENTER)
        self.entryA.pack()
        self.btn3 = tk.Button(self, text="Načíst graf", command=self.graf)
        self.btn3.pack()
        self.btn = tk.Button(self, text="Konec", command=self.quit)
        self.btn.pack()

    def graf(self):
        self.start = self.var_entryS.get()
        self.frekvence = self.var_entryF.get()
        self.amplituda = self.var_entryA.get()
        
        
        t = plt.linspace(0, 10/self.frekvence, self.frekvence*10000)
        x = self.amplituda * (plt.sin(2*pi*self.frekvence*t ))

        plt.plot(t,x)
        plt.title("generování sihnálu")
        plt.xlabel("t [s]")
        plt.ylabel("u V]")
        plt.grid()
        plt.show()

    def quit(self, event=None):
        super().quit()


    

        
app = Application()
app.mainloop()
