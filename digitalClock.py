from tkinter import Tk
from tkinter import Label
import time
import sys
master = Tk()
master.title("digital clock")
#get time and update it
def get_time():
    timeVar = time.strftime("%I:%M:%S %p")
    clock.config(text = timeVar)
    #update every 2millisceonds
    clock.after(2,get_time)

clock = Label(master, font = ('Arial',100), bg='black',fg = 'white')
clock.pack()

get_time()

master.mainloop()
