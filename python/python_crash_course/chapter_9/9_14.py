# 9-14. Lottery

import random

numbers_letters = [1,2,3,4,5,6,7,8,9,0,'a','r','h','m','d']

ticket = random.choices(numbers_letters, k=4)

print("Any ticket matching the following '",end='')
print(*ticket,sep='',end='')
print("' wins a prize.")
