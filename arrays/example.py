a = [1, 2, 3, 4]
print(a[0], a[3])

for item in a:
    print(item ** 2)

print(min(a), max(a), sum(a))

# n = int(input())
n = 7
# 0, 1, 4, ..., (n - 1) ** 2
b = []
for i in range(n):
    b.append(i ** 2)
print(b)

b = [45, 67, 1, 34, 0, -100]
b.sort()
b.reverse()
print(b)

if 1 in b:
    print(f'1 is indeed in b on position {b.index(1)}')
else:
    print('nope')

del b[3]
print(b)

b.insert(3, 1)
print(b)