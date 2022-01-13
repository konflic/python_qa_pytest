import uuid


class Account:
    CREATED = 0

    def __init__(self, owner_id, balance):
        self.__uid = str(uuid.uuid4())
        self.__owner = owner_id
        self.__set_balance(balance)
        print("Account({}) was created!".format(self.__uid))
        self.__increase_count()

    @property
    def balance(self):
        return self.__balance

    @property
    def owner(self):
        return self.__owner

    @classmethod
    def __increase_count(cls):
        cls.CREATED += 1

    @classmethod
    def __decrease_count(cls):
        cls.CREATED -= 1

    def __set_balance(self, amount):
        if not isinstance(amount, int) and not isinstance(amount, float) or amount < 0:
            amount = 0.0
        self.__balance = amount

    def deposit(self, amount):
        if (isinstance(amount, int) or isinstance(amount, float)) and amount > 0:
            self.__balance += amount
            return True
        return False

    def withdraw(self, amount):
        if amount > 0 and (isinstance(amount, int) or isinstance(amount, float)):
            self.__balance -= amount
            return amount
        return 0

    def transfer(self, other_account, amount):
        other_account.deposit(self.withdraw(amount))

    def close(self):
        if self.__balance > 0:
            print("Can't close not empty account!")
            return False
        else:
            print("Account: {} was closed!".format(self))
            del self
            return True

    def __repr__(self):
        return "({}){}:{}$".format(self.__uid, self.owner, self.__balance)
