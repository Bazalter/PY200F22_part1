# TODO Добавить методы add_water и remove_water
from typing import Union
class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        self.capacity_volume = None
        self.init_capacity_volume(capacity_volume)
        self.occupied_volume = None
        self.init_occupied_volume(occupied_volume)

    def init_capacity_volume(self, capacity_volume):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        if not capacity_volume > 0:
            raise ValueError
        self.capacity_volume = capacity_volume

    def init_occupied_volume(self, occupied_volume):
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if not occupied_volume > 0:
            raise ValueError
        self.occupied_volume = occupied_volume

    def add_water(self, add_water):
        if add_water + self.occupied_volume > self.capacity_volume:
            raise ValueError("Больше, чем возможно")
        if not isinstance(add_water, (int, float)):
            raise TypeError("Введите число")
        self.occupied_volume = self.occupied_volume + add_water
    def remove_water(self, remove_water):
        if remove_water > self.occupied_volume:
            raise ValueError("Больше, чем возможно")
        if not isinstance(remove_water, (int, float)):
            raise TypeError("Введите число")
        self.occupied_volume = self.occupied_volume - remove_water

if __name__ == "__main__":
    glass = Glass(200, 100)  # экземпляр класса
    print(glass.capacity_volume, glass.occupied_volume)
    glass.remove_water(50)
    print(glass.capacity_volume, glass.occupied_volume)
    glass.add_water(100)
    print(glass.capacity_volume, glass.occupied_volume)