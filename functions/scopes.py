x = 0


def f():
    x = 1

    def _helper():
        nonlocal x
        x += 10

    _helper()
    print(x)


x = 1
f()
print(x)
