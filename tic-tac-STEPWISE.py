# tic-tac-STEPS
# STEP 1 
tic = [" ", " ", " "," ", " ", " "," ", " ", " "]
def print_board():
    print(" "+tic[0]+" "+"|"+" "+tic[1]+" "+"|"+" "+tic[2]+" ")
    print("=================")
    print(" "+tic[3]+" "+"|"+" "+tic[4]+" "+"|"+" "+tic[5]+" ")
    print("=================")
    print(" "+tic[6]+" "+"|"+" "+tic[7]+" "+"|"+" "+tic[8]+" ")
    
    
print_board() 

======================================================================

# tic-tac-STEPS
# STEP 2  
tic = [" ", " ", " "," ", " ", " "," ", " ", " "]
def print_board():
    print(" "+tic[0]+" "+"|"+" "+tic[1]+" "+"|"+" "+tic[2]+" ")
    print("=================")
    print(" "+tic[3]+" "+"|"+" "+tic[4]+" "+"|"+" "+tic[5]+" ")
    print("=================")
    print(" "+tic[6]+" "+"|"+" "+tic[7]+" "+"|"+" "+tic[8]+" ")

print_board()
 
for x in range(0,9):
    in1 = int(input("enter a position :"))
    if x%2 == 0:
        tic[in1-1] = 'X'
    else :
        tic[in1-1] = 'O'
    print_board()

======================================================================


# tic-tac-STEPS
# STEP 3  
tic = [" ", " ", " "," ", " ", " "," ", " ", " "]
def print_board():
    print(" TIC - TAC - TOE ")
    print(" "+tic[0]+" "+"|"+" "+tic[1]+" "+"|"+" "+tic[2]+" ")
    print("=================")
    print(" "+tic[3]+" "+"|"+" "+tic[4]+" "+"|"+" "+tic[5]+" ")
    print("=================")
    print(" "+tic[6]+" "+"|"+" "+tic[7]+" "+"|"+" "+tic[8]+" ")

print_board()

def check_win():
    # Winning Combination 1 for X
    if tic[0] == 'X' and tic[1] == 'X' and tic[2] == 'X':
        return "User X won"
    # Winning Combination 2 for X
    if tic[0] == 'X' and tic[3] == 'X' and tic[6] == 'X':
        return "User X won"
    # Winning Combination 3 to 8 for X
    
    
for x in range(0,9):
    in1 = int(input("enter your position :"))
    if x%2 == 0:
        tic[in1-1] = 'X'
    else :
        tic[in1-1] = 'O'

    print_board()
    
    check = check_win()
    if check == 'User X won':
        print("User X won the game")
        break

======================================================================


# tic-tac-STEPS
# STEP 4  
# COMPLETE X WINS

tic = [" ", " ", " "," ", " ", " "," ", " ", " "]
def print_board():
    print(" TIC - TAC - TOE ")
    print(" "+tic[0]+" "+"|"+" "+tic[1]+" "+"|"+" "+tic[2]+" ")
    print("=================")
    print(" "+tic[3]+" "+"|"+" "+tic[4]+" "+"|"+" "+tic[5]+" ")
    print("=================")
    print(" "+tic[6]+" "+"|"+" "+tic[7]+" "+"|"+" "+tic[8]+" ")

print_board()

def check_win():
    # Winning Combination 1 for X ** STRAIGHT 
    if tic[0] == 'X' and tic[1] == 'X' and tic[2] == 'X':
        return "User X won"

    # Winning Combination 2 for X ** DIAGONAL 
    if tic[0] == 'X' and tic[3] == 'X' and tic[6] == 'X':
        return "User X won"
    
    # Winning Combination 2 for X ** CROSS DIAGONAL 
    if tic[2] == 'X' and tic[4] == 'X' and tic[6] == 'X':
        return "User X won"
    
    # Winning Combination 3 to 8 for X ** STRAIGHT
    if tic[3] == 'X' and tic[4] == 'X' and tic[5] == 'X':
        return "User X won"
    # Winning Combination 4 to 8 for X ** STRAIGHT
    if tic[6] == 'X' and tic[7] == 'X' and tic[8] == 'X':
        return "User X won"    
    # Winning Combination 5 to 8 for X ** UP-DOWN
    if tic[0] == 'X' and tic[3] == 'X' and tic[6] == 'X':
        return "User X won"    
    # Winning Combination 3 to 8 for X ** UP-DOWN
    if tic[1] == 'X' and tic[4] == 'X' and tic[7] == 'X':
        return "User X won"    
    # Winning Combination 3 to 8 for X ** UP-DOWN
    if tic[2] == 'X' and tic[5] == 'X' and tic[8] == 'X':
        return "User X won"    
    
    
    
for x in range(0,9):
    in1 = int(input("enter your position :"))
    if x%2 == 0:
        tic[in1-1] = 'X'
    else :
        tic[in1-1] = 'O'

    print_board()
    
    check = check_win()
    if check == 'User X won':
        print("User X won the game")
        break

======================================================================



# tic-tac-STEPS
# STEP 5  
# COMPLETE X & O WINS

tic = [" ", " ", " "," ", " ", " "," ", " ", " "]
def print_board():
    print(" TIC - TAC - TOE ")
    print(" "+tic[0]+" "+"|"+" "+tic[1]+" "+"|"+" "+tic[2]+" ")
    print("=================")
    print(" "+tic[3]+" "+"|"+" "+tic[4]+" "+"|"+" "+tic[5]+" ")
    print("=================")
    print(" "+tic[6]+" "+"|"+" "+tic[7]+" "+"|"+" "+tic[8]+" ")

print_board()

def check_win():
    # Winning Combination 1 for X ** STRAIGHT 
    if tic[0] == 'X' and tic[1] == 'X' and tic[2] == 'X':
        return "User X won"

    # Winning Combination 2 for X ** DIAGONAL 
    if tic[0] == 'X' and tic[3] == 'X' and tic[6] == 'X':
        return "User X won"
    
    # Winning Combination 2 for X ** CROSS DIAGONAL 
    if tic[2] == 'X' and tic[4] == 'X' and tic[6] == 'X':
        return "User X won"
    
    # Winning Combination 3 to 8 for X ** STRAIGHT
    if tic[3] == 'X' and tic[4] == 'X' and tic[5] == 'X':
        return "User X won"
    # Winning Combination 4 to 8 for X ** STRAIGHT
    if tic[6] == 'X' and tic[7] == 'X' and tic[8] == 'X':
        return "User X won"    
    # Winning Combination 5 to 8 for X ** UP-DOWN
    if tic[0] == 'X' and tic[3] == 'X' and tic[6] == 'X':
        return "User X won"    
    # Winning Combination 3 to 8 for X ** UP-DOWN
    if tic[1] == 'X' and tic[4] == 'X' and tic[7] == 'X':
        return "User X won"    
    # Winning Combination 3 to 8 for X ** UP-DOWN
    if tic[2] == 'X' and tic[5] == 'X' and tic[8] == 'X':
        return "User X won"    
#--------------------------------------------------------

    # Winning Combination 1 for O ** STRAIGHT 
    if tic[0] == 'O' and tic[1] == 'O' and tic[2] == 'O':
        return "User O won"

    # Winning Combination 2 for O ** DIAGONAL 
    if tic[0] == 'O' and tic[3] == 'O' and tic[6] == 'O':
        return "User O won"
    
    # Winning Combination 2 for O ** CROSS DIAGONAL 
    if tic[2] == 'O' and tic[4] == 'O' and tic[6] == 'O':
        return "User O won"
    
    # Winning Combination 3 to 8 for O ** STRAIGHT
    if tic[3] == 'O' and tic[4] == 'O' and tic[5] == 'O':
        return "User O won"
    # Winning Combination 4 to 8 for O ** STRAIGHT
    if tic[6] == 'O' and tic[7] == 'O' and tic[8] == 'O':
        return "User O won"    
    # Winning Combination 5 to 8 for O ** UP-DOWN
    if tic[0] == 'O' and tic[3] == 'O' and tic[6] == 'O':
        return "User O won"    
    # Winning Combination 3 to 8 for O ** UP-DOWN
    if tic[1] == 'O' and tic[4] == 'O' and tic[7] == 'O':
        return "User O won"    
    # Winning Combination 3 to 8 for O ** UP-DOWN
    if tic[2] == 'O' and tic[5] == 'O' and tic[8] == 'O':
        return "User O won"    
        
    
    
for x in range(0,9):
    in1 = int(input("enter your position :"))
    if x%2 == 0:
        tic[in1-1] = 'X'
    else :
        tic[in1-1] = 'O'

    print_board()
    
    check = check_win()
    if check == 'User X won':
        print("User X won the game")
        break
    if check == 'User O won':
        print("User O won the game")
        break

======================================================================