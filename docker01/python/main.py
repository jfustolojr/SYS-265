import matplotlib.pyplot as plt
import pandas as pd
import mysql.connector as mysql
import time
from scipy import signal

mydb = None

def connect_test():
	i = 0
	global mydb

	while True:

		try:
				mydb = mysql.connect(
					host="mysql",
					user="joe",
					password="<insert_pass>",
					database="docker_project",
					auth_plugin='mysql_native_password'
				)
				break
		except mysql.Error as err:
			print(err)
			i += 1
			if (i >= 10):
				print("Failed")
				break
			time.sleep(5)
			print("Sleeping")
			continue
		break

def create_table():
	mycursor = mydb.cursor()

	mycursor.execute("CREATE TABLE sample_table (name VARCHAR(255), city VARCHAR(255), state VARCHAR(255))")

def insert_data():
	mycursor = mydb.cursor()

	sql = "INSERT INTO sample_table (name, city, state) VALUES (%s, %s, %s)"
	val1 = ("Nico", "Burlington", "VT")
	val2 = ("Joe", "Boston", "MA")

	mycursor.execute(sql, val1)
	mycursor.execute(sql, val2)

	mydb.commit()

	print(mycursor.rowcount, "was inserted.")

	mycursor.execute("SELECT * FROM sample_table")

	myresult = mycursor.fetchall()

	for x in myresult:
		print(x)

	mycursor.close()


if __name__ == "__main__":
	connect_test()
	print("Creating table...")
	create_table()
	print("Table created!")

	print("Populating data")
	insert_data()
	mydb.close()
