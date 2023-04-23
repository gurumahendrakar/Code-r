import tkinter as tk
from tkinter import ttk
from webscraping import  colums,city_names



class goldminer:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Goldminer")
        self.window.geometry('500x500')
        self.label = tk.Label(text="City",foreground='black',font='Samsum 12 bold',padx=100,
                              justify='center')
        self.label.grid(row=0,column=0)
        self.label1 = tk.Label(text="1Gram",foreground='black',font='Samsum 12 bold',padx=20)
        self.label1.grid(row=0,column=1)



        self.x = 50
        self.y = 50
        for x in range(len(city_names)):
            tk.Label(text=city_names[x],foreground='black').place(x=50,y=self.y)
            self.y+=30

        else:
            self.y = 50

        for x in range(len(colums)):
            tk.Label(text=f"{colums[x][0]}",foreground='black').place(x=250,y=self.y)
            self.y+=30




if __name__=='__main__':
    goldminerO = goldminer()

    goldminerO.window.mainloop()
