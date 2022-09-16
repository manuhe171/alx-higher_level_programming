#!/usr/bin/python3
'''script that displays all values in states table where
name matches the argument from the database hbtn_0e_0_usa
code should not be executed when imported (name=main...)
'''

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name
                LIKE BINARY '{}' ORDER BY states.id ASC;"""
                .format(argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
