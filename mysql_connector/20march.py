# pip install mysql-connector-python

import mysql.connector 

mydb = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="root"
)

conn =mydb.cursor()

# create database :   ==> create database  database_name; 

conn.execute("CREATE DATABASE 25_gen_python") 
print("Database created successfully")

conn.close()
mydb.close()