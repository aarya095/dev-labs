# 9-15. Lottery Analysis

import random

numbers_letters = [1,2,3,4,5,6,7,8,9,0,'a','r','h','m','d']
ticket = random.choices(numbers_letters, k=4)

index = 0
my_list = []
my_guess = []
while my_guess != ticket:
    my_guess = random.choices(numbers_letters, k=4)
    my_list.append(my_guess)
    index += 1

print(f"These are the guesses I have made: {my_list}")
print(f"No. of guesses it took me to win the lottery: {index}")