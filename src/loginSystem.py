# loginSystem.py
import bcrypt

class Data:
    def __init__(self, username, hashed_password, role):
        self.username = username
        self.hashed_password = hashed_password
        self.role = role
        
    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.hashed_password)
   
    @staticmethod
    def hashed_password(password):
        salt = bcrypt.gensalt()  # Generate a salt
        return bcrypt.hashpw(password.encode('utf-8'), salt)  # Hash the password with the salt
        
        
class System:
    def __init__(self):
        self.users = {}
        self.user_database('src/users.txt')
        
    def user_database(self, filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    username, hashed_password, role = line.strip().split()
                    self.users[username] = Data(username, hashed_password.encode('utf-8'), role)
        except FileNotFoundError:
            print(f"File {filename} not found")
        
    def register_user(self):
        username = input("Username: ")
        role = "none"
        if username in self.users:
            print("This username already exists")
            return None
        else:
            password = input("Password: ")
            hashed_password = Data.hashed_password(password)
            new_user = Data(username, hashed_password, role)
            self.users[username] = new_user
        
            with open('src/users.txt', 'a') as file:
                file.write(f"{username} {hashed_password.decode('utf-8')} {role}\n")
                return new_user
        
    def login(self, username, password):
        user = self.users.get(username)
        if user and user.check_password(password):
            return user  
        return None  
        
def user_login(system):
    print("1. Create an account\n2. Login")
    user_request = input("Choose an option (1 or 2): ")
    
    if user_request == "1":
        return system.register_user()
    
    elif user_request == "2":
        username = input('Username: ')
        password = input('Password: ')
        user = system.login(username, password)
        return user
    else:
        print("Invalid option. Please choose 1 or 2.")
        return None 


