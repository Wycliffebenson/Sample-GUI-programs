
from tkinter import Tk, Label
import time


root = Tk()
root.title("Digital Clock in 24Hr Clock System")


def present_time():
    display_time =time.strftime('%H:%M:%S \n %a: %d-%b-%Y \n %z : %Z ')
    digi_clock.config(text=display_time)
    digi_clock.after(200, present_time)

digi_clock = Label(root, font=("impact", 50), bg="green", fg= "white")
digi_clock.pack()
present_time()

root.mainloop()
