firstname = input("Type your first name: ")
lastname =  input("Type your last name: ")
username = input("Select a username for your account: ")
password = input("Choose a suitable password for your account: ")
password_length = len(password)
hidden_password = "*"*password_length

if (password_length>12):
    print(f"{firstname}! The password you have chosen {hidden_password} is very long.")
    print("Your password should be 8-12 characters long")
elif (password_length<8):
    print(f"{firstname}! The password you have chosen {hidden_password} is very short.")
    print("Your password should be 8-12 characters long")
else:       
    print("Valid password")       
