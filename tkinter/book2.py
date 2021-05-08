# Importing required libraries.
from tkinter import *
from PIL import ImageTk , Image

#Creating a new Tkinter instance
top = Tk() 
top.iconbitmap('D:\Documents\ico\calc.ico')
# top.geometry('250x250')

#Title-ing the Tkinter object
top.title("Find and Replace")

Label(top,text="Find:").grid(row=0, column=0, sticky='e')
Entry(top).grid(row=0,column=1,padx=2,pady=2,sticky='we',columnspan=9)
Label(top, text="Replace:").grid(row=1, column=0, sticky='e')
Entry(top).grid(row=1,column=1,padx=2,pady=2,sticky='we',columnspan=9)
Button(top, text="Find").grid(row=0, column=10, sticky='ew', padx=2, pady=2)
Button(top, text="Find All").grid(row=1, column=10, sticky='ew', padx=2)
Button(top, text="Replace").grid(row=2, column=10, sticky='ew', padx=2)
Button(top, text="Replace All").grid(row=3, column=10, sticky='ew', padx=2)
Button(top, text="Exit",command=top.quit).grid(row=4, column=10, sticky='ew', padx=2)
Checkbutton(top, text='Match whole word only').grid(row =2, column=1, columnspan=4, sticky='w')
Checkbutton(top, text='Match Case').grid(row =3, column=1, columnspan=4, sticky='w')
Checkbutton(top, text='Wrap around').grid(row =4, column=1, columnspan=4, sticky='w')
Label(top, text="Direction:").grid(row=2, column=6, sticky='w')
Radiobutton(top, text='Up', value=1).grid(row=3, column=6, columnspan=6, sticky='w')
Radiobutton(top, text='Down', value=2).grid(row=3, column=7, columnspan=2, sticky='e')

# Looping the Tkinter instance
top.mainloop()
