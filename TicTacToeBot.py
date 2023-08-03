#By Aidan Watson
from random import randint


board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]


def checkWin(board, player):
    for i in range(0, 7, 3):
        if(board[i] == player and board[i+1] == player and board[i+2] == player): #checking for horizontal win
            return True
        for i in range(0, 3):
            if(board[i] == player and board[i+3] == player and board[i+6] == player): #checking for vertical win
                return True
        if(board[0] == player and board[4] == player and board[8] == player): #checking for L-R diagonal win
            return True
        if(board[2] == player and board[4] == player and board[6] == player): #checking for R-L diagonal win
            return True
    return False    


def checkLose(board, player):
    if(player == "X"): #Checking if opponent won
        opponent = "O"
    else:
        opponent = "X"
    if(checkWin(board, opponent)):
        return True
    return False


def checkTie(board):
    for x in board: #Checking if all positions are full
        if(x == " "):
            return False
    return True


def getAIMove(board, nextMove, aiPlayer,numMove):
    Sides = [1,3,5,7]
    if numMove == 1:
        if board[0]=='X' or board[2]=='X' or board[6]=='X' or board[8]=='X':
            return 4
        elif board[4]=='X':
            #Could remove this and just use the else
            #keeping for now incase the else return 0 doesnt work
            return 0
        else: 
            return 0
    for i in range(0,8):
    #Checking if Player is one move away from win. If they are block it
        if board[i] == " ":
            board[i] = "X"
            if checkWin(board, "X"):
                board[i] = " "
                return i
            board[i] = " " #errasing temp X
    if numMove==3: #Not one move away from win
        if board[4] == "X": #If middle and bottom right is occupied by Player while Bot occupies top left
            return 2
        for i in Sides: #putting bot one move away from win
            if board[i] == " ":
                return i
    return 0

def getRandomBoard():
    filledPositions = randint(2, 8)
    board = [" " for _ in range(9)]
    r = randint(0, 1)
    moves = ["X", "O"]
    nextMove = moves[r]
    for i in range(filledPositions):
        pos = randint(0, 8)
    while(board[pos] != " "):
        pos = randint(0, 8)
        board[pos] = nextMove
        if(nextMove == "X"):
            nextMove = "O"
        else:
            nextMove = "X"
    return (board, nextMove)


def printBoard(board):
    print("\n")
    for i in range(9):
        if(not board[i] == " "):
            print (board[i], end=""),
        else:
            print ("_", end=""),
        if(i==2 or i==5):
            print("", end="")
            print("\n", end="")


# Now we'll write the main function which has all the gameplay functionality.
def game():
    moveNum = 0
    while(not (checkWin(board, "O") or checkLose(board, "O") or checkTie(board))):
        playerPosition = int(input("Where do you want to play X: ")) - 1
        if not board[playerPosition] == " ":
            print("Choose a new spot not already taken")
            continue
        moveNum+=1
        board[playerPosition] = "X"
        aiMovePosition = int(getAIMove(board, "O", "O",moveNum))
        board[aiMovePosition] = "O"
        printBoard(board)
        moveNum+=1
    print() #new line
    retry = int(input("Press 0 to play again and 1 to exit"))
    while not retry == 1:
        if retry == 0:
            break
        retry = int(input("Press 0 to play again and 1 to exit"))
    if retry == 0:
        for i in range(0,8,1):#resetting board
            board[i] = " "
        game()
    print("Thanks for playing!")



if __name__ == "__main__":
    game()
