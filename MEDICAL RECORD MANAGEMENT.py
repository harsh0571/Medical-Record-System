import matplotlib.pyplot as plt


class Patient:
    def __init__(
        self, name, age, gender, address, phone_number, medical_history, location
    ):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
        self.phone_number = phone_number
        self.medical_history = medical_history
        self.location = location


class MedicalRecord:
    def __init__(self):
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def search_patient(self, name):
        for patient in self.patients:
            if patient.name == name:
                return patient
        return None

    def display_records(self):
        for patient in self.patients:
            print("Name:", patient.name)
            print("Age:", patient.age)
            print("Gender:", patient.gender)
            print("Address:", patient.address)
            print("Phone Number:", patient.phone_number)
            print("Medical History:", patient.medical_history)
            print("Location:", patient.location)
            print("-------------------------------")

    def generate_graph(self, patient_name):
        patient = self.search_patient(patient_name)
        if patient:
            x = [i for i in range(len(patient.medical_history))]
            y = patient.medical_history
            plt.plot(x, y)
            plt.title("Patient Health History Graph")
            plt.xlabel("Visit Number")
            plt.ylabel("Health Score")
            plt.show()
        else:
            print("Patient not found!")


if __name__ == "__main__":
    record = MedicalRecord()
    while True:
        print("\n1. Add patient")
        print("2. Search patient")
        print("3. Display all records")
        print("4. Generate patient health history graph")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = input("Enter patient name: ")
            age = int(input("Enter patient age: "))
            gender = input("Enter patient gender: ")
            address = input("Enter patient address: ")
            phone_number = input("Enter patient phone number: ")
            medical_history = []
            while True:
                score = input("Enter health score (or q to stop): ")
                if score == "q":
                    break
                medical_history.append(int(score))
            location = input("Enter patient location: ")
            patient = Patient(
                name, age, gender, address, phone_number, medical_history, location
            )
            record.add_patient(patient)
            print("Patient added successfully!")
        elif choice == 2:
            name = input("Enter patient name to search: ")
            patient = record.search_patient(name)
            if patient:
                print("Name:", patient.name)
                print("Age:", patient.age)
                print("Gender:", patient.gender)
                print("Address:", patient.address)
                print("Phone Number:", patient.phone_number)
                print("Medical History:", patient.medical_history)
                print("Location:", patient.location)
            else:
                print("Patient not found!")
        elif choice == 3:
            record.display_records()
        elif choice == 4:
            name = input("Enter patient name to generate graph: ")
            record.generate_graph(name)
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")
