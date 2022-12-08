import sys
import numpy as np

data = '''30373
25512
65332
33549
35390'''.split('\n')

data = open('8.input.txt', 'r').read().split('\n')

data = [list(x) for x in data]

array = np.array(data, dtype=int)
ymax, xmax = array.shape
#print(array)

flag_array = np.zeros(array.shape, dtype=int)
viewing_array = np.zeros(array.shape, dtype=int)

#print(flag_array)

it = np.nditer(array, flags=['multi_index'])

for tree in it:
    y, x = it.multi_index
    if y == 0 or x == 0 or y == ymax - 1 or x == xmax - 1:
        # Mark Border
        flag_array[it.multi_index] = 1
        #continue

    left = array[y, 0:x]
    right = array[y, x + 1:]
    top = array[0:y, x]
    bottom = array[y + 1:, x]

    left_vis = [True if tree > e else False for e in left]
    right_vis = [True if tree > e else False for e in right]
    top_vis = [True if tree > e else False for e in top]
    bottom_vis = [True if tree > e else False for e in bottom]

    left_vis.reverse()
    top_vis.reverse()

    # Not tracking which direction visible
    if False not in left_vis:
        flag_array[it.multi_index] = 1
    elif False not in right_vis:
        flag_array[it.multi_index] = 1
    elif False not in top_vis:
        flag_array[it.multi_index] = 1
    elif False not in bottom_vis:
        flag_array[it.multi_index] = 1

    if False in left_vis:
        left_score = left_vis.index(False) + 1
    else:
        left_score = len(left_vis)

    if False in right_vis:
        right_score = right_vis.index(False) + 1
    else:
        right_score = len(right_vis)

    if False in top_vis:
        top_score = top_vis.index(False) + 1
    else:
        top_score = len(top_vis)

    if False in bottom_vis:
        bottom_score = bottom_vis.index(False) + 1
    else:
        bottom_score = len(bottom_vis)

    '''
    if it.multi_index == (3, 2):
        print(tree)
        print(left_score, right_score, top_score, bottom_score)
        print(left_vis)
        print(right_vis)
        print(top_vis)
        print(bottom_vis)
        print(left)
        print(right)
        print(top)
        print(bottom)
    '''

    viewing_array[it.multi_index] = left_score * right_score * top_score * bottom_score

    '''
    print('Left', left_vis)
    print('Right', right_vis)
    print('Top', top_vis)
    print('Bottom', bottom_vis)
    print(left)
    print(right)
    print(top)
    print(bottom)
    print(tree, y, x)
    sys.exit()
    '''

#print(flag_array)
print('Part 1 Total Visible Trees', np.sum(flag_array))
#print(viewing_array)
print('Part 2 Max Viewing Score', viewing_array.max())