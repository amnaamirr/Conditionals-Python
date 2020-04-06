print("Are you a magician?")
is_magician = input("Enter 'YES' OR 'NO'\n>  ")
print("\n")
print("Are you an expert magician?")
is_expert = input("Enter 'YES' OR 'NO'\n>  ")
print("\n")

if is_magician == "YES" and is_expert == "YES":
    print("You are a master magician!")
elif is_magician =="YES"and is_expert == "NO":
    print("Atleast you are getting there!")
elif is_magician == "NO" and is_expert == "NO" :
    print("You need some magic in your life!")
else:
    print("SORRY! I didn't get what you said.")        
