Проект: BooksCollector — Автотесты на Python в спринте Юнит-тестирования.
Автор: Вадим Нестеров

Данный проект содержит набор юнит-тестов, написанных с использованием фреймворка pytest.
Цель - проверка работы класса BooksCollector, который управляет коллекцией книг, их жанрами, возрастными ограничениями и списком избранного.

Протестированы 9 методов класса BooksCollector:

add_new_book
set_book_genre
get_book_genre
get_books_with_specific_genre
get_books_genre
get_books_for_children
add_book_in_favorites
delete_book_from_favorites
get_list_of_favorites_books

Позитивные тесты:
test_add_new_book_valid_names — Добавление книг с корректными названиями — каждая книга сохраняется в словарь
test_set_book_genre_valid — Присвоение допустимого жанра ранее добавленной книге
test_get_book_genre_returns_correct_genre — Получение жанра книги по названию
test_get_books_with_specific_genre_returns_correct_books — Получение списка книг по жанру при наличии таких книг
test_get_books_for_children_includes_child_friendly — Книга с 'детским' жанром отображается в списке get_books_for_children
test_add_book_in_favorites_adds_correctly — Добавление книги в избранное
test_delete_book_from_favorites_removes_book — Удаление книги из избранного

Негативные тесты:
test_add_book_in_favorites_does_not_duplicate — Повторное добавление книги в избранное не дублирует её
test_add_new_book_too_long_name — Книга с названием длиной более 40 символов не сохраняется
test_get_books_for_children_excludes_age_restricted — Книги с возрастными ограничениями не попадают в список детских


Структура файлов проекта:

qa_python/
├── main.py # Исходный код приложения: класс BooksCollector
├── tests.py # Основной файл с тестами
├── conftest.py # Файл с фикстурой для тестов
└── README.md 
