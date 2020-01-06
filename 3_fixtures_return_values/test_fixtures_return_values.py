def test_the_number(fixture_return_rnd_number):
    assert fixture_return_rnd_number == 20


def test_the_class(fixture_return_class):
    assert fixture_return_class.mod2.pow(2, 3) == 8
    assert fixture_return_class.mod1.choice(['a', 'b', 'c']) == 'a'


def test_the_class2(fixture_return_class):
    assert fixture_return_class.hello('Vasya') == 'Hello, Vasya'
