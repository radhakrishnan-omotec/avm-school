################################################
""" 
B = [" ", " ", " "," ", " ", " "," ", " ", " "]
def print_board():
    print(" "+B[0]+" "+"|"+" "+B[1]+" "+"|"+" "+B[2]+" ")
    print("=================")
    print(" "+B[3]+" "+"|"+" "+B[4]+" "+"|"+" "+B[5]+" ")
    print("=================")
    print(" "+B[6]+" "+"|"+" "+B[7]+" "+"|"+" "+B[8]+" ")
    
    
print_board() """


################################################
""" 
B = [" ", " ", " "," ", " ", " "," ", " ", " "]
def print_board():
    print(" "+B[0]+" "+"|"+" "+B[1]+" "+"|"+" "+B[2]+" ")
    print("=================")
    print(" "+B[3]+" "+"|"+" "+B[4]+" "+"|"+" "+B[5]+" ")
    print("=================")
    print(" "+B[6]+" "+"|"+" "+B[7]+" "+"|"+" "+B[8]+" ")

print_board()
 
for x in range(0,9):
    in1 = int(input("enter a position :"))
    if x%2 == 0:
        B[in1-1] = 'X'
    else :
        B[in1-1] = 'O'
    print_board()  """

################################################

B = [" ", " ", " "," ", " ", " "," ", " ", " "]
def print_board():
    print(" TIC - TAC - TOE ")
    print(" "+B[0]+" "+"|"+" "+B[1]+" "+"|"+" "+B[2]+" ")
    print("=================")
    print(" "+B[3]+" "+"|"+" "+B[4]+" "+"|"+" "+B[5]+" ")
    print("=================")
    print(" "+B[6]+" "+"|"+" "+B[7]+" "+"|"+" "+B[8]+" ")

print_board()

def check_win():
    # Winning Combination 1 for X
    if B[0] == 'X' and B[1] == 'X' and B[2] == 'X':
        return "User X won"
    # Winning Combination 2 for X
    if B[0] == 'X' and B[3] == 'X' and B[6] == 'X':
        return "User X won"
    # Winning Combination 3 to 8 for X
    
    
for x in range(0,9):
    in1 = int(input("enter your position :"))
    if x%2 == 0:
        B[in1-1] = 'X'
    else :
        B[in1-1] = 'O'

    print_board()
    
    check = check_win()
    if check == 'User X won':
        print("User X won the game")
        break


################################################
# COMPLETE X WINS

B = [" ", " ", " "," ", " ", " "," ", " ", " "]
def print_board():
    print(" TIC - TAC - TOE ")
    print(" "+B[0]+" "+"|"+" "+B[1]+" "+"|"+" "+B[2]+" ")
    print("=================")
    print(" "+B[3]+" "+"|"+" "+B[4]+" "+"|"+" "+B[5]+" ")
    print("=================")
    print(" "+B[6]+" "+"|"+" "+B[7]+" "+"|"+" "+B[8]+" ")

print_board()

def check_win():
    # Winning Combination 1 for X ** STRAIGHT 
    if B[0] == 'X' and B[1] == 'X' and B[2] == 'X':
        return "User X won"

    # Winning Combination 2 for X ** DIAGONAL 
    if B[0] == 'X' and B[3] == 'X' and B[6] == 'X':
        return "User X won"
    
    # Winning Combination 2 for X ** CROSS DIAGONAL 
    if B[2] == 'X' and B[4] == 'X' and B[6] == 'X':
        return "User X won"
    
    # Winning Combination 3 to 8 for X ** STRAIGHT
    if B[3] == 'X' and B[4] == 'X' and B[5] == 'X':
        return "User X won"
    # Winning Combination 4 to 8 for X ** STRAIGHT
    if B[6] == 'X' and B[7] == 'X' and B[8] == 'X':
        return "User X won"    
    # Winning Combination 5 to 8 for X ** UP-DOWN
    if B[0] == 'X' and B[3] == 'X' and B[6] == 'X':
        return "User X won"    
    # Winning Combination 3 to 8 for X ** UP-DOWN
    if B[1] == 'X' and B[4] == 'X' and B[7] == 'X':
        return "User X won"    
    # Winning Combination 3 to 8 for X ** UP-DOWN
    if B[2] == 'X' and B[5] == 'X' and B[8] == 'X':
        return "User X won"    
    
    
    
for x in range(0,9):
    in1 = int(input("enter your position :"))
    if x%2 == 0:
        B[in1-1] = 'X'
    else :
        B[in1-1] = 'O'

    print_board()
    
    check = check_win()
    if check == 'User X won':
        print("User X won the game")
        break


################################################

# COMPLETE X & O WINS

B = [" ", " ", " "," ", " ", " "," ", " ", " "]
def print_board():
    print(" TIC - TAC - TOE ")
    print(" "+B[0]+" "+"|"+" "+B[1]+" "+"|"+" "+B[2]+" ")
    print("=================")
    print(" "+B[3]+" "+"|"+" "+B[4]+" "+"|"+" "+B[5]+" ")
    print("=================")
    print(" "+B[6]+" "+"|"+" "+B[7]+" "+"|"+" "+B[8]+" ")

print_board()

def check_win():
    # Winning Combination 1 for X ** STRAIGHT 
    if B[0] == 'X' and B[1] == 'X' and B[2] == 'X':
        return "User X won"

    # Winning Combination 2 for X ** DIAGONAL 
    if B[0] == 'X' and B[3] == 'X' and B[6] == 'X':
        return "User X won"
    
    # Winning Combination 2 for X ** CROSS DIAGONAL 
    if B[2] == 'X' and B[4] == 'X' and B[6] == 'X':
        return "User X won"
    
    # Winning Combination 3 to 8 for X ** STRAIGHT
    if B[3] == 'X' and B[4] == 'X' and B[5] == 'X':
        return "User X won"
    # Winning Combination 4 to 8 for X ** STRAIGHT
    if B[6] == 'X' and B[7] == 'X' and B[8] == 'X':
        return "User X won"    
    # Winning Combination 5 to 8 for X ** UP-DOWN
    if B[0] == 'X' and B[3] == 'X' and B[6] == 'X':
        return "User X won"    
    # Winning Combination 3 to 8 for X ** UP-DOWN
    if B[1] == 'X' and B[4] == 'X' and B[7] == 'X':
        return "User X won"    
    # Winning Combination 3 to 8 for X ** UP-DOWN
    if B[2] == 'X' and B[5] == 'X' and B[8] == 'X':
        return "User X won"    
####################################################

    # Winning Combination 1 for O ** STRAIGHT 
    if B[0] == 'O' and B[1] == 'O' and B[2] == 'O':
        return "User O won"

    # Winning Combination 2 for O ** DIAGONAL 
    if B[0] == 'O' and B[3] == 'O' and B[6] == 'O':
        return "User O won"
    
    # Winning Combination 2 for O ** CROSS DIAGONAL 
    if B[2] == 'O' and B[4] == 'O' and B[6] == 'O':
        return "User O won"
    
    # Winning Combination 3 to 8 for O ** STRAIGHT
    if B[3] == 'O' and B[4] == 'O' and B[5] == 'O':
        return "User O won"
    # Winning Combination 4 to 8 for O ** STRAIGHT
    if B[6] == 'O' and B[7] == 'O' and B[8] == 'O':
        return "User O won"    
    # Winning Combination 5 to 8 for O ** UP-DOWN
    if B[0] == 'O' and B[3] == 'O' and B[6] == 'O':
        return "User O won"    
    # Winning Combination 3 to 8 for O ** UP-DOWN
    if B[1] == 'O' and B[4] == 'O' and B[7] == 'O':
        return "User O won"    
    # Winning Combination 3 to 8 for O ** UP-DOWN
    if B[2] == 'O' and B[5] == 'O' and B[8] == 'O':
        return "User O won"    
        
    
    
for x in range(0,9):
    in1 = int(input("enter your position :"))
    if x%2 == 0:
        B[in1-1] = 'X'
    else :
        B[in1-1] = 'O'

    print_board()
    
    check = check_win()
    if check == 'User X won':
        print("User X won the game")
        break
    if check == 'User O won':
        print("User O won the game")
        break

################################################