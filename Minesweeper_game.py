import random

def coord_to_index(coord):
    i=coord[0]      #extracts first character of user's input that is a letter.
    i=ord(i)-65     #conversion mapping from letter to index.
    try:    
        j=int(coord[1:3]) #extracts second character that is an integer.
        j=j-1
    except:
        j=-999 #conversion to integer failed, force j to an invalid integer
    return i,j

def index_to_coord(i,j):      
    return chr(i+65) + str(j+1)

# As first steps the application asks for two numbers from the user.
# First question is about the board size:
repeat = True
while repeat :
    try:
        string_boardsize=input("Define the size of the board between 2 and 26: ")
        boardsize=int(string_boardsize) #it try to convert input into integer
        if boardsize>=2 and boardsize<=26:
            repeat = False
        # if conversion fails, code will jump to the except block.
        # otherwise repeat=False will break from the loop.
    except:
        pass

# Second question is about the number of mines. Similar to the above code we create a similar condition:
repeat = True
while repeat :
    try:
        string_number_mines=input(f"Define the number of mines between 1 and {boardsize**2}: ")
        number_mines=int(string_number_mines) #try to convert input into integer
        if number_mines>0 and number_mines<boardsize**2:
            repeat= False
        # if conversion fails, code will jump to the except block.
        # otherwise repeat=False will break from the loop.
    except:
        pass

#It initializes an empty board with 2 dimensions based on the received input from the user. This is an initial board with empty cells.
board=[]
for i in range(boardsize):
    rows=[]
    for j in range(boardsize):
        rows.append(0)
    board.append(rows)

# Adding randomly N mines into the board
bomb="X"
for z in range(number_mines):
    i=random.randint(0,len(board)-1)
    j=random.randint(0,len(board)-1)
    board[i][j] = bomb

# Counting the number of neighboring cells containing bombs and updates each cell with this information.
# u and v iterates through each cell on the board
for u in range(boardsize): 
    for v in range(boardsize):
        t=0         #total number of neighbouring mines
        if board[u][v]==bomb:
            continue
        # (u+i,v+j) loops represent the relative coordinates of neighboring cells within a 3x3 square
        for i in range(-1,2):
            for j in range(-1,2): 
                if (u+i) < 0 or (v+j) < 0 or (u+i) >= boardsize or (v+j) >= boardsize: #if examined cell is outside the range of the board, skip
                    continue 
                if (i==0 and j==0): # skip the center cell
                    continue
                if board[u+i][v+j]==bomb:
                    t+=1
        board[u][v]=t

# # Printing the board but also the coordinates. This Board is not visible for the user, so I just commented this one out completely.
# # Creating two spaces in the first line
# print("  ",end="")
# # Creating the numbers in the first line
# for i in range(0,len(board)):
#     print(i+1,"",end="")
# print("")
# # Creating the letters in the first column.
# for i in range(0,len(board)):
#     letter = chr(ord('A') + i)
# # Printing the letter variables followed by the contents of the i-ths row of the board
#     print(letter,*board[i])


#Here we create the Board that will be visible for the user. 
user_board=[]
for i in range(boardsize):
    rows=[]
    for j in range(boardsize):
        rows.append('#')
    user_board.append(rows)

#User interaction with the minesweeper game:
l=0
while l<boardsize**2-number_mines:
    l+=1
    guess=input("What field to reveal?: ")
    i,j=coord_to_index(guess)
    if i<0 or i>boardsize or j<0 or j>boardsize:
        print("Invalid guess, Give a new one!:")
        continue

    if board[i][j]==bomb:
        print('You lost!')
        break

    user_board[i][j]=board[i][j]

    #Revealing of "0" cells and their neighboring cells
    zeroes_list=[] # to store "zeroes" to be examined
    if board[i][j] == 0:
        zeroes_list.append(guess)

    while len(zeroes_list) > 0:
        zero_cell = zeroes_list.pop(0) #the current 0 that is going to be analyzed
        u,v =coord_to_index(zero_cell)
        for m in range(-1,2):
            for n in range(-1,2):
                if (u+m) < 0 or (v+n) < 0 or (u+m) >= boardsize or (v+n) >= boardsize:
                    continue    #skip cell out of the board range
                if (m==0 and n==0): # skip the central cell
                    continue
                if user_board[u+m][v+n] != "#": # already revealed, skip this cell
                    continue
                user_board[u+m][v+n]=board[u+m][v+n] # reveal the cell
                if board[u+m][v+n] == 0: #save zero to be cheked later
                    c = index_to_coord(u+m,v+n)
                    zeroes_list.append(c)
    #End of revealing zeroes

    print("  ",end="")  #printing the board in the next steps:
    print(*range(1,boardsize+1))
    for x in range(len(user_board)):
        letter = chr(ord('A') + x)
        print(letter, end=" ")
        print(*user_board[x])

if l==boardsize**2-number_mines:
    print('You won!')

#printing the board as final step
print("  ",end="") 
print(*range(1,boardsize+1))
for x in range(len(board)):
    letter = chr(ord('A') + x)
    print(letter, end=" ")
    print(*board[x])

