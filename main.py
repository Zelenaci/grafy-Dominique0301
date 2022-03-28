#!/usr/bin/env python3
from importlib.metadata import PathDistribution
from os.path import basename, splitext
import math
from math import pi
import tkinter as tk
from tkinter import messagebox, IntVar
from tkinter.messagebox import showerror
from matplotlib import pyplot as plt
import numpy as np


class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Luxus"
    
    
    


    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.geometry("400x400")

<<<<<<< HEAD
        self.btn = tk.Button(self, text="soubor", command=self.soubor)
        self.btn.grid(row=1, column=1)
        self.btn2 = tk.Button(self, text="graf", command=self.graf)
        self.btn2.grid(row=6, column=1)
=======
        self.btn = tk.Button(self, text="graf", command=self.soubor)
        self.btn.grid(row=1, column=2)
>>>>>>> adcf18d0f50d0f6b3b7c35f582d2b74320c667b2

        self.freq = tk.Entry(self, validate="key", validatecommand=(self.register(self.validate), "%P"))
        self.freq.grid(row=2, column=2, padx=10, pady=10)
        self.frekvence = tk.Label(self,text="f =")
        self.frekvence.grid(row=2, column=1)
        
        self.amplituda = tk.Entry(self, validate="key", validatecommand=(self.register(self.validate), "%P"))
        self.amplituda.grid(row=5, column=2, padx=10, pady=10)

        self.Um = tk.Label(self, text="Amplituda")
        self.Um.grid(row=5, column=1 )

        self.cas_start = tk.Entry(self,validate="key",  validatecommand=(self.register(self.validate), "%P"))
        self.cas_start.grid(row=3, column=2, padx=10, pady=10)
        self.cas_konec = tk.Entry(self,validate="key",  validatecommand=(self.register(self.validate), "%P"))
        self.cas_konec.grid(row=4, column=2, padx=10, pady=10)
      

<<<<<<< HEAD
=======
        self.btn = tk.Button(self, text="graf", command=self.cosinus)
        self.btn.grid(row=1, column=2)
>>>>>>> adcf18d0f50d0f6b3b7c35f582d2b74320c667b2

        self.freq = tk.Entry(self, validate="key", validatecommand=(self.register(self.validate), "%P"))
        self.freq.grid(row=2, column=2)

        self.cas_start = tk.Entry(self,validate="key", validatecommand=(self.register(self.validate), "%P"))
        self.cas_start.grid(row=3, column=2)
        self.cas_konec = tk.Entry(self,validate="key", validatecommand=(self.register(self.validate), "%P"))
        self.cas_konec.grid(row=4, column=2)
        self.cas_zacatek = tk.Label(self, text="OD")
        self.cas_zacatek.grid(row=3, column=1)
        self.cas_final = tk.Label(self, text="DO")
        self.cas_final.grid(row=4, column=1)

        self.hodnoty_x = []
        self.hodnoty_y = []
<<<<<<< HEAD
        self.amp = self.amplituda.get()
        self.frq = self.freq.get()
=======
        #self.amp = float(self.amplituda.get())
        #self.frq = float(self.freq.get())
>>>>>>> adcf18d0f50d0f6b3b7c35f582d2b74320c667b2


    def validate(self, value):
        if len(value) == 0 or value.isnumeric() or self.nula(value) or self.desetinne(value):
            return True
        else:
            return False

    def nula(self, value):
        if value == "-":
            return True
        else:
            return False

    def desetinne(self, value):
        try:
            float(value)
        except:
            return False
        return True


    def graf(self):
        if self.freq.get()=="" or self.amplituda.get()=="":
            messagebox.showerror("Pozor", "chybějící paramtery")
        else:
            self.cosinus()

    def cosinus(self):
        f = open("soubor-ux.txt", "r")
        self.hodnoty_x = []
        self.hodnoty_y = []
        while 1:
            radek=f.readline()
            if radek=='':
                break
            cisla=radek.split()
            self.hodnoty_x.append( float(cisla[0]))
            self.hodnoty_y.append(float(cisla[1]))
        t = np.linspace(self.hodnoty_x[0],self.hodnoty_x[-1], len(self.hodnoty_x))
<<<<<<< HEAD
        u = self.amp*(np.cos(2*pi*self.frq*t))
=======
        u = (np.cos(2*pi*20*t))
>>>>>>> adcf18d0f50d0f6b3b7c35f582d2b74320c667b2
        plt.xlim(-10,10)
        plt.plot(t,u)
        plt.grid()
        plt.show()


    def soubor(self):
        f = open("soubor-ux.txt", "r")
        self.hodnoty_x = []
        self.hodnoty_y = []
        while 1:
            radek=f.readline()
            if radek=='':
                break
            cisla=radek.split()
            self.hodnoty_x.append( float(cisla[0]))
            self.hodnoty_y.append(float(cisla[1]))
        #x = np.linspace(self.hodnoty_x[0],self.hodnoty_x[-1], len(self.hodnoty_x))
        #y = np.linspace(self.hodnoty_y[0],self.hodnoty_y[-1],len(self.hodnoty_y))
        plt.plot(self.hodnoty_x, self.hodnoty_y)
        plt.grid(True)
        plt.show()



 



app = Application()
app.mainloop()