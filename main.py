#!/usr/bin/env python3
from os.path import basename, splitext
import math
from math import pi
import tkinter as tk
from tkinter import messagebox
from tkinter.messagebox import showerror
from matplotlib import pyplot as plt
import numpy as np


class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Absolutní Luxus"
    


    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.geometry("200x200")

        self.btn = tk.Button(self, text="luxus", command=self.graf)
        self.btn.grid(row=1, column=1)

        self.freq = tk.Entry(self, validate="key", validatecommand=(self.register(self.validate), "%P"))
        self.freq.grid(row=2, column=1)

        self.hodnoty = []


    def validate(self, value):
        if len(value) == 0 or value.isnumeric():
            return True
        else:
            return False


    def graf(self):
        if self.freq.get()=="":
            messagebox.showerror("Pozor", "Zadejte ffrekvenci")
        else:
            self.cosinus()

    def cosinus(self):
        with open("soubor-win.txt", "r") as f:
            radky = f.readlines()
            x = [float(line.split()[0]) for line in radky]
            self.hodnoty.append(x)
            for radek in self.hodnoty:
                start = radek[0]
                konec = radek[-1]
            hodnoty_x = np.linspace(start, konec,len(radky))
            #print(len(radky))
            f = float(self.freq.get())                   
            u = np.cos(2*pi*f*hodnoty_x)   
            plt.plot(hodnoty_x,u)
            plt.grid()
            plt.show()


 



app = Application()
app.mainloop()