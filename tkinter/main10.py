# Importing required libraries.
from tkinter import *
from PIL import ImageTk , Image

#Creating a new Tkinter instance
root = Tk() 
root.iconbitmap('D:\Documents\ico\calc.ico')
root.geometry('250x250')

#Title-ing the Tkinter object
root.title("Msg box")

def popup():
   messagebox.showinfo("Hello","Hello World!!")

#creating a new tkinter button
a = Button(root,text = "heya",command = popup).pack()

# Looping the Tkinter instance
root.mainloop()
