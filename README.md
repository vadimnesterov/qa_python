# BooksCollector Project  
Автотесты на Python с использованием **pytest**

Автор: Вадим Нестеров

---

## Описание
Данный проект содержит набор юнит-тестов, написанных с использованием фреймворка **pytest**.  
Цель — проверка работы класса **BooksCollector**, который управляет коллекцией книг, их жанрами, возрастными ограничениями и списком избранного.

---

## Методы класса BooksCollector
- `add_new_book`
- `set_book_genre`
- `get_book_genre`
- `get_books_with_specific_genre`
- `get_books_genre`
- `get_books_for_children`
- `add_book_in_favorites`
- `delete_book_from_favorites`
- `get_list_of_favorites_books`

---

## Позитивные тесты
- `test_add_new_book_valid_names` — добавление книг с корректными названиями  
- `test_set_book_genre_valid` — присвоение допустимого жанра ранее добавленной книге  
- `test_get_book_genre_returns_correct_genre` — получение жанра книги по названию  
- `test_get_books_with_specific_genre_returns_correct_books` — получение списка книг по жанру при наличии таких книг  
- `test_get_books_for_children_includes_child_friendly` — книги с «детским» жанром попадают в список для детей  
- `test_add_book_in_favorites_adds_correctly` — добавление книги в избранное  
- `test_delete_book_from_favorites_removes_book` — удаление книги из избранного  
- `test_get_list_of_favorites_books_returns_correct_list` — получение корректного списка избранных книг

---

## Негативные тесты
- `test_add_book_in_favorites_does_not_duplicate` — повторное добавление книги в избранное не дублирует её  
- `test_add_new_book_too_long_name` — книга с названием более 40 символов не сохраняется  
- `test_get_books_for_children_excludes_age_restricted` — книги с возрастными ограничениями не попадают в список детских

---

## Структура проекта
qa_python/
├── main.py # Класс BooksCollector
├── tests.py # Основные тесты
├── conftest.py # Фикстуры для pytest
├── README.md # Документация проекта
└── .gitignore