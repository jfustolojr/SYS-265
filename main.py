import matplotlib.pyplot as plt
import pandas as pd
import mysql.connector as mysql
from scipy import signal

mydb = mysql.connect(
        host="mysql",
        user="root",
        password="Un0M@ssy123",
        database="docker_project",
        auth_plugin='mysql_native_password'
)

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


if __name__ == "__main__":
        print("Creating table...")
        create_table()
        print("Table created!")

        print("Populating data")
        insert_data()
