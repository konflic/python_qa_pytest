import pytest


@pytest.fixture()
def function_fixture(request):
    print(f"\n Hello from {request.scope} fixture!")

    def fin():
        print(f"\n Finalize from {request.scope} fixture!")

    request.addfinalizer(fin)


@pytest.fixture(scope="class")
def class_fixture(request):
    print(f"\n Hello from {request.scope} fixture!")

    def fin():
        print(f"\n Finalize from {request.scope} fixture!")

    request.addfinalizer(fin)


@pytest.fixture(scope="module")
def module_fixture(request):
    print(f"\n Hello from {request.scope} fixture!")

    def fin():
        print(f"\n Finalize from {request.scope} fixture!")

    request.addfinalizer(fin)


@pytest.fixture(scope="session")
def session_fixture(request):
    print(f"\n Hello from {request.scope} fixture!")

    def fin():
        print(f"\n Finalize from {request.scope} fixture!")

    request.addfinalizer(fin)


@pytest.fixture(autouse=True)
def always_used_fixture():
    print(f"\n Hello, I'm fixture with autouse and funcction scope used always!")
