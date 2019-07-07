import pytest


@pytest.fixture
def first_fixture():
    print("\nPrint from 'first_fixture'")


def test_one(first_fixture):
    pass


def test_two(first_fixture):
    pass


class TestFunction:

    def test_from_test_class_one(self, first_fixture):
        pass

    def test_from_test_class_two(self, first_fixture):
        pass
