import tkinter as tk
from tkinter import*
from tkinter.ttk import*
import time
import os

def progress():  
    x = 0
    for i in range(0,100):
    	x+=1
    	PgBar['value'] = x 
    	frame.update_idletasks() 
    	time.sleep(0.05)

window = tk.Tk()
window.title('BusinessTech')
window.geometry('1280x720')
window.resizable(width=False, height=False)

frame = tk.Frame(window, bg='#013D6B', padx=400, pady=50)
frame.pack(side='bottom')

image = PhotoImage(file='Image/bt.gif', master=window)
canvas = Canvas(window, width=1280, height=720, background='#013D6B', bd=0, highlightthickness=0)
canvas.pack()
canvas.create_image((1280//2, 720//2), image=image)
icon = tk.PhotoImage(file='Image/bt.gif')
window.iconphoto(True, icon)

PgBar = Progressbar(frame, orient='horizontal', length=500, maximum=100, mode="determinate")  
PgBar.pack()
progress()

window.destroy()
os.system("python loginpage.py")
window.mainloop()