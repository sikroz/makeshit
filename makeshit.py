import os
import random
import string


class Color:
    OK = '\033[92m'
    ERR = '\033[91m'
    END = '\033[0m'


class MakeShit:
    def __init__(self, path, count_files=1000, total_size=200):
        """
        :param path: Путь где надо нашитеть
        :param count_files: Общее кол-во файлов
        :param total_size: Общий размер всего shit (MB)
        """

        self.path = path
        self.count_files = count_files
        self.total_size = total_size

    @staticmethod
    def generate_string(length):
        lower = string.ascii_lowercase.lower()
        return ''.join(random.choice(lower) for i in range(length))

    def generate_data(self):
        if not os.path.exists(self.path):
            print(Color.ERR + "[ERROR]" + Color.END, self.path, "not exists")
            return False

        dir_list = [
            "/src", "/src/config", "/media", "/media/css",
            "/media/js", "/media/img", "/media/img/icons", "/media/img/sprites"
        ]

        #Кол-во файлов в одной дире
        cf = int(self.count_files / len(dir_list))
        #Размер одного файла
        fs = int(self.total_size / self.count_files * 1000**2)

        for folder in dir_list:
            path = os.path.join(self.path + folder)
            try:
                os.mkdir(path)
                print(Color.OK + "[OK]" + Color.END, "Создание директории", path)
            except FileNotFoundError:
                print(Color.ERR + "[ERROR]" + Color.END, "Директория", path, "не существует")
            except PermissionError:
                print(Color.ERR + "[ERROR]" + Color.END, "Недостаточно прав на создание", path, "директории")
            except FileExistsError:
                print(Color.ERR + "[ERROR]" + Color.END, "Директория", path, "уже существует")

            for i in range(cf):
                file_name = os.path.join(path, self.generate_string(10) + "." + self.generate_string(3))
                f = open(file_name, "w")
                try:
                    f.write(self.generate_string(fs))
                    print(Color.OK + "[OK]" + Color.END, "Создание файла", file_name)
                except FileNotFoundError:
                    print(Color.ERR + "[ERROR]" + Color.END, "Файл", file_name, "не существует")
                except PermissionError:
                    print(Color.ERR + "[ERROR]" + Color.END, "Недостаточно прав на создание файла", file_name)
                except FileExistsError:
                    print(Color.ERR + "[ERROR]" + Color.END, "Файл", file_name, "уже существует")
                finally:
                    f.close()