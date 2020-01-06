import pytest

# --fixtures

@pytest.fixture
def first_fixture():
    print("\n===> Print from 'first_fixture'")


@pytest.fixture
def second_fixture():
    """
    This is test fixture.
    :return: None
    """
    print("===> Print from 'second_fixture'")
    return None


def test_one(first_fixture):
    """
    This is first empty test
    """
    pass


def test_two(second_fixture):
    """
    This is second empty test
    """
    pass


class TestFunction:

    def test_from_test_class_one(self, first_fixture):
        pass

    def test_from_test_class_two(self, first_fixture, second_fixture):
        pass
