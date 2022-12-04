import sys

test = ['vJrwpWtwJgWrhcsFMMfFFhFp',
        'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
        'PmmdzqPrVvPwwTWBwg',
        'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
        'ttgJtRGJQctTZtZT',
        'CrZsJsPPZsGzwwsLwLmpwMDw']

def chunk(l, n) -> list:
    for i in range(0, len(l), n):
        yield l[i:i + n]

def alpha(c):
    if c.isupper():
        return ord(c) - 65 + 27
    else:
        return ord(c) - 96    

fh = open('3.input.txt', 'r')
data = fh.read().split('\n')

total = 0
for d in data:
    z = int(len(d) / 2)
    a = d[0:z]
    b = d[z:]
    common = set(a).intersection(set(b))
    common = list(common)[0]

    val = alpha(common)

    #print(common, val)
    total += val

print('Total Part 1', total)

# Lazy loop through again.
total2 = 0

for d in chunk(data, 3):
    a = set(d[0])
    b = set(d[1])
    c = set(d[2])

    i = a.intersection(b)
    i = i.intersection(c)
    p = list(i)[0]
    #print(p, alpha(p))
    total2 += alpha(p)

print('Total Part 2', total2)
