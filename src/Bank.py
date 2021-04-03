class Bank:

    def __init__(self, name, accounts: list):
        self.accounts = accounts
        self.name = name
        print("Created Bank: '{}:{}' with {} accounts.".format(name, id(self), len(accounts)))

    def close(self):
        del self
        print("Bank {} was destroyed!")
