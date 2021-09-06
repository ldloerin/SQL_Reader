import os
import sqlite3
import sys
from Services.SQL_Interface.read_sql import ReadSql


class AccessDatabase():
    def __init__(self, input):
        self.root = input.root
        database_path = input.database_path
        database = input.database
        self.table_name = input.table_name
        self.database_file = os.path.join(self.root, database_path, database)
        self.connect_database()

    def connect_database(self):
        if os.path.exists(self.database_file):
            self.conn = sqlite3.connect(self.database_file)
            self.c = self.conn.cursor()
        else:
            sys.exit("\n\nError: Defined file does not exist.\n" + self.database_file + "\n\n")

    def read_all(self):
        sql_command = "SELECT * FROM " + self.table_name
        data = ["All customers"]
        data += ReadSql.read_table(self, sql_command)
        # self.__print_list(data)
        return data

    def read_german_customers(self):
        sql_command = "SELECT * FROM " + self.table_name + " "
        sql_command += "WHERE Country = 'Germany'"
        data = ["German customers"]
        data += ReadSql.read_table(self, sql_command)
        # self.__print_list(data)
        return data

    def read_german_speaking_customers(self):
        sql_command = "SELECT * FROM " + self.table_name + "\n"
        sql_command += "WHERE Country = 'Germany' OR \n"
        sql_command += "Country = 'Austria' OR \n"
        sql_command += "Country = 'Switzerland' AND City = 'Bern' \n"
        sql_command += "ORDER BY Country"
        data = ["German speaking customers"]
        data += ReadSql.read_table(self, sql_command)
        # self.__print_list(data)
        return data

    def read_french_speaking_customers(self):
        sql_command = "SELECT * FROM " + self.table_name + "\n"
        sql_command += "WHERE Country = 'France' OR \n"
        sql_command += "Country = 'Belgium' OR \n"
        sql_command += "Country = 'Switzerland' AND City = 'Genève' \n"
        sql_command += "ORDER BY Country"
        data = ["French speaking customers"]
        data += ReadSql.read_table(self, sql_command)
        # self.__print_list(data)
        return data
    
    def __print_list(self, data):
        for line in data:
            print(line)
        print("\n")
