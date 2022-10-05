def f(n):
    if n == 0:
        return 1
    else:
        return n * f(n - 1)


print(f(3))

'''
f(3) -> 6
    f(2) -> 2
        f(1) -> 1
            f(0) -> 1
'''

n = 7
result = 1
for i in range(1, n + 1):
    result *= i


# os, pathlib
def walk(path):
    for item in list_al_items(path):
        if is_file(item):
            ...
        elif is_directory(item):
            walk(item)