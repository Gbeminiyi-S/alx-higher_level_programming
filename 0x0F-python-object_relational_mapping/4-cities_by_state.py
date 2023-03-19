#!/usr/bin/python3
""" a script that lists all `cities` from the database `hbtn_0e_4_usa`
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT c.id, c.name, s.name FROM cities as c\
                    inner join states as s\
                    ON c.state_id = s.id")
    cities = cursor.fetchall()

    for city in cities:
        print(city)

    cursor.close()
    db.close()
