import sqlite3

CONN = sqlite3.connect('hospice.db')
CURSOR = CONN.cursor()