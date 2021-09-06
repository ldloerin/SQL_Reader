import os
import sys
sys.path.append(os.path.split(os.path.dirname(__file__))[0])
from Services.Config.get_input import GetInput
from Services.Output.write_dockerfile import WriteDockerfile
from Services.SQL_Interface.read_sql import ReadSql


class ReadSqlDatabase(GetInput):
    def execute_workflow(self):
        self.__main()
        #self.__create_dockerfile()

    def __main(self):
        self.root = os.path.split(os.path.dirname(__file__))[0]
        sql = ReadSql(self)
        sql.execute_workflow()
        #self.sql_command_list = sql.sql_command_list

    def __create_dockerfile(self):
        self.root_path = os.path.dirname(self.code_path)
        WriteDockerfile(self)


my_code = ReadSqlDatabase(__file__)
my_code.execute_workflow()
