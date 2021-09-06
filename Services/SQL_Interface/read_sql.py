import os
import sqlite3


class ReadSql():
    def __init__(self, input):
        self.root = input.root
        database_path = input.database_path
        database = input.database
        self.table_name = input.table_name
        self.database_file = os.path.join(self.root, database_path, database)

    def execute_workflow(self):
        self.__connect_database()
        self.query_table()
        #self.__close_connection()

    def __connect_database(self):
        if os.path.exists(self.database_file):
            self.conn = sqlite3.connect(self.database_file)
            self.c = self.conn.cursor()
        else:
            raise Error("\n\nError: Defined file does not exist.\n" + self.database_file + "\n\n")

    def query_table(self):
        sql_command = "SELECT * FROM " + self.table_name
        try:
            query = self.c.execute(sql_command)
            rows = query.fetchall()
            for row in rows:
                print(row)
        except Exception as e:
            print(e)
            print('Database connection not available during test')

    def __close_connection(self):
        self.conn.close()
