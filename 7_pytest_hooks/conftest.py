# https://docs.pytest.org/en/latest/reference.html#id54
import pytest


def pytest_runtest_protocol(item, nextitem):
    print('\n', "item = ", item, "nextitem = ", nextitem)


def pytest_runtest_setup(item):
    if "three" in item.name:
        item.name = "NAME OF {} IS CHANGED!".format(item.name)
    print('\n', "item = ", item)

def pytest_runtest_call(item):
    if "four" in item.name:
        item.name = "NAME OF {} IS CHANGED!".format(item.name)
