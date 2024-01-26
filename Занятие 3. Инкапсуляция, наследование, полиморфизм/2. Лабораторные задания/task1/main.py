class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author



class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    def __str__(self):
        return super().__str__()

    def __repr__(self):
        return f"{super().__repr__()},pages={self.pages})"

    def valid(self, value):
        if not isinstance(value, int):
            TypeError()

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        self.valid(value)
        # if not isinstance(value, int):
        #     TypeError()
        self._pages = value



class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    def __str__(self):
        return super().__str__()

    def __repr__(self):
        return f"{super().__repr__()},duration={self.duration})"


if __name__ == "__main__":

    book = Book("1", "23")
    print(book.__repr__())
    print(book)

    paper = PaperBook("1", "23", 231.15)
    print(paper.__repr__())
    print(paper)

    audio = AudioBook("1", "23", 231.12)
    print(audio.__repr__())
    print(audio)
