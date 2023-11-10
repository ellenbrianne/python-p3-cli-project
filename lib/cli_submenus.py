from helpers import (
    list_facilities,
    search_f_name,
    create_facility,
    update_facility,
    delete_facility,
    list_patients,
    search_p_name,
    create_patient,
    update_patient,
    delete_patient,
    match_patients
)
    
def facility_menu():
    print("How would you like to manage your facilities? Enter the corresponding number.")
    print("1 | List all of my facilities")
    print("2 | Search for a facility by name")
    print("3 | Add a new facility to my list")
    print("4 | Update one of my existing facilities")
    print("5 | Remove a facility from my list")
    print("Press enter to return to main menu")

def facility_handler():
    f_selection = input("> ")
    if f_selection == "1":
        list_facilities()
    elif f_selection == "2":
        search_f_name()
    elif f_selection == "2":
        search_f_name
    elif f_selection == "3":
        create_facility()
    elif f_selection == "4":
        update_facility()
    elif f_selection == "5":
        delete_facility()

def patient_menu():
    print("How would you like to handle your patients? Enter the corresponding number.")
    print("1 | List all of my patients")
    print("2 | Search for a patient by name")
    print("3 | Add a new patient to my list")
    print("4 | Update one of my existing patients")
    print("5 | Remove a patient from my list")
    print("6 | List patients according to facility")
    print("Press enter to return to main menu")

def patient_handler():
    p_selection = input("> ")
    if p_selection == "1":
        list_patients()
    elif p_selection == "2":
        search_p_name()
    elif p_selection == "3":
        create_patient()
    elif p_selection == "4":
        update_patient()
    elif p_selection == "5":
        delete_patient()
    elif p_selection == "6":
        match_patients()