#!/usr/bin/python3
"""
Write a script that lists all cities from the database hbtn_0e_4_usa
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
    """Create a cursor object to interact with the database."""
    cursor = db.cursor()

    query = "SELECT cities.id , cities.name , states.name \
            FROM cities JOIN states ON states.id = cities.state_id \
            ORDER BY cities.id"
    cursor.execute(query)

    results = cursor.fetchall()
    for row in results:
        print(row)
