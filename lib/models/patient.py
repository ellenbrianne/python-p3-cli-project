from models.__init__ import CURSOR, CONN
from models.facility import Facility

class Patient:
    all = {}

    def __init__(self, name, diagnosis, facility_id, id=None):
        self.name = name
        self.diagnosis = diagnosis
        self.facility_id = facility_id

    