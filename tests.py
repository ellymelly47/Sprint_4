import pytest

from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_dupl_book_not_added(self):
        collector = BooksCollector()

        collector.add_new_book('Приключения Шерлока Холмса')
        collector.add_new_book('Приключения Шерлока Холмса')

        assert len(collector.books_genre) == 1

    @pytest.mark.parametrize('name', ['', 'Удивительное путешествие Нильса Хольгерсс'])
    def test_add_new_book_invalid_name_not_added(self, name):
        collector = BooksCollector()

        collector.add_new_book(name)

        assert name not in collector.books_genre

    def test_set_book_genre_book_in_dict_genre_added(self):
        collector = BooksCollector()

        collector.add_new_book('Приключения Шерлока Холмса')
        collector.set_book_genre('Приключения Шерлока Холмса', 'Детективы')

        assert collector.get_books_genre() == {'Приключения Шерлока Холмса': 'Детективы'}

    def test_get_book_genre_name_in_dict_genre_shown(self):
        collector = BooksCollector()

        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')

        assert collector.get_book_genre('Сияние') == 'Ужасы'

    def test_get_books_with_specific_genre_books_shown(self):
        collector = BooksCollector()

        collector.add_new_book('Приключения Шерлока Холмса')
        collector.add_new_book('Двенадцать стульев')
        collector.add_new_book('Пигмалион')
        collector.set_book_genre('Приключения Шерлока Холмса', 'Детективы')
        collector.set_book_genre('Двенадцать стульев', 'Комедии')
        collector.set_book_genre('Пигмалион', 'Комедии')

        assert collector.get_books_with_specific_genre('Комедии') == ['Двенадцать стульев', 'Пигмалион']

    def test_get_books_genre_dict_shown(self):
        collector = BooksCollector()

        collector.add_new_book('Приключения Шерлока Холмса')
        collector.add_new_book('Двенадцать стульев')
        collector.set_book_genre('Приключения Шерлока Холмса', 'Детективы')

        assert collector.get_books_genre() == {
            'Приключения Шерлока Холмса': 'Детективы',
            'Двенадцать стульев': ''
        }

    def test_get_books_for_children_books_shown(self):
        collector = BooksCollector()

        collector.add_new_book('Приключения Шерлока Холмса')
        collector.add_new_book('Пигмалион')
        collector.add_new_book('Дюна')
        collector.set_book_genre('Приключения Шерлока Холмса', 'Детективы')
        collector.set_book_genre('Пигмалион', 'Комедии')
        collector.set_book_genre('Дюна', 'Фантастика')

        assert collector.get_books_for_children() == ['Пигмалион', 'Дюна']

    def test_add_book_in_favorites_not_in_dict_book_not_added(self):
        collector = BooksCollector()

        collector.add_book_in_favorites('Маленький принц')

        assert 'Маленький принц' not in collector.favorites

    def test_delete_book_from_favorites_added_book_deleted(self):
        collector = BooksCollector()

        collector.add_new_book('Приключения Шерлока Холмса')
        collector.add_book_in_favorites('Приключения Шерлока Холмса')
        collector.delete_book_from_favorites('Приключения Шерлока Холмса')

        assert 'Приключения Шерлока Холмса' not in collector.favorites

    def test_get_list_of_favorites_books_list_shown(self):
        collector = BooksCollector()

        collector.add_new_book('Двенадцать стульев')
        collector.add_new_book('Пигмалион')
        collector.add_book_in_favorites('Двенадцать стульев')
        collector.add_book_in_favorites('Пигмалион')

        assert collector.favorites == ['Двенадцать стульев', 'Пигмалион']
