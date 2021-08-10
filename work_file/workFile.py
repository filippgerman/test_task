import csv
import os

class WorkFile():
    '''
    Класс представляет основные методы по  работе с файлом 
    '''
    def __init__(self, file_name, path_to_file, fieldnames):
        self.file_name = file_name
        self.path_to_file = path_to_file
        self.fieldnames = fieldnames
        self.check_file()

        
    def check_file(self):
        '''
        Проверяет наличие файла в папке,
        если его нет, то вызывает метод
        create_file
        '''
        if self.file_name not in os.listdir(self.path_to_file):
            self.create_file()
            
    def create_file(self):
        '''
        Создает файл с именем file_name и столбцами FIELDNAMES
        '''
        with open(self.file_name, 'x', newline='') as File:
            fieldnames = self.fieldnames
            writer = csv.DictWriter(File, fieldnames=fieldnames)
            writer.writeheader()

    def writing_file(self, data):
        '''
        Записывает data в файл
        '''
        with open(self.file_name, 'a', newline='') as File:
            writer = csv.writer(File)
            writer.writerows(data)

    @staticmethod
    def get_last_index(file_name):
        '''
        Возвращает последний id
        '''
        try:
            with open(file_name,'r') as File:
                reader = csv.DictReader(File)
                index = 0
                for row in reader:
                    index_row = int(row['ID пользователя'])
                    if index < index_row:
                        index = index_row
                return index
        except FileNotFoundError:
            return 1
