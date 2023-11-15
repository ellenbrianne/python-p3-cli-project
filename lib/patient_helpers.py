from models.patient import Patient

def search_p_name(f):
    name = input("Enter the patient's name: ")
    match = Patient.find_by_name(name)

    from models.facility import Facility
    patients = f.find_patients()
    
    if match := Patient.find_by_name(name):
        for index, p in enumerate(patients, start=1):
                if match.name == p.name:
                    print(f"{index} | {p.name}, {p.diagnosis}")

        from cli_submenus import pt_search_handler
        pt_search_handler(f)
    else:
        print(f"{name} could not be found")
        from cli_submenus import patient_handler
        patient_handler(f)

def create_patient(f):
    name = input("Enter the new patient's name: ")
    diagnosis = input("Enter the new patient's diagnosis: ")
    from models.facility import Facility
    try:
        Patient.create(name, diagnosis, int(f.id))
        print(f"{name} has been added to your patients!")

        patients = f.find_patients()
        print(f"{f.name}'s PATIENTS:")
        for index, p in enumerate(patients, start=1):
            print(f"{index} | {p.name}, {p.diagnosis}")

        from cli_submenus import patient_handler
        patient_handler(f)
    except Exception as exc:
        print("Error -- patient was not added because:", exc)

def update_patient(f):
    choice  = input("Enter the number of the patient you want to update: ")

    from models.facility import Facility
    facility = Facility.find_by_id(f.id)
    patients = facility.find_patients()

    while choice == "":
        print("Please provide a number")
        choice  = input("Enter the number of the patient you want to update: ")
    
    if match := patients[int(choice) - 1]:
        try:
            name = input("Enter the patient's new name: ")
            match.name = name
            diagnosis = input("Enter the patient's new diagnosis: ")
            match.diagnosis = diagnosis
            match.facility_id = int(f.id)
            match.update()
            print(f"Successfully udpated: {int(choice)} | {match.name}, {match.diagnosis}")

            newly_added_p = f.find_patients()
            print(f"{f.name}'s PATIENTS:")
            for index, p in enumerate(newly_added_p, start=1):
                print(f"{index} | {p.name}, {p.diagnosis}")

            from cli_submenus import patient_handler
            patient_handler(f)
        except Exception as exc:
            print(f"Error updating this patient:", exc)
    else: 
        print(f"Patient {int(choice)} not found")

def delete_patient(f):
    choice = input("Enter the number of the patient you want to delete: ")

    from models.facility import Facility
    facility = Facility.find_by_id(f.id)
    patients = facility.find_patients()

    while choice == "":
        print("Please provide a number")
        choice = input("Enter the number of the patient you want to delete: ")

    if match := patients[int(choice) - 1]:
        match.delete()
        print(f"Patient {choice} successfully deleted!")

        new_p_list = f.find_patients()
        print(f"{f.name}'s PATIENTS:")
        for index, p in enumerate(new_p_list, start=1):
            print(f"{index} | {p.name}, {p.diagnosis}")
            
        from cli_submenus import patient_handler
        patient_handler(f)
    else:
        print(f"Patient {int(choice)} not found")

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

    return match