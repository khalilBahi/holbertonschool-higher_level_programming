#!/usr/bin/python3
"""
Write a script that takes in an argument and displays all
values in the states table of hbtn_0e_0_usa where name matches the argument
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Main function to connect to the MySQL server and fetch states data.
    """

    username, password, state, database = sys.argv[1:5]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states \
                WHERE name LIKE BINARY '{}' \
                ORDER BY states.id ASC".format(sys.argv[4]))
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
