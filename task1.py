class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f'Книга "{self._name}". Автор - {self._author}'

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"
    @property
    def     name(self) -> str:
        """ Возвращение названия книги. """
        return self._name

    @property
    def author(self) -> str:
        """ Возвращение автора книги. """
        return self._author

class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    def __str__(self):
        return f"{super().__str__()}.  Количество страниц - {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.pages!r})"

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, pages: int) -> None:
        if not isinstance(pages, int):
            raise TypeError
        if pages <= 0:
            raise ValueError
        self._pages = pages


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    def __str__(self):
        return f"{super().__str__()}.  Длительность - {self._duration!r} ч."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self._duration!r})"

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, duration: float) -> None:
        if not isinstance(duration, float):
            raise TypeError
        if duration <= 0:
            raise TypeError
        self._duration = duration


print(abook1 := AudioBook('Cказки', 'Пушкин', 33.2))
abook1.duration = 12.3
### abook1.name = "другая сказка" - проверка недоступности изменения атрибута вне класса
print(abook1)
