import pytest


@pytest.fixture()
def first_fixture_for_request(request):
    print("___________________________")
    print(f"{request.node}")
    print(f"{request.scope}")
    print(f"{request.cls}")
    print(f"{request.module}")
    print("___________________________")
    # print("\nRequset object data: ")
    # for el in list(dir(request)):
    #     print(el)


def test_one(first_fixture_for_request):
    print("\nPrint from 'test_one'")


class TestClass:

    def test_two(self, first_fixture_for_request):
        print("\nPrint from 'test_two'")

    def test_three(self, first_fixture_for_request):
        print("\nPrint from 'test_three'")
