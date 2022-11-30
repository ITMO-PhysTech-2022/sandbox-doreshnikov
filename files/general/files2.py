import json
import pandas


with open('files/data.json') as input_file:
    obj = json.load(input_file)


def encode(obj, filename):
    with open(filename, 'wb') as output_file:
        for person in obj:
            info = [person['age'], len(person['name'])]
            for c in person['name']:
                info.append(ord(c))
            output_file.write(bytes(info))


def decode(filename):
    with open(filename, 'rb') as input_file:
        data = input_file.read()

    idx = 0

    def _next(cnt=1):
        nonlocal idx
        c = data[idx:idx + cnt]
        idx += cnt
        return c if cnt > 1 else c[0]

    result = []
    while idx < len(data):
        age = int(_next())
        name_length = int(_next())
        name = _next(name_length)
        result.append({
            'age': age,
            'name': name.decode(encoding='utf-8')
        })

    return result


def read_csv(filename, datatypes):
    with open(filename) as input_file:
        header = input_file.readline()
        data = input_file.readlines()

    columns = header.strip().split(',')
    result = []
    for line in data:
        values = line.strip().split(',')
        for i, t in enumerate(datatypes):
            values[i] = datatypes[i](values[i])
        result.append(dict(zip(columns, values)))

    return result


if __name__ == '__main__':
    # data = decode('files/data')
    # with open('files/data2.json', 'w') as output_file:
    #     json.dump(data, output_file, indent=2)
    with open('files/data.csv') as input_file:
        data = pandas.read_csv(input_file, sep='\t')

    print(data)
