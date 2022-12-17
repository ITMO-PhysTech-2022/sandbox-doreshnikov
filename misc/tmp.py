def g(*args):
    print(*args)


array = [1, 2, 3, 4, 5]
g(array)
g(*array)