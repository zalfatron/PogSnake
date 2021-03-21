## PogSnake
#import Curses

# 258 == down_arrow
# 259 == up_arrow
# 260 == left_arrow
# 261 == right_arrow

## Basic CLI interface

print("Type 's' for the snake game.")
print("Type 'h' for a list of highscores.")
print("Type 'q' to exit this program.")

run = True
while (run == True):
    pass
    user = input("Please enter your option here H for help: ")
    if (user == "s"):
        ## Enter snake game
        pass
    elif(user == "h"):
        ## Print list of top 10 highscores
        pass
    elif(user == "q"):
        ## Exit the program
        run = False
    elif(user == "H" or user == "Help"):
        ## Print a help screen
        print("Type 's' for the snake game.")
        print("Type 'h' for a list of highscores.")
        print("Type 'q' to exit this program.")
        pass
    else:
        print("ERROR: Incorrect Input.")
        pass
