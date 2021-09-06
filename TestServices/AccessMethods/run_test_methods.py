import os
import sys
file_path = os.path.split(os.path.dirname(__file__))[0]
sys.path.append(os.path.split(file_path)[0])
from Services.SQL_Interface.access_database import AccessDatabase


class RunTestMethods():
    def __init__(self, input):
        self.database = input.database
        self.database_path = input.database_path
        self.table_name = input.table_name
        self.root = input.root
        self.sql = AccessDatabase(self)
    
    def read_all(self):
        list = self.sql.read_all()
        return list
    
    def read_german_customers(self):
        list = self.sql.read_german_customers()
        return list
    
    def read_german_speaking_customers(self):
        list = self.sql.read_german_speaking_customers()
        return list
    
    def read_french_speaking_customers(self):
        list = self.sql.read_french_speaking_customers()
        return list
