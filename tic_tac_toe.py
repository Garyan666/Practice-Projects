
board = [" " for x in range(10)] # For any tic tac toe game the first thing we need is a board. This board list stores all our X's and O's. We take range 10 and " ", which is the leading position, so that we have 1-9, instead of 0-8. We always want the leading position to be empty otherwise it'll start from 0 instead of 1 
# Board is now: [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],  We can define the board by just replacing 'board = [" " for x in range(10)]' with 'board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

# Defining the required functions
def insertLetter(letter, pos): # To insert a letter into our board list
    board[pos] = letter

def spaceIsFree(pos):          # Checks if space is free. Basicalyy if it has either an X or an O.  # insertLetter() and spaceIsFree() are required for playerMove() and main()
    return board[pos] == " "   # Simply returns True or False, as it's a Boolean expression. 

def isWinner(bo, le):          # Checks for winner, i.e, when any of the rows, columns or diagonals are filled, the numbers, eg [1] represent the position, like [1] is the 1st row 1st column and [5] is 2nd row 2nd column and also the center
    # bo and le are nothing but board and letter. We're using these short forms so that we don't have to type as much
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (bo[2] == le and bo[5] == le and bo[8] == le) or (bo[3] == le and bo[6] == le and bo[9] == le) or  (bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le)

def playerMove():              # To ask the player for bis move and execute it
    run = True # We need this so that the loop runs until we get a valid no. 
    while run: # Keep looping until we get a valid move
        move = input("\nPlease select a position to place an 'X' from (1-9): ")
        try:
            move = int(move) # Checks if the input is an integer, if not it goes to the except statement
            if move > 0 and move < 10:  # Makes sure we type in an integer between 1-9
                if spaceIsFree(move):   # Checks if the move we choose is valid, i.e no other letter is there already
                    run = False         # If all the above conditions are satisfied, then the loop is not repeated again
                    insertLetter("X", move) # Because all the above conditions are satisfied the letter is inserted in the appropriate position
                else: 
                    print("\nSorry this space is occupied...")
            else:
                print("\nPlease type a number within the range!")
        except:
            print("\nPlease type a number...")

def selectRandom(li):          # Will randomly decide on a move to take given a list of possible positions, Imported from module random 
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]
    
def compMove():                # After the player makes his move, the move is made appropriately
    possibleMoves = [x for x, letter in enumerate(board) if letter == " " and x != 0] # Creates a list of possible moves
    move = 0 # Assigns the starting move to be 0, to signify that no move has been made 
    
    # Checks for possible winning move to take or to block opponents winning move
    for let in ["O", "X"]:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let 
            if isWinner(boardCopy, let):
                move = i
                return move

# Tries to take one of the corners
    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
    
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move
    
    # Tries to take the center
    if 5 in possibleMoves:
        move = 5
        return move

   # Take any edge
    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
    
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)

    return move

def isBoardFull(board):        # Checks if there are any spaces(" ") in the board, if there are then it's returned false, if not it's returned true
    if board.count(" ") > 1:    # We take > 1 and not >= 1 or > 0 bcuz we took range as 10 in the first line. We need there to always be an extra " ", so that we can start with [1], instead of [0]. We can use [0] as well, but it's more convenient to code using [1] in this case
        return False
    else:
        return True

def printBoard(board):         # Simply printing out the space where the game is played. Purely visual. The board[] are important cuz that's how we take the input for X's and O's position.

    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("-----------")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("-----------")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])

def main():                    # Where all fuctions come together and the actual 'game' of tic tac toe is defined 
    print("Welcome to Tic-Tac Toe!\n") # Opening statement. Nothing complex, just a simple greeting
    printBoard(board)                  # Prints out a blank 'board'
    
    while not(isBoardFull(board)): #1                 # Basically the loop runs as long as there is an empty space (" ") it will run
        if (isWinner(board, "O")): #2.1               # If any of the conditions to win are fulfilled by O, you lose and loop breaks
            print("\nSorry, O's won this time...\n")
            break
        else: #2.1                                    # If O hasn't won then the player gets a turn
            playerMove()
            printBoard(board)                         # Once the turn is done, the updated board is printed

        if  (isWinner(board,"X")): #2.2               # After player's turn is done, f any of the conditions to win are fulfilled by O, you win and loop breaks
            print("\nYou Won!!!\n")
            break
        else: #2.2                                    # If the player still hasn't won, then O, the computer gets a turn
            move = compMove()
            if move == 0: #3                          # If the board is full and nobody has won, then it's declared a tie
                print("\nTie Game.\n")
            else: #3                                  # If there is space on the board, the the computer places an O on the board and then informs us where it was placed
                insertLetter("O", move)
                print("\nComputer placed an O in position", move, "\n" ) 
                printBoard(board)
    
main()                         # Applying the defined functions...                                                                                                       