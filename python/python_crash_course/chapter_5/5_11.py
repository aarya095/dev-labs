# 5-11. Ordinal Numbers

list_of_first_9_numbers = []

for i in range(1,10):
    list_of_first_9_numbers.append(i)

for list_of_first_9_number in list_of_first_9_numbers:
    
    if list_of_first_9_number == 1:
        print(f"{list_of_first_9_number}st")
    elif list_of_first_9_number == 2:
        print(f"{list_of_first_9_number}nd")
    elif list_of_first_9_number == 3:
        print(f"{list_of_first_9_number}rd")
    else:
        print(f"{list_of_first_9_number}th")