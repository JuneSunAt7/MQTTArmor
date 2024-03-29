import os
import hashlib
from logger.printer import Logger


class Configure:
    def __init__(self):
        self.logger = Logger()
        if self.is_file_empty("test\\data.conf"):
            self.logger.warning("Файл пустой. Создается конфигурация")
            self.__setup_config_from_input()
        else:
            self.logger.success("Конфигурация успешно загружена")

    def is_file_empty(self, file_path):
        return os.stat(file_path).st_size == 0

    def __setup_config_from_input(self):
        self.noHashedUname = input("Имя: ")
        self.noHashedPasswd = input("Пароль: ")

        self.__save_to_config()

    def create_hash(self, input_string):
        hash_object = hashlib.md5(input_string.encode())
        return hash_object.hexdigest()

    def __save_to_config(self):
        with open("test\\data.conf", "w") as config:
            config.write("[passwd]:" + str(self.create_hash(str(self.noHashedPasswd))) + '\n')
            config.write("[uname]:" + str(self.create_hash(str(self.noHashedUname))) + '\n')