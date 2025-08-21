import pytest
from main import BooksCollector

# Возвращает новый экземпляр BooksCollector для каждого теста
@pytest.fixture
def collector():
    return BooksCollector()

