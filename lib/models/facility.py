from models.__init__ import CURSOR, CONN

class Facility:
    all = {}

    def __init__(self, name, location, id=None):
        self.id = id
        self.name = name
        self.location = location

    def __repr__(self):
        return f"<Facility {self.id}: {self.name} in {self.location}>"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else: 
            raise ValueError("Must include facility name")
        
    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self, location):
        if isinstance(location, str) and len(location):
            self._location = location
        else:
            raise ValueError("Must include facility location")
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS facilities(
            id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT);
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS facilities;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO facilities (name, location)
            VALUES (?, ?);
        """
        CURSOR.execute(sql, (self.name, self.location))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, location):
        facility = cls(name, location)
        facility.save()
        return facility
    
    def update(self):
        sql = """
            UPDATE facilities
            SET name = ?, location = ?
            WHERE id = ?;
        """
        CURSOR.execute(sql, (self.name, self.location, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM facilities
            WHERE id = ?;
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        facility = cls.all.get(row[0])
        if facility:
            facility.name = row[1]
            facility.location = row[2]
        else:
            facility = cls(row[1], row[2])
            facility.id = row[0]
            cls.all[facility.id] = facility
        return facility
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM facilities;
        """
        f_table = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in f_table]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM facilities
            WHERE id = ?;
        """
        f_row = CURSOR.execute(sql, (id,)).fetchone()

        return cls.instance_from_db(f_row) if f_row else None
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT * FROM facilities
            WHERE name is ?;
        """
        f_row = CURSOR.execute(sql, (name,)).fetchone()

        return cls.instance_from_db(f_row) if f_row else None
  
    def find_patients(self):
        from models.patient import Patient
        sql = """
            SELECT * FROM patients
            WHERE facility_id = ?
        """
        CURSOR.execute(sql, (self.id,),)
        patients = CURSOR.fetchall()
        return [Patient.instance_from_db(p) for p in patients]