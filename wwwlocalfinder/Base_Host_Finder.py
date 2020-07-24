import os

class Base_Host_Finder:

    def set_os_name(self, os_name: str):
        self.os_name = os_name
        return self


    def get_www_path(self):

        if self.os_name == 'posix':
            return os.sep + os.path.join('var', 'www', 'html')

        raise Exception("I don't know this 'os name': " + self.os_name)
