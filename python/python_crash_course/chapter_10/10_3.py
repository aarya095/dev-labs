user_input = input("Enter your name: ")

with open('guest.txt','w') as f:
    f.write(user_input)