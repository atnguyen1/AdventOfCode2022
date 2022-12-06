import sys
from collections import deque

test = ['mjqjpqmgbljsphdztnvjfqwrcgsmlb',
        'bvwbjplbgvbhsrlpgdmjqwftvncz',
        'nppdvjthqldpwncqszvftbrmjlhg',
        'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg',
        'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw']

data = open('6.input.txt', 'r').read()

def packet_indicator(stream, u):
    '''u == buffer size of uniques'''
    buffer = deque()
    for z, d in enumerate(stream):
        if len(buffer) == u:
            buffer.popleft()
            buffer.append(d)
        else:
            buffer.append(d)

        if len(set(buffer)) == u:
            return (z + 1)


for t in test:
    print('Part1 Test:', packet_indicator(t, 4))

for t in test:
    print('Part2 Test', packet_indicator(t, 14))

print('Part1', packet_indicator(data, 4))
print('Part2', packet_indicator(data, 14))