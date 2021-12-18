import numpy as np
import random as r

board = np.zeros((4,4))
clearSpace = []

for i in range(4):
    for j in range(4):
        clearSpace.append(tuple((i,j)))


def null_space(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0 and tuple((i,j)) not in clearSpace: 
                clearSpace.append(tuple((i,j)))
            elif board[i][j] != 0 and tuple((i,j)) in clearSpace:
                clearSpace.remove(tuple((i,j)))


def print_board(board):
    
    for row in board:
        string_row = str(row).replace("[", "").replace("]", "").replace(".", "")
        print(string_row)
    
    
def upMove(board):
    for i in reversed(range(1,4)):
        for j in reversed(range(4)):
            
            if board[i-1][j] == 0 or board[i-1][j] == board[i][j]:
                board[i-1][j] += board[i][j]
                board[i][j] = 0 

def downMove(board):
    for i in range(0,3):
        for j in range(4):
            
            if board[i+1][j] == 0 or board[i+1][j] == board[i][j]:
                board[i+1][j] += board[i][j]
                board[i][j] = 0

def leftMove(board):
    for i in reversed(range(4)):
        for j in reversed(range(1,4)):
            
            if board[i][j-1] == 0 or board[i][j-1] == board[i][j]:
                board[i][j-1] += board[i][j]
                board[i][j] = 0

def rightMove():
    for i in range(4):
        for j in range(0,3):
            
            if board[i][j+1] == 0 or board[i][j+1] == board[i][j]:
                board[i][j+1] += board[i][j]
                board[i][j] = 0
                
                
                
while True:
    
    stop = input()
    
    
    randVal = r.randint(1,2) * 2
    
    #//
    randSpace = r.randint(0, (len(clearSpace)-1))
    x = clearSpace[randSpace][0]
    y = clearSpace[randSpace][1]
    board[x][y] = randVal #adds a value in the board
    #//
    
    
    rightMove() #mvoes the board up 
    
    
    null_space(board) #appends clearSpcae
    
    print_board(board)
    #print(clearSpace)
    
    if len(clearSpace) == 0:
        break

print("game over!")


