from typing import Union
import doctest
class OfficeTable:
    def __init__(self, material: str, weight: Union[int, float], legs: int):
        """
        Выдает характеристики стола
        :param material: материал сделан стол
        :param weight: вес стола
        :param legs: количество ножек стола
        """
        if not isinstance(material, str):
            raise TypeError("Введите материал стола")
        self.material = material
        if not isinstance(weight, (int, float)):
            raise TypeError("Введите вес стола в килограммах")
        self.weight = weight
        if not isinstance(legs, (int, float)):
            raise TypeError("Введите количество ножек стола")
        self.legs = legs

    def type_of_table(self) -> str:

        if self.material != "дерево" or self.material != "металл":
            raise ValueError("Выберете подходящий материал")
        ...
    def weight_office_table(self) -> str:
        """
        Проверяет является ли стол офисным по весу (не более 150 кг)
        :param weight: вес стола
        :return Возвращает является ли стол офисным
        """
        ...
    def count_legs_of_table(self) -> str:
        """
        Проверяет является ли стол офисным по количеству ножек (2 или 4)
        :param legs: количество ножек стола
        :return Возвращает является ли стол офисным
        """
        ...
class ReadBook:
    def __init__(self, quantity_of_pages: int, current_page: int):
        """
        Выдает характеристики стола
        :param quantity_of_pages: количество страниц
        :param current_page: текущая страница
        """
        if not isinstance(quantity_of_pages, int):
            raise TypeError("Введите количество страниц в книге или целое количество страниц")
        if quantity_of_pages <= 0:
            raise ValueError("Колиичетсво страниц в книге должно быть положительным")
        self.quantity_of_pages = quantity_of_pages
        if not isinstance(current_page, int):
            raise TypeError("Введите текущую страницу или целое количество прочитанных страниц")
        if quantity_of_pages <= 0:
            raise ValueError("Колиичетсво прочитанных страниц должно быть положительным")
        self.current_page = current_page


    def current_page_of_boor(self):
        """
            Выдает характеристики стола
            :param quantity_of_pages: количество страниц
            :param current_page: текущая страница
            :raise ValueError: Если количество прочитанных страниц, превышает, количество страниц
            в книге
            :return Возвращает количество прочитанных страниц из книги
            """
        if self.current_page > self.quantity_of_pages:
            raise ValueError("Количество прочитанных страниц, не может быть больше страниц в книге")
        ...

    def percernt_of_compelte(self):
        """
        Выдает процент прочитанных страниц
        :param quantity_of_pages: количество страниц
        :param current_page: текущая страница
        :raise ValueError: Если количество прочитанных страниц, превышает, количество страниц
        в книге
        :return Возвращает процент прочитанных страниц в книге
        """
        if self.current_page > self.quantity_of_pages:
            raise ValueError("Количество прочитанных страниц, не может быть больше страниц в книге")
        ...

class MainInformationOfIdPage:
    def __init__(self, name: str, surname: str, age: int, id_: int):
        """
        Выдает основную информацию о владельце страницы
        :param name: Имя владельца
        :param surname: Фамилия владельца
        :param age: Возраст владельца
        :param id_: Номер страницы
        """
        if not isinstance(name, str):
            raise TypeError("Введите имя владельца страницы")
        self.name = name
        if not isinstance(surname, str):
            raise TypeError("Введите имя владельца страницы")
        self.surname = surname
        if not isinstance(age, int):
            raise TypeError("Введите полное количество лет")
        self.age = age
        if not isinstance(id_, int):
            raise TypeError("Введите id страницы")
        self.id_ = id_

    def name_surname_person(self):
        """
        Выдает имя-фамилию владельца страницы
        :param name: Имя владельца
        :param surname: Фамилия владельца
        :return Возвращает имя-фамилию владельца страницы
        """
    def age_person(self):
        """
        Выдает возраст владельца страницы
        :param age: Возраст владельца
        :raise ValueError: Отрицательный возраст
        :return Возвращает возраст владельца страницы
        """
        if self.age < 0:
            raise ValueError("Отрицательный возраст")
        ...
    def id_person(self):
        """
        Выдает номер страницы владельца
        :param id_: id страницы владельца
        :raise ValueError: Невозвожный id страницы
        :return Возвращает номер страницы владельца
        """
        if len(self.id_) < 7 and self.id_ < 0:
            raise ValueError("Невозвожный id страницы")
        ...

if __name__ == "__main__":

    table_1 = OfficeTable("дерево", 100, 4)
    print(table_1.material, table_1.weight, table_1.legs)
    book_1 = ReadBook(200, 100)
    print(book_1.quantity_of_pages, book_1.current_page)
    print(book_1)
    person_1 = MainInformationOfIdPage("Имя", "Фамилия", 24, 123456789)
    print(person_1.name, person_1.surname, person_1.age, person_1.id_)

    pass
