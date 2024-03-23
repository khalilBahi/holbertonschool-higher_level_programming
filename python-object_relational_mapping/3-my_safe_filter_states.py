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

    username, password, database, state = sys.argv[1:5]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    """Create a cursor object to interact with the database."""
    cursor = db.cursor()

    query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id"
    cursor.execute(query, (state,))

    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    db.close()
