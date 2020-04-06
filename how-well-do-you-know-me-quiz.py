playername = input("Enter your name: ")
print("INSTRUCTIONS: ENTER YOUR ANSWER IN BLOCK LETTERS ONLY")
print("\n")

print("What would Amna do if she won a lottery?")
print(" TRAVEL THE WORLD\n BUY HER DREAM HOUSE\n DO SHOPPING")
ans1 = input("> ")
if (ans1 == "TRAVEL THE WORLD"):
    print("THAT'S CORRECT!")
    score = 1
else:
    print("WRONG CHOICE!")
    score = 0
print("\n")
print("Amna's favourite hobby is: ")
print(" BINGE WATCHING\n ORGANIZING HER THINGS\n READING")
ans2 = input("> ")
if (ans2 == "READING"):
    print("THAT'S CORRECT!")
    score += 1
else:
    print("WRONG CHOICE!")
print("\n")
print("In her free time,where would Amna go?")
print(" GYM\n SHOPPING\n SLEEPING")
ans3 = input("> ")
if (ans3 == "SHOPPING"):
    print("THAT'S CORRECT!")
    score += 1
else:
    print("WRONG CHOICE!")
print("\n")
print("Which type of movies does Amna like?")
print(" COMEDY\n HORROR\n THRILLER")
ans4 = input("> ")
if (ans4 == "THRILLER"):
    print("THAT'S CORRECT!")
    score += 1
else:
    print("WRONG CHOICE!")
print("\n")
print("Amna's favourite dessert is: ")
print(" ICECREAM\n CAKES\n WAFFLES")
ans5 = input("> ")
if (ans5 == "CAKES"):
    print("THAT'S CORRECT!")
    score += 1
else:
    print("WRONG CHOICE!")
print("\n")
print("YOUR SCORE IS:",score)
if (score > 3):
    print("YOU KNOW AMNA VERY WELL")
print("\n")
print("THANKYOU FOR PLAYING!")      



  

    

