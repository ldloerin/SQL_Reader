import os
import sys
sys.path.append(os.path.split(os.path.dirname(__file__))[0])
from Services.Config.get_input import GetInput
from Services.Output.write_dockerfile import WriteDockerfile
from Services.SQL_Interface.access_database import AccessDatabase


class ReadSqlDatabase(GetInput):
    def execute_workflow(self):
        self.__main()
        self.__create_dockerfile()

    def __main(self):
        self.root = os.path.split(os.path.dirname(__file__))[0]
        sql = AccessDatabase(self)
        self.docker_output = sql.read_all()
        self.docker_output += sql.read_german_customers()
        self.docker_output += sql.read_german_speaking_customers()
        self.docker_output += sql.read_french_speaking_customers()

    def __create_dockerfile(self):
        WriteDockerfile(self)


my_code = ReadSqlDatabase(__file__)
my_code.execute_workflow()
