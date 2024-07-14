from tkinter import *

root = Tk()
ans = 0
curr = ""
display = Label(root, text=f'{ans}', font=('Arial',36))
display.pack(padx=10)

def clear():
    display.config(text="")

def buttonHandler(value):
    global ans, curr
    if value in ["+","-","x","/"]:
        if curr not in ["+","-","x","/"]:
            ans += int(display.cget("text"))
            curr = value
            clear()
        else:
            if curr == "+":
                ans += int(display.cget("text"))
                clear()
            elif curr == "-":
                ans -= int(display.cget("text"))
                clear()
            elif curr == "x":
                ans *= int(display.cget("text"))
                clear()
            elif curr == "/":
                ans /= int(display.cget("text"))
                clear()
            curr = value
    elif value == "=":
        if curr == "+":
            ans += int(display.cget("text"))
            clear()
        elif curr == "-":
            ans -= int(display.cget("text"))
            clear()
        elif curr == "x":
            ans *= int(display.cget("text"))
            clear()
        elif curr == "/":
            ans /= int(display.cget("text"))
            clear()
        curr = ""
        display.config(text=str(ans))
    elif value == "C":
        curr = ""
        ans = 0
        clear()
    else:
        display.config(text=display.cget("text") + str(value))
        
        

buttonFrame = Frame(root)
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)
buttonFrame.columnconfigure(3, weight=1)

buttonText = [1,2,3,"+",4,5,6,"-",7,8,9,"=",0,"x","/","C"]
btn = {}

for i in buttonText:
    btn[i] = Button(buttonFrame, text=str(i), font=('Arial',38), command=lambda x=i : buttonHandler(x))

for i ,v in enumerate(btn.values()):
    v.grid(column=(i)%4,row=(i-(i%4)))
#123456789
#000111222
buttonFrame.pack(fill='x')

root.mainloop()