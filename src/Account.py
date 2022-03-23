import uuid


class Account:
    CREATED = 0

    def __init__(self, name, balance=0):
        self.__uid = str(uuid.uuid4())
        self.__owner = name
        self.__balance = 0
        self.deposit(amount=balance)
        self.__increase_accounts_count()

    @property
    def balance(self):
        return self.__balance

    @property
    def owner(self):
        return self.__owner

    @classmethod
    def __increase_accounts_count(cls):
        cls.CREATED += 1

    @classmethod
    def __decrease_accounts_count(cls):
        cls.CREATED -= 1

    def deposit(self, amount):
        if (isinstance(amount, int) or isinstance(amount, float)) and amount > 0:
            self.__balance += amount
            return True
        return False

    def withdraw(self, amount):
        if (isinstance(amount, int) or isinstance(amount, float)):
            if amount > 0 and self.__balance > amount:
                self.__balance -= amount
                return amount
        return 0

    def transfer(self, other_account, amount):
        return other_account.deposit(self.withdraw(amount))

    def __del__(self):
        self.__decrease_accounts_count()
