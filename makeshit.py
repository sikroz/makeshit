#!/usr/bin/env python3
import os
import random
import string

class Color:
    OK = '\033[92m'
    ERR = '\033[91m'
    WARNING = '\e[0;35m'
    END = '\033[0m'

class MakeShit:
    def __init__(self, path, count_files, total_size):
        """
        :param path: Path for make shit
        :param count_files: Count of files
        :param total_size: Size оf shit (MB)
        """

        self.path = path
        self.count_files = count_files
        self.total_size = total_size

    @staticmethod
    def generate_string(length):
        return ('%0' + str(length) + 'x') % random.randrange(16**length)

    def generate_data(self):
        if os.path.exists(self.path):
             os.removedirs(self.path)
        os.makedirs(self.path)

        dir_list = [
            "/src", "/src/config", "/media", "/media/css",
            "/media/js", "/media/img", "/media/img/icons", "/media/img/sprites"
        ]

        #Count of files in directory
        cf = int(self.count_files / len(dir_list))
        #File size
        fs = int(self.total_size * 2**20 / self.count_files)

        for folder in dir_list:
            path = os.path.normpath(self.path + folder)
            try:
                os.mkdir(path)
                print(Color.OK + "[OK]" + Color.END, "Create directory", path)
            except FileNotFoundError:
                print(Color.ERR + "[ERROR]" + Color.END, "Directory", path, "not exists")
            except PermissionError:
                print(Color.ERR + "[ERROR]" + Color.END, "Permission denied", path, "to create directory")
            except FileExistsError:
                print(Color.WARNING + "[WARNING]" + Color.END, "Directory", path, "exists")

            for i in range(cf):
                file_name = os.path.join(path, self.generate_string(10) + "." + self.generate_string(3))
                f = open(file_name, "w")
                try:
                    f.write(self.generate_string(fs))
                    print(Color.OK + "[OK]" + Color.END, "Create file", file_name)
                except FileNotFoundError:
                    print(Color.ERR + "[ERROR]" + Color.END, "File", file_name, "not exists")
                except PermissionError:
                    print(Color.ERR + "[ERROR]" + Color.END, "Permission denied to create file", file_name)
                except FileExistsError:
                    print(Color.WARNING + "[WARNING]" + Color.END, "File", file_name, "exists")
                finally:
                    f.close()
