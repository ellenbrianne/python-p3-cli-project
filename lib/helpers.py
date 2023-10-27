from models.facility import Facility

def exit_manager():
    print("Closing Hospice Manager...")
    exit() 

def list_facilities():
    facilities = Facility.get_all()
    for f in facilities: print(f)

def search_f_name():
    name = input("Enter the facility's name: ")
    facility = Facility.find_by_name(name)
    print(facility) if facility else print(
        f"{name} not found")

def search_f_id():
    id_ = input("Enter the facility's id number: ")
    facility = Facility.find_by_id(id_)
    print(facility) if facility else print(
        f"Facility {id_} not found")

def create_facility():
    name = input("Enter the new facility's name: ")
    location = input("Enter the new facility's location: ")
    try:
        facility = Facility.create(name, location)
        print(f"{name} has been added to your facilities!\n{facility}")
    except Exception as exc:
        print("Error -- facility was not added because:", exc)

def update_facility():
    pass

def delete_facility():
    pass