import numpy as np
import math

a = [1, 2, 3]
b = [0.1, 0.2, 0.3]

a = np.array(a)
b = np.array(b)

c = np.array([100, 200, 350, 500, 800])


def calculate(x):
    # большое длинное вычисление каких-то параметров
    return x * math.sin(x) / math.sqrt(x)


f = np.vectorize(calculate)
a = f(a)
a += b

# print(a)
# print(f(c))
