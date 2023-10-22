
 #GAME DESIGN
 #Game of Connect 4 on a standard 7 wide x 6 tall board
 #Primary purpose of this program is smart AI playstyle. Dont make AI perfect but make them smart
 #Secondary - Try to find an efficient way to check for win conditions thats not an if statement for each possible position.

 #Use a list to store the game board - Use B and W for pieces atm

 #Goals:    Graphics output
 #          Versus Computer opponent
 #          Implement actually skilled AI

 #Challenges:   Check for win condition
 #              Skilled AI
 #              "Graphics"

 # Will certainly need random for AI to prevent always playing the same exact way.
import random

# Variables
# First try for game_board I'll use "B" for black", "W" for White and "E" for empty as the possible states 
# Will need a function to populate this because I'm not doing this manually.
game_board = [] #Game board will be a list

# --- Generic Functions for cleaner code ---
def GameIntro():
    print("Welcome to Connect 4!")
    print("The objective is to get 4 of your game pieces in a row")
    print("either vertically, horizontally or diagonally before your opponnent.")
    AddBreak(1)
    print("In this case, your opponent will be a trash talking AI who thinks") 
    print("they're on the path to world domination. Dash their hopes here and now!")

def GameRules():        #//TODO This needs to be expanded upon a bit but atm its a WIP
    print("GAME RULES")
    print("Enter a number of the column you wish to drop your piece down.")
    print("First one win get 4 in a row wins.")

def AddBreak(Qty):
    for x in range(0, int(Qty)):
        print("")

def BuildBlankGameBoard():
    game_board.clear()
    for x in range(0, 42):      #0-41 results in len(game_board) = 41 which seems off..... gotta make sure about this. Will tweak when seting up game board
        game_board.append("E")

# Functions to control game flow
    # Check for win
def CheckForWin():
    CheckForVerticalWin()
    CheckForHorizontalWin()
    CheckForDiagonalWin()

# Split these 3 up for cleaner coding as I expect this to be a challenge
def CheckForVerticalWin():
    pass

def CheckForHorizontalWin():
    pass

def CheckForDiagonalWin():
    pass

        #Include subfunctions for checking vertical/horizontal/diagonal - Try not to just If/Then 100 times.....
    # ANything else?....

# Art Functions - Re-Use formatting tools from grade average assignment and art code concept from Hangman
    #//TODO Sketch UI first to avoid problems from hangman with 5+ re-designs

# Make DrawBoard() ONLY draw the board. 
def DrawBoard(provided_board):        
    print("  1   2   3   4   5   6   7")
    print("____________________________")
    for x in range(0,36,7):     # ending at 36 means it can trigger on 35 and then I dont need it to go any further.
        print(f"| {Translate(provided_board[x])} | {Translate(provided_board[x+1])} | {Translate(provided_board[x+2])} | {Translate(provided_board[x+3])} | {Translate(provided_board[x+4])} | {Translate(provided_board[x+5])} | {Translate(provided_board[x+6])} |")
        if x != 35: #Its not last line
            print("|--- --- --- --- --- --- ---|")
    print("|---------------------------|")

# I added a translate feature to allow for me to easily change how the game pieces look without changing any other code.
# Right now I'm using it to blank out the E which stands for empty.
def Translate(input):
    if input == "E":
        return " "
    else:
        return input


def AddPiece(input):        #Input will be "W" or "B"
    global game_board
    column_list = []
    for x in range(input-1, input+35, 7):   # Create a list including the index of each column from top to bottom
        column_list.append(x)
    column_list.reverse()
    for x in range(len(column_list)):
        if game_board[column_list[x]] == "E":
            game_board[column_list[x]] = "W"
            return
    # If we get to here then no empty spots were found so we need a way to tell the user they cant do this

#Idea 1: Too Small
#_______________
#|B| | | | | | |
#|B| | | | | | |
#|B| | | | | | |
#|B| | | | | | |
#|B| | | | | | |
#|B| | | | | | |
#---------------

#Idea 2: Maybe?
#____________________________
#| B |   |   |   |   |   |   |
#| B |   |   |   |   |   |   |
#| B |   |   |   |   |   |   |
#| B |   |   |   |   |   |   |
#| B | W |   |   |   |   |   |
#| B | W | W |   |   |   |   |
#-----------------------------

#Idea 3: I like it
#  1   2   3   4   5   6   7
#____________________________
#| B |   |   |   |   |   |   |
#|--- --- --- --- --- --- ---|
#| B |   |   |   |   |   |   |
#|--- --- --- --- --- --- ---|
#| B |   |   |   |   |   |   |
#|--- --- --- --- --- --- ---|
#| B |   |   |   |   |   |   |
#|--- --- --- --- --- --- ---|
#| B | W |   |   |   |   |   |
#|--- --- --- --- --- --- ---|
#| B | W | W |   |   |   |   |
#|---------------------------|

#Output Ideas
#Info to display:
#    Board - duh
#    Whose turn is it?
#    warn at 3 in a row? option? for now... No
#    prompt for input. How do I ask?

#|---------------------------|       Bottom of Board

#It is your turn

#----Pick something to prompt for input... these all sound dumb to me.
#What column do you select?
#Drop in column: 
#Where do you play?
#Drop your piece: 
#Play in column:                                                                                     

# AI Functions - Easily the biggest challenge and real point of this program
#     Starting idea. pick best ~5 moves and then weight them and randomly select.
#     Maybe allow user to select difficulty which will impact weight of chances for each move.

def AIPlay():
    pass

# GAME START

# Introduce player to the game 
BuildBlankGameBoard()
GameIntro()
AddBreak(1)

# Explain rules
GameRules() # Rules are so simple I wont bother giving the option to repeat them.
AddBreak(5)

while 1 == 1:
    DrawBoard(game_board)
    print("")
    player_input = int(input("Play in Column number: "))
    AddPiece(player_input)

#//TODO Let me add a piece in a loop

# Give Options
    # Difficulty - Maybe?
    #//TODO consider possible options given how AI and check win coding goes. 
    # Maybe add special win conditions (connect 5 or 3?)
    # AI trash talker function?

# Main Gameplay loop
    # While loop with display UI, get input and check for win
    # For input use column number
