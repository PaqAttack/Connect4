# Consolidated Game Version
# This version gives the user the ability to decide the control style of each player. Either player 1 or player 2 can be a human player or an AI.
# As I add new types of AI you can pit different AIs against each other.

# Who goes first is random

# NOTES TO SET UP AI v AI
# player_one_name is the name for player one
# player_two_name is the name for player two
# player_###_ctrl_type determines control type (AI v PLAYER)


# game_board is a list from index 0 in top left to 41 in bottom right
# E means a space is empty. This is made to appear invisible on output
# B is for black piece
# W is for black piece

#Useful Functions
# ValidatePiece(input) where input is a number 1-7. This validates a piece can be played in the corresponding column Output is True/False
# AddPiece(input, color) where input is column 1-7 and color is "B" or "W"
    # If you dont validate first AddPiece() can add in an invalid spot and it'll break

# AIOnePlay() and AITwoPlay() are the AI functions and all logic for AI should be in there (or functions called from there)

# AI names to differentiate
player_one_name = "AI One"
player_two_name = "AI Two"

# Not an option in game
rush_mode = True    # If this is true the AI will play at max speed. If this is False then you can watch every turn. Only an option if AI v AI

# Default player types (AI v PLAYER)
player_one_ctrl_type = "PLAYER"
player_two_ctrl_type = "AI"

import random
# Variables
# First try for game_board I'll use "B" for black", "W" for White and "E" for empty as the possible states 
# Will need a function to populate this because I'm not doing this manually.
game_board = [] #Game board will be a list
player_one_black_wins = False
player_two_white_wins = False
message_from_last_player = ""
ok_answers = [1,2,3,4,5,6,7] #played around with a few ways to validate input. this worked the best. Probably could be improved

# --- Generic Functions for cleaner code ---
def GameIntro():
    print("Welcome to Connect 4 - AI Battle!")
    print("The objective is to get 4 pieces of the same color in a row either")
    print("vertically, horizontally or diagonally before your opponnent does.")
    AddBreak(1)
    print("You may select each player to be either human or AI controlled. For AI") 
    print("players you will need to select a profile. At the moment there is only") 
    print("one but more to follow.") 

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
    global player_one_black_wins
    global player_two_white_wins
    for x in range(0, 6):       # Cycle through columns
        column_string = ""      # clear out string for each column
        for y in range(0,6):    # cycle through each row
            column_string = column_string + game_board[x+(7*y)]     # Creates a top to bottom string of each column
        if "BBBB" in column_string:     # Check for 4 Bs in a row in the column
            player_one_black_wins = True
        elif "WWWW" in column_string:   # Same for W
            player_two_white_wins = True

def CheckForHorizontalWin():
    global player_one_black_wins
    global player_two_white_wins
    for x in range(0, 36, 7):   #Cycle through rows starting at 0 and each multiple of 7 following
        row_string = ""         # clear out row string on each row
        for y in range(0,7):    # cycle through each column on the selected row
            row_string = row_string + game_board[x+y]     # Creates a left to right string of each row
        if "BBBB" in row_string:    # Same as above
            player_one_black_wins = True
        elif "WWWW" in row_string:  # Ditto
            player_two_white_wins = True

def CheckForRLDiagonalWin():        #I changes this to be 2 seperate functions. one for right to left and the other for left to right
    global player_one_black_wins
    global player_two_white_wins
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
            player_one_black_wins = True
        elif "WWWW" in diag_string:
            player_two_white_wins = True           

def CheckForLRDiagonalWin():    #This operates the same as above except looks the other way
    global player_one_black_wins
    global player_two_white_wins
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
            player_one_black_wins = True
        elif "WWWW" in diag_string:
            player_two_white_wins = True
        #Include subfunctions for checking vertical/horizontal/diagonal - Try not to just If/Then 100 times.....

def CheckIfValidMovesRemain():
    for x in range(0,6):
        if game_board[x].upper() == "E":
            return True
    return False

# WIN FUNCTIONS
def PlayerOneWinFunction():
    print(f"Player One ({player_one_ctrl_type}): {player_one_name.upper()} - BLACK - HAS WON!")

def PlayerTwoWinFunction():
    print(f"Player Two ({player_two_ctrl_type}): {player_two_name.upper()} - WHITE - HAS WON!")

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
                                                                                    
def AIOnePlay(player_name, player_ID, color):   #Left this as AIOne despite it being logic for all AI since I plan to have several options
    global message_from_last_player
    the_input = False
    while the_input == False:
        AI_Guess_Random = random.randint(1, 7)
        if ValidatePiece(AI_Guess_Random) == True:
            AddPiece(AI_Guess_Random, color.upper())
            message_from_last_player = (f"Player {player_ID} (AI): {player_name} plays in column {AI_Guess_Random}")
            the_input = True

def TakeTurn(player_number):        # Shared function so take in player number (1 or 2)   #I think this can be condensed a lot more than it is but i'll do that after its all tested and working
    global message_from_last_player
    if player_number == 1:          #Player 1's turn
        if player_one_ctrl_type == "AI":
            AIOnePlay(player_one_name, 1, "B")      # For AI pass in name, player number and color of game piece.
        else:                       # Human Player is player 1
            the_input = False
            print(f"It's Player 1: {player_one_name}'s turn!")
            while the_input == False:
                player_input = input("Play in Column number: ")
                for x in range(len(ok_answers)):
                    if player_input == str(ok_answers[x]):
                        final_input = int(ok_answers[x])
                        if ValidatePiece(final_input) == True:
                            AddPiece(final_input, "B")
                            message_from_last_player = (f"Player 1 (PLAYER): {player_one_name} plays in column {final_input}")
                            the_input = True
    if player_number == 2:      #player 2s turn
        if player_two_ctrl_type == "AI":
            AIOnePlay(player_two_name, 2, "W")      # For AI pass in name, player number and color of game piece.
        else:                       # Human Player is player 2
            the_input = False
            print(f"It's Player 2: {player_two_name}'s turn!")
            while the_input == False:
                player_input = input("Play in Column number: ")
                for x in range(len(ok_answers)):
                    if player_input == str(ok_answers[x]):
                        final_input = int(ok_answers[x])
                        if ValidatePiece(final_input) == True:
                            AddPiece(final_input, "W")
                            message_from_last_player = (f"Player 2 (PLAYER): {player_two_name} plays in column {final_input}")
                            the_input = True

# GAME START

# Introduce player to the game 
BuildBlankGameBoard()
GameIntro()
AddBreak(1)

# Explain rules
GameRules() # Rules are so simple I wont bother giving the option to repeat them.
AddBreak(1)

AskWhenRdy()

#Randomly select first player
start_first = random.randint(1,2)
if start_first == 1:
    Is_Player_One_Turn = True
else:
    Is_Player_One_Turn = False

while 1 == 1:                   #Not going to bother pretending here. I'll just break out when game over.
    if CheckIfValidMovesRemain() == True:
        if Is_Player_One_Turn == True:
            AddBreak(50)
            print(message_from_last_player)
            message_from_last_player = ""
            AddBreak(2)
            DrawBoard
            AddBreak(2)

            TakeTurn(1)
            CheckForWin()

            Is_Player_One_Turn = False
        else:
            AddBreak(50)
            print(message_from_last_player)
            message_from_last_player = ""
            AddBreak(2)
            DrawBoard
            AddBreak(2)

            TakeTurn(2)
            CheckForWin()

            Is_Player_One_Turn = True


        
        # After someone takes a turn check to see if someone won.
        if player_two_white_wins == True:        
            AddBreak(50)
            DrawBoard(game_board)
            AddBreak(1)
            PlayerTwoWinFunction()
            break
        elif player_one_black_wins == True:
            AddBreak(50)
            DrawBoard(game_board)
            AddBreak(1)
            PlayerOneWinFunction()
            break
    else:
        AddBreak(50)
        DrawBoard(game_board)
        print("GAME IS A TIE. NO WINNERS")
        break

AddBreak(1)
print(" --- GAME OVER ---")


            #if rush_mode == False and player_one_ctrl_type == "AI" and player_two_ctrl_type == "AI":
            #    AddBreak(50)
            #    DrawBoard(game_board)
            #    AddBreak(1)
            #    print(f"Player One ({player_one_ctrl_type}): {player_one_name} - BLACK - Has Played")