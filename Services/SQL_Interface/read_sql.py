class ReadSql():
    def read_table(self, sql_command):
        query = self.c.execute(sql_command)
        self.data = query.fetchall()
        ReadSql.__convert_to_string(self)
        return self.data

    def __convert_to_string(self):
        for i in range(0, len(self.data)):
            self.data[i] = str(self.data[i])[1:-1]
            self.data[i] = self.data[i].replace("'", "")
            self.data[i] = self.data[i].replace(", ", ",")
