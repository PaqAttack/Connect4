# Consolidated Game Version

# CODE HAS BEEN HEAVILY RESTRUCTURED AND PSEUDOCODE UPDATED

# Code is organized as follows:
#   SIMPLE GENERIC FUNCTIONS
#   CHECK FOR WIN FUNCTIONS
#   TAKE TURN FUNCTION
#   AI FUNCTIONS
#   MAIN GAMEPLAY LOOP

# This version gives the user the ability to decide the control style of each player. Either player 1 or player 2 can be a human player or an AI.
# All AI is assigned a profile which determines which function is called when they take a turn.
# If only 1 profile is available then it's auto assigned. If there are several then the user is prompted to pick one.

# Currently there are 2 AIs loaded Random Moves and Super Smart. Both are the same and exist for demo purposes only.
# Instructions for loading new AIs are listed in the AI FUNCTION section

# Who goes first is random

# game_board is a list from index 0 in top left to 41 in bottom right
# E means a space is empty. This is made to appear invisible on output
# B is for black pieces
# W is for white pieces

#Useful Functions
# ValidatePiece(input) where input is a number 1-7. This validates a piece can be played in the corresponding column Output is True/False
# AddPiece(input, color) where input is column 1-7 and color is "B" or "W"
    # If you dont validate first AddPiece() can add in an invalid spot and AddPiece() will notice and end the program

# ---------------- IMPORTS ----------------
import random
import sys
# ---------------- GAME VARIABLES ----------------

# AI names to differentiate - This sets default but will be changed by player input
player_one_name = "Human Player"
player_two_name = "AI Two"

# Presented as an option for AI v AI matches
rush_mode = False    # If this is true the AI will play at max speed. If this is False then you can watch every turn. Only an option if AI v AI

# Default player types (AI v PLAYER) - This will be changed by player input during options selection
player_one_ctrl_type = "PLAYER"
player_two_ctrl_type = "AI"

#The game board 
game_board = [] # This is populated by a function at the start as 42 "E"s I will make temp versions for AI to evaluate. This will only ever be the legit gameboard

# Win triggers
player_one_black_wins = False
player_two_white_wins = False
sim_black_win = False
sim_white_win = False

# This will populate with the last action done and display above the gameboard as a reference
message_from_last_player = ""

# Used to help validate proper input.
ok_answers = [1,2,3,4,5,6,7] #played around with a few ways to validate input. this worked the best. Probably could be improved


# --------------------- SIMPLE GENERIC FUNCTIONS ---------------------
# --------------------- SIMPLE GENERIC FUNCTIONS ---------------------
# --------------------- SIMPLE GENERIC FUNCTIONS ---------------------
# --------------------- SIMPLE GENERIC FUNCTIONS ---------------------


def GameIntro():        # Welcomes the player to the game
    print("Welcome to Connect 4")
    print("The objective is to get 4 pieces of the same color in a row either")
    print("vertically, horizontally or diagonally before your opponnent does.")
    AddBreak(1)
    print("You may select each player to be either human or AI controlled. For AI") 
    print("players you will need to select a profile. At the moment there is only") 
    print("one but more to follow.") 

def GameRules():        # Explains game rules
    print("GAME RULES")
    print("Enter a number of the column you wish to drop your piece down.")
    print("First one win get 4 in a row wins.")

def AskWhenRdy():       # Require player input to proceed past this point
    dontcare = input("Press Enter to continue!") 

def AddBreak(Qty):              # This allows me to add multiple extra lines without a ton of wasted space in code
    for x in range(0, int(Qty)):
        print("")

def BuildBlankGameBoard():      #This populates game_board at game start with E which tells the game the space is blank
    game_board.clear()
    for x in range(0, 42):
        game_board.append("E")

def CreateOfLength(input_string, length):       # Simple utility function that takes a string and a length and makes the input string the length that was requested but with a blank space at the end.
    if len(str(input_string)) >= length:        # If input string is longer than desired
        the_output = str(input_string)[:length-1] + " "     # Cut string off 1 character short of desired length and add a blank at the end
    else:                                       # If input is less than desired length
        the_output = str(input_string)
        for x in range(length-len(str(input_string))):  # Add blank spaces to the end to make it the right length
            the_output += " "
    return the_output

def AttachProfile(player):      # This will hook up an AI profile to each AI player.
    global available_ai_profiles
    global player_one_AI_profile
    global player_two_AI_profile
    if player == 1:
        if len(available_ai_profiles) == 1:        # If only 1 AI is in the list of available profiles then its auto assigned and the player is not told anything
            player_one_AI_profile = available_ai_profiles[0]
        else:                   # If there are more AI profiles available then the player must select one.
            AddBreak(1)
            print("You must select an AI profile for Player 1")
            AddBreak(1)
            for x in range(len(available_ai_profiles)):     # Print out all options in a list
                print(f"{x+1} - {available_ai_profiles[x]}")
            selection = input("Enter the number of the profile you want to select: ")   
            try:
                player_one_AI_profile = available_ai_profiles[int(selection)-1]
            except:               # If invalid entry then select profile 1 (index 0)
                AddBreak(1)
                print("Error in selection. Profile 1 is being loaded.")
                player_one_AI_profile = available_ai_profiles[0]
    if player == 2:             # SAME AS ABOVE FOR PLAYER 2
        if len(available_ai_profiles) == 1:
            player_two_AI_profile = available_ai_profiles[0]
        else:
            AddBreak(1)
            print("You must select an AI profile for Player 1")
            AddBreak(1)
            for x in range(len(available_ai_profiles)):
                print(f"{x+1} - {available_ai_profiles[x]}")
            selection = input("Enter the number of the profile you want to select: ")
            try:
                player_two_AI_profile = available_ai_profiles[int(selection)-1]
            except:
                AddBreak(1)
                print("Error in selection. Profile 1 is being loaded.")
                player_two_AI_profile = available_ai_profiles[0]

def GiveGameOptions():          # This will present the user with all the available options
    global player_one_name
    global player_two_name
    global player_one_ctrl_type
    global player_two_ctrl_type
    global rush_mode
    print("Select who will control Player 1")       # Select who controls player 1
    print("1 - Human")
    print("2 - AI")
    POne = input("Enter 1 or 2: ")
    if POne == "1":
        player_one_ctrl_type = "PLAYER"             # Set control type
    else:
        player_one_ctrl_type = "AI"
        AttachProfile(1)
    AddBreak(1)
    player_one_name = input("What is Player 1's name (Limit 10 characters): ")      # Set player 1 name
    if len(player_one_name) > 10:
        player_one_name = player_one_name[:10]                                      # Cut down to 10 characters if too long.
        print(f"Name has been shrunk to: {player_one_name}")
    AddBreak(2)

    print("Select who will control Player 2")        # Same process for player 2
    print("1 - Human")
    print("2 - AI")
    PTwo = input("Enter 1 or 2: ")
    if PTwo == "1":
        player_two_ctrl_type = "PLAYER"
    else:
        player_two_ctrl_type = "AI"
        AttachProfile(2)
    AddBreak(1)
    player_two_name = input("What is Player 2's name (Limit 10 characters): ")
    if len(player_two_name) > 10:
        player_two_name = player_two_name[:10]
        print(f"Name has been shrunk to: {player_two_name}")

    if player_one_ctrl_type == "AI" and player_two_ctrl_type == "AI":           # If both players are AI ask if you want rush mode
        AddBreak(1)
        print("You have chosen 2 AI players. Would you like to see")
        print("each turn or allow them to operate at the speed of light?")
        AddBreak(1)
        print("1 - See Each Turn")
        print("2 - Speed of Light (You will see the game result instantly...nearly)")
        AddBreak(1)
        selection = input("Choose 1 or 2: ")
        if selection == "1":
            rush_mode = False
        else:
            rush_mode = True

    AddBreak(50)            # Clear the screen and show selections - This doesnt look great atm. WIP
    print("---- You have chosen the following contest! ----")
    AddBreak(1)
    if player_one_ctrl_type == "PLAYER":
        print(f"PLAYER 1: {CreateOfLength(player_one_name.upper(), 11)} - {CreateOfLength(player_one_ctrl_type, 7)} will play as Black")
    else:                   # If AI then display AI profile
        print(f"PLAYER 1: {CreateOfLength(player_one_name.upper(), 11)} - {CreateOfLength(player_one_ctrl_type, 7)} will play as Black  (AI Profile: {player_one_AI_profile})")
    AddBreak (1)
    print("              ---- Versus ----")
    AddBreak(1)

    if player_two_ctrl_type == "PLAYER":
        print(f"PLAYER 2: {CreateOfLength(player_two_name.upper(), 11)} - {CreateOfLength(player_two_ctrl_type, 7)} will play as White")
    else:                   # If AI then display AI profile
        print(f"PLAYER 2: {CreateOfLength(player_two_name.upper(), 11)} - {CreateOfLength(player_two_ctrl_type, 7)} will play as White  (AI Profile: {player_two_AI_profile})")

    AddBreak(2)
    PickRandomFirstPlayer() #determine who goes first (randomly)
    if Is_Player_One_Turn == True:      # Tell the player who was chosen
        print("Player 1 will go first!")
    else:
        print("Player 2 will go first!")

    if rush_mode == True:   # Tell player if rush mode is on
        AddBreak(2)
        print("         --- RUSH MODE IS ACTIVE ---")
 
def CheckIfValidMovesRemain():      # Verifies there are still moves that can be played. This will protect against a full board with no wins. game logic calls this a tie if false
    for x in range(0,6):            # Only looks at top 7 slots (index 0-6)
        if game_board[x].upper() == "E":    # If anything comes back as empty then a move remains
            return True
    return False

def PlayerOneWinFunction():         # Called when player 1 wins. I may make this more snazzy later
    print(f"Player One ({player_one_ctrl_type}): {player_one_name.upper()} - BLACK - HAS WON!")

def PlayerTwoWinFunction():         # Called when player 2 wins.
    print(f"Player Two ({player_two_ctrl_type}): {player_two_name.upper()} - WHITE - HAS WON!")

def DrawBoard(provided_board):      # Draw the gameboard
    print("  1   2   3   4   5   6   7")
    print("____________________________")
    for x in range(0,36,7):     # ending at 36 means it can trigger on 35 and then I dont need it to go any further.
        print(f"| {Translate(provided_board[x])} | {Translate(provided_board[x+1])} | {Translate(provided_board[x+2])} | {Translate(provided_board[x+3])} | {Translate(provided_board[x+4])} | {Translate(provided_board[x+5])} | {Translate(provided_board[x+6])} |")
        if x != 35: # This means its not last line so print a special seperator
            print("|--- --- --- --- --- --- ---|")
    print("|---------------------------|")

def Translate(input):   # Used when printing game board to swap E with blank
    if input == "E":
        return " "
    else:
        return input

def ValidatePiece(board, input):       # error checking to ensure a piece can go into the input column
    if type(input) != int:      # if input is not type int
        return False
    elif len(str(input)) != 1:  # If length is too long
        return False
    elif board[int(input)-1] == "E":   # if the top slot in the selected column is empty then we are good to go
        return True
    else:
        return False

def PickRandomFirstPlayer():    # Randomly select first player
    global Is_Player_One_Turn
    start_first = random.randint(1,2)
    if start_first == 1:
        Is_Player_One_Turn = True
    else:
        Is_Player_One_Turn = False

def AddPiece(input, color):     # Adds a piece to the board. Input is the column and color is either "B" or "W"
    global game_board
    if ValidatePiece(game_board, input) == False:   # catch if an AI enters a bad move.
        print("You didn't validate this move! Programming bug here. Fix and restart program. Behavior after this will fail")
        sys.exit(1)
    column_list = []            # Make a blank temp list that will hold the columns status
    for x in range(input-1, input+35, 7):   # Create a list including the index of each column from top to bottom
        column_list.append(x)   
    column_list.reverse()       # Reverse the list so we look for the first E going from bottom up
    for x in range(len(column_list)):
        if game_board[column_list[x]] == "E":
            game_board[column_list[x]] = color.upper()  # Swaps first E from bottom to top with the input color to show that pice has been played.
            return

# --------------------- END OF SIMPLE GENERIC FUNCTIONS ---------------------
# --------------------- END OF SIMPLE GENERIC FUNCTIONS ---------------------

# --------------------- START OF CHECK FOR WIN FUNCTIONS ---------------------
# --------------------- START OF CHECK FOR WIN FUNCTIONS ---------------------

def CheckForWin(input_gameboard, code):              # This function is called after a player's turn and it checks for a win condition and updates a global bool if someone won.

    # MODIFIED: adapted to work with a sim or real gameboard
    # CODE 1 = real - trigger actual game win
    # CODE 2 = sim - just make sim var true

    CheckForVerticalWin(input_gameboard, code)       # This function checks all columns for 4 in a row
    CheckForHorizontalWin(input_gameboard, code)     # This function checks all rows for 4 in a row
    CheckForRLDiagonalWin(input_gameboard, code)     # This function checks all diagonals from right to left for 4 in a row
    CheckForLRDiagonalWin(input_gameboard, code)     # This function checks all diagonals from left to right for 4 in a row

def CheckForVerticalWin(input_gameboard, code):      # This function checks all columns for 4 in a row
    global sim_black_win
    global sim_white_win
    global player_one_black_wins
    global player_two_white_wins
    for x in range(0, 6):       # Cycle through columns
        column_string = ""      # clear out string for each column
        for y in range(0,6):    # cycle through each row
            column_string = column_string + input_gameboard[x+(7*y)]     # Creates a top to bottom string of each column
        if "BBBB" in column_string:     # Check for 4 Bs in a row in the column
            if code == 1:
                player_one_black_wins = True
            else:
                sim_black_win = True
        elif "WWWW" in column_string:   # Same for W
            if code == 1:
                player_two_white_wins = True
            else:
                sim_white_win = True

def CheckForHorizontalWin(input_gameboard, code):    # This function checks all rows for 4 in a row
    global sim_black_win
    global sim_white_win    
    global player_one_black_wins
    global player_two_white_wins
    for x in range(0, 36, 7):   #Cycle through rows starting at 0 and each multiple of 7 following
        row_string = ""         # clear out row string on each row
        for y in range(0,7):    # cycle through each column on the selected row
            row_string = row_string + input_gameboard[x+y]     # Creates a left to right string of each row
        if "BBBB" in row_string:    # Same as above
            if code == 1:
                player_one_black_wins = True
            else:
                sim_black_win = True
        elif "WWWW" in row_string:  # Ditto
            if code == 1:
                player_two_white_wins = True
            else:
                sim_white_win = True

def CheckForRLDiagonalWin(input_gameboard, code):    # This function checks all diagonals from right to left for 4 in a row
    global sim_black_win
    global sim_white_win
    global player_one_black_wins
    global player_two_white_wins
    right_diag_starts = [14, 7, 0, 1, 2, 3]     # Shortest way I could think of doing this would be make a list of all starting points that have at least 4 spots in their diagonal line.
    for x in range(len(right_diag_starts)):     # Cycle through each starting point
        diag_string = ""                        # Clear out string same as others
        reached_edge = False                    # Gotta stop looking for slots at the edge of the board
        for y in range(0,10):                   # Made this big enough to cover all situations plus some. I'll weed out numbers that are too big.
            if right_diag_starts[x-1]+(y*8) <= len(game_board)-1 and reached_edge == False:     # Check to ensure id'd spot is within game_board list and we have not reached an edge
                diag_string = diag_string + input_gameboard[right_diag_starts[x-1]+(y*8)]            #Add spot to list of id'd spots
                if ((right_diag_starts[x-1]+(y*8))+1) % 7 == 0:                                 # If spot is 1 less than a number that's divisible by 7 then its on the right edge
                    reached_edge = True         # Since this spot is on the edge we don't want to look further.
            else:
                pass                            # This means we are out of bounds. pass means do nothing
        if "BBBB" in diag_string:
            if code == 1:
                player_one_black_wins = True
            else:
                sim_black_win = True
        elif "WWWW" in diag_string:  # Ditto
            if code == 1:
                player_two_white_wins = True
            else:
                sim_white_win = True        

def CheckForLRDiagonalWin(input_gameboard, code):    # This function checks all diagonals from left to right for 4 in a row
    global sim_black_win
    global sim_white_win
    global player_one_black_wins
    global player_two_white_wins
    Left_diag_starts = [3, 4, 5, 6, 13, 20]
    for x in range(len(Left_diag_starts)):
        diag_string = ""
        reached_edge = False
        for y in range(0,10):
            if Left_diag_starts[x-1]+(y*6) <= len(game_board)-1 and reached_edge == False:
                diag_string = diag_string + input_gameboard[Left_diag_starts[x-1]+(y*6)]
                if (Left_diag_starts[x-1]+(y*6)) % 7 == 0:
                    reached_edge = True
            else:
                pass
        if "BBBB" in diag_string:
            if code == 1:
                player_one_black_wins = True
            else:
                sim_black_win = True
        elif "WWWW" in diag_string:  # Ditto
            if code == 1:
                player_two_white_wins = True
            else:
                sim_white_win = True  

# --------------------- END OF CHECK FOR WIN FUNCTIONS ---------------------
# --------------------- END OF CHECK FOR WIN FUNCTIONS ---------------------

# --------------------- TAKE TURN FUNCTION ---------------------
# --------------------- TAKE TURN FUNCTION ---------------------
                                                                                    
def TakeTurn(player_number):        # Shared function so take in player number (1 or 2)   #I think this can be condensed a lot more than it is but i'll do that after its all tested and working
    global message_from_last_player
    if player_number == 1:          #Player 1's turn
        if player_one_ctrl_type == "AI":

            if player_one_AI_profile == "Random Moves": # Add If statement for each added profile and direct to the appropriate function
                AIOnePlay(player_one_name, 1, "B")      # For AI pass in name, player number and color of game piece. Some AI could be different but not advised.
            elif player_one_AI_profile == "Super Smart":
                SSAIPlay(player_one_name, 1, "B")
            else:
                pass

        else:                       # Human Player is player 1
            the_input = False
            print(f"It's Player 1: {player_one_name}'s turn!")
            while the_input == False:
                player_input = input("Play in Column number: ")
                for x in range(len(ok_answers)):
                    if player_input == str(ok_answers[x]):
                        final_input = int(ok_answers[x])
                        if ValidatePiece(game_board, final_input) == True:
                            AddPiece(final_input, "B")
                            message_from_last_player = (f"Player 1 (PLAYER): {player_one_name} plays in column {final_input}")
                            the_input = True
    if player_number == 2:      #player 2s turn
        if player_two_ctrl_type == "AI":

            if player_two_AI_profile == "Random Moves": # Add If statement for each added profile and direct to the appropriate function
                AIOnePlay(player_two_name, 2, "W")      # For this AI I pass in name, player number and color of game piece.
            elif player_two_AI_profile == "Super Smart":
                SSAIPlay(player_two_name, 2, "W")
            else:
                pass

        else:                       # Human Player is player 2
            the_input = False
            print(f"It's Player 2: {player_two_name}'s turn!")
            while the_input == False:
                player_input = input("Play in Column number: ")
                for x in range(len(ok_answers)):
                    if player_input == str(ok_answers[x]):
                        final_input = int(ok_answers[x])
                        if ValidatePiece(game_board, final_input) == True:
                            AddPiece(final_input, "W")
                            message_from_last_player = (f"Player 2 (PLAYER): {player_two_name} plays in column {final_input}")
                            the_input = True


# --------------------- END OF TAKE TURN FUNCTION ---------------------
# --------------------- END OF TAKE TURN FUNCTION ---------------------

# --------------------- START OF AI FUNCTIONS ---------------------
# --------------------- START OF AI FUNCTIONS ---------------------

# Populate available_ai_profiles with names for each completed profile. This will be how the user views them in options.
# Hook up player AI profile names to apprpriate function in TakeTurn()
# If there is only 1 then its auto assigned. If there are more the user will be prompted to select one
available_ai_profiles = ["Random Moves", "Super Smart"]

# Random Moves AI profile.
def AIOnePlay(player_name, player_ID, color):   #Left this as AIOne despite it being logic for all AI since I plan to have several options
    global message_from_last_player
    the_input = False
    while the_input == False:
        AI_Guess_Random = random.randint(1, 7)
        if ValidatePiece(game_board, AI_Guess_Random) == True:
            AddPiece(AI_Guess_Random, color.upper())
            message_from_last_player = (f"Player {player_ID} (AI): {player_name} plays in column {AI_Guess_Random}")
            the_input = True

# SuperSmart AI profile. - created to test multiple AIs
def SSAIPlay(player_name, player_ID, color):
    global message_from_last_player

    # Set colors for self and opponent
    my_color = color
    if color == "B":
        Opponent_color = "W"
    else:
        Opponent_color = "B"

    # Build and populate a new sim board each turn
    sim_board = []
    for y in range(0, 42):
        sim_board.append(game_board[y])

    # Clear past input
    the_input = False

    # Gameplay loop to search for move
    while the_input == False:

        # This block sims a piece being added to each slot and checks if there are any win conditions. If there are then that is the move thats played
        for x in range(1, 8):
            if ValidatePiece(sim_board, x) == True:
                SimPlay(sim_board, x, my_color)
                sim_board = []
                for y in range(0, 42):
                    sim_board.append(game_board[y])
            if WasWinningMove():
                # If this is true then that play is a winning move for the AI so it should do it.
                AddPiece(x, my_color.upper())  # Plays move on real board
                message_from_last_player = (f"Player {player_ID} (AI): {player_name} plays in column {x} - Winning Move")
                the_input = True
                break

        #Skip this if an above higher priority move was identified
        for x in range(1, 8):
            if ValidatePiece(sim_board, x) == True and the_input == False:
                SimPlay(sim_board, x, Opponent_color)
                sim_board = []
                for y in range(0, 42):
                    sim_board.append(game_board[y])
                if WasWinningMove():
                    # If this is true then that play is a winning move for the opponent so lets block it
                    AddPiece(x, my_color.upper())  # Plays move on real board
                    message_from_last_player = (f"Player {player_ID} (AI): {player_name} plays in column {x} - Blocking move")
                    the_input = True
                    break
            

        # If none of the above checks give higher priority moves then a random move is made
        AI_Guess_Random = random.randint(1, 7)
        if ValidatePiece(game_board, AI_Guess_Random) == True and the_input == False:
            AddPiece(AI_Guess_Random, color.upper())
            message_from_last_player = (f"Player {player_ID} (AI): {player_name} plays in column {AI_Guess_Random} - Random Move")
            the_input = True

# --------------------- END OF AI BASE FUNCTIONS ---------------------
# --------------------- END OF AI BASE FUNCTIONS ---------------------

# --------------------- START OF AI SUPPORT FUNCTIONS ---------------------
# --------------------- START OF AI SUPPORT FUNCTIONS ---------------------

def SimPlay(board, input, color):
    column_list = [] 
    played = False
    for x in range(input-1, input+35, 7): 
        column_list.append(x)   
    column_list.reverse()   
    for x in range(len(column_list)):
        if board[column_list[x]] == "E" and played == False:
            board[column_list[x]] = color.upper()
            played = True
            # With the update made check for win with sim code of 2
            CheckForWin(board, 2)   # This will trigger a win bool update which we'll see above. If no wins then nothing happens and the change wont be saved as this function treats sim_board as view only
            break

# Check if a simmed move caused win condition
def WasWinningMove():
    global sim_white_win
    global sim_black_win
    # The only change is for the current AI so the only plays will be with current AI color so checking for both prevents us needing to care about distinguishing them.
    if sim_black_win == True or sim_white_win == True:
        sim_white_win = False   #Reset these to false since this looks at opponent plays to and a simmed play by them will trigger and random move on their next turn to make AI think it won
        sim_black_win = False
        return True
    else:
        return False


# --------------------- END OF AI SUPPORT FUNCTIONS ---------------------
# --------------------- END OF AI SUPPORT FUNCTIONS ---------------------

# --------------------- START OF MAIN GAMEPLAY LOOP ---------------------
# --------------------- START OF MAIN GAMEPLAY LOOP ---------------------

# Game Setup
BuildBlankGameBoard()

# Introduce player to the game 
GameIntro()
AddBreak(1)
# Explain rules
GameRules()
AddBreak(1)

# Ask player for AI/Human, Rush Mode yes/no and player names. Rush mode is only an option for AI v AI
GiveGameOptions()
AddBreak(1)

# Require user input to start so they can review their selections and choose when to proceed
AskWhenRdy()

while 1 == 1:                   #Not going to bother pretending here. I'll just break out when game over.
    if CheckIfValidMovesRemain() == True:   # Verifies there is still a valid move and the board is not full
        if Is_Player_One_Turn == True:
            if rush_mode == False:          # If rush mode is not active then print output each turn
                AddBreak(50)                # "Refresh screen"
                print(message_from_last_player)     # AI now populate this string when they play as otherwise it'll jump to next player's turn and wipe the screen
                message_from_last_player = ""       # Wipe string so it'll only display from last turn
                AddBreak(2)
                DrawBoard(game_board)               # Show game board current status
                AddBreak(2)
                if player_one_ctrl_type == "AI" and player_two_ctrl_type == "AI":       # Rush mode will be false if a human plays v AI. Their plays will allow them to see each play so there is no need to add an interrupt a second time.
                    AskWhenRdy()
            TakeTurn(1)
            CheckForWin(game_board, 1)                   # See if this player won

            Is_Player_One_Turn = False      # Change to other players turn
        else:                   # This is exactly the same as above except for player two who could be either human or AI
            if rush_mode == False:
                AddBreak(50)
                print(message_from_last_player)
                message_from_last_player = ""
                AddBreak(2)
                DrawBoard(game_board)
                AddBreak(2)
                if player_one_ctrl_type == "AI" and player_two_ctrl_type == "AI":
                    AskWhenRdy()
            TakeTurn(2)
            CheckForWin(game_board, 1)

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
    else:       # If there are no valid moves at all its a tie. I could make this count # of 3 in a rows and use that to determine winner. maybe later
        AddBreak(50)
        DrawBoard(game_board)
        print("GAME IS A TIE. NO WINNERS")
        break

AddBreak(1)
print(" --- GAME OVER ---")
