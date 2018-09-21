import mysql.connector
mydata=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="SAVANJI"
    )
print mydata
