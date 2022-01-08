import pytest
from src.Account import Account


@pytest.fixture
def empty_account():
    return Account("Test", 0)


@pytest.fixture
def activated_account():
    return Account("Test", 100, True)


def test_one(empty_account):
    """This is first empty test"""
    pass


def test_two(activated_account):
    """This is second empty test"""
    pass


class TestFunction:
    def test_from_test_class_one(self, empty_account):
        pass

    def test_from_test_class_two(self, activated_account, empty_account):
        pass
