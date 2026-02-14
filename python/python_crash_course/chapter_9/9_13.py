# 9-13. Dice

import random

class Dice:

    def __init__(self, sides = 6):
        self.sides = sides

    def roll_method(self):
        print(f"Result: {random.choice(range(1,self.sides))}")

print("--Six sided dice--")
dice_six_sided = Dice()
dice_six_sided.roll_method()
dice_six_sided.roll_method()
dice_six_sided.roll_method()
dice_six_sided.roll_method()
dice_six_sided.roll_method()
dice_six_sided.roll_method()
dice_six_sided.roll_method()
dice_six_sided.roll_method()
dice_six_sided.roll_method()
dice_six_sided.roll_method()

print("\n--Ten sided dice--")
dice_ten_sided = Dice(10)
dice_ten_sided.roll_method()
dice_ten_sided.roll_method()
dice_ten_sided.roll_method()
dice_ten_sided.roll_method()
dice_ten_sided.roll_method()
dice_ten_sided.roll_method()
dice_ten_sided.roll_method()
dice_ten_sided.roll_method()
dice_ten_sided.roll_method()
dice_ten_sided.roll_method()

print("\n--Twenty sided dice--")
dice_twenty_sided = Dice(20)
dice_twenty_sided.roll_method()
dice_twenty_sided.roll_method()
dice_twenty_sided.roll_method()
dice_twenty_sided.roll_method()
dice_twenty_sided.roll_method()
dice_twenty_sided.roll_method()
dice_twenty_sided.roll_method()
dice_twenty_sided.roll_method()
dice_twenty_sided.roll_method()
dice_twenty_sided.roll_method()