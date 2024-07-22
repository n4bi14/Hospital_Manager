#main.py
from loginSystem import System, user_login
from doctor import Doctor
from patient import Patient_Management

def main():
    pm = Patient_Management()
    pm.patient_database("src/patients.txt")
    
    loginSys = System()
    user = user_login(loginSys)
    
    if user:
        if user.role == 'doctor':
            doctor = Doctor(user.username, user.role, pm)
            doctor.doctorMenu()  
        else:
            print(f"\nWelcome, {user.username}")
    else:
        print("Invalid username or password")

if __name__ == "__main__":
    main()
