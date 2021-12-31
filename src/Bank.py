class Bank:

    def __init__(self, name, accounts: list):
        self.accounts = accounts
        self.name = name
        self.id = str(id(self))
        print("Created bank: '{}:{}' with {} accounts.".format(self.name, self.id, len(self.accounts)))

    def add_account(self, account):
        self.accounts.append(account)

    def close(self):
        print("Destroyed bank '{}:{}' with {} accounts.".format(self.name, self.id, len(self.accounts)))
        del self
