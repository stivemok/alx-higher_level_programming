#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """open database connection"""
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    """create cursor for operating the database"""
    cursor = db.cursor()
    """execute a sql sentence"""
    cursor.execute("SELECT cities.id, cities.name, states.name \
    FROM cities JOIN states ON cities.state_id = states.id\
    ORDER BY cities.id")
    """get record/fill cursor"""
    rows = cursor.fetchall()
    """print rows"""
    for row in rows:
        print(row)
    cursor.close()
    db.close()
