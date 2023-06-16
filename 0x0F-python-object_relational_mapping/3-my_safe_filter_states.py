#!/usr/bin/python3
"""
displays values in states table of hbtn_0e_0_usa where
name matches the argument that is safe from MySQL injections
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """open database connection"""
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    """create cursor for operating the database"""
    cursor = db.cursor()
    """execute a sql sentence"""
    cursor.execute("SELECT * FROM states WHERE name LIKE %s\
    ORDER BY id ASC", (argv[4],))
    """get record/fill cursor"""
    rows = cursor.fetchall()
    """print rows"""
    for row in rows:
        print(row)
    cursor.close()
    db.close()
