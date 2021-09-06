import os
import sqlite3

database = r"C:/Users/david/Documents/GitHub/SQL_Reader/Database/Customers2.db"

#if os.path.isfile(database):
#    os.remove(database)


conn = sqlite3.connect(database)
c = conn.cursor()

def build(conn, c):
    sql_command = "CREATE TABLE Customers (CustomerID, CustomerName, ContactName)"
    c.execute(sql_command)
    sql_command = "INSERT INTO Customers VALUES ('1', 'Firma 1', 'Person 1')"
    c.execute(sql_command)
    sql_command = "INSERT INTO Customers VALUES ('2', 'Firma 2', 'Person 2')"
    c.execute(sql_command)
    conn.commit()

def read(conn, c):
    sql_command = "SELECT * FROM Customers"
    x = c.execute(sql_command)
    rows = x.fetchall()
    print(rows)
    conn.commit()


#conn.close()

#build(conn, c)
read(conn, c)
