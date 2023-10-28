from models.__init__ import CURSOR, CONN
from models.facility import Facility

class Patient:
    all = {}

    def __init__(self, name, diagnosis, facility_id, id=None):
        self.name = name
        self.diagnosis = diagnosis
        self.facility_id = facility_id

    def __repr__(self):
        return (
            f"<Patient {self.id}: {self.name}, {self.diagnosis}, " +
            f"Facility ID: {self.facility_id}>"
        )
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Must include patient name")

    @property
    def diagnosis(self):
        return self._diagnosis

    @diagnosis.setter
    def diagnosis(self, diagnosis):
        if isinstance(diagnosis, str) and len(diagnosis):
            self._diagnosis = diagnosis
        else:
            raise ValueError("Must include diagnosis")

    @property
    def facility_id(self):
        return self._facility_id

    @facility_id.setter
    def facility_id(self, facility_id):
        if type(facility_id) is int and Facility.find_by_id(facility_id):
            self._facility_id = facility_id
        else:
            raise ValueError("facility_id must correspond with a facility in the database")
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY,
            name TEXT,
            diagnosis TEXT,
            facility_id INTEGER,
            FOREIGN KEY (facility_id) REFERENCES facilities(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS patients;
        """
        CURSOR.execute(sql)
        CONN.commit()