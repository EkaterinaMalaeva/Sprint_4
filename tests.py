import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2


    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_books_books_is_added(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert 'Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить' in collector.get_books_genre()

    def test_add_invalid_book_name_too_long(self):
        collector = BooksCollector()
        long_name = "А" * 100
        collector.add_new_book(long_name)
        assert long_name not in collector.get_books_genre()

    def test_set_and_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')
        assert collector.get_book_genre('Шерлок Холмс') == 'Детективы'

    def test_books_with_age_rating_not_in_children_books(self):
        collector = BooksCollector()
        collector.add_new_book('+18')
        collector.set_book_genre('+18', 'Ужасы')
        children_book = collector.get_books_for_children()
        assert '+18' not in children_book

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' not in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        favorites_books = collector.get_books_genre()
        assert 'Гордость и предубеждение и зомби' in favorites_books

    def test_add_not_existent_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Нет книги')
        favorites_books = collector.get_books_genre()
        assert 'Нет книги' not in favorites_books

    def test_add_twice_new_book(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.add_new_book('Книга')
        assert len(collector.get_books_genre()) == 1

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.set_book_genre('Книга 1', 'Ужасы')
        collector.set_book_genre('Книга 2', 'Ужасы')
        specific_genre_books = collector.get_books_with_specific_genre('Ужасы')
        assert specific_genre_books == ['Книга 1', 'Книга 2']

@pytest.mark.parametrize('name, genre',
        [
            ('Гордость и предубеждение и зомби', 'Фантастика'),
            ('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        ]
        )

def test_add_name_and_check_genre(name, genre):
    collector = BooksCollector()
    collector.add_new_book(name)
    collector.set_book_genre(name, genre)
    assert collector.get_book_genre(name) == genre
        
