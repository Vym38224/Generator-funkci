#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from tkinter import Entry

# from tkinter import ttk


class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Generátor funkcí"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.lbl = tk.Label(self, text="Generátor funkcí")
        self.lbl.pack()
        self.lbl2 = tk.Label(self, text="Nastavení frekvence:")
        self.lbl2.pack()
        self.f = Entry(self)
        self.f.pack()
        self.f.focus_set()

        def frekvence():
            try:
                f1 = open("frekvence.txt", "w")
            except FileNotFoundError:
                print("Soubor nebyl nalezen")

            text = (self.f.get())
            f1.write(text)
            print(self.f.get())
            f1.close()
            
        self.btn3 = tk.Button(self, text="Zapiš", command=frekvence)
        self.btn3.pack()
        self.btn2 = tk.Button(self, text="Vygeneruj", command=self.graf)
        self.btn2.pack()
        self.btn = tk.Button(self, text="Konec", command=self.quit)
        self.btn.pack()
       

    def graf(self):
        #TIME
        sample_rate = 45000
        t = np.arange(0,1,1/sample_rate)

        #FREQUENCY        
        f1 = open("frekvence.txt", "r")         
        f = f1.read()
        f = np.int16(f)                         
        f1.close()
                                           
        #SIGNALS
        signal = np.sin(2*np.pi*f*t)            #Sinus
        #signal = np.cos(2*np.pi*f*t)           #Cosinus
        #signal = (np.mod(f*t,1) < 0.5)*2.0-1   #Rectangle

        noise = np.random.randn(*signal.shape)

        #COMBINE NOISE AND SIGNAL
        def norm(data):
        
            min_v = min(data)
            max_v = max(data)
            return np.array([((x-min_v) / (max_v-min_v)) for x in data])*2-1

        dirty =  norm(signal+noise)

        #WRITE AUDIO FILE
        signal = signal * 15000
        signal = np.int16(signal)
        wavfile.write("file.wav", sample_rate, signal)

        #PLOT SIGNAL
        plt.plot(t, signal,"black")
        plt.plot(t, signal+noise,"blue")
        plt.ylabel("Up-p[mV]")
        plt.xlabel("čas[s]")
        plt.title("Signál")
        plt.grid()
        plt.show()

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()





