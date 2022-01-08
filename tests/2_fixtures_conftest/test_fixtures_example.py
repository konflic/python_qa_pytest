import pytest
from src.Account import Account


# Уровень поиска фикстур в файлах conftest
# В файле теста > в ближайшем conftest


@pytest.fixture
def activated_account():
    return Account("Test", 100, True)


def test_one(activated_account):
    pass


def test_two(empty_account):
    pass


class TestFunction:
    def test_from_test_class_one(self, activated_account):
        pass

    def test_from_test_class_two(self, empty_account):
        pass
