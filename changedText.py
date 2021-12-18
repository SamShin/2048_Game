from tkinter import *

root = Tk()
root.title("test")


def change(name):
    name.configure(text="CHanged text")
    
test = Label(root, text="original text", height=2, width=10,bg='#333333',fg='#776e65')
test.grid(column=2,row=2)

button = Button(root, text="change", height =2, width = 10, command = lambda: change(test))
button.grid(column=0, row=0)
root.mainloop()
