# Создание тестовых файлов
def test_one():
    print(" >>> I'm test one!")


# Так тоже можно, но не нужно и с модулем не заработает
def testwo():
    pass


# Создание тестовых классов
class TestClass:

    def test_one(self):
        pass

    def testtwo(self):
        pass

# Запуск отдельных файлов, функций, классов
# pytest 0_pytest_intro/
# pytest 0_pytest_intro/test_pytest_intro_1.py
# pytest 0_pytest_intro/test_pytest_intro_1.py::TestClass
# pytest 0_pytest_intro/test_pytest_intro_1.py::test_one
