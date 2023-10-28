from models.__init__ import CONN, CURSOR
from models.facility import Facility
from models.patient import Patient

def seed_db():
    Facility.drop_table()
    Facility.create_table()
    Patient.drop_table()
    Patient.create_table()

    southside = Facility.create("Southside Manor", "Tampa, FL")
    hilltop = Facility.create("Hilltop Heights LTAC", "Destin, FL")
    Patient.create("John H", "CHF", southside.id)
    Patient.create("Amber F", "stroke", hilltop.id)
    Patient.create("Whitney L", "cardiomyopathy", hilltop.id)
    Patient.create("Lucas J", "pancreatic CA", southside.id)
    
seed_db()