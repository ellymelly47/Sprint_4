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

        collector.books_genre['Сияние'] = 'Ужасы'

        assert collector.get_book_genre('Сияние') == 'Ужасы'

    def test_get_books_with_specific_genre_books_shown(self):
        collector = BooksCollector()

        collector.books_genre['Приключения Шерлока Холмса'] = 'Детективы'
        collector.books_genre['Сияние'] = 'Ужасы'
        collector.books_genre['Двенадцать стульев'] = 'Комедии'
        collector.books_genre['Пигмалион'] = 'Комедии'

        assert collector.get_books_with_specific_genre('Комедии') == ['Двенадцать стульев', 'Пигмалион']

    def test_get_books_genre_dict_shown(self):
        collector = BooksCollector()

        collector.books_genre['Приключения Шерлока Холмса'] = 'Детективы'
        collector.books_genre['Сияние'] = 'Ужасы'
        collector.books_genre['Двенадцать стульев'] = 'Комедии'

        assert collector.get_books_genre() == {
            'Приключения Шерлока Холмса': 'Детективы',
            'Сияние': 'Ужасы',
            'Двенадцать стульев': 'Комедии'
        }

    def test_get_books_for_children_books_shown(self):
        collector = BooksCollector()

        collector.books_genre['Приключения Шерлока Холмса'] = 'Детективы'
        collector.books_genre['Сияние'] = 'Ужасы'
        collector.books_genre['Двенадцать стульев'] = 'Комедии'
        collector.books_genre['Пигмалион'] = 'Комедии'
        collector.books_genre['Дюна'] = 'Фантастика'

        assert collector.get_books_for_children() == ['Двенадцать стульев', 'Пигмалион', 'Дюна']

    def test_add_book_in_favorites_not_in_dict_book_not_added(self):
        collector = BooksCollector()

        collector.add_book_in_favorites('Маленький принц')

        assert 'Маленький принц' not in collector.favorites

    def test_delete_book_from_favorites_added_book_deleted(self):
        collector = BooksCollector()

        collector.books_genre['Приключения Шерлока Холмса'] = 'Детективы'
        collector.add_book_in_favorites('Приключения Шерлока Холмса')
        collector.delete_book_from_favorites('Приключения Шерлока Холмса')

        assert 'Приключения Шерлока Холмса' not in collector.favorites

    def test_get_list_of_favorites_books_list_shown(self):
        collector = BooksCollector()

        collector.books_genre['Двенадцать стульев'] = 'Комедии'
        collector.books_genre['Пигмалион'] = 'Комедии'
        collector.add_book_in_favorites('Двенадцать стульев')
        collector.add_book_in_favorites('Пигмалион')

        assert collector.favorites == ['Двенадцать стульев', 'Пигмалион']
