def test_account_deposit(empty_account):
    empty_account.deposit(100)
    assert empty_account.balance == 100


def test_not_activated_account_cant_transfer(empty_account, activated_account):
    empty_account.deposit(100)
    balance_before_transfer = activated_account.balance
    empty_account.transfer(activated_account, 100)
    assert (
            activated_account.balance == balance_before_transfer + 100
    ), f"Баланс {activated_account} должен измениться"
