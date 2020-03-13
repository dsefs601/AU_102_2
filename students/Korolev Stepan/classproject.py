import csv


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
        print(f'{self.__first_name}, {self.__last_name} was destroyed.')


def main():
    dm2020 = [Student('Stepan', 'Korolev', 'Igneaalis', 1, 'https://github.com/Igneaalis', 'Nostaleal.ru@yandex.ru')]
    save_path = r'dm2020.csv'  # путь до файла

    with open(save_path, 'w') as k:  # обычно k принимается за csvfile
        writer = csv.writer(k)
        writer.writerow(('Имя', 'Фамилия', 'Псевдоним', 'Группа', 'Github', 'E-Mail'))
        for x in dm2020:
            print('First name: {0[0]}, last name: {0[1]}, nickname: {0[2]}, '
                  'group: {0[3]}, github: {0[4]}, E-Mail: {0[5]}'.format(x.data()))
            writer.writerow(x.data())


if __name__ == '__main__':
    print('Initialized')
    main()
    print('Finished')
