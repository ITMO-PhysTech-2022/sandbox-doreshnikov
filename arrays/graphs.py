import matplotlib.pyplot as plt
import math
import numpy as np


def f(x):
    return x * math.sqrt(abs(x)) / (2 + math.sin(x))


xs = np.arange(-10, 10, 0.01)
f = np.vectorize(f)
ys = f(xs)

plt.plot(xs, ys)

fig, ax = plt.subplots(figsize=(5, 3))
# Axes
ax.plot(xs, ys)
ax.set_title('Some weird function')
ax.legend()

plt.savefig('C:/Users/jetbrains/PycharmProjects/sandbox-doreshnikov/graph.pdf')