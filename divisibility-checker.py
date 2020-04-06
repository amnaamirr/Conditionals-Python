
num = int(input("ENTER YOUR NUMBER: "))
print("\n")
if num%2 == 0 and num%3 ==0:
   print("This number is divisible by both 2 and 3")
elif num%2 == 0 and num%5 == 0:
   print("This number is divisible by both 2 and 5")
elif num%3 == 0 and num%5 == 0:
    print("This number is divisible by both 3 and 5")
elif num%2 == 0:
    print("This number is divisible by 2")    
elif num%3 == 0:
    print("This number is divisible by 3")
elif num%5 == 0:
    print("This number is divisible by 5")
else:
    print("The number is not divisible by 2,3 or 5")    

              
