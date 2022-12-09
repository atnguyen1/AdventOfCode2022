import sys
import numpy as np
import re

data = '''R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2'''

data = '''R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20'''

data = open('9.input.txt', 'r').read()

data = data.rstrip().lstrip().split('\n')

head = (0, 0)
tail = (0, 0)

knots = [(0,0) for x in range(0, 10)]

visited = set()
visited.add(tail)

visited2 = set()
visited2.add(knots[-1])

def plot(head, tail):
    arr = np.empty((16,16), dtype=str)
    heady = head[0] + 5
    headx = head[1] + 5
    taily = tail[0] + 5
    tailx = tail[1] + 5
    if head == tail:
        arr[heady, headx] = 'X'
    else:
        arr[taily, tailx] = 'T'
        arr[heady, headx] = 'H'

    print(arr)

def near(head, tail):
    tail_y, tail_x = tail
    head_y, head_x = head

    if tail_y + 1 == head_y or tail_y - 1 == head_y or tail_y == head_y:
        if tail_x + 1 == head_x or tail_x - 1 == head_x or tail_x == head_x:
            return True

    return False

# Unit Test Near

'''
print('H covers T', near((0,0), (0,0)))
print('HT', near((0,0), (0,1)))
print('TH', near((0,0), (0, -1)))
print('T\nH', near((0,0), (1,0)))
print('H\nT', near((0,0), (-1, 0)))
print('H\n T', near((0,0), (-1, 1)))
print(' T\nH', near((0,0), (1, 1)))
print('T\n H', near((0,0), (1, -1)))
print(' H\nT', near((0,0), (-1, -1)))
print('H  T', near((0,0), (0, 2)))
'''

def move_head(head, d) -> tuple:
    return (head[0] + d[0], head[1] + d[1])

def move_tail(head, tail):
    # Head is distance 2 away
    heady = head[0]
    headx = head[1]
    taily = tail[0]
    tailx = tail[1]

    if headx == tailx:
        # Same col
        if heady > taily:
            taily += 1
        else:
            taily -= 1
    elif heady == taily:
        # Same Row
        if headx > tailx:
            tailx += 1
        else:
            tailx -= 1
    else:
        # Not in row or col
        # Must move diag

        if headx > tailx:
            if heady > taily:
                # Move Up Left
                tailx += 1
                taily += 1
            else:
                tailx += 1
                taily -= 1
        elif headx < tailx:
            if heady > taily:
                tailx -= 1
                taily += 1
            else:
                tailx -= 1
                taily -= 1

    return (taily, tailx)

# Unit Test Move Tail
'''
head = (2, 1)
tail = (0, 0)
plot(head, tail)
print('')
tail = move_tail(head, tail)
plot(head, tail)
'''

for d in data:
    res = re.match('(\w+) (\d+)', d)
    if res:

        match res.group(1):
            case 'R':
                #print('Right', res.group(2))
                for x in range(0, int(res.group(2))):
                    head = move_head(head, (0,1))

                    if not near(head, tail):
                        tail = move_tail(head, tail)
                        visited.add(tail)
                        assert near(head, tail)      # After head moves, tail moves and is near

                for x2 in range(0, int(res.group(2))):
                    head2 = knots[0]
                    head2 = move_head(head2, (0, 1))
                    knots[0] = head2

                    for k in range(0,9):
                        head2 = knots[k]
                        tail2 = knots[k + 1]

                        if not near(head2, tail2):
                            tail2 = move_tail(head2, tail2)
                            knots[k + 1] = tail2

                    visited2.add(knots[-1])
            case 'U':
                #print('Up', res.group(2))
                for x in range(0, int(res.group(2))):
                    head = move_head(head, (1,0))

                    if not near(head, tail):
                        tail = move_tail(head, tail)
                        visited.add(tail)
                        assert near(head, tail)      # After head moves, tail moves and is near

                for x2 in range(0, int(res.group(2))):
                    head2 = knots[0]
                    head2 = move_head(head2, (1, 0))
                    knots[0] = head2

                    for k in range(0,9):
                        head2 = knots[k]
                        tail2 = knots[k + 1]

                        if not near(head2, tail2):
                            tail2 = move_tail(head2, tail2)
                            knots[k + 1] = tail2

                    visited2.add(knots[-1])
            case 'L':
                #print('Left', res.group(2))
                for x in range(0, int(res.group(2))):
                    head = move_head(head, (0, -1))

                    if not near(head, tail):
                        tail = move_tail(head, tail)
                        visited.add(tail)
                        assert near(head, tail)      # After head moves, tail moves and is near

                for x2 in range(0, int(res.group(2))):
                    head2 = knots[0]
                    head2 = move_head(head2, (0, -1))
                    knots[0] = head2

                    for k in range(0,9):
                        head2 = knots[k]
                        tail2 = knots[k + 1]

                        if not near(head2, tail2):
                            tail2 = move_tail(head2, tail2)
                            knots[k + 1] = tail2

                    visited2.add(knots[-1])
            case 'D':
                #print('Down', res.group(2))
                for x in range(0, int(res.group(2))):
                    head = move_head(head, (-1,0))

                    if not near(head, tail):
                        tail = move_tail(head, tail)
                        visited.add(tail)
                        assert near(head, tail)      # After head moves, tail moves and is near

                for x2 in range(0, int(res.group(2))):
                    head2 = knots[0]
                    head2 = move_head(head2, (-1, 0))
                    knots[0] = head2

                    for k in range(0,9):
                        head2 = knots[k]
                        tail2 = knots[k + 1]

                        if not near(head2, tail2):
                            tail2 = move_tail(head2, tail2)
                            knots[k + 1] = tail2

                    visited2.add(knots[-1])

print('Part 1', len(visited))
print('Part 2', len(visited2))