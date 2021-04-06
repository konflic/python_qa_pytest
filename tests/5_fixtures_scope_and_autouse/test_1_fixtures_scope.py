from src.Account import Account


def test_one(function_bank, class_bank, module_bank, session_bank):
    function_bank.add_account(Account("test", 100))
    class_bank.add_account(Account("test", 100))
    module_bank.add_account(Account("test", 100))
    session_bank.add_account(Account("test", 100))


def test_two(function_bank, class_bank, module_bank, session_bank):
    function_bank.add_account(Account("test", 100))
    class_bank.add_account(Account("test", 100))
    module_bank.add_account(Account("test", 100))
    session_bank.add_account(Account("test", 100))


class TestClass:

    def test_one(self, function_bank, class_bank, module_bank, session_bank):
        function_bank.add_account(Account("test", 100))
        class_bank.add_account(Account("test", 100))
        module_bank.add_account(Account("test", 100))
        session_bank.add_account(Account("test", 100))

    def test_two(self, function_bank, class_bank, module_bank, session_bank):
        function_bank.add_account(Account("test", 100))
        class_bank.add_account(Account("test", 100))
        module_bank.add_account(Account("test", 100))
        session_bank.add_account(Account("test", 100))

    def test_three(self, function_bank, class_bank, module_bank, session_bank):
        function_bank.add_account(Account("test", 100))
        class_bank.add_account(Account("test", 100))
        module_bank.add_account(Account("test", 100))
        session_bank.add_account(Account("test", 100))
