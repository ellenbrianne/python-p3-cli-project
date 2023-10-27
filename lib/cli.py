from helpers import (
    exit_manager
)

def main():
    while True:
        primary_menu()
        selection = input("> ")
        if selection == "2":
            exit_manager()

def primary_menu():
    print("Type the number of the section you need to manage: Facilities or Patients?")
    print("0 | Facilities")
    print("1 | Patients")
    print("2 | Exit Hospice Manager")


if __name__ == "__main__":
    main()