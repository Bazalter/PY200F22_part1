
class Parent:
    public_class_attribute = 'публичный атрибут класса'
    _protective_class_attribute = 'защищенный атрибут класса'
    _private_class_attribute = 'приватный атрибут класса'

    @classmethod
    def public_class_method(cls):
        return 'Вызван публичный метод класса'

    @classmethod
    def _protected_class_method(cls):
        return 'Вызван защищенный метод класса'

    @classmethod
    def __private_class_method(cls):
        return 'Вызван приватный метод класса'

    @staticmethod
    def _public_static_method():
        return 'Вызван публичный статический метод'

    @staticmethod
    def __protected_static_method():
        return 'Вызван защищенный статический метод'

    @staticmethod
    def private_static_method():
        return 'Вызван приватный статический метод'
    def __init__(self):
        self.public_example_attribute = 'публичный атрубут экземпляра'
        self._protective_example_attribute = 'защищенный атрубут экземпляра'
        self.__private_example_attribute = 'приватный атрубут экземпляра'

    def public_method(self):
        return 'Вызван публичный метод экземпляра'

    def _protected_method(self):
        return 'Вызван защищенный метод экземпляра'

    def __private_method(self):
        return 'Вызван приватный метод экземпляра'


class Child(Parent):
    ...










if __name__ == "__main__":
    parents = Parent()
    print(parents.public_method())
    child = Child()
    print(child._protective_example_attribute)


