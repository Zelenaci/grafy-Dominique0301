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

        self.btn = tk.Button(self, text="luxus", command=self.cosinus)
        self.btn.grid(row=1, column=1)

        self.freq = tk.Entry(self, validate="key", validatecommand=(self.register(self.validate), "%P"))
        self.freq.grid(row=2, column=1)

        self.hodnoty_x = []
        self.hodnoty_y = []


    def validate(self, value):
        if len(value) == 0 or value.isnumeric():
            return True
        else:
            return False


    def graf(self):
        if self.freq.get()=="":
            messagebox.showerror("Pozor", "Zadejte frekvenci")
        else:
            self.cosinus()

    def cosinus(self):
        with open("soubor-ux.txt", "r") as f:
            
            while 1:
                radek=f.readline()
                if radek=='':
                    break
                cisla=radek.split()
            self.hodnoty_x.append( float(cisla[0]))
            self.hodnoty_y.append(float(cisla[1]))
            t = np.linspace(self.hodnoty_x[0],self.hodnoty_x[-1], len(self.hodnoty_x))
            u = np.cos(2*pi*50*t)
            plt.plot(self.hodnoty_x,u)
            plt.grid()
            plt.show()


 



app = Application()
app.mainloop()