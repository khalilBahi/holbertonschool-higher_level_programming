#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Main function to connect to the MySQL server and fetch states data.
    """

    username, password, database = sys.argv[1:4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id")
    rows = cursor.fetchall()

    for row in rows:
        print(row) 
