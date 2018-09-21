import mysql.connector
'''create database table'''
mydata=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="SAVANJI"
    )
cursor=mydata.cursor()
cursor.execute("CREATE TABLE student (name VARCHAR(25),address VARCHAR(25))")
print cursor