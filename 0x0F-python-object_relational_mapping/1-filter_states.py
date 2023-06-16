#!/usr/bin/python3
"""lists all states with a name starting with N from hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """open database connection"""
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    """create cursor for operating the database"""
    cursor = db.cursor()
    """execute a sql sentence to list names starting with N"""
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    """get record/fill cursor"""
    rows = cursor.fetchall()
    """print rows"""
    for row in rows:
        """if row [1][0] == 'N':"""
        print(row)
    cursor.close()
    db.close()
