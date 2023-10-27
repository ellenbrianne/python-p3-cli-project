from models.__init__ import CONN, CURSOR
from models.facility import Facility

def seed_db():
    Facility.drop_table()
    Facility.create_table()

    
seed_db()