from tkinter import *
import tkinter.font as font
import numpy as np
import random as r

board = np.zeros((4,4))
#board = np.array(([8,4,4,4],
#                  [4,4,4,4], 
#                  [4,4,4,4], 
#                  [4,4,4,4]))
clearSpace = []
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
    
#print_board()    

def upMove(moved):
    for j in (range(4)):
        for correction in range(4):
            for i in (range(1,4)):
                
                if board[i-1][j] == 0 or (board[i-1][j] == board[i][j] and (not moved[i-1] and not moved[i])):
                    if((board[i-1][j] == board[i][j]) and (board[i-1][j] != 0)):
                        moved[i-1] = True
                        
                    board[i-1][j] += board[i][j]
                    board[i][j] = 0
                    
        moved = [False, False, False, False]

def downMove(moved):

    for j in range(4):
        for correction in range(4):
            for i in reversed(range(0,3)):
                
                if board[i+1][j] == 0 or (board[i+1][j] == board[i][j] and (not moved[i+1] and not moved[i])):
                    if((board[i+1][j] == board[i][j]) and (board[i+1][j] != 0)):
                        moved[i+1] = True
                        
                    board[i+1][j] += board[i][j]
                    board[i][j] = 0
                    
        moved = [False, False, False, False]

def leftMove(moved):
    
    for i in range(4):
        for correction in range(4):
            for j in range(1,4):
                
                if board[i][j-1] == 0 or (board[i][j-1] == board[i][j] and (not moved[j-1] and not moved[j])):
                    if ((board[i][j-1] == board[i][j]) and (board[i][j-1] != 0)):
                        moved[j-1] = True  
                        
                    board[i][j-1] += board[i][j]
                    board[i][j] = 0
                    
        moved = [False, False, False, False]


def rightMove(moved):
    
    for i in range(4):
        for correction in range(4):
            for j in reversed(range(0,3)):
                
                if board[i][j+1] == 0 or (board[i][j+1] == board[i][j] and (not moved[j+1] and not moved[j])):
                    if ((board[i][j+1] == board[i][j]) and (board[i][j+1] != 0)):
                        moved[j+1] = True       
                        
                    board[i][j+1] += board[i][j]
                    board[i][j] = 0  
                    
        moved = [False, False, False, False]


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
    
    
    moved = [False, False, False, False] 
    
    if gameEnd == 0:
        if direction == "left":
            leftMove(moved)
        elif direction == "right":
            rightMove(moved)
        elif direction == "down":
            downMove(moved)
        elif direction == "up":
            upMove(moved)
            
    
    randBoard()
    
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

resetFont = font.Font(family="Helvetica Neue", size=15, weight='bold')

numFontList = [font.Font(family="Helvetica Neue", size=45, weight='bold'),
               font.Font(family="Helvetica Neue", size=45, weight='bold'),
               font.Font(family="Helvetica Neue", size=40, weight='bold'),
               font.Font(family="Helvetica Neue", size=30, weight='bold')]
                         

blockSize = 100
blockPad = 5

rootbg = "#faf8ef"
titletextbg = '#808080'
scorebg = "#808080"
scorefg = "#faf8ef"
boardbg = "#bbada0"
numbg = "#ffffff"
numfg =  "#000000"

def colorCheck():
    
    for i in labelDict:

        blockText = str(labelDict.get(i)[1].cget("text")) 
        
        if int(blockText) <= 5:
            for j in labelDict.get(i):
                j.configure(fg = "#776e65")
        else:
            for j in labelDict.get(i):
                j.configure(fg = "#f9f6f2")
        
        if blockText == "0":
            for j in labelDict.get(i):
                j.configure(text = "", bg = "#ccc1b4")
        elif blockText == "2":
            for j in labelDict.get(i):
                j.configure(bg = "#efe4da")
        elif blockText == "4":
            for j in labelDict.get(i):
                j.configure(bg = "#eee1c9")
        elif blockText == "8":
            for j in labelDict.get(i):
                j.configure(bg = "#f4b27a")
        elif blockText == "16":
            for j in labelDict.get(i):
                j.configure(bg = "#f79664")
        elif blockText == "32":
            for j in labelDict.get(i):
                j.configure(bg = "#f87c5f")
        elif blockText == "64":
            for j in labelDict.get(i):
                j.configure(bg = "#f75f3b")
        elif blockText == "128":
            for j in labelDict.get(i):
                j.configure(bg = "#edd073")
                
            
def sizeCheck():

    for i in labelDict:
        for j in range(1,5):
            if len(str(labelDict.get(i)[1].cget("text"))) == j:
                labelDict.get(i)[1].configure(font = numFontList[j-1])

def numUpdate():
    for i in range(4):
        
        for j in range(4):
            val = board[i][j]
            position = 4*i + j
            
            labelDict.get(position)[1].configure(text = int(val))
            
            
def guiUpdate():
    numUpdate()
    colorCheck()
    sizeCheck()
    
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


cr00Frame = LabelFrame(boardFrame, width=blockSize, height=blockSize, borderwidth=0, highlightthickness=0)
cr00Frame.grid(column=0, row=0, padx=blockPad, pady=blockPad)
cr00Frame.grid_propagate(0)

cr00Label = Label(cr00Frame)
cr00Label.place(x=blockSize/2, y=blockSize/2, anchor=CENTER)


cr01Frame = LabelFrame(boardFrame, width=blockSize, height=blockSize, borderwidth=0, highlightthickness=0)
cr01Frame.grid(column=1, row=0, padx=blockPad,pady=blockPad)
cr01Frame.grid_propagate(0)

cr01Label = Label(cr01Frame)
cr01Label.place(x=blockSize/2,y=blockSize/2,anchor=CENTER)


cr02Frame = LabelFrame(boardFrame, text="", width=blockSize, height=blockSize, borderwidth=0, highlightthickness=0)
cr02Frame.grid(column=2, row=0, padx=blockPad,pady=blockPad)
cr02Frame.grid_propagate(0)

cr02Label = Label(cr02Frame)
cr02Label.place(x=blockSize/2,y=blockSize/2 ,anchor=CENTER)


cr03Frame = LabelFrame(boardFrame, text="", width=blockSize, height=blockSize, borderwidth=0, highlightthickness=0)
cr03Frame.grid(column=3, row=0, padx=blockPad,pady=blockPad)
cr03Frame.grid_propagate(0)

cr03Label = Label(cr03Frame)
cr03Label.place(x=blockSize/2,y=blockSize/2 - 10,anchor=CENTER)


cr10Frame = LabelFrame(boardFrame, text="", width=blockSize, height=blockSize, borderwidth=0, highlightthickness=0)
cr10Frame.grid(column=0, row=1, padx=blockPad,pady=blockPad)
cr10Frame.grid_propagate(0)

cr10Label = Label(cr10Frame)
cr10Label.place(x=blockSize/2,y=blockSize/2 - 10,anchor=CENTER)


cr11Frame=LabelFrame(boardFrame, width=blockSize, height=blockSize, borderwidth=0, highlightthickness=0)
cr11Frame.grid(column=1, row=1, padx=blockPad, pady=blockPad)
cr11Frame.grid_propagate(0)

cr11Label=Label(cr11Frame)
cr11Label.place(x=blockSize/2, y=blockSize/2, anchor=CENTER)


cr12Frame=LabelFrame(boardFrame, width=blockSize, height=blockSize, borderwidth=0, highlightthickness=0)
cr12Frame.grid(column=2, row=1, padx=blockPad, pady=blockPad)
cr12Frame.grid_propagate(0)

cr12Label=Label(cr12Frame)
cr12Label.place(x=blockSize/2, y=blockSize/2, anchor=CENTER)


cr13Frame=LabelFrame(boardFrame, width=blockSize, height=blockSize, borderwidth=0, highlightthickness=0)
cr13Frame.grid(column=3, row=1, padx=blockPad, pady=blockPad)
cr13Frame.grid_propagate(0)

cr13Label=Label(cr13Frame)
cr13Label.place(x=blockSize/2, y=blockSize/2, anchor=CENTER)


cr20Frame=LabelFrame(boardFrame, width=blockSize, height=blockSize, borderwidth=0, highlightthickness=0)
cr20Frame.grid(column=0, row=2, padx=blockPad, pady=blockPad)
cr20Frame.grid_propagate(0)

cr20Label=Label(cr20Frame)
cr20Label.place(x=blockSize/2, y=blockSize/2, anchor=CENTER)


cr21Frame=LabelFrame(boardFrame, width=blockSize, height=blockSize, borderwidth=0, highlightthickness=0)
cr21Frame.grid(column=1, row=2, padx=blockPad, pady=blockPad)
cr21Frame.grid_propagate(0)

cr21Label=Label(cr21Frame)
cr21Label.place(x=blockSize/2, y=blockSize/2, anchor=CENTER)


cr22Frame=LabelFrame(boardFrame, width=blockSize, height=blockSize, borderwidth=0, highlightthickness=0)
cr22Frame.grid(column=2, row=2, padx=blockPad, pady=blockPad)
cr22Frame.grid_propagate(0)

cr22Label=Label(cr22Frame)
cr22Label.place(x=blockSize/2, y=blockSize/2, anchor=CENTER)


cr23Frame=LabelFrame(boardFrame, width=blockSize, height=blockSize, borderwidth=0, highlightthickness=0)
cr23Frame.grid(column=3, row=2, padx=blockPad, pady=blockPad)
cr23Frame.grid_propagate(0)

cr23Label=Label(cr23Frame)
cr23Label.place(x=blockSize/2, y=blockSize/2, anchor=CENTER)


cr30Frame=LabelFrame(boardFrame, width=blockSize, height=blockSize, borderwidth=0, highlightthickness=0)
cr30Frame.grid(column=0, row=3, padx=blockPad, pady=blockPad)
cr30Frame.grid_propagate(0)

cr30Label=Label(cr30Frame)
cr30Label.place(x=blockSize/2, y=blockSize/2, anchor=CENTER)


cr31Frame=LabelFrame(boardFrame, width=blockSize, height=blockSize, borderwidth=0, highlightthickness=0)
cr31Frame.grid(column=1, row=3, padx=blockPad, pady=blockPad)
cr31Frame.grid_propagate(0)

cr31Label=Label(cr31Frame)
cr31Label.place(x=blockSize/2, y=blockSize/2, anchor=CENTER)


cr32Frame=LabelFrame(boardFrame, width=blockSize, height=blockSize, borderwidth=0, highlightthickness=0)
cr32Frame.grid(column=2, row=3, padx=blockPad, pady=blockPad)
cr32Frame.grid_propagate(0)

cr32Label=Label(cr32Frame)
cr32Label.place(x=blockSize/2, y=blockSize/2, anchor=CENTER)


cr33Frame=LabelFrame(boardFrame, width=blockSize, height=blockSize, borderwidth=0, highlightthickness=0)
cr33Frame.grid(column=3, row=3, padx=blockPad, pady=blockPad)
cr33Frame.grid_propagate(0)

cr33Label=Label(cr33Frame)
cr33Label.place(x=blockSize/2, y=blockSize/2, anchor=CENTER)



labelDict = {0: [cr00Frame, cr00Label],
             1: [cr01Frame, cr01Label],
             2: [cr02Frame, cr02Label],
             3: [cr03Frame, cr03Label],
             4: [cr10Frame, cr10Label],
             5: [cr11Frame, cr11Label],
             6: [cr12Frame, cr12Label],
             7: [cr13Frame, cr13Label],
             8: [cr20Frame, cr20Label],
             9: [cr21Frame, cr21Label],
             10:[cr22Frame, cr22Label],
             11:[cr23Frame, cr23Label],
             12:[cr30Frame, cr30Label],
             13:[cr31Frame, cr31Label],
             14:[cr32Frame, cr32Label],
             15:[cr33Frame, cr33Label]
                }

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



#TODO Try dict to store all the values 

#Current goal is to have a dict of list of attributes of each block (bg, fg, fontSize, )

