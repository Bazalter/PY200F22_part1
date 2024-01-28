class Calculator:
    @staticmethod
    def add(a, b):  # TODO написать статические методы
        return a + b

    @staticmethod
    def mul(a, b):  # TODO написать статические методы
        return a * b


if __name__ == "__main__":
    print(Calculator.add(5, 6))  # 11
    print(Calculator.mul(5, 6))  # 30
