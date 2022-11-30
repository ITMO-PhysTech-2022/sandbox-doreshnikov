used = set()
filename = 'cities.in'

with open(filename, 'r') as cities:
    pool = cities.readlines()
    pool = list(map(str.strip, pool))


def follows(word1, word2):
    """
    Checks if word2 can follow word1
    """
    return word1[-1].lower() == word2[0].lower()


def make_move(c):
    """
    Name an unused city starting with letter c
    """
    for word in pool:
        if word not in used and follows(c, word):
            used.add(word)
            return word


word = None
while True:
    s = input('Enter a city: ')
    if len(s) == 0:
        print('You lose! Incorrect input format')
        break

    if s not in pool:
        # компьютер запомнил s в файл cities.in
        with open(filename, 'a') as cities:
            print(s, file=cities)
        pool.append(s)

    if word is not None and not follows(word, s):
        print('Incorrect city, should start with different letter')
        continue
    if s in used:
        print('You lose! This city was already used')
        break
    used.add(s)

    word = make_move(s[-1].lower())
    if word is None:
        print('You win!')
        break
    print(word)

'''
-- 1. что делать, если у компьютера нет хода
-- 2. проверять корректность хода пользователя
-- 2.5. проверять корректность ввода пользователя
-- 3. компьютер должен запоминать новые слова, которые не знает
'''
