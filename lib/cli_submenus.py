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
)
    
def facility_menu():
    print("Facility Menu:")
    print("1 | List all of my facilities")
    print("2 | Search for a facility by name")
    print("3 | Add a new facility to my list")
    print("4 | Update one of my existing facilities")
    print("5 | Remove a facility from my list")
    print("6 | Return to main menu")

def facility_handler():
    facility_menu()
    selection = input("> ")
    if selection == "1":
        list_facilities()
    elif selection == "2":
        search_f_name()
    elif selection == "3":
        create_facility()
    elif selection == "4":
        update_facility()
    elif selection == "5":
        delete_facility()
    elif selection == "6":
        from cli import main
        main()
    



def patient_menu():
    print("How would you like to handle your patients? Enter the corresponding number.")
    print("1 | List all of my patients")
    print("2 | Search for a patient by name")
    print("3 | Add a new patient to my list")
    print("4 | Update one of my existing patients")
    print("5 | Remove a patient from my list")
    print("6 | Return to main menu")

def patient_handler():
    selection = input("> ")
    if selection == "1":
        list_patients()
    elif selection == "2":
        search_p_name()
    elif selection == "3":
        create_patient()
    elif selection == "4":
        update_patient()
    elif selection == "5":
        delete_patient()
    elif selection == "6":
        from cli import main
        main()