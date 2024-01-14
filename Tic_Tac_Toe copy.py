import sys
t = [["_","_","_"],["_","_","_"],["_","_","_"]]

# print (t)

# extras:
# row_col=[]
# for i in range(len(t)):
#     cols=[]
#     for j in range(len(t[0])):
#         cols.append(j)
#     row_col.append([i,cols])
# diag = [[[0,0],[1,1],[2,2]],[[0,2],[1,1],[2,0]]]
# print (row_col)

inputs = []
def input_storer():
    global inputs
    tup = tuple([row-1,col-1])
    inputs.append(tup)
    # print (inputs)

def XO():
    global t
    for i in range (3):
        for j in range (3):
            print (t[i][j],end=" ")
        print ()
    print ()

XO()
print ('''O for player 1\t\tX for player 2\n''')


while True:

    print ("Player 1's Turn\n\tType in the co-ordinates to place O")
    row = int(input("Enter the row: "))
    col = int(input("Enter the column: "))
    tup_new=(row-1,col-1)
    if tup_new in inputs:
        print ("Error")
        row = int(input("Enter the row: "))
        col = int(input("Enter the column: "))
        input_storer()
        t[row-1][col-1] = "O"
        XO() 
    else:
        t[row-1][col-1] = "O"
        input_storer()
        XO()

    if (t[0][0] == 'X' and t[0][1] == 'X' and t[0][2] == 'X'):
        print (1)
        print ("PLAYER 2 Wins".center(50))
        break
    if (t[1][0] == 'X'and t[1][1] == 'X' and t[1][2] == 'X'):
        print (2)
        print ("PLAYER 2 Wins".center(50))
        break
    if (t[2][0] == 'X' and t[2][1] == 'X' and t[2][2] == 'X') :
        print (3)
        print ("PLAYER 2 Wins".center(50))
        break
    if (t[0][0] == 'X' and t[1][0] == 'X' and t[2][0] == 'X') :
        print (4)
        print ("PLAYER 2 Wins".center(50))
        break
    if (t[0][1] == 'X' and t[1][1] == 'X' and t[2][1] == 'X') :
        print (5)
        print ("PLAYER 2 Wins".center(50))
        break
    if (t[0][2] == 'X' and t[1][2] == 'X' and t[2][2] == 'X') :
        print (6)
        print ("PLAYER 2 Wins".center(50))
        break
    if (t[0][0] == 'X' and t[1][1] == 'X' and t[2][2] == 'X') :
        print (7)
        print ("PLAYER 2 Wins".center(50))
        break
    if (t[0][2] == 'X' and t[1][1] == 'X' and t[2][0] == 'X'):
        print (8)
        print ("PLAYER 2 Wins".center(50))
        break
    if (t[0][0] == 'O' and t[0][1] == 'O' and t[0][2] == 'O'):
        print (10)
        print ("PLAYER 1 Wins".center(50))
        break
    if (t[1][0] == 'O'and t[1][1] == 'O' and t[1][2] == 'O'):
        print (20)
        print ("PLAYER 1 Wins".center(50))
        break
    if (t[2][0] == 'O' and t[2][1] == 'O' and t[2][2] == 'O') :
        print (30)
        print ("PLAYER 1 Wins".center(50))
        break
    if (t[0][0] == 'O' and t[1][0] == 'O' and t[2][0] == 'O') :
        print (40)
        print ("PLAYER 1 Wins".center(50))
        break
    if (t[0][1] == 'O' and t[1][1] == 'O' and t[2][1] == 'O') :
        print (50)
        print ("PLAYER 1 Wins".center(50))
        break
    if (t[0][2] == 'O' and t[1][2] == 'O' and t[2][2] == 'O') :
        print (60)
        print ("PLAYER 1 Wins".center(50))
        break
    if (t[0][0] == 'O' and t[1][1] == 'O' and t[2][2] == 'O') :
        print (70)
        print ("PLAYER 1 Wins".center(50))
        break
    if (t[0][2] == 'O' and t[1][1] == 'O' and t[2][0] == 'O'):
        print (80)
        print ("PLAYER 1 Wins".center(50))
        break

    print ("Player 2's Turn\n\tType in the co-ordinates to place X")
    row = int(input("Enter the row: "))
    col = int(input("Enter the column: "))
    tup_new=(row-1,col-1)
    if tup_new in inputs:
        print ("Error")
        row = int(input("Enter the row: "))
        col = int(input("Enter the column: "))
        input_storer()
        t[row-1][col-1] = "X"
        XO()
    else:
        t[row-1][col-1] = "X"
        input_storer()
        XO()

    if (t[0][0] == 'X' and t[0][1] == 'X' and t[0][2] == 'X'):
        print (1)
        print ("PLAYER 2 Wins".center(50))
        break
    if (t[1][0] == 'X'and t[1][1] == 'X' and t[1][2] == 'X'):
        print (2)
        print ("PLAYER 2 Wins".center(50))
        break
    if (t[2][0] == 'X' and t[2][1] == 'X' and t[2][2] == 'X') :
        print (3)
        print ("PLAYER 2 Wins".center(50))
        break
    if (t[0][0] == 'X' and t[1][0] == 'X' and t[2][0] == 'X') :
        print (4)
        print ("PLAYER 2 Wins".center(50))
        break
    if (t[0][1] == 'X' and t[1][1] == 'X' and t[2][1] == 'X') :
        print (5)
        print ("PLAYER 2 Wins".center(50))
        break
    if (t[0][2] == 'X' and t[1][2] == 'X' and t[2][2] == 'X') :
        print (6)
        print ("PLAYER 2 Wins".center(50))
        break
    if (t[0][0] == 'X' and t[1][1] == 'X' and t[2][2] == 'X') :
        print (7)
        print ("PLAYER 2 Wins".center(50))
        break
    if (t[0][2] == 'X' and t[1][1] == 'X' and t[2][0] == 'X'):
        print (8)
        print ("PLAYER 2 Wins".center(50))
        break
    if (t[0][0] == 'O' and t[0][1] == 'O' and t[0][2] == 'O'):
        print (10)
        print ("PLAYER 1 Wins".center(50))
        break
    if (t[1][0] == 'O'and t[1][1] == 'O' and t[1][2] == 'O'):
        print (20)
        print ("PLAYER 1 Wins".center(50))
        break
    if (t[2][0] == 'O' and t[2][1] == 'O' and t[2][2] == 'O') :
        print (30)
        print ("PLAYER 1 Wins".center(50))
        break
    if (t[0][0] == 'O' and t[1][0] == 'O' and t[2][0] == 'O') :
        print (40)
        print ("PLAYER 1 Wins".center(50))
        break
    if (t[0][1] == 'O' and t[1][1] == 'O' and t[2][1] == 'O') :
        print (50)
        print ("PLAYER 1 Wins".center(50))
        break
    if (t[0][2] == 'O' and t[1][2] == 'O' and t[2][2] == 'O') :
        print (60)
        print ("PLAYER 1 Wins".center(50))
        break
    if (t[0][0] == 'O' and t[1][1] == 'O' and t[2][2] == 'O') :
        print (70)
        print ("PLAYER 1 Wins".center(50))
        break
    if (t[0][2] == 'O' and t[1][1] == 'O' and t[2][0] == 'O'):
        print (80)
        print ("PLAYER 1 Wins".center(50))
        break
    
                
# print (t)


#small errors
'''
SHould not overwrite the values of X with O and O with X when given at same coordinate - DONE
Should print win or lose as soon as there is a strike, not wait for inputs of two users - DONE
End condition for tie situation'''