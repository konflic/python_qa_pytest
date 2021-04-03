import pytest
from src.Account import Account


@pytest.fixture
def empty_account():
    return Account("Test", 0)


@pytest.fixture
def activated_account():
    return Account("Test", 100, True)
