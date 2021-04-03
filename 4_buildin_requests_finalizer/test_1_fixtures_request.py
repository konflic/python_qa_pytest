import pytest


@pytest.fixture()
def first_fixture_for_request(request):
    print("___________________________")
    print(f"{request.node}")
    print(f"{request.scope}")
    print(f"{request.cls}")
    print(f"{request.module}")
    print("___________________________")
    for entry in dir(request):
        print(entry)


def test_one(first_fixture_for_request):
    print("\nPrint from 'test_one'")
