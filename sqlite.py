# Importing required library
import sqlite3

# Connecting to SQlite and assigning the DB name---employee
connection=sqlite3.connect("employee.db")

# Creating a cursor object to insert record,create table or retrive result

cursor=connection.cursor()

# Creating the table
table_info="""
Create table EMPLOYEE(NAME VARCHAR(25),DEPARTMENT VARCHAR(25),
SECTION VARCHAR(25),SALARY INT);

"""
# To create the table
cursor.execute(table_info)

# Queries to Insert Some records

cursor.execute('''Insert Into EMPLOYEE values('Mohan','Data Science','A',95)''')
cursor.execute('''Insert Into EMPLOYEE values('Tanushree','Data Science','B',90)''')
cursor.execute('''Insert Into EMPLOYEE values('Raushan','Data Science','A',95)''')
cursor.execute('''Insert Into EMPLOYEE values('Sandeep','Gen AI','A',95)''')
cursor.execute('''Insert Into EMPLOYEE values('Meghana','Gen AI','B',98)''')
cursor.execute('''Insert Into EMPLOYEE values('Suman','Gen AI','A',90)''')
cursor.execute('''Insert Into EMPLOYEE values('Nagaraju','DB','B',90)''')
cursor.execute('''Insert Into EMPLOYEE values('Muru','DB','B',95)''')
cursor.execute('''Insert Into EMPLOYEE values('Anusha','DB','A',90)''')
cursor.execute('''Insert Into EMPLOYEE values('Shaik','PBI','A',95)''')
cursor.execute('''Insert Into EMPLOYEE values('Kavya','PBI','A',90)''')
cursor.execute('''Insert Into EMPLOYEE values('Karthik','PBI','B',90)''')

# Dispaly ALl the records

print("The isnerted records are")
data=cursor.execute('''Select * from EMPLOYEE''')
for row in data:
    print(row)

# Commit changes in the databse
connection.commit()
# Closing the connection 
connection.close()
