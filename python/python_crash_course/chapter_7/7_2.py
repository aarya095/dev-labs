while True:
    try:
        input_for_num_of_people = int(input("How many people are in your dining group? "))

        if input_for_num_of_people > 8:
            print("You'll have to wait!")
            break
        if input_for_num_of_people <= 0:
            print("Enter a number above zero!")
        else:
            print("The table is ready!")
            break
    except ValueError:
        print("Please enter an integer")