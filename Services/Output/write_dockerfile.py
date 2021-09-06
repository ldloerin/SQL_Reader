import codecs
import os


class WriteDockerfile():
    def __init__(self, input):
        self.dockerfile = os.path.join(input.root, 'Docker', 'dockerfile')
        self.docker_output = input.docker_output
        self.__build_content()
        self.__write_file()

    def __build_content(self):
        self.output_content = "FROM ubuntu\n\n"
        self.output_content += "RUN apt-get update\n\n"
        for line in self.docker_output:
            self.output_content += 'CMD ["echo", "' + line + '"]\n'

    def __write_file(self):
        f = codecs.open(self.dockerfile, "w", "utf-8")
        f.write(self.output_content)
        f.close()
