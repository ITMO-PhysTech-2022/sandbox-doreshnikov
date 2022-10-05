from math import sin


# x -> x * sin(x)

def f(x):
    return x * sin(x)


a = f(3)
# print(a)
print(f(3))

b: int = min(1, 2, 3)
if a < 2:
    b = []
else:
    b = 'asdawd'


def greet(s, separate=True, end='\n'):
    print('Hello', end=end)
    if separate:
        print('-----', end=end)
    print(s)

greet('world')
greet('cat', False)
greet('python', end='|')

x = greet('something')
y = None
y = print(x, y)
print(y)

# ---------- old
x, y, z = 1, 2, 3
print(x, y, z)

# ----------- new
def f(x, y, z):
    return x + y + z