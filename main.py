from tkinter import *
import tkinter.font as font
import numpy as np
import random as r

board = np.zeros((4,4))
clearSpace = []
moved = []
gameEnd = 0

for i in range(4):
    for j in range(4):
        clearSpace.append(tuple((i,j)))
  
        
def null_space():
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0 and tuple((i,j)) not in clearSpace: 
                clearSpace.append(tuple((i,j)))
            elif board[i][j] != 0 and tuple((i,j)) in clearSpace:
                clearSpace.remove(tuple((i,j)))


def print_board():
    
    for row in board:
        string_row = str(row).replace("[", "").replace("]", "").replace(".", "")
        print(string_row)
    
    
def upMove():
    for correction in range(4):
        for i in (range(1,4)):
            for j in (range(4)):
                
                if board[i-1][j] == 0 or board[i-1][j] == board[i][j]:
                    board[i-1][j] += board[i][j]
                    board[i][j] = 0 

def downMove():
    for correction in range(4):
        for i in reversed(range(0,3)):
            for j in range(4):
                
                if board[i+1][j] == 0 or board[i+1][j] == board[i][j]:
                    board[i+1][j] += board[i][j]
                    board[i][j] = 0

def leftMove():
    for correction in range(4):
        for i in range(4):
            for j in range(1,4):
                
                if board[i][j-1] == 0 or board[i][j-1] == board[i][j]:
                    board[i][j-1] += board[i][j]
                    board[i][j] = 0

def rightMove():
    for correction in range(4):
        for i in range(4):
            for j in reversed(range(0,3)):
                
                if board[i][j+1] == 0 or (board[i][j+1] == board[i][j] and not moved[i-1]):
                    board[i][j+1] += board[i][j]
                    board[i][j] = 0       

def randBoard():
    randVal = r.randint(1,2) * 2
    
    try:
        randSpace = r.randint(0, (len(clearSpace)-1))
        x = clearSpace[randSpace][0]
        y = clearSpace[randSpace][1]
        board[x][y] = randVal
    except:
        global gameEnd
        gameEnd = 1
    


def boardAction(direction):
    randBoard()
    
    if gameEnd == 0:
        if direction == "left":
            leftMove()
        elif direction == "right":
            rightMove()
        elif direction == "down":
            downMove()
        elif direction == "up":
            upMove()
        
    null_space()
    
    print_board()


#GUI START ---------------------------
root = Tk()
root.geometry("540x960")

root.minsize(540, 960)
root.maxsize(540, 960)

root.title("2048")

root['background'] = '#faf8ef'
titleFont = font.Font(family="Helvetica Neue", size=50, weight='bold')
scoreFont = font.Font(family="Helvetica Neue", size=15, weight='bold')
numFont = font.Font(family="Helvetica Neue", size=50, weight='bold')
resetFont = font.Font(family="Helvetica Neue", size=15, weight='bold')


blockSize = 100
blockPad = 5

rootbg = "#faf8ef"
titletextbg = '#808080'
scorebg = "#808080"
scorefg = "#faf8ef"
boardbg = "#bbada0"

testfg = "#776e65"
bg2 = "#eee4da"
bg01 = bg2
fg01 = testfg


#for 4 digit numbers, fontsize = 30
#for 3 digit numbers, fontsize = 40
#for 2 digit numbers, fontsize = 45
#for 1 digit numbers, fontsize = 45
def guiUpdate():
    
    ()
def leftKey(event):
    
    boardAction("left")
    guiUpdate()
    print ("Left key pressed")

def rightKey(event):
    boardAction("right")
    guiUpdate()
    print ("Right key pressed")

def upKey(event):
    boardAction("up")
    guiUpdate()
    print("up key pressed")
    
def downKey(event):
    boardAction("down")
    guiUpdate()
    print("down key pressed")
    
root.bind('<Left>', leftKey)
root.bind('<Right>', rightKey)
root.bind('<Up>', upKey)
root.bind('<Down>', downKey)

#<0th row Frame>
infoFrame = LabelFrame(root, text="test frame")
infoFrame.grid(column=0, row=0, columnspan=10)

#Label widget 
titleLabel = Label(infoFrame, text="2048", font=titleFont)
titleLabel.grid(column=0,row=0, columnspan=2)

#Label widget
bScoreLabel = Label(infoFrame, text="bScoreLabel\n 128080", font=scoreFont)
bScoreLabel.grid(column=3, row=0, padx=(50,0))

#Label widget
scoreLabel = Label(infoFrame, text="scoreLabel\n 128000", font=scoreFont)
scoreLabel.grid(column=4, row=0, padx=(25,0))

#-----------------------
#<1st row Frame>
resetFrame = LabelFrame(root, text="resetFrame")
resetFrame.grid(column=0, row=1, columnspan=10)

#Button widget
resetButton = Button(resetFrame, text="New Game", font=resetFont)
resetButton.grid(column=0, row=0, padx=(300,0))

#-----------------------
#<3rd row Frame>
boardFrame = LabelFrame(root, text="", bg=boardbg)
boardFrame.grid(column=0, row=2, columnspan=10, padx=(27,0), pady=(50,0))


cr00Frame = LabelFrame(boardFrame, text="", width=blockSize, height=blockSize, bg=bg01, borderwidth=0, highlightthickness=0)
cr00Frame.grid(column=0, row=0, padx=blockPad, pady=blockPad)
cr00Frame.grid_propagate(0)

cr00Label = Label(cr00Frame, text = "256", font=numFont, bg = bg01, fg=fg01)
cr00Label.place(x=blockSize/2,y=blockSize/2,anchor=CENTER)


cr01Frame = LabelFrame(boardFrame, text="cr01Frame", width=blockSize, height=blockSize)
cr01Frame.grid(column=1, row=0, padx=blockPad,pady=blockPad)
cr01Frame.grid_propagate(0)

cr01Label = Label(cr01Frame, text = "2", font=numFont)
cr01Label.place(x=blockSize/2,y=blockSize/2 - 10,anchor=CENTER)


cr02Frame = LabelFrame(boardFrame, text="cr02Frame", width=blockSize, height=blockSize)
cr02Frame.grid(column=2, row=0, padx=blockPad,pady=blockPad)
cr02Frame.grid_propagate(0)

cr02Label = Label(cr02Frame, text = "2048", font=numFont)
cr02Label.place(x=blockSize/2,y=blockSize/2 - 10,anchor=CENTER)


cr03Frame = LabelFrame(boardFrame, text="cr03Frame", width=blockSize, height=blockSize)
cr03Frame.grid(column=3, row=0, padx=blockPad,pady=blockPad)
cr03Frame.grid_propagate(0)

cr03Label = Label(cr03Frame, text = "2", font=numFont)
cr03Label.place(x=blockSize/2,y=blockSize/2 - 10,anchor=CENTER)


cr10Frame = LabelFrame(boardFrame, text="cr00Frame", width=blockSize, height=blockSize)
cr10Frame.grid(column=0, row=1, padx=blockPad,pady=blockPad)
cr10Frame.grid_propagate(0)

cr10Label = Label(cr10Frame, text = "2", font=numFont)
cr10Label.place(x=blockSize/2,y=blockSize/2 - 10,anchor=CENTER)


cr20Frame = LabelFrame(boardFrame, text="cr00Frame", width=blockSize, height=blockSize)
cr20Frame.grid(column=0, row=2, padx=blockPad,pady=blockPad)
cr20Frame.grid_propagate(0)

cr20Label = Label(cr20Frame, text = "2", font=numFont)
cr20Label.place(x=blockSize/2,y=blockSize/2 - 10,anchor=CENTER)


cr30Frame = LabelFrame(boardFrame, text="cr00Frame", width=blockSize, height=blockSize)
cr30Frame.grid(column=0, row=3, padx=blockPad,pady=blockPad)
cr30Frame.grid_propagate(0)

cr30Label = Label(cr30Frame, text = "2", font=numFont)
cr30Label.place(x=blockSize/2,y=blockSize/2 - 10,anchor=CENTER)


root.mainloop()



#TODO Bad news... row movements are in the wrong order: ex) If I move left and there are two elements in a same row,
#the program currently moves from the farthest row to the cloest row, so the back element is blocked by the element
#in the front, while the front element is not blocked so it moves leaving a space in between
# 0 0 2 4 (Before state)
# 0 2 0 4 (outcome)
# 2 4 0 0 (expected)

#gameEnd currently stops board operations if board is full, make sure this ends the current game 

#Each block has its own bg, fg, fontSize, etc, attached to it, the goal is to check the gui against the np array
#and to update the gui as the array updates, each element in the 4x4 np array corosponds to a block in gui
#using if else (at least right now) if that spot in array is 2 digit, update font for that block etc.

