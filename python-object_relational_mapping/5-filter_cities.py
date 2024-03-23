#!/usr/bin/python3
"""
Write a script that takes in the name of a state
as an argument and lists all cities of that state"""

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
    query = "SELECT cities.name \
            FROM states INNER JOIN cities ON states.id = cities.state_id \
            WHERE states.name = '{}'".format(state)
    cursor.execute(query)

    rows = cursor.fetchall()
    city_names = [row[0] for row in rows]
    print(', '.join(city_names))
