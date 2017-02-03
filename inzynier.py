#importing modules for python
import time #storage of time variables (year, month, seconds etc.) and sleep function
import RPi.GPIO as GPIO #default module for RPi I/O
import pymysql #simple module for MySQL databases

#callback definition for rising edge
def insert_data():
	#gathering data from time module
	year = str(time.gmtime().tm_year) #casting variables into STR for safety
	month = str(time.gmtime().tm_mon)
	day = str(time.gmtime().tm_mday)
	hour = str(time.gmtime().tm_hour)
	minute = str(time.gmtime().tm_min)
	second = str(time.gmtime().tm_sec)
	
	#inserting data
	sql_query = 'INSERT INTO pomiary (year,month,day,hour,minute,second,data) VALUES (%s,%s,%s,%s,%s,%s,%s)' #specyfying columns due to autoincrement key
	c.execute(sql_query,(year,month,day,hour,minute,second,'1'))
	conn.commit() #commiting changes
	#checking if last data has been putted corectly
	check = c.execute('SELECT * FROM pomiary WHERE id = (SELECT MAX(id) FROM pomiary)') #select last record from table
	print('Last record is:')	
	print([(r[1], r[2], r[3], r[4], r[5], r[6], r[7]) for r in c.fetchall()])

#connecting w DB
conn = pymysql.connect(
	db='example', #database name
	user='root', #MySQL server user
	passwd='#inzynier2017', #password to user
	host='138.68.111.100') #VPS adress
c = conn.cursor() #gathering cursor

#settings GPIO RPi
GPIO.setmode(GPIO.BCM) 
GPIO.setup(4,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) 

counter = 0 #setting checkout counter

while 1: #infinite loop
	time.sleep(5) #delay
	if int(GPIO.input(4)):
		print('Signal gathered. Put it into DB')		
		insert_data()
		print(20*'#')
	else:
		counter += 1 #increasing counter
		print("Signal hasn't been gathered.") 
		print("Counter checking that system is not stopped:",str(counter))
	
		

