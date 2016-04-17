#!/usr/bin/python

import sqlite3 as sqlite

def getColumnList(database, table, column):
	
	conn = None
	columnList = []

	try:
		conn = sqlite.connect(database)
		cur = conn.cursor()

		query = "SELECT %s FROM %s"
		cur.execute(query)

		recievedList = cur.fetchall()

		for x in recievedList:
			columnList.append(str(x[0]))

	except sqlite.Error, e:
        print "Error %s:" % e.args[0]
        sys.exit(1)
    finally:
        if conn:
            conn.close()
            return columnList