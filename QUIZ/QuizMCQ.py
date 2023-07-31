# Creating a function to give options
def give_options(x,y,z):
    print("a):", x)
    print("b):", y)
    print("c):", z)

print("Hello! Welcome to my Quiz" "\n" "All Questions carries 10 marks each")
# To ask for input from the user
ans = input("Are you ready to play (yes/no): ")
a ="Note: Type Right option , not answers."

score = 0
total_questions = 4
correct_ans =["a", "c", "b", "c"]

if ans.lower() == "yes":
    print(a)

print("Question- What is the best Programming Language? ")
give_options("Python", "C", "Java" )
ans=input("===>>>")

if ans.lower() == correct_ans[0]:
    score=score+1
    print("Correct")
else:
    print("Incorrect")

print(a)
print("Question- Who is the Founder of Apple Inc? ")
give_options("Mark Zuckerberg", "Warren Buffet", "Steve jobs")
ans = input(">>>")

if ans.lower() == correct_ans[1]:
    score=score+1
    print("Correct")
else:
    print("Incorrect")

print(a)
print("Question- What is more better among these? ")
give_options("Data Science", "Artificial Intelligence", "Digital Marketing")
ans = input(">>>")

if ans.lower() == correct_ans[2]:
    score=score+1
    print("Correct")
else:
    print("Incorrect")

print(a)
print("Question- What is the best Investment? ")
give_options("Share Capital", "Mutual Funds", "Bitcoin")
ans = input(">>>")

if ans.lower() == correct_ans[3]:
    score=score+1
    print("Correct")
else:
    print("Incorrect")

#Counting score
i = score*10
if i < 30:
    print("OOPS, your score is ",i,"/ 40 better luck next time.")
elif i ==30:
    print("WOW! you scored ",i,"/ 40 you are Quiet SMART.")
else:
    print("CONGRATULATIONS! it's a perfect ",i,"/ 40 you are INTELLIGENT.")