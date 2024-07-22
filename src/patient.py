class Patient:
    def __init__(self, firstname, lastname, birthdate, meds):
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate
        self.meds = meds

    def add_meds(self, new_meds):
        if self.meds == "none":
            self.meds = new_meds
        else:
            self.meds += f", {new_meds}"

class Patient_Management:
    def __init__(self):
        self.patients = {}

    def add_meds_to_patient(self, birthdate, meds):
        if birthdate in self.patients:
            self.patients[birthdate].add_meds(meds)
            print(f"Added meds to patient with birthdate {birthdate}.")
        else:
            print(f"No patient found with that birthdate.")

    def patient_database(self, filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    firstname, lastname, birthdate, meds = line.strip().split()
                    self.patients[birthdate] = Patient(firstname, lastname, birthdate, meds)
        except FileNotFoundError:
            print(f"File {filename} not found")

    def print_patients(self):
        for birthdate, patient in self.patients.items():
            print(f"Name: {patient.firstname} {patient.lastname}, Birthdate: {patient.birthdate}, Meds: {patient.meds}")

    def save_patients(self, filename):
        with open(filename, 'w') as file:
            for patient in self.patients.values():
                file.write(f"{patient.firstname} {patient.lastname} {patient.birthdate} {patient.meds}\n")
