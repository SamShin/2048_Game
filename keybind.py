from tkinter import *
import numpy as np
import random as r 

main = Tk()

board = np.zeros((4,4))
#board.fill(3)
print(board)

def some():
    x = r.randint(0,3)
    y = r.randint(0,3)
    rand = r.randint(1,2) * 2
    board[x][y] = rand
    
    print(board)
    
    clearSpace = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                clearSpace.append
                
                
                
    
def leftKey(event):
    some()
    print ("Left key pressed")

def rightKey(event):
    some()
    print ("Right key pressed")

def upKey(event):
    some()
    print("up key pressed")
    
def downKey(event):
    some()
    print("down key pressed")
    
def change():
    test.configure(text = board[0][1])

#frame = Frame(main, width=100, height=100)

#button = Button(main, text = "change", command = lambda: change())
#button.pack(side = LEFT)

#test = Label(main, text="test")
#test.pack(side= LEFT)

main.bind('<Left>', leftKey)
main.bind('<Right>', rightKey)
main.bind('<Up>', upKey)
main.bind('<Down>', downKey)

#frame.pack()
main.mainloop()