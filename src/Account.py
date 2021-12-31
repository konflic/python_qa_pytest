import uuid


class Account:
    CREATED = 0

    def __init__(self, owner_id, balance, activated=False):
        self.__uid = str(uuid.uuid4())
        self.__owner = owner_id
        self.__set_balance(balance)
        self.__activated = activated
        print("Account({}) was created!".format(self.__uid))
        self.__increase_count()

    @property
    def balance(self):
        return self.__balance

    @property
    def owner(self):
        return self.__owner

    @property
    def activated(self):
        return self.__activated

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

    def activate(self):
        self.__activated = True

    def deposit(self, amount):
        if not isinstance(amount, int) and not isinstance(amount, float) or amount < 0:
            amount = 0.0
        self.__balance += amount

    def withdraw(self, amount):
        if amount < 0 or not isinstance(amount, int) or not isinstance(amount, float):
            amount = 0.0
        self.__balance -= amount
        return amount

    def transfer(self, other_account, amount):
        if self.__activated:
            self.withdraw(amount)
            other_account.deposit(amount)
            return True
        else:
            print("Can't transfer from not activated account!")
            return None

    def close(self):
        if self.__balance > 0:
            print("Can't close not empty account!")
        else:
            print("Account: {} was closed!".format(self))
            del self

    def __repr__(self):
        return "({}) {}:{}$:{}".format(self.__uid, self.owner, self.__balance, self.__activated)
