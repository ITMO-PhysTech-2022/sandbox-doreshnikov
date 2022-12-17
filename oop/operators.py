from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int
    job: str
    phone: str

    def print(self):
        print(self.name, self.age)


person = Person('Dan', 23, 'Teacher', 'None')
person.print()


class A:
    @property
    def x(self):
        return 'Actual attribute'

    @staticmethod
    def construct():
        return A()

    def __getattr__(self, item):
        return f'Attribute {item}'


class TestResult:
    def __init__(self):
        pass

    @property
    def message(self):
        raise NotImplementedError('abstract')

    @property
    def score(self):
        raise NotImplementedError('abstract')


class OK(TestResult):
    def __init__(self, full_score):
        super().__init__()
        self.full_score = full_score

    @property
    def message(self):
        return 'OK'

    @property
    def score(self):
        return self.full_score


class WrongAnswer(TestResult):
    def __init__(self, result, answer):
        super().__init__()
        self.result = result
        self.answer = answer

    @property
    def message(self):
        return f'Expected {self.answer}, got {self.result}'

    @property
    def score(self):
        return 0.0


a = A.construct()
print(a.x)
print(a.y)


class Logger:
    _instance = None

    def __init__(self):
        ...

    @staticmethod
    def instance():
        if Logger._instance is None:
            Logger._instance = Logger()
        return Logger._instance


# вместо logger = Logger()
# logger = Logger.instance()