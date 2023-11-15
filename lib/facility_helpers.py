from models.facility import Facility

def list_facilities():
    facilities = Facility.get_all()
    print("FACILITIES:")
    for index, f in enumerate(facilities, start=1): 
        print(f"{index} | {f.name} in {f.location}")

def search_f_name():
    name = input("Enter the facility's name: ")
    facility = Facility.find_by_name(name)
    print(facility) if facility else print(
        f"{name} not found")

def create_facility():
    name = input("Enter the new facility's name: ")
    location = input("Enter the new facility's location: ")
    try:
        facility = Facility.create(name, location)
        print(f"{name} has been added to your facilities!\n{facility}")
    except Exception as exc:
        print("Facility could not be added --", exc)

def update_facility():
    choice = int(input("Enter the number of the facility you want to update: "))
    facilities = Facility.get_all()
    match = facilities[choice - 1]

    if match:
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
    id_ = input("Verify the number of the facility you want to delete: ")
    if facility := Facility.find_by_id(id_):
        facility.delete()
        print(f"Facility {id_} successfully deleted!")
    else:
        print(f"Facility {id_} not found")

