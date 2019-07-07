def test_one(function_fixture, class_fixture, module_fixture, session_fixture):
    print("I test_one NOT in test class 1!")


def test_two(function_fixture, class_fixture, module_fixture, session_fixture):
    print("I test_two NOT in test class 2!")


class TestClass:

    def test_one(self, function_fixture, class_fixture, module_fixture, session_fixture):
        print("Im test_one in TestClass test class!")

    def test_two(self, function_fixture, class_fixture, module_fixture, session_fixture):
        print("Im test_two in TestClass test class!")

    def test_three(self, function_fixture, class_fixture, module_fixture, session_fixture):
        print("Im test_three in TestClass test class!")
