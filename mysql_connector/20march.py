# pip install mysql-connector-python

import mysql.connector 

mydb = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="root",
    database="25_gen_python"
)

conn =mydb.cursor()

# create database :   ==> create database  database_name; 

# conn.execute("CREATE DATABASE 25_gen_python") 
# print("Database created successfully")

'''conn.execute("""
             
             CREATE TABLE IF NOT EXISTS student (
                 id INT AUTO_INCREMENT PRIMARY KEY,
                 name VARCHAR(50),
                 salary INT
             )
             """)
'''
# print("TABLE created successfully")
"""
conn.execute("INSERT INTO student (name, salary) VALUES ('moksh', 100000)")
conn.execute("INSERT INTO student (name, salary) VALUES ('pinal', 200000)")
conn.execute("INSERT INTO student (name, salary) VALUES ('dhruv', 90000)")
conn.execute("INSERT INTO student (name, salary) VALUES ('keshav', 80000)")
conn.execute("INSERT INTO student (name, salary) VALUES ('het', 10000)")

mydb.commit()
print("Data inserted successfully")"""

conn.execute("select *  from student")
rows = conn.fetchall()

for i in rows : 
    print(i)

conn.close()
mydb.close()

# update  : moksh  het  salary 
# delete  : keshav 