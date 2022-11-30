f = open('files/sample.out', 'w')
# 'r', 'w', 'a', 'rb', 'wb', 'ab'
...
f.close()

with open('files/sample.out', 'w') as f:
    print(1, 2, 3, file=f)
    f.write('Example string\n')

    # x, y = map(int, input().split())
    x, y = 10, 2
    print(x / y, file=f)

code = open('files/files.py', 'r')
# code.read()
# code.readline()
# code.readlines()
for line in code.readlines():
    # print(line, end='')
    print(line.rstrip())