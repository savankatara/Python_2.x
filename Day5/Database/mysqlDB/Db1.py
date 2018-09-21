import mysql.connector
'''check  database table'''
mydata=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="SAVANJI"
    )
cursor=mydata.cursor()
cursor.execute("SHOW TABLES ")

for a in cursor:
    print a