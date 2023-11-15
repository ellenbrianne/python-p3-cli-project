from models.__init__ import CONN, CURSOR
from models.facility import Facility
from models.patient import Patient

def reset_db():
    Facility.drop_table()
    Facility.create_table()
    Patient.drop_table()
    Patient.create_table()

reset_db()