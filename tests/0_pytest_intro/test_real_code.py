from src.Account import Account


def test_account_create():
    a = Account("Mr.X", 0)
    assert isinstance(a, Account)
    a.close()


def test_default_not_activated():
    a = Account("Mr.X", 0)
    assert a.balance == 0
    a.close()
