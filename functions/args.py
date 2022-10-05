def f(arg1, arg2, *args):
    count = 0
    for i in args:
        if i % 3 == 0:
            count += 1
    print(count)
    # print(args)


# f()
# f(1)
f(1, 2)
f(1, 2, 3)
f(1, 2, 3, 4)


def g(arr):
    count = 0
    for i in arr:
        if i % 3 == 0:
            count += 1
    print(count)


g([1, 2])
g([1, 2, 3])
g([1, 2, 3, 4])

# print(min(1, 2))
# print(min(1, 2, 3))
# print(min(1, 2, 3, 4))
# print(min(1, 2, 3, 4, 5))

args = [1, 2, 'xyz', '100', None]
# same as print([1, 2, 'xyz', '100', None])
print(args)
# same as print(1, 2, 'xyz', '100', None)
print(*args)


def hard(*args, **kwargs):
    print(args)
    # args[0]
    print(kwargs)
    # kwargs['x']


hard(1, 2, 3, x=10, y=100)
hard(1, name='s', end='\n')
hard(1, 4, 5, 6)
hard(only='xyz')


def twice(f, *args, **kwargs):
    f(*args, **kwargs)
    f(*args, **kwargs)


twice(print, 1, 2, 3, sep=': ')
# print(1, 2, 3, sep=': ')