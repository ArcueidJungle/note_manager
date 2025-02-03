class Book:

    def __init__(self, title, author, year, publisher, isbn):
        self.title = title
        self.author = author
        self._year = year
        self.__isbn = isbn
        self._publisher = publisher

    def info(self):
        return f'"Название: {self.title}, Автор: {self.author}, Год: {self.year}"'

    def ge_isbn(self):
        return self.__isbn

    def info(self):
        return f"Название: {self.title}, Автор: {self.author}, Год: {self.year}, Издательство: {self._publisher}, ISBN: {self.get_isbn()}"

