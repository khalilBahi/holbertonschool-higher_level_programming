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

    db = MySQLdb.connect(
        host="localhost", user=sys.argv[1], port=3306, passwd=sys.argv[2], db=sys.argv[3])
    


    cursor = db.cursor()
    cursor.execute(
        "SELECT * \
                 FROM states \
                WHERE BINARY name = '{}'".format(sys.argv[4]))
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
