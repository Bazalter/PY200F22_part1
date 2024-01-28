class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

        self.is_valid_date(self.day, self.month, self.year)

    @classmethod
    def is_leap_year(cls, year: int):
        """Проверяет, является ли год високосным"""
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:  # TODO реализовать метод
            return cls.DAY_OF_MONTH[1]
        else:
            return cls.DAY_OF_MONTH[0]



    def get_max_day(self, month: int, year: int):
        """Возвращает максимальное количество дней в месяце для указанного года"""
        # TODO используя атрибут класса DAY_OF_MONTH вернуть количество дней в запрашиваемом месяце и году
        return self.is_leap_year(year)[month-1]

    def is_valid_date(self, day: int, month: int, year: int):
        """Проверяет, является ли дата корректной"""
        if month > 12:
            raise ValueError("Введите корректный месяц")# TODO проверить валидность даты
        if day > 31:
            raise ValueError("Введите корректное число")
        if not isinstance(year, int):
            raise ValueError("Введите корректный год")


date = Date(31, 2, 2012)
date1 = date.is_leap_year(2012)
date2 = date.get_max_day(2, 2019)
print(date1)
