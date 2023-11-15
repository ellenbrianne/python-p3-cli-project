from models.patient import Patient

def search_p_name():
    name = input("Enter the patient's name: ")
    patient = Patient.find_by_name(name)
    print(patient) if patient else print(
        f"{name} not found")

def create_patient(id_):
    name = input("Enter the new patient's name: ")
    diagnosis = input("Enter the new patient's diagnosis: ")
    try:
        Patient.create(name, diagnosis, int(id_))
        print(f"{name} has been added to your patients!")
    except Exception as exc:
        print("Error -- patient was not added because:", exc)

def update_patient(f_id):
    choice  = int(input("Enter the number of the patient you want to update: "))

    from models.facility import Facility
    facility = Facility.find_by_id(f_id)
    patients = facility.find_patients()

    if match := patients[choice - 1]:
        try:
            name = input("Enter the patient's new name: ")
            match.name = name
            diagnosis = input("Enter the patient's new diagnosis: ")
            match.diagnosis = diagnosis
            match.facility_id = int(f_id)
            match.update()
            print(f"Successfully udpated: {choice} | {match.name}, {match.diagnosis}")
        except Exception as exc:
            print(f"Error updating this patient:", exc)
    else: 
        print(f"Patient {choice} not found")

def delete_patient(f_id):
    choice = int(input("Enter the number of the patient you want to delete: "))

    from models.facility import Facility
    facility = Facility.find_by_id(f_id)
    patients = facility.find_patients()

    if match := patients[choice - 1]:
        match.delete()
        print(f"Patient {choice} successfully deleted!")
    else:
        print(f"Patient {choice} not found")

def match_patients():
    choice = int(input("Enter the facility's number to view their patients: "))

    from models.facility import Facility
    facilities = Facility.get_all()
    if match := facilities[choice - 1]:
        patients = match.find_patients()
        print(f"{match.name}'s PATIENTS:")
        for index, p in enumerate(patients, start=1): 
            print(f"{index} | {p.name}, {p.diagnosis}")
    else:
        print(f"No matching patients found for Facility {choice}")

    return match.id