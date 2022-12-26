import sys
import numpy as np
from collections import deque, defaultdict

data = '''
....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#..'''

data1 = '''
.....
..##.
..#..
.....
..##.
.....'''

def pad(array):
    ''' Given an array, pad the array with 0s to extend the field, cheat to ignore bound checking'''

    maxy, maxx = array.shape
    if 1 in array[0,:] or 1 in array[:,0] or 1 in array[maxy-1,:] or 1 in array[:,maxx-1]:
        ar = np.pad(array, 1, mode='constant')
    else:
        ar = array
    return ar

def printa(array):
    y, x = array.shape
    out = list()
    for z in range(0,y):
        o = list(array[z,])
        o = ['.' if w == 0 else '#' for w in o]
        out.append(''.join(o))

    for o in out:
        print(o)

data = open('23.input.txt', 'r').read()

data = data.rstrip().lstrip().split('\n')
data = np.array([[0 if y == '.' else 1 for y in list(x)] for x in data], dtype=np.int8)

#print(data)

directions = deque([((-1,0), [(-1,-1), (-1,0), (-1,1)]), ((1,0), [(1,-1), (1,0), (1,1)]), ((0,-1), [(-1,-1), (0,-1), (1,-1)]), ((0,1), [(-1,1), (0,1), (1,1)])])

all_sides_check = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

m = data
r = 0
debug = False
if debug:
    print('Initial State', r)
    printa(m)

while True:
    proposed_moves = defaultdict(list)

    m = pad(m)
    #print(m)

    y1, x1 = np.where(m > 0)
    elves = [x for x in zip(y1,x1)]
    for e in elves:
        y1, x1 = e

        all_check_spots = [(y1 + a[0], x1 + a[1]) for a in all_sides_check]
        all_check = [True if m[z] == 0 else False for z in all_check_spots]

        if False in all_check:
            for d in directions:
                move, check = d

                move = (move[0] + y1, move[1] + x1)
                zones = [(y1 + c[0], x1 + c[1]) for c in check]
                zone_check = [True if m[z] == 0 else False for z in zones]

                #print(e)
                #print(zones)
                #print(zone_check)

                if False not in zone_check:
                    # Propose Move
                    proposed_moves[move].append(e)
                    break

    # Swap direction Priority
    d = directions.popleft()
    directions.append(d)

    #print(proposed_moves)

    for p in proposed_moves:
        if len(proposed_moves[p]) > 1:
            continue
        new_spot = p
        old_spot = proposed_moves[p][0]
        m[new_spot] = 1
        m[old_spot] = 0

    r += 1
    if debug:
        print('End of Round', r)
        printa(m)

    #if r >= 10:
    #    break

    if len(proposed_moves) == 0:
        # All elves isolated, stop moving
        break
print(r)
sys.exit()
y, x = np.where(m > 0)
elf10 = list(zip(y,x))
smallest_y = sys.maxsize
smallest_x = sys.maxsize
largest_x = 0
largest_y = 0

for y,x in elf10:
    if y < smallest_y:
        smallest_y = y
    if x < smallest_x:
        smallest_x = x
    if y > largest_y:
        largest_y = y
    if x > largest_x:
        largest_x = x

#print(elf10)
squash = m[smallest_y:largest_y+1, smallest_x:largest_x+1]
#printa(squash)

#print(len(np.where(squash == 0)[0]))
print(r)