#CMPT 120 Intro to Programming
#Lab #7 - Lists and Error Handling
#Author: Ryan Straub
#Created : 19-04-08

symbol = [" ", "x", "o"]
def printRow (row):
    # initialize output to the left border
    output = "|"
    # for each square in the row...
    for i in range(3):
        # add to output the symbol for this square followed by a border
        output = output + " " + symbol[row[i]] +" |"
    # print the completed output for this row
    print(output)
    pass

def printBoard(board):
    #print the top border
    print("+-----------+")
    #for each row in the board...
    for i in range(3):
        #print the row
        printRow(board[i])
        #print the next border
        print("+-----------+")
    pass

def markBoard(board, row, col, player):
    #check to see whether the desierd square is blank
    if board[row][col] == 0:
        #if so, set it to the player number
        board[row][col] = player
    else:
        print("That spot is already taken. Pick another one.")
    pass


def getPlayerMove():
    row = int(input("Select row to put X/O (1-3): "))
    col = int(input("Select column to put X/O (1-3): "))
    return (row-1, col-1)


def hasBlanks(board):
    # for each row in the board..
        for i in range(3):
    # for each square in the row..
            for j in range(3):
    # check whether the square is blank
                if board[i][j] == 0:
    # if so, return True
                    return True # if no square is blank, return False
            
        print("That space is already filled.")
        return False
            
def main():
    board = [[0,0,0],
             [0,0,0],
             [0,0,0]]# TODO replace this with a three-by-three matrix of zeros
    player = 1
    while hasBlanks(board):
        printBoard(board)
        row,col = getPlayerMove()
        markBoard(board,row,col,player)
        player = player % 2 + 1 # switch player for next turn
    printBoard(board)
    
main()

    
    
    
    
