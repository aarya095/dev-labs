# 5-8. Hello Admin | 5-9. No Users

usernames = ['aarya','sam','pushkar','admin','savita']

for username in usernames:
    if username == 'admin':
        print("Hello Admin, would you like to see a staus report?")
    else:
        print(f"Hello {username.title()}, thank you for logging in again.")

usernames = []

if not usernames:
    print("We need to find some users!")