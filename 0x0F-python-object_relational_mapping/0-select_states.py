#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """open database connection"""
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    """create cursor for operating the database"""
    cursor = db.cursor()
    """execute a sql sentence"""
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    """get record/fill cursor"""
    rows = cursor.fetchall()
    """print rows"""
    for row in rows:
        print(row)
    cursor.close()
    db.close()
