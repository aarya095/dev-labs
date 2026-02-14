# 3-4. Guest List | 3-5. Changing Guest List | 3-6. More Guests | 3-7. Shrinking Guest List | 3-9. Dinner Guests

guest_list = ['ram','laxam','sita']

print(f"I am inviting {guest_list[0]} to tonight's dinner.")
print(f"I am inviting {guest_list[1]} to tonight's dinner.")
print(f"I am inviting {guest_list[2]} to tonight's dinner.\n")

print(f"Unfortunately, {guest_list[2]} can't make it to tonight's dinner.\n")
guest_list[2] = 'hanuman'

print(f"I am inviting {guest_list[0]} to tonight's dinner.")
print(f"I am inviting {guest_list[1]} to tonight's dinner.")
print(f"I am inviting {guest_list[2]} to tonight's dinner.\n")

print("I've found a bigger dinner table.\n")

guest_list.insert(0,'nal')
guest_list.insert(3,'neel')
guest_list.append('garud')

print(f"I am inviting {guest_list[0]} to tonight's dinner.")
print(f"I am inviting {guest_list[1]} to tonight's dinner.")
print(f"I am inviting {guest_list[2]} to tonight's dinner.")
print(f"I am inviting {guest_list[3]} to tonight's dinner.")
print(f"I am inviting {guest_list[4]} to tonight's dinner.")
print(f"I am inviting {guest_list[5]} to tonight's dinner.\n")

print("Unfortunately, the new dinner table won't arrive in time for the dinner, and I have space for only two guests. " \
"I sincerely apologize for the inconvinence!\n")

pop_garud = guest_list.pop()
print(f"{pop_garud.title()} sorry to inform that I can't invite you to the dinner.")

pop_hanuman = guest_list.pop()
print(f"{pop_hanuman.title()} sorry to inform that I can't invite you to the dinner.")

pop_neel = guest_list.pop()
print(f"{pop_neel.title()} sorry to inform that I can't invite you to the dinner.")

pop_laxman = guest_list.pop()
print(f"{pop_laxman.title()} sorry to inform that I can't invite you to the dinner.\n")

print(f"{guest_list[0].title()} are still invited to tonight's dinner.")
print(f"{guest_list[1].title()} are still invited to tonight's dinner.")

number_of_guests = len(guest_list)
print(f"Number of guests coming are {number_of_guests}.")

del guest_list[1]
del guest_list[0]

print(guest_list)

number_of_guests = len(guest_list)
print(f"Number of guests coming are {number_of_guests}.")