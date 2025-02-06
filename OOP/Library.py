class Library:

    class Book:
        def __init__(self, title, author):
            self.__title = title
            self.__author = author

    def __init__(self,):
        self.__book_list = []

    def add_book(self, title, author):
        self.__book_list.append(self.Book(title, author))

    def __del__(self):
        self.__book_list.clear()