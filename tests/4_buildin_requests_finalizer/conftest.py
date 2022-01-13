import pytest
from src.Account import Account


@pytest.fixture
def empty_account(request):
    """Способ создания финализатора через addfinalizer"""
    account = Account("Empty", 0)

    # Нужно доработать финализатор
    request.addfinalizer(account.close)

    return account


@pytest.fixture
def activated_account():
    """Способ создания финализатора через yield"""
    account = Account("Activated", 100)

    yield account

    account.withdraw(account.balance)
    account.close()
