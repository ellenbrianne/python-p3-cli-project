from helpers import (
    exit_manager,
    list_facilities,
    search_f_name,
    search_f_id,
    create_facility,
    update_facility,
    delete_facility
)


def main():
    while True:
        primary_menu()
        p_selection = input("> ")
        if p_selection == "2":
            exit_manager()
        elif p_selection == "0":
            facility_menu()
            facility_handler()

def primary_menu():
    print("Type the number of the section you need to manage: Facilities or Patients?")
    print("0 | Facilities")
    print("1 | Patients")
    print("2 | Exit Hospice Manager")

def facility_menu():
    print("How would you like to manage your facilities? Enter the corresponding number.")
    print("0 | List all of my facilities")
    print("1 | Search for a facility by name")
    print("2 | Search for a facility by id number")
    print("3 | Add a new facility to my list")
    print("4 | Update one of my existing facilities")
    print("5 | Remove a facility from my list")
    print("6 | Return to main menu")

def facility_handler():
    f_selection = input("> ")
    if f_selection == "0":
        list_facilities()
    elif f_selection == "1":
        search_f_name()
    elif f_selection == "2":
        search_f_id()
    elif f_selection == "3":
        create_facility()
    elif f_selection == "4":
        update_facility()
    elif f_selection == "5":
        delete_facility()
    elif f_selection == "6":
        primary_menu()


if __name__ == "__main__":
    main()