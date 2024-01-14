# TODO class Date
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __repr__(self):
        return f"Data({self.day}, {self.month}, {self.year})"

    def __str__(self):
        return f"{self.day:02}/{self.month:02}/{self.year}"

if __name__ == "__main__":
    data_1 = Date(3, 3, 2021)
    print(data_1)
