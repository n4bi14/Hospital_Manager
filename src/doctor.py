
class Doctor:
    def __init__(self, username, role, patient_management):
        self.username = username
        self.role = role
        self.patient_management = patient_management

    def add_meds(self):
        birthdate = input('Patient birthdate: ')
        new_meds = input('New meds: ')
        self.patient_management.add_meds_to_patient(birthdate, new_meds)
        self.patient_management.save_patients("src/patients.txt")
        print("Medications updated and saved to file.")
    
    def print_patients(self):
        self.patient_management.print_patients()

    def doctorMenu(self):
        print(f"Hello, {self.username}.")
        while True:
            print("Menu")
            print("1. Prescribe medication")
            print("2. Print patients")
            print("3. Exit")
            request = input("")

            if request == "1":
                self.add_meds()
            elif request == "2":
                self.print_patients()
            elif request == "3":
                break
            else:
                print("Invalid selection")
