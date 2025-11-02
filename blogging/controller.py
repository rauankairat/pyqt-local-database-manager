
class Controller:
    def __init__(self):
        self.username = 'user'
        self.password = 'blogging2025'
        self.logged_in = False 

    def login(self, name, password):
        if self.username == name and self.password == password and not self.logged_in:
            self.logged_in = True
            return True
        return False

    def logout(self):
        if self.logged_in:
            self.logged_in = False
            return True
        else:
            return False