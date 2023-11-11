from models.facility import Facility
from models.patient import Patient

def exit_manager():
    print("Closing Hospice Manager...")
    exit() 

def list_facilities():
    facilities = Facility.get_all()
    print("FACILITIES:")
    for f in facilities: print(f)

def search_f_name():
    name = input("Enter the facility's name: ")
    facility = Facility.find_by_name(name)
    print(facility) if facility else print(
        f"{name} not found")

def search_f_id():
    id_ = input("Enter the facility's id number: ")
    facility = Facility.find_by_id(id_)
    print(facility) if facility else print(
        f"Facility {id_} not found")

def create_facility():
    name = input("Enter the new facility's name: ")
    location = input("Enter the new facility's location: ")
    try:
        facility = Facility.create(name, location)
        print(f"{name} has been added to your facilities!\n{facility}")
    except Exception as exc:
        print("Error -- facility was not added because:", exc)

def update_facility():
    id_ = input("Enter the number of the facility you want to update: ")
    if facility := Facility.find_by_id(id_):
        try:
            name = input("Enter the facility's new name: ")
            facility.name = name
            location = input("Enter the facility's new location: ")
            facility.location = location
            facility.update()
            print(f"Successfully udpated: {facility}")
        except Exception as exc:
            print(f"Error updating this facility:", exc)
    else: 
        print(f"Facility {id_} not found")

def delete_facility():
    id_ = input("Enter the number of the facility you want to delete: ")
    if facility := Facility.find_by_id(id_):
        facility.delete()
        print(f"Facility {id_} successfully deleted!")
    else:
        print(f"Facility {id_} not found")

### PATIENT HELPERS

def list_patients():
    patients = Patient.get_all()
    for p in patients: print(p)

def search_p_name():
    name = input("Enter the patient's name: ")
    patient = Patient.find_by_name(name)
    print(patient) if patient else print(
        f"{name} not found")

def search_p_id():
    id_ = input("Enter the patient's id number: ")
    patient = Patient.find_by_id(id_)
    print(patient) if patient else print(
        f"Patient {id_} not found")

def create_patient(id_):
    name = input("Enter the new patient's name: ")
    diagnosis = input("Enter the new patient's diagnosis: ")
    try:
        patient = Patient.create(name, diagnosis, int(id_))
        print(f"{name} has been added to your patients!\n{patient}")
    except Exception as exc:
        print("Error -- patient was not added because:", exc)

def update_patient():
    id_ = input("Enter the number of the patient you want to update: ")
    if patient := Patient.find_by_id(id_):
        try:
            name = input("Enter the patient's new name: ")
            patient.name = name
            diagnosis = input("Enter the patient's new diagnosis: ")
            patient.diagnosis = diagnosis
            facility_id = input("Enter the patient's facility id: ")
            patient.facility_id = int(facility_id)
            patient.update()
            print(f"Successfully udpated: {patient}")
        except Exception as exc:
            print(f"Error updating this patient:", exc)
    else: 
        print(f"Patient {name} not found")

def delete_patient():
    id_ = input("Enter the number of the patient you want to delete: ")
    if patient := Patient.find_by_id(id_):
        patient.delete()
        print(f"Patient {id_} successfully deleted!")
    else:
        print(f"Patient {id_} not found")

def match_patients():
    id_ = input("Enter the facility's number to view their patients: ")
    if facility := Facility.find_by_id(id_):
        patients = facility.find_patients()
        print(f"{facility.name} PATIENTS:")
        for p in patients: print(p)
    else:
        print(f"No matching patients found for Facility {id_}")
    return id_
