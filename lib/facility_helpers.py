from models.facility import Facility

def list_facilities():
    facilities = Facility.get_all()
    print("FACILITIES:")
    for index, f in enumerate(facilities, start=1): 
        print(f"{index} | {f.name} in {f.location}")

def search_f_name():
    name = input("Enter the facility's name: ")
    match = Facility.find_by_name(name)
    facilities = Facility.get_all()
    
    if match := Facility.find_by_name(name):
        for index, f in enumerate(facilities, start=1):
                if match.name == f.name:
                    print(f"{index} | {f.name} in {f.location}")
        from cli_submenus import f_search_handler
        f_search_handler()
    else:
        print("This facility could not be found")
        from cli_submenus import facility_handler
        facility_handler()

def create_facility():
    name = input("Enter the new facility's name: ")
    location = input("Enter the new facility's location: ")
    try:
        Facility.create(name, location)
        print(f"{name} has been added to your facilities!")
    except Exception as exc:
        print("Facility could not be added --", exc)

def update_facility():
    ## trouble with error handling when input is ' '
    choice = int(input("Enter the number of the facility you want to update: "))
    facilities = Facility.get_all()
    if match := facilities[choice - 1]:
        try:
            name = input("Enter the facility's new name: ")
            match.name = name
            location = input("Enter the facility's new location: ")
            match.location = location
            match.update()
            print(f"Successfully udpated: {choice} | {match.name} in {match.location}")
        except Exception as exc:
            print(f"Error updating this facility:", exc)
    else: 
        print(f"Facility {choice} not found")
 
def delete_facility():
    ## trouble with error handling when input is ' '
    choice = int(input("Enter the number of the facility you want to delete: "))
    facilities = Facility.get_all()

    if match := facilities[choice - 1]:
        try:
            match.delete()
            print(f"Facility {choice} successfully deleted.")
        except Exception as exc:
            print(f"Error finding facility:", exc)
    else:
        print(f"Facility {choice} not found.")
