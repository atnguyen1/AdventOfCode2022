import math
import sys

data = '''1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122'''

data = open('25.input.txt', 'r').read()

def convert(entry) -> int:
    if entry in ['0', '1', '2']:
        return int(entry)
    elif entry == '-':
        return -1
    elif entry == '=':
        return -2
    else:
        print('TYPE ERROR', file=sys.stderr)
        return None

def make_place_val(digits) -> list:
    place_val = list()
    for x in range(0, digits):
        place_val.append(int(math.pow(5, x)))

    return place_val[::-1]

def todecimal(snafu, place_val):
    vals = [convert(y) for y in snafu]

    res = []
    for z, i in enumerate(vals):
        res.append(vals[z] * place_val[z])

    return sum(res)

def tosnafu(dec):
    snafu = ''
    s = {0: '0', 1: '1', 2:'2', 4:'-', 3:'='}
    d = dec
    while d:

        d, r = divmod(d, 5)
        match r:
            case 0|1|2:
                snafu += s[r]
            case 3|4:
                snafu += s[r]
                d += 1

    return ''.join(list(snafu)[::-1])

data = data.rstrip().lstrip().split('\n')
data = [list(x) for x in data]

total_fuel = []
for d in data:
    v = todecimal(d, make_place_val(len(d)))
    total_fuel.append(v)

print(tosnafu(sum(total_fuel)), sum(total_fuel))
