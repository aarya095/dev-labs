# 5-10. Checking Usernames

current_users = ['Aarya','Monika','Lakshman','Roger','Punit']
copy_current_users = []
for i in current_users:
    copy_current_users.append(i.lower()) 
print(copy_current_users)

new_users = ['puNit','Isha','moniKa','Nisarg','omkar']

for new_user in new_users:
    formatted_new_username = new_user.lower()
    if formatted_new_username in copy_current_users:
        print(f"Username '{new_user}' already taken!")
    else:
        print(f"Username '{new_user}' is available.")