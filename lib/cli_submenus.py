from facility_helpers import (
    list_facilities,
    search_f_name,
    create_facility,
    update_facility,
    delete_facility
)
    
def facility_menu():
    print("Facility Menu:")
    print("1 | Access my facilities")
    print("2 | Search for a facility by name")
    print("3 | Add a new facility to my list")
    print("4 | Return to main menu")
    print("5 | Exit Hospice Manager")

def facility_handler():
    facility_menu()
    selection = input("> ")
    while selection < "5":
        if selection == "1":
            list_facilities()
            f_sub_menu_handler()
        elif selection == "2":
            search_f_name()
        elif selection == "3":
            create_facility()
            list_facilities()
            facility_handler()
        elif selection == "4":
            from cli import main
            main()

    from cli import exit_manager
    exit_manager()



def f_sub_menu():
    print("Select from one of these options to handle your facilities info: ")
    print("1 | View all patients in one facility")
    print("2 | Update a facility")
    print("3 | Delete a facility")
    print("4 | Return to facility menu")
    print("5 | Exit Hospice Manager")
    
def f_sub_menu_handler():
    f_sub_menu()
    selection = input("> ")
    while selection < "5":
        if selection == "1":
            f_id = match_patients()
            patient_handler(f_id)
        elif selection == "2":
            update_facility()
            list_facilities()
            facility_handler()
        elif selection == "3":
            delete_facility()
            list_facilities()
            facility_handler()
        elif selection == "4":
            facility_handler()
    
    from cli import exit_manager
    exit_manager()



def f_search_menu():
    print("What would you like to do with this facility? ")
    print("1 | Update info")
    print("2 | Delete this facility")
    print("3 | Return to facility menu")
    print("4 | Exit Hospice Manager")

def f_search_handler():
    f_search_menu()
    selection = input("> ")
    while selection < "4":
        if selection == "1":
            update_facility()
            list_facilities()
            facility_handler()
        elif selection == "2":
            delete_facility()
            list_facilities()
            facility_handler()
        elif selection == "3":
            facility_handler()

    from cli import exit_manager
    exit_manager()


from patient_helpers import (
    search_p_name,
    create_patient,
    update_patient,
    delete_patient,
    match_patients
)

def patient_menu():
    print("How would you like to handle these patients?")
    print("1 | Search by name")
    print("2 | Add a new patient to this facility's list")
    print("3 | Update one of these patients")
    print("4 | Remove one of these patients")
    print("5 | Return to facility menu")
    print("6 | Exit Hospice Manager")

def patient_handler(f_id):
    patient_menu()
    selection = input("> ")
    while selection < "6":
        if selection == "1":
            search_p_name()
            pt_search_handler(f_id)
        elif selection == "2":
            create_patient(f_id)
        elif selection == "3":
            update_patient(f_id)
        elif selection == "4":
            delete_patient(f_id)
        elif selection == "5":
            facility_handler()
    
    from cli import exit_manager
    exit_manager()

def pt_search_menu():
    print("What would you like to do with this patient? ")
    print("1 | Update info")
    print("2 | Delete this patient")
    print("3 | Return to facility menu")
    print("4 | Exit Hospice Manager")

def pt_search_handler(f_id):
    pt_search_menu()
    selection = input("> ")
    while selection < "4":
        if selection == "1":
            update_patient(f_id)
        elif selection == "2":
            delete_patient(f_id)
        elif selection == "3":
            facility_handler()
        
    from cli import exit_manager
    exit_manager()
