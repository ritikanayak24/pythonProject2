import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root", password="")

if mydb:
    print("connection created succesfully")
else:
    print("connection failed")