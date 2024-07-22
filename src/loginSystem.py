# loginSystem.py
class Data:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role
        
    def check_password(self, password):
        return self.password == password
        
class System:
    def __init__(self):
        self.users = {}
        self.user_database('src/users.txt')
        
    def user_database(self, filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    username, password, role = line.strip().split()
                    self.users[username] = Data(username, password, role)
        except FileNotFoundError:
            print(f"File {filename} not found")
        
    def register_user(self, username, password, role):
        if username in self.users:
            print("This username already exists")
        else:
            self.users[username] = Data(username, password, role)
        
    def login(self, username, password):
        user = self.users.get(username)
        if user and user.check_password(password):
            return user  
        return None  
        
def user_login(system):
    username = input('Username: ')
    password = input('Password: ')
    user = system.login(username, password)
    return user
