import sqlite3

from mysql.connector import cursor
db = sqlite3.connect("appp.db")
cursor = db.cursor()
cursor.execute('select * from CongeRecupere;')
result = cursor.fetchall()
for i in result:
    print(i)
db.close()