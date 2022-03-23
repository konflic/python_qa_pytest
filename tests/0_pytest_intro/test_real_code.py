from src.Account import Account


def test_account_create():
    a = Account("Mr.X", 0)
    assert isinstance(a, Account)
    assert a.balance == 0
    assert a.owner == "Mr.X"


def test_account_with_balance_create():
    a = Account("Mr.X", 100)
    assert a.balance == 100


def test_account_create_counter():
    a = Account("Mr.X", 100)
    b = Account("Mr.Y", 100)
    assert a.CREATED, b.CREATED == (2, 2)


def test_account_delete_counter():
    a = Account("Mr.X", 100)
    b = Account("Mr.Y", 100)
    assert a.CREATED == 2
    del b
    assert a.CREATED == 1
