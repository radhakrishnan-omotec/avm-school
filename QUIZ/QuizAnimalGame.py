def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score = score + 10
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Sorry Wrong Answer, try again")
            attempt = attempt + 1
    if attempt == 3:
        print("The Correct answer is ",answer )
    
    
# MAIN PROGRAM
    
score = 0
print("**** Animal Quiz ****")
print("Guess the Animal Quiz")
print("*********************")
guess1 = input("Which bear lives at the North Pole? \n a)polar bear \n b)bear \n c)dolphin \n Type your option -->")
check_guess(guess1, "a")
guess2 = input("Which is the fastest land animal? \n a)Lion \n b)Cheetah \n c)Bear \n Type your option -->")
check_guess(guess2, "b")
guess3 = input("Which is the larget animal? \n a)Dolphin \n b)Giraffe \n c)Blue Whale \n Type your option -->")
check_guess(guess3, "c")
print("Your Score is "+ str(score))

#Counting score
i = score
if i < 20:
    print("OOPS, your score is ",i,"/ 30 better luck next time.")
elif i ==20:
    print("WOW! you scored ",i,"/ 30 you are Quiet SMART.")
else:
    print("CONGRATULATIONS! it's a perfect ",i,"/ 30 you are INTELLIGENT.")