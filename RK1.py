from operator import itemgetter


class Chapter:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Book:
    def __init__(self, id, name, pages, chap_id):
        self.id = id
        self.name = name
        self.pages = pages
        self.chap_id = chap_id


class ChapterBook:
    def __init__(self, chap_id, book_id):
        self.chap_id = chap_id
        self.book_id = book_id


chapters = [
    Chapter(1, "Artillery Tactics"),
    Chapter(2, "Armored Vehicles"),
    Chapter(3, "Aviation"),
    Chapter(4, "Naval Strategy"),
]

books = [
    Book(1, "Tankov", 150, 2),
    Book(2, "Guns and Glory", 200, 1),
    Book(3, "Air Combat", 180, 3),
    Book(4, "Suvorov", 120, 1),
    Book(5, "Aviation History", 220, 3),
]

chapter_books = [
    ChapterBook(1, 2),
    ChapterBook(1, 4),
    ChapterBook(2, 1),
    ChapterBook(3, 3),
    ChapterBook(3, 5),
    ChapterBook(4, 2),
]


# Задание 1
def task1():
    result = [(book.name, chapter.name)
              for book in books
              for chapter in chapters
              if book.chap_id == chapter.id and book.name.endswith("ov")]
    return result


# Задание 2
def task2():
    result = []
    for chapter in chapters:
        books_in_chapter = [book.pages for book in books if book.chap_id == chapter.id]
        if books_in_chapter:
            avg_pages = sum(books_in_chapter) / len(books_in_chapter)
            result.append((chapter.name, avg_pages))
    result.sort(key=itemgetter(1), reverse=True)
    return result


# Задание 3
def task3():
    result = []
    for chapter in chapters:
        if chapter.name.startswith("A"):
            books_in_chapter = [book.name for book in books if book.chap_id == chapter.id]
            result.append((chapter.name, books_in_chapter))
    return result


# Main function
def main():
    print("Задание 1: Список книг, название которых заканчивается на 'ов', и их главы:")
    print(task1())

    print("\nЗадание 2: Список глав со средней длиной книг в страницах, отсортированный по средней длине:")
    print(task2())

    print("\nЗадание 3: Список глав, название которых начинается с 'А', и книги, относящиеся к ним:")
    print(task3())


if __name__ == '__main__':
    main()
