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

# Second question is about the number of mines. Similar to the above code we create a similar condition:
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
bomb="X"


#It initializes an empty board with 2 dimensions based on the received input from the user. This is an initial board with empty cells.
board=[]
for i in range(boardsize):
    innerlist=[]
    for j in range(boardsize):
        innerlist.append(0)
    board.append(innerlist)


# Adding randomly N mines into the board

for z in range(number_mines):
    i=random.randint(0,len(board)-1)
    j=random.randint(0,len(board)-1)
    board[i][j] = bomb


# Printing the board but also the coordinates. This Board is not visible for the user, so I just commented this one out completely.
# Creating two spaces in the first line
# print("  ",end="")
# Creating the numbers in the first line
# for i in range(0,len(board)):
#     print(i+1,"",end="")
# print("")
# Creating the letters in the first column.
# for i in range(0,len(board)):
#     letter = chr(ord('A') + i)
#Printing the letter variables followed by the contents of the i-ths row of the board
#     print(letter,*board[i])


#Here we create the Board that will be visible for the user. Board stores 0 as field without a bomb and 1 as chosen cell of the user.
user_board=[]
for i in range(boardsize):
    innerlist=[]
    for j in range(boardsize):
        innerlist.append(0)
    user_board.append(innerlist)

#Doing the mapping on codes (letters and numbers)
#conversion mapping
#extract the first letter from the user input and convert it to a number

# We are revealing the user's inputs. This does not have the condition how long the user can guess, and also does not notify if it hits the bomb.
repeat=True
while repeat:
    guess=input("What field to reveal?: ")
    i=guess[0]      #extracts first character of user's input that is a letter.
    i=ord(i)-65     #conversion mapping from letter to index.
    j=int(guess[1]) #extracts second character that is a integer.
    j=j-1           #due to 0-based indexing 
    user_board[i][j]=1
    print("  ",end="")  #printing the board in the next steps:
    for x in range(0,len(user_board)):
        print(x+1,"",end="")
    print("")
    for x in range(0,len(user_board)):
        letter = chr(ord('A') + x)
        print(letter, end=" ")
        for y in range(len(user_board)):   
            if user_board[x][y]==1:     #revealing the chosen cell in the user board.
                print(board[x][y], end=" ")
            else:
                print("#", end=" ")
        print()
