# As first steps the application asks for two numbers from the user.
# First question is about the board size:
import random 
repeat = True
while repeat :
    try:
        string_boardsize=input("Define the size of the board: ")
        boardsize=int(string_boardsize) #it try to convert input into integer
        if boardsize>0:
            repeat = False
        else:
            print("Define a positive integer: ")
        # if conversion fails, code will jump to the except block.
        # otherwise repeat=False will break from the loop.
        
    except:
        print("Please define an integer!")

# Second question is about the mine size. Similar to the above code we create a similar condition:
repeat = True
while repeat :
    try:
        string_number_mines=input("Define the number of mines: ")
        number_mines=int(string_number_mines) #try to convert input into integer
        if number_mines>0:
            repeat= False
        else:
            print("Define a positive integer: ")
        # if conversion fails, code will jump to the except block.
        # otherwise repeat=False will break from the loop.
    except:
        print("Define the number of mines: ")


#Setting up the variables that will be used for setting up the board:
no_bomb=0
bomb=1
field='#'

#
board=[]
for i in range(boardsize):
    innerlist=[]
    for j in range(boardsize):
        innerlist.append(0)
    board.append(innerlist)

# using the code of matrix.py, print the board


# fill board with random mines using the most powerful tool of informatic: copy-paste
#Adding randomly N mines into the board

for z in range(number_mines):
    i=random.randint(0,len(board)-1)
    j=random.randint(0,len(board)-1)
    board[i][j] = 1


# make an advanced printing where you print the board but also the coordinates
# Creating two spaces in the first line
print("  ",end="")
# Creating the numbers in the first line
for i in range(0,len(board)):
    print(i+1,"",end="")
print("")
# Creating the letters and cells without bombs
for i in range(0,len(board)):
    letter = chr(ord('A') + i)
    print(letter,*board[i])


