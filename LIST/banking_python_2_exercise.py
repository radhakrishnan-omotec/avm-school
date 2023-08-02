#Global variables used for program state

# account holder dictionary to store all the user details
account_holder_detail = {}
'''
account_holder_detail {
                         user_name : "Aesha"
                         pass      : "pass123"
                         bal       : 100000
                         
                         ,
                         
                         user_name : "Ram"
                         pass      : "ram123"
                         bal       : 500000
                         
                     
                         }
'''

# variables used to check the state of things
login = False
running = True



 # Function to create account
def create_acc():
    user_name = input("Enter the user name: ")
    password = input("Enter the password: ")
    int_dep = int(input("Enter a deposit amount: "))
    
    #Check if the user name provided is already in use
    if user_name in account_holder_detail:
        print("user name already taken")
    else:
        account_holder_detail[user_name] = {"pass":password,"bal":int_dep}
        print("account created")
        

# Login function
def login():
    global login
    user_name = input("Enter the user name : ")
    password = input("Enter the password : ")
    
    if user_name in account_holder_detail:
        if account_holder_detail[user_name]["pass"] == password:
            print("Successful Logging in")
            login = True
            login_menu(user_name)
        else:
            print("wrong password")
    else:
        print("account not found")



# Logout Function
def logout():
    global login
    login = False
    print("logging out")



# Login Menu
def login_menu(user):
    global login
    while login:
        print("For deposit press 1: ")
        print("For withdrawal press 2: ")
        print("Check Minimum Eligibilty 4:")
        print("For logout press 3: ")
        
        x = int(input("Enter your choice: "))
        if x == 1:
            dep = int(input("Enter deposit amount: "))
            account_holder_detail[user]["bal"] = account_holder_detail[user]["bal"]+dep
            print("current balance is:",account_holder_detail[user]["bal"])
        elif x == 2:
            wit = int(input("Enter withdraw amount: "))
            if wit > account_holder_detail[user]["bal"]:
                print("not sufficient balance.")
            else:
                account_holder_detail[user]["bal"] = account_holder_detail[user]["bal"]-wit
                print("current balance is:",account_holder_detail[user]["bal"])
            
        #HOMEWORK EXCERCISE
        #elif x ==4:
        # if check balance - wit < 10000
        # " Minimum balance is not maintained"
        elif x == 3:
            logout()     

        

# Function for the main menu of the banking app
def main_menu():
    print("Welcome to the banking app.")
    print("For login press 1: ")
    print("For creating new account press 2: ")
    print("For exiting the app press 3: ")
    
    x = int(input("Enter your choice: "))
    
    if x == 1:
        login()
    elif x == 2:
        create_acc()
    
    elif x == 3:
        exit()
        
        
# Function exit the banking app      
def exit():
    global running
    print("closing the app")
    running = False
 
 
 
#MAIN PROGRAM   
while running:
    main_menu()   
    



# EXCERCISE       
# def withdraw_amt(user):

   # check the balance of the user (if conditon)
   # if the balance amount is > 10000 then print("User eligible for withdrawal amount )
   # else say print ("Error - Insufficient Balance" )