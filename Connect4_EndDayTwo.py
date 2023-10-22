

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
Black_Win = False
White_Win = False
ok_answers = [1,2,3,4,5,6,7] #played around with a few ways to validate input. this worked the best. Probably could be improved

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

def AskWhenRdy():
    AddBreak(1)
    dontcare = input("Press Enter to begin!")       #This just is to require player input to move to start game

def AddBreak(Qty):              # This allows me to add multiple extra lines without a ton of wasted space in code
    for x in range(0, int(Qty)):
        print("")

def BuildBlankGameBoard():      #This populates game_board at game start with E which tells the game the space is blank
    game_board.clear()
    for x in range(0, 42):
        game_board.append("E")

# Functions to control game flow

# Check for win
def CheckForWin():
    CheckForVerticalWin()
    CheckForHorizontalWin()
    CheckForRLDiagonalWin() # Right to left diag
    CheckForLRDiagonalWin() # Left to right diag

# Split these 4 up for cleaner coding as I expect this to be a challenge
def CheckForVerticalWin():
    global Black_Win
    global White_Win
    for x in range(0, 6):       # Cycle through columns
        column_string = ""      # clear out string for each column
        for y in range(0,6):    # cycle through each row
            column_string = column_string + game_board[x+(7*y)]     # Creates a top to bottom string of each column
        if "BBBB" in column_string:     # Check for 4 Bs in a row in the column
            Black_Win = True
        elif "WWWW" in column_string:   # Same for W
            White_Win = True

def CheckForHorizontalWin():
    global Black_Win
    global White_Win
    for x in range(0, 36, 7):   #Cycle through rows starting at 0 and each multiple of 7 following
        row_string = ""         # clear out row string on each row
        for y in range(0,7):    # cycle through each column on the selected row
            row_string = row_string + game_board[x+y]     # Creates a left to right string of each row
        if "BBBB" in row_string:    # Same as above
            Black_Win = True
        elif "WWWW" in row_string:  # Ditto
            White_Win = True

def CheckForRLDiagonalWin():        #I changes this to be 2 seperate functions. one for right to left and the other for left to right
    global Black_Win
    global White_Win
    right_diag_starts = [14, 7, 0, 1, 2, 3]     # Shortest way I could think of doing this would be make a list of all starting points that have at least 4 spots in their diagonal line.
    for x in range(len(right_diag_starts)):     # Cycle through each starting point
        diag_string = ""                        # Clear out string same as others
        reached_edge = False                    # Gotta stop looking for slots at the edge of the board
        for y in range(0,10):                   # Made this big enough to cover all situations plus some. I'll weed out numbers that are too big.
            if right_diag_starts[x-1]+(y*8) <= len(game_board)-1 and reached_edge == False:     # Check to ensure id'd spot is within game_board list and we have not reached an edge
                diag_string = diag_string + game_board[right_diag_starts[x-1]+(y*8)]            #Add spot to list of id'd spots
                if ((right_diag_starts[x-1]+(y*8))+1) % 7 == 0:                                 # If spot is 1 less than a number that's divisible by 7 then its on the right edge
                    reached_edge = True         # Since this spot is on the edge we don't want to look further.
            else:
                pass                            # This means we are out of bounds. pass means do nothing
        if "BBBB" in diag_string:
            Black_Win = True
        elif "WWWW" in diag_string:
            White_Win = True           

def CheckForLRDiagonalWin():    #This operates the same as above except looks the other way
    global Black_Win
    global White_Win
    Left_diag_starts = [3, 4, 5, 6, 13, 20]
    for x in range(len(Left_diag_starts)):
        diag_string = ""
        reached_edge = False
        for y in range(0,10):
            if Left_diag_starts[x-1]+(y*6) <= len(game_board)-1 and reached_edge == False:
                diag_string = diag_string + game_board[Left_diag_starts[x-1]+(y*6)]
                if (Left_diag_starts[x-1]+(y*6)) % 7 == 0:
                    reached_edge = True
            else:
                pass
        if "BBBB" in diag_string:
            Black_Win = True
        elif "WWWW" in diag_string:
            White_Win = True
        #Include subfunctions for checking vertical/horizontal/diagonal - Try not to just If/Then 100 times.....

# WIN FUNCTIONS
def PlayerWins():
    print("THE PLAYER HAS WON!")

def AIWins():
    print("THE COMPUTER HAS WON")

# Art Functions - Re-Use formatting tools from grade average assignment and art code concept from Hangman

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

def ValidatePiece(input):
    if type(input) != int:
        return False
    elif len(str(input)) != 1:
        return False
    elif game_board[int(input)-1] == "E":
        return True
    else:
        return False

#Added second argument to this so it can be called by AI or player (or maybe 2nd AI?)
def AddPiece(input, color):        #Input will be "W" or "B" for now
    global game_board
    column_list = []
    for x in range(input-1, input+35, 7):   # Create a list including the index of each column from top to bottom
        column_list.append(x)
    column_list.reverse()
    for x in range(len(column_list)):
        if game_board[column_list[x]] == "E":
            game_board[column_list[x]] = color.upper()
            return
    # If we get to here then no empty spots were found so we need a way to tell the user they cant do this
                                                                                    

# AI Functions - Easily the biggest challenge and real point of this program
#     Starting idea. pick best ~5 moves and then weight them and randomly select.
#     Maybe allow user to select difficulty which will impact weight of chances for each move.

def AIPlay():   #Right now this plays a random valid move while i test everything out
    the_input = False
    while the_input == False:
        AI_Guess_Random = random.randint(1, 7)
        if ValidatePiece(AI_Guess_Random) == True:
            AddPiece(AI_Guess_Random, "B")
            the_input = True

# GAME START

# Introduce player to the game 
BuildBlankGameBoard()
GameIntro()
AddBreak(1)

# Explain rules
GameRules() # Rules are so simple I wont bother giving the option to repeat them.
AddBreak(2)
AskWhenRdy()
Player_Turn = True

while 1 == 1:                   #Not going to bother pretending here. I'll just break out when game over.

    if Player_Turn == True:
        AddBreak(50)
        DrawBoard(game_board)
        print("")
        the_input = False
        print("It's your turn!")
        while the_input == False:
            player_input = input("Play in Column number: ")
            for x in range(len(ok_answers)):
                if player_input == str(ok_answers[x]):
                    final_input = int(ok_answers[x])
                    if ValidatePiece(final_input) == True:
                        AddPiece(final_input, "W")
                        the_input = True
            if the_input == False:
                AddBreak(1)
                print("Enter the number that corosponds with the column you wish to drop your next game piece into.")
                print("You can't play in a full column.")
                AddBreak(1)

        CheckForWin()
        Player_Turn = False
    else:
        AIPlay()
        #//TODO Figure out display. what does AI turn need to drive being shown to player? 
        # No need to print AI played X
        # on players next turn new board will be shown
        # Maybe have AIPlay populate a string and post that above the board? Yeah lets do that
        CheckForWin()
        Player_Turn = True

    if White_Win == True:
        AddBreak(50)
        DrawBoard(game_board)
        AddBreak(1)
        PlayerWins()
        break
    elif Black_Win == True:
        AddBreak(50)
        DrawBoard(game_board)
        AddBreak(1)
        AIWins()
        break

AddBreak(1)
print(" --- GAME OVER ---")

# Give Options
    # Difficulty - Maybe?
    #//TODO consider possible options given how AI and check win coding goes. 
    # Maybe add special win conditions (connect 5 or 3?)
    # AI trash talker function?

# Main Gameplay loop
    # While loop with display UI, get input and check for win
    # For input use column number
