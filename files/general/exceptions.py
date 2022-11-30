x = 10
y = 1

try:
    print(x / y)
except ZeroDivisionError:
    print('Division by zero')
finally:
    print('Done..')


def get(d: dict, key1: str, key2: str):
    if key1[0] == key2[0]:
        return d.popitem()
    raise KeyError('First letters are not equal')
