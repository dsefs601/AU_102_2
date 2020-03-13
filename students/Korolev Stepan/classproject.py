import csv
import sys
import threading
import time
import os

dm2020 = []


class Student:
    """Описание класса Student"""

    def __init__(self, first_name: str, last_name: str, nickname: str, group: int, github: str, email: str):
        self.__first_name = first_name
        self.__last_name = last_name
        self.nickname = nickname
        self.group = group
        self.github = github
        self.email = email

    def data(self):
        return self.__first_name, self.__last_name, self.nickname, str(self.group), self.github, self.email

    def __del__(self):
        """Все варианты допускаются"""
        print('{} {} was destroyed.'.format(self.__first_name, self.__last_name))
        # print('%s %s was destroyed.' % (self.__first_name, self.__last_name))
        # print(f'{self.__first_name}, {self.__last_name} was destroyed.')


def read():
    """Возобновляет список студентов из csv файла"""
    read_path = r'dm2020.csv'
    if len(sys.argv) > 1:
        read_path = r'' + sys.argv[1]  # путь до файла
    with open(read_path) as k:  # обычно k принимается за f_obj
        reader = csv.DictReader(k, delimiter=',')
        for x in reader:
            dm2020.append(Student(x['Имя'], x['Фамилия'], x['Псевдоним'], x['Группа'], x['Github'], x['E-Mail']))


def delete(student):
    """Корректное удаление студента из списка"""
    dm2020.remove(student)
    student.__del__()


def save():
    """Сохраняет список студентов в виде csv файла"""
    save_path = r'dm2020.csv'
    if len(sys.argv) > 1:
        save_path = r'' + sys.argv[1]  # путь до файла
    while True:
        with open(save_path, 'w') as k:  # обычно k принимается за csvfile
            writer = csv.writer(k)
            writer.writerow(('Имя', 'Фамилия', 'Псевдоним', 'Группа', 'Github', 'E-Mail'))
            for x in dm2020:
                writer.writerow(x.data())
            k.close()
            time.sleep(2)


def main():
    read()
    # tmp = dm2020.copy()
    # for x in tmp:
    #     delete(x)
    # dm2020.append(Student('Stepan', 'Korolev', 'Igneaalis',
    #                      1, 'https://github.com/Igneaalis', 'Nostaleal.ru@yandex.ru'))

    t = threading.Thread(target=save)  # Демонстрация работы потоков
    t.start()
    time.sleep(0.5)
    while True:
        os.system('cls')  # Команда очистки консоли
        for x in dm2020:
            print('First name: {0[0]}, last name: {0[1]}, nickname: {0[2]}, '
                  'group: {0[3]}, github: {0[4]}, E-Mail: {0[5]}'.format(x.data()))
        dm2020.append(Student(input('First name: '), input('Last name: '), input('Nickname: '),
                              int(input('Group: ')), input('github: '), input('E-Mail: ')))


if __name__ == '__main__':
    print('Initialized')
    main()
    print('Finished')
