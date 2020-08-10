#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa:

The script should take 3 arguments: mysql username,
mysql password and database name (no argument validation needed)
The script use the module MySQLdb (import MySQLdb)
The script connect to a MySQL server running on localhost at port 3306
Results are sorted in ascending order by states.id
The code does not executed when imported
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dataBase = sys.argv[3]
    dbase = MySQLdb.connect(host="localhost", port=3306,
                            user=username, passwd=password, db=dataBase)
    cursor = dbase.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    dbase.close()
