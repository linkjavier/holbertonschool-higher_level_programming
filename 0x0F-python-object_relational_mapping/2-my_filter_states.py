#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    dbase = MySQLdb.connect(host="localhost", port=3306,
                            user=sys.argv[1],
                            passwd=sys.argv[2],
                            db=sys.argv[3])
    cursor = dbase.cursor()
    cursor.execute("SELECT * FROM states WHERE BINARY name='{:}'\
                    ORDER BY id ASC;".format(sys.argv[4]))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    dbase.close()
