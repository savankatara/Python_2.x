import mysql.connector
mydata=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
    )
cursor=mydata.cursor()
cursor.execute("SHOW DATABASES")

for databfetch in cursor:
    print databfetch