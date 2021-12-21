from tkinter import *


def change():
    for i in labelTest:
        for j in labelTest.get(i):
            
            if len(j.cget("text")) == 1:
                j.configure(bg = "#00FF00")
            elif len(j.cget("text")) == 2:
                j.configure(bg = "#ff0000")
            elif len(j.cget("text")) == 3:
                j.configure(bg = "#9F2B68")
                     
    
root = Tk()
root.geometry("700x700")

bgSam = "#000000"
fgSam = "#ffffff"

bgBen = "#080808"
fgBen = "#343434"

sam = Label(root, text = "4", bg= bgSam, fg=fgSam)
sam.grid(column=0, row=0)

ben = Label(root, text = "16", bg= bgBen, fg=fgBen)
ben.grid(column=1, row=0)

can = Label(root, text="button")
can.grid(column=2, row=1)

den = Label(root, text ="den")
den.grid(column=3, row=4)

test = Button(root, text= "Button", command = lambda: change())
test.grid(column=2, row=0)



labelTest = {0: [sam, ben],
             1: [can, den]
             }


mainloop()