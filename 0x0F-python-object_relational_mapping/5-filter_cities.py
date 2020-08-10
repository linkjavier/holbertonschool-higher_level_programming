#!/usr/bin/python3
"""
script that takes in arguments and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument. Safe from MySQL injections!
"""
import MySQLdb
import sys

if __name__ == "__main__":
    dbase = MySQLdb.connect(host="localhost", port=3306,
                            user=sys.argv[1],
                            passwd=sys.argv[2],
                            db=sys.argv[3])
    cursor = dbase.cursor()
    cursor.execute("SELECT cities.name \
                 FROM cities INNER JOIN states ON cities.state_id = states.id \
                 WHERE states.name=%s \
                 ORDER BY cities.id ASC", (sys.argv[4], ))
    rows = cursor.fetchall()
    print(", ".join(row[0] for row in rows))
    cursor.close()
    dbase.close()
