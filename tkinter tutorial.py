from tkinter import *

root = Tk()
root.geometry('200x300')

lbl = Label(root, text="test")
lbl.pack()

#userinput = Text(root,font=('Arial',15))
#userinput.pack(padx=20,pady=100)

btn = Button(root,text='Press me')
btn.pack()

root.mainloop()