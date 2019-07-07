import pytest


# Уровень поиска фикстур в файлах conftest
# В файле теста > в ближайшем conftest

@pytest.fixture
def first_fixture():
    print("\nPrint from 'first_fixture'")


def test_one(first_fixture):
    pass


class TestFunction:

    def test_from_test_class_one(self, first_fixture):
        pass

    def test_from_test_class_two(self, first_fixture):
        pass
