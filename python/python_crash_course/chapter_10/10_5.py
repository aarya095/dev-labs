while True:
    user_input = input("Why do you like programming?\n")
    if user_input == 'exit':
        break
    
    with open('responses.txt','a') as f:
        f.write('\n')
        f.write(f"Response: {user_input}")
        f.write('\n---------------')