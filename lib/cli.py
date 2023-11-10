from helpers import (
    exit_manager,
)

from cli_submenus import (
    facility_menu,
    facility_handler,
    patient_menu,
    patient_handler
)


def main():
    while True:
        primary_menu()
        selection = input("> ")
        if selection == "3":
            exit_manager()
        elif selection == "1":
            facility_menu()
            facility_handler()
        elif selection == "2":
            patient_menu()
            patient_handler()

def primary_menu():
    print("Welcome to Hospice Manager!")
    print("1 | View My Facilities")
    print("2 | View My Patients")
    print("3 | Exit Hospice Manager")


if __name__ == "__main__":
    main()