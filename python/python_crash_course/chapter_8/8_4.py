# 8-4. Large Shirts

def make_shirt(size, txt_message='I love Python!'):
    print(f"Size of your shirt is {size.lower()}. The text printed on it is going to be '{txt_message.title()}'.")

make_shirt("Large")
print('')
make_shirt("Medium")
print('')
make_shirt("Small","I love JavaScript!")