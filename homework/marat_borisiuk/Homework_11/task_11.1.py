class Book:
    page_material = 'бумага'
    text_presence = True

    def __init__(self, book_title, author, numbers_of_pages, isbn, reserved):
        self.book_title = book_title
        self.author = author
        self.numbers_of_pages = numbers_of_pages
        self.isbn = isbn
        self.reserved = reserved

    def book_print(self):
        if self.reserved:
            print(f'Название: {self.book_title}, Автор: {self.author}, страниц: '
                  f'{self.numbers_of_pages}, материал: {self.page_material}, зарезервирована')
        else:
            print(f'Название: {self.book_title}, Автор: {self.author}, страниц: '
                  f'{self.numbers_of_pages}, материал: {self.page_material}')


book_1 = Book('First', 'Пушкин', 100, 111111, False)
book_2 = Book('Second', 'Пелевин', 200, 222222, False)
book_3 = Book('Third', 'Достоевский', 300, 333333, True)
book_4 = Book('Fourth', 'Лермонтов', 400, 444444, False)
book_5 = Book('Fifth', 'Никонов', 500, 555555, False)

book_1.book_print()
book_2.book_print()
book_3.book_print()
book_4.book_print()
book_5.book_print()


class SchoolBooks(Book):
    def __init__(self, book_title, author, numbers_of_pages, isbn, reserved, subject, group, task):
        super().__init__(book_title, author, numbers_of_pages, isbn, reserved)
        self.subject = subject
        self.group = group
        self.task = task

    def school_books_print(self):
        if self.reserved:
            print(f'Название: {self.book_title}, Автор: {self.author}, страниц: {self.numbers_of_pages}, '
                  f'предмет: {self.subject}, класс: {self.group}, зарезервирована')
        else:
            print(f'Название: {self.book_title}, Автор: {self.author}, страниц: {self.numbers_of_pages}, '
                  f'предмет: {self.subject}, класс: {self.group}')


book_6 = SchoolBooks('Алгебра', 'Иванов', '323',
                     123123, True, 'Математика', '10', True)
book_7 = SchoolBooks('Геометрия', 'Неиванов', '420',
                     123124, False, 'Геометрия', '3', False)
book_8 = SchoolBooks('Физика', 'Петров', '350',
                     123125, False, 'Физика', '11', True)

book_6.school_books_print()
book_7.school_books_print()
book_8.school_books_print()
