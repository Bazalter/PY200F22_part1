from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Неправильный тип данных")
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Неправильный тип данных")
        if capacity_volume <= 0 or occupied_volume <= 0:
            raise ValueError("Невозможна отрицательная величина")

        if capacity_volume < occupied_volume:
            raise TypeError("Вместимость меньше желаемого заполнения")

        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume


if __name__ == "__main__":
    glass_1 = Glass(200, 100)
    glass_2 = Glass(50, 50)
    print(glass_1)

    # TODO попробовать инициализировать не корректные объекты
