import pytest

from src.Bank import Bank
from src.Account import Account


@pytest.fixture
def function_bank(request):
    bank = Bank("FunctionBank", [])
    request.addfinalizer(bank.close)
    return bank


@pytest.fixture(scope="class")
def class_bank(request):
    bank = Bank("ClassBank", [])
    request.addfinalizer(bank.close)
    return bank


@pytest.fixture(scope="module")
def module_bank(request):
    bank = Bank("ModuleBank", [])
    request.addfinalizer(bank.close)
    return bank


@pytest.fixture(scope="session")
def session_bank(request):
    bank = Bank("SessionBank", [])
    request.addfinalizer(bank.close)
    return bank

# @pytest.fixture(autouse=True)
# def always_used_fixture():
#     print(f"\n Hello, I'm fixture with autouse and function scope used always!")
