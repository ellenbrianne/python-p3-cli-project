from helpers import (
    exit_manager
)
from lib.cli_submenus import (
    facility_menu,
    facility_handler,
    patient_menu,
    patient_handler
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
        elif p_selection == "1":
            patient_menu()
            patient_handler()

def primary_menu():
    print("Type the number of the section you need to manage: Facilities or Patients?")
    print("0 | Facilities")
    print("1 | Patients")
    print("2 | Exit Hospice Manager")


if __name__ == "__main__":
    main()