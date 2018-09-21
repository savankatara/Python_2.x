import mysql.connector
mydata=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
    )
cursor=mydata.cursor()
cursor.execute("CREATE DATABASE SAVANJI")
print "database succesfully created",cursor