from helpers import (
    exit_manager,
)

from cli_submenus import (
    facility_menu,
    facility_handler
)


def main():
    primary_menu()
    selection = input("> ")
    while selection < "2":
        if selection == "1":
            facility_handler()
    
    exit_manager()

def primary_menu():
    print("Welcome to Hospice Manager!")
    print("1 | Manage Facilities & Patients")
    print("2 | Exit Hospice Manager")


if __name__ == "__main__":
    main()