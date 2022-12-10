import sys
from collections import deque
import numpy as np

data = '''noop
addx 3
addx -5'''

data = open('10.input.txt', 'r').read()
#data = open('10.test.txt', 'r').read()

data = data.rstrip().lstrip().split('\n')

class CRT:
    def __init__(self):
        self.x_register = 1
        self.clock = 0
        self.done = deque()
        self.stack = deque()
        self.stack_ptr = 0
        self.todo = deque()

        self.screen = np.empty((6,40), dtype=str)
        self.screen_ptr = (0,0)

    def read(self, data):
        for d in data:
            d = d.split()
            self.todo.append(d)

        # Init the stack
        self.loadstack()


    def loadstack(self):
        if self.todo:
            ins = self.todo.popleft()

            match ins[0]:
                case 'noop':
                    # 1 Cycle
                    self.stack.append(ins)
                case 'addx':
                    # 2 Cycles
                    self.stack.append(ins)
                    self.stack.append(ins)

            self.stack_ptr = 0


    def tick(self):
        self.clock += 1
        if self.stack:
            self.stack_ptr += 1

    def tock(self):
        # If the clock advances past the instruction compute cycle, update registers pop the stack
        if (self.stack_ptr >= len(self.stack)) and self.stack:
            completed_ins = self.stack.popleft()

            match completed_ins[0]:
                case 'noop':
                    pass
                case 'addx':
                    self.x_register += int(completed_ins[1])

            self.done.append(completed_ins)
            self.stack = deque()
            self.stack_ptr = 0
            self.loadstack()


    def draw(self):
        sprit_pos = self.x_register
        xpos = self.screen_ptr[1]
        ypos = self.screen_ptr[0]

        if (sprit_pos - 1 == xpos) or (sprit_pos == xpos) or (sprit_pos + 1 == xpos):
            self.screen[self.screen_ptr] = '#'
        else:
            self.screen[self.screen_ptr] = '.'

        xpos += 1

        if xpos > 39:
            xpos = 0
            ypos += 1

        self.screen_ptr = (ypos, xpos)


    def state(self):
        #print('Clock Finish:', self.clock - 1)
        print('Clock Start:', self.clock)
        print('x_register', self.x_register)
        print('Done:', self.done)
        print('Stack:', self.stack, 'Ptr:', self.stack_ptr)
        print('Ins:', self.todo)
        print('')


computer = CRT()
computer.read(data)

run = 239
clocks = [20, 60, 100, 140, 180, 220]
signal_strength = []
while computer.clock <= run:
    computer.tick()
    if computer.clock in clocks:
        #print(computer.clock, computer.x_register)
        #computer.state()
        signal_strength.append((computer.clock, computer.x_register))
    computer.draw()
    computer.tock()

#print(signal_strength)
print('Part 1:', sum([x[0] * x[1] for x in signal_strength]))
print('Part 2:')
for k in range(0, 6):
    print(''.join(computer.screen[k]))
