# a, b, c = map(int, input().split())
# print(a, b, c)
# x = ['12', '134', '56']
# map(int, x) ~ [int('12'), int('134'), int('56')]


def extract(s):
    return s.split()[2]


print(extract('abc def xyz 123'))

file = [
    'abc xyz nnn 123',
    'abacaba xx yy',
    'zhc 000 192 144',
]

info = []
for line in file:
    info.append(extract(line))
# same as
info = list(map(extract, file))


def ok(x):
    return x % 2 == 0


a = [1, 2, 3, 4, 5, 6, 7]

b = []
for item in a:
    if ok(item):
        b.append(item)
# same as
b = list(filter(ok, a))


def custom_map(fun, arr):
    result = []
    for item in arr:
        result.append(fun(item))
    return result

x = custom_map(min, [[1, 2, 3], [6, -1, 2], ['x', 'y', 'z'], [111]])
# [min([1, 2, 3]), min([6, -1, 2]), min(['x', 'y', 'z']), min([111])]
print(x)