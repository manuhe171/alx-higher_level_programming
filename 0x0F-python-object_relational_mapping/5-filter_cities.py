#!/usr/bin/python3
'''script that takes in the name of a state as argument and lists all
"cities" of that state using the database hbtn_0e_4_usa
argumenst should be SQL injection free
code should not be executed when imported (name=main...)
'''

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name\
                FROM cities LEFT JOIN states\
                ON states.id = cities.state_id\
                WHERE states.name = %s\
                ORDER BY cities.id ASC;", (argv[4], ))
    rows = cur.fetchall()
    cityStr = ''
    for row in rows:
        if cityStr != '':
            cityStr += ', '
        cityStr += row[0]
    print(cityStr)
