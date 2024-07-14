from tkinter import *

root = Tk()
ans = 0
display = Label(root, text=f'{ans}', font=('Arial',36))
display.pack(padx=10)

buttonFrame = Frame(root)
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)
buttonFrame.columnconfigure(3, weight=1)

buttonText = [1,2,3,"+",4,5,6,"-",7,8,9,0]
btn = {}

for i in buttonText:
    btn[i] = Button(buttonFrame, text=str(i), font=('Arial',38))

for i ,v in enumerate(btn.values()):
    v.grid(row=(i-1)%4,column=(i-(i%3)))
#123456789
#000111222
buttonFrame.pack()

root.mainloop()