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
        patient = Patient.create(name, diagnosis, int(id_))
        print(f"{name} has been added to your patients!\n{patient}")
    except Exception as exc:
        print("Error -- patient was not added because:", exc)

def update_patient(id_):
    p_id = input("Enter the number of the patient you want to update: ")
    if patient := Patient.find_by_id(p_id):
        try:
            name = input("Enter the patient's new name: ")
            patient.name = name
            diagnosis = input("Enter the patient's new diagnosis: ")
            patient.diagnosis = diagnosis
            patient.facility_id = int(id_)
            patient.update()
            print(f"Successfully udpated: {patient}")
        except Exception as exc:
            print(f"Error updating this patient:", exc)
    else: 
        print(f"Patient {name} not found")

def delete_patient():
    id_ = input("Verify the number of the patient you want to delete: ")
    if patient := Patient.find_by_id(id_):
        patient.delete()
        print(f"Patient {id_} successfully deleted!")
    else:
        print(f"Patient {id_} not found")

def match_patients():
    id_ = input("Enter the facility's number to view their patients: ")
    from models.facility import Facility
    if facility := Facility.find_by_id(id_):
        patients = facility.find_patients()
        print(f"{facility.name}'s PATIENTS:")
        for p in patients: print(p)
    else:
        print(f"No matching patients found for Facility {id_}")
    return id_