# 9-3. Users

class User:

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def describe_user(self):
        print(f"Name: {self.first_name.title()} {self.last_name.title()}, Email: {self.email}.")

    def greet_user(self):
        print(f"Hello {self.first_name.title()}! May you have a good day!")

aarya = User('aarya','patel','aarya.patel@hotmail.com')
monika = User('monika','sharma','monika.sharma@gmail.com')
punit = User('punit','yadav','punit.yadav@proton.me')
lavanya = User('lavanya','joshi','lavanya.joshi@zohomail.in')

aarya.describe_user()
aarya.greet_user()
print('')
monika.describe_user()
monika.greet_user()
print('')
punit.describe_user()
punit.greet_user()
print('')
lavanya.describe_user()
lavanya.greet_user()