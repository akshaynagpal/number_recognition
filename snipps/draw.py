gifdir = "C:\/Users\/advance\/Documents\/GitHub\/number_recognition\/snipps\/"
from sys import argv
from Tkinter import *
filename = 'white_back.png'    
win = Tk()
img = PhotoImage(file=gifdir+filename)
can = Canvas(win)
can.pack(fill=BOTH)
can.config(width=img.width(), height=img.height())        
can.create_image(2, 2, image=img, anchor=NW)
win.mainloop()
