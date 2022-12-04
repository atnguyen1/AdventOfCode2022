import sys

test = ['2-4,6-8',
        '2-3,4-5',
        '5-7,7-9',
        '2-8,3-7',
        '6-6,4-6',
        '2-6,4-8']

fh = open('4.input.txt', 'r')
data = fh.read().split('\n')

contains = 0
some_overlap = 0

for d in data:
    d = d.split(',')
    a = d[0].split('-')
    b = d[1].split('-')

    a = set([x for x in range(int(a[0]), int(a[1]) + 1)])
    b = set([y for y in range(int(b[0]), int(b[1]) + 1)])

    if len(a.difference(b)) == 0 or len(b.difference(a)) == 0:
        contains += 1

    if len(a.intersection(b)) > 0:
        some_overlap += 1

print('Total Overlaps: ', contains)
print('Some Overlaps:', some_overlap)