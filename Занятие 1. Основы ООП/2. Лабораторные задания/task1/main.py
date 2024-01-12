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
    ...

if __name__ == "__main__":

    table_1 = OfficeTable("дерево", 100, 4)
    print(table_1.material, table_1.weight, table_1.legs)

    pass
