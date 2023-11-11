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
    print("Facility Menu:")
    print("1 | List all of my facilities")
    print("2 | Search for a facility by name")
    print("3 | Add a new facility to my list")
    print("4 | Return to main menu")

def facility_handler():
    facility_menu()
    selection = input("> ")
    if selection == "1":
        list_facilities()
        f_sub_menu_handler()
    elif selection == "2":
        search_f_name()
        f_search_handler()
    elif selection == "3":
        create_facility()
    elif selection == "4":
        from cli import main
        main()

def f_sub_menu():
    print("Select from one of these options to handle your facilities info: ")
    print("1 | View all patients in one facility")
    print("2 | Update a facility")
    print("3 | Delete a facility")
    print("4 | Return to facility menu")
    
def f_sub_menu_handler():
    f_sub_menu()
    selection = input("> ")
    if selection == "1":
        id_ = match_patients()
        patient_handler(id_)
    elif selection == "2":
        update_facility()
    elif selection == "3":
        delete_facility()
    elif selection == "4":
        facility_handler()
    

def patient_menu():
    print("How would you like to handle these patients?")
    print("1 | Search by name")
    print("2 | Add a new patient to this facility's list")
    print("3 | Update one of these patients")
    print("4 | Remove one of these patients")
    print("5 | Return to facility menu")

def patient_handler(id_):
    patient_menu()
    selection = input("> ")
    if selection == "1":
        search_p_name()
        pt_search_handler(id_)
    elif selection == "2":
        create_patient(id_)
    elif selection == "3":
        update_patient(id_)
    elif selection == "4":
        delete_patient()
    elif selection == "5":
        facility_handler()

def pt_search_menu():
    print("What would you like to do with this patient? ")
    print("1 | Update info")
    print("2 | Delete this patient")
    print("3 | Return to facility menu")

def pt_search_handler(id_):
    pt_search_menu()
    selection = input("> ")
    if selection == "1":
        update_patient(id_)
    elif selection == "2":
        delete_patient()
    elif selection == "3":
        facility_handler()

def f_search_menu():
    print("What would you like to do with this facility? ")
    print("1 | Update info")
    print("2 | Delete this facility")
    print("3 | Return to facility menu")

def f_search_handler():
    f_search_menu()
    selection = input("> ")
    if selection == "1":
        update_facility()
    elif selection == "2":
        delete_facility()
    elif selection == "3":
        facility_handler()