while True:
    user_input = input("Enter your name: ")
    if user_input == 'exit':
        break

    print(f"Hello {user_input.title()}!")

    with open('guest_book.txt','a') as f:
        f.write(f"{user_input.title()} visited here.")
        f.write('\n')