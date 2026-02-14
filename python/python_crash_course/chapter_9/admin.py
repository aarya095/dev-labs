from user import User

class Privileges:

    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(f"Admin has the following privileges: {self.privileges}.")

class Admin(User):

    def __init__(self, first_name, last_name, email):
        super().__init__(first_name, last_name, email)
        self.privileges1 = Privileges()
