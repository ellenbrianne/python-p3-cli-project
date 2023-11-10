from models.__init__ import CURSOR, CONN
from models.facility import Facility

class Patient:
    all = {}

    def __init__(self, name, diagnosis, facility_id, id=None):
        self.id = id
        self.name = name
        self.diagnosis = diagnosis
        self.facility_id = facility_id

    def __str__(self):
        return (
            f"{self.name}, {self.diagnosis}"
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
            FOREIGN KEY (facility_id) REFERENCES facilities(id));
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

    def save(self):
        sql = """
                INSERT INTO patients (name, diagnosis, facility_id)
                VALUES (?, ?, ?);
        """
        CURSOR.execute(sql, (self.name, self.diagnosis, self.facility_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, diagnosis, facility_id):
        patient = cls(name, diagnosis, facility_id)
        patient.save()
        return patient

    def update(self):
        sql = """
            UPDATE patients
            SET name = ?, diagnosis = ?, facility_id = ?
            WHERE id = ?;
        """
        CURSOR.execute(sql, (self.name, self.diagnosis,
                             self.facility_id, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM patients
            WHERE id = ?;
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        patient = cls.all.get(row[0])
        if patient:
            patient.name = row[1]
            patient.diagnosis = row[2]
            patient.facility_id = row[3]
        else:
            patient = cls(row[1], row[2], row[3])
            patient.id = row[0]
            cls.all[patient.id] = patient
        return patient
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM patients;
        """
        p_table = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in p_table]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM patients
            WHERE id = ?;
        """
        p_row = CURSOR.execute(sql, (id,)).fetchone()

        return cls.instance_from_db(p_row) if p_row else None
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT * FROM patients
            WHERE name is ?;
        """
        p_row = CURSOR.execute(sql, (name,)).fetchone()

        return cls.instance_from_db(p_row) if p_row else None