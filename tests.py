import pytest
from main import BooksCollector

class TestBooksCollector:


    # ПОЗИТИВНЫЕ ТЕСТЫ


    # Тест: Добавление книг с корректными названиями
    @pytest.mark.parametrize('book_name', [
        'Гарри Поттер',
        'Питер Пэн',
        'Винни-Пух',
    ])
    def test_add_new_book_valid_names(self, collector, book_name):
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre()

    # Тест: Установка жанра из допустимого списка
    @pytest.mark.parametrize('genre', [
        'Фантастика',
        'Мультфильмы',
        'Комедии'
    ])
    def test_set_book_genre_valid(self, collector, genre):
        collector.add_new_book('Книга Джунглей')
        collector.set_book_genre('Книга Джунглей', genre)
        assert collector.get_book_genre('Книга Джунглей') == genre

    # Тест: Получение жанра книги по названию
    def test_get_book_genre_returns_correct_genre(self, collector):
        collector.add_new_book('Незнайка')
        collector.set_book_genre('Незнайка', 'Комедии')
        assert collector.get_book_genre('Незнайка') == 'Комедии'

    # Тест: Получение корректного словаря после добавления книги
    def test_get_books_genre_returns_correct_dict(self, collector):
        collector.add_new_book('Чиполлино')
        result = collector.get_books_genre()
        assert result == {'Чиполлино': ''}

    # Тест: Получение книг по жанру
    def test_get_books_with_specific_genre_returns_correct_books(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Гарри Поттер']

    # Тест: Возвращаются только книги с детским жанром
    def test_get_books_for_children_includes_child_friendly(self, collector):
        collector.add_new_book('Маугли')
        collector.set_book_genre('Маугли', 'Мультфильмы')
        assert collector.get_books_for_children() == ['Маугли']

    # Тест: Получение списка избранных книг
    def test_get_list_of_favorites_books_returns_correct_list(self, collector):
        collector.add_new_book('Колобок')
        collector.add_book_in_favorites('Колобок')
        assert collector.get_list_of_favorites_books() == ['Колобок']


    # Тест: Добавление книги в избранное
    def test_add_book_in_favorites_adds_correctly(self, collector):
        collector.add_new_book('Винни-Пух')
        collector.add_book_in_favorites('Винни-Пух')
        assert collector.get_list_of_favorites_books() == ['Винни-Пух']

    # Тест: Удаление книги из избранного
    def test_delete_book_from_favorites_removes_book(self, collector):
        collector.add_new_book('Карлсон')
        collector.add_book_in_favorites('Карлсон')
        collector.delete_book_from_favorites('Карлсон')
        assert collector.get_list_of_favorites_books() == []


    # НЕГАТИВНЫЕ ТЕСТЫ


    # Тест: Повторное добавление книги в избранное не дублирует её
    def test_add_book_in_favorites_does_not_duplicate(self, collector):
        collector.add_new_book('Буратино')
        collector.add_book_in_favorites('Буратино')
        collector.add_book_in_favorites('Буратино')
        assert collector.get_list_of_favorites_books() == ['Буратино']

    # Тест: Книга с названием длиннее 40 символов не добавляется
    @pytest.mark.parametrize('long_name', [
        'x' * 41,
        'Очень длинное название книги, которое превышает сорок символов'
    ])
    def test_add_new_book_too_long_name(self, collector, long_name):
        collector.add_new_book(long_name)
        assert long_name not in collector.get_books_genre()

    # Тест: Книга с возрастным рейтингом не попадает в список для детей
    @pytest.mark.parametrize('genre', ['Ужасы', 'Детективы'])
    def test_get_books_for_children_excludes_age_restricted(self, collector, genre):
        collector.add_new_book('Страшилка')
        collector.set_book_genre('Страшилка', genre)
        assert collector.get_books_for_children() == []

