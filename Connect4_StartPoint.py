
# GAME DESIGN
# Game of Connect 4 on a standard 7 wide x 6 tall board
# Primary purpose of this program is smart AI playstyle. Dont make AI perfect but make them smart
# Secondary - Try to find an efficient way to check for win conditions thats not an if statement for each possible position.

# Use a list to store the game board - Use unicode to find gamepiece art

# Goals:    Graphics output
#           Versus Computer opponent
#           Implement actually skilled AI

# Challenges:   Check for win condition
#               Skilled AI
#               "Graphics"

# Will certainly need random for AI to prevent always playing the same exact way.
import random

# Functions to control game flow
    # Check for win
        #Include subfunctions for checking vertical/horizontal/diagonal - Try not to just If/Then 100 times.....
    # ANything else?....

# Art Functions - Re-Use formatting tools from grade average assignment and art code concept from Hangman
    #//TODO Sketch UI first to avoid problems from hangman with 5+ re-designs

# AI Functions - Easily the biggest challenge and real point of this program
    # Starting idea. pick best ~5 moves and then weight them and randomly select.
    # Maybe allow user to select difficulty which will impact weight of chances for each move.

# GAME START

# Introduce player to the game
# Explain rules
# Give Options
    # Difficulty - Maybe?
    #//TODO consider possible options given how AI and check win coding goes. 
    # Maybe add special win conditions (connect 5 or 3?)
    # AI trash talker function?

# Main Gameplay loop
    # While loop with display UI, get input and check for win
    # For input use column number