import sys
from collections import deque
import numpy as np
import re
import copy

test = '''
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2'''

data = open('5.input.txt', 'r').read()

start, instructions = data.rstrip().lstrip('\n').split('\n\n')
start = [[x for x in y] for y in start.split('\n')]

initial_state = np.array(start, dtype=str)
initial_state = initial_state.transpose()

deques = list()

for i in initial_state:
    i = list(i)
    i.reverse()
    if i[0] == '' or i[0] == ' ':
        continue
    elif int(i[0]) > 0:
        a = deque()
        for char in i[1:]:
            res = re.match('(\w+)', char)
            if res:
                a.append(res.group(1))

        deques.append(a)

# Initial State
#print(deques)

deques2 = copy.deepcopy(deques)

for x in instructions.split('\n'):
    res2 = re.match('move (\d+) from (\d+) to (\d+)', x)
    if res2:
        count = int(res2.group(1))
        source = int(res2.group(2))
        dest = int(res2.group(3))

        for i in range(0, count):
            container = deques[source - 1].pop()
            deques[dest - 1].append(container)

        if count > 1:
            order = deque()
            for i in range(0, count):
                container2 = deques2[source - 1].pop()
                order.appendleft(container2)
            for o in order:                
                deques2[dest - 1].append(o)
        else:
            container2 = deques2[source - 1].pop()
            deques2[dest - 1].append(container2)

# Final State
print(deques2)

final_str = ''
final_str2 = ''

for d in deques:
    final_str += str(d.pop())

for d2 in deques2:
    final_str2 += str(d2.pop())

print('Part 1: ', final_str)
print('Part 2: ', final_str2)