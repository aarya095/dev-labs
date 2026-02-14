# 9-8. Privileges

class User:

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def describe_user(self):
        print(f"Name: {self.first_name.title()} {self.last_name.title()}, Email: {self.email}.")

    def greet_user(self):
        print(f"Hello {self.first_name.title()}! May you have a good day!")

class Privileges:

    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(f"Admin has the following privileges: {self.privileges}.")

class Admin(User):

    def __init__(self, first_name, last_name, email):
        super().__init__(first_name, last_name, email)
        self.privileges1 = Privileges()

admin1 = Admin('Aarya','Sarfare','aarya@mail.in')
admin1.privileges1.show_privileges()