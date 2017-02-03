#importing modules for python
import pymysql #simple module for MySQL databases

#connecting w DB
conn = pymysql.connect(
	db='example', #database name
	user='root', #MySQL server user
	passwd='#inzynier2017', #password to user
	host='138.68.111.100') #VPS adress
c = conn.cursor() #gathering cursor

#callback definition for rising edge
check = c.execute('SELECT * FROM pomiary') #select last record from table
print([(r[1], r[2], r[3], r[4], r[5], r[6], r[7]) for r in c.fetchall()])
