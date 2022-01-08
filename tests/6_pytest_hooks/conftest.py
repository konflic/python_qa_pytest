# https://docs.pytest.org/en/latest/reference/reference.html?highlight=hooks#hooks

def pytest_runtest_setup(item):
    if "three" in item.name:
        item.name = "NAME OF {} IS CHANGED!".format(item.name)
    print("\n", "item = ", item)


def pytest_runtest_call(item):
    if "four" in item.name:
        item.name = "NAME OF {} IS CHANGED!".format(item.name)


def pytest_configure(config):
    print(config)


def pytest_sessionstart(session):
    print(session)


def pytest_sessionfinish(session):
    print(session)
