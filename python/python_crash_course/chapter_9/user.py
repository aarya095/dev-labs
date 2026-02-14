class User:

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def describe_user(self):
        print(f"Name: {self.first_name.title()} {self.last_name.title()}, Email: {self.email}.")

    def greet_user(self):
        print(f"Hello {self.first_name.title()}! May you have a good day!")

