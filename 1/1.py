import sys

with open('1.input.txt', 'r') as fh:
    data = fh.read()
    data = data.split('\n\n')

    elf_cal = list()

    for d in data:
        e = d.split()
        e = sum([int(x) for x in e])
        elf_cal.append(e)

    print(max(elf_cal))

    elf_cal = sorted(elf_cal, reverse=True)

    print(sum(elf_cal[0:3]))

    print('Tests:')
    test = [[1000, 2000, 3000], [4000], [5000, 6000], [7000, 8000, 9000], [10000]]
    f = [sum(x) for x in test]
    print(f, max(f))
    f = sorted(f, reverse=True)
    print(f, sum(f[0:3]))