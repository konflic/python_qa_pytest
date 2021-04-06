import pytest
from src.Account import Account


@pytest.mark.parametrize("amount", [0, 100, 9999, 0.01])
def test_creating_account_valid(amount):
    a = Account("Test", amount)
    assert a.balance == amount


@pytest.mark.parametrize("amount", [-100, "", [], "-100"])
def test_creating_account_invalid(amount):
    a = Account("Test", amount)
    assert a.balance == 0


@pytest.mark.parametrize("amount,expected_amount", [
    (0, 0), (100, 100), (9999, 9999), (-10, 0), ("", 0), (0.01, 0.01)
])
def test_deposit_account(amount, expected_amount, empty_account):
    empty_account.deposit(amount)
    assert empty_account.balance == expected_amount
