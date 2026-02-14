# 9-5. Login Attempts

class User:

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print(f"Name: {self.first_name.title()} {self.last_name.title()}, Email: {self.email}.")

    def greet_user(self):
        print(f"Hello {self.first_name.title()}! May you have a good day!")

    def increment_login_attempts(self):
        self.login_attempts = self.login_attempts + 1

    def reset_login_attempts(self):
        self.login_attempts = 0
        print("Resetting the number of login attempts.")

aarya = User('aarya','patel','aarya.patel@hotmail.com')
aarya.increment_login_attempts()
aarya.increment_login_attempts()
aarya.increment_login_attempts()
aarya.increment_login_attempts()
print(f"Number of Login attempts have been made are {aarya.login_attempts}.")

aarya.reset_login_attempts()
print(f"Number of Login attempts have been made are {aarya.login_attempts}.")