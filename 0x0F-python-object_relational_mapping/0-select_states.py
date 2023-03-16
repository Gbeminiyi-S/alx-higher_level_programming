#!/usr/bin/python3
import MySQLdb
db = MySQLdb.connect(host="localhost", user="root", passwd="",
                     db="hbtn_0e_0_usa")
cursor = db.cursor()
cursor.execute("SELECT id, name FROM states")
for state in cursor:
    print(f"({state[0]}, '{state[1]}')")
