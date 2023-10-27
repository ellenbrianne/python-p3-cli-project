from models.__init__ import CONN, CURSOR
from models.facility import Facility

def seed_db():
    Facility.drop_table()
    Facility.create_table()

    Facility.create("Southside Manor", "Tampa, FL")
    Facility.create("Hilltop Heights LTAC", "Destin, FL")
    
seed_db()