import sys

vals = {'A': 1, 'B': 2, 'C': 3}
rev_vals = {1: 'A', 2: 'B', 3: 'C'}
ins = {'X': 'A', 'Y': 'B', 'Z': 'C'}
rev_ins = {'A': 'X', 'B': 'Y', 'C': 'Z'}

win_val = 6
draw_val = 3

def rps(s):
    '''
         s is a string of format 'B Y'
    '''
    e = s.split(' ')
    turn_val = 0

    # Tie Case
    if e[0] == ins[e[1]]:
        turn_val = draw_val + vals[ins[e[1]]]
    # Win
    elif (vals[ins[e[1]]] - vals[e[0]] == 1) or (vals[ins[e[1]]] - vals[e[0]] == -2):
        turn_val = win_val + vals[ins[e[1]]]
    # Loss
    elif (vals[ins[e[1]]] - vals[e[0]] == -1) or (vals[ins[e[1]]] - vals[e[0]] == 2):
        turn_val = vals[ins[e[1]]]

    return turn_val

fh = open('2.input.txt', 'r')
data = fh.read().split('\n')

test = ['A Y', 'B X', 'C Z']

score1 = 0
score2 = 0

for d in data:
    e = d.split(' ')

    # Part 1
    turn_val_1 = rps(d)

    # Part 2
    turn_val_2 = 0
    if e[1] == 'X':
        # Lose
        needed = vals[e[0]] + -1

        if needed < 1:
            needed = 3

        turn_val_2 = rps(e[0] + ' ' + rev_ins[rev_vals[needed]])

    elif e[1] == 'Y':
        # Tie
        turn_val_2 = rps(e[0] + ' ' + rev_ins[e[0]])
    elif e[1] == 'Z':
        # Win
        needed = vals[e[0]] + 1

        if needed > 3:
            needed = 1

        turn_val_2 = rps(e[0] + ' ' + rev_ins[rev_vals[needed]])

    #print(d + ' Score for Round: ', turn_val_1)
    #print(d + ' Score for Round:', turn_val_2)
    score1 += turn_val_1
    score2 += turn_val_2

print('Part 1A:')
print('Total Score:', score1)
print('Part 1B:')
print('Total Score', score2)