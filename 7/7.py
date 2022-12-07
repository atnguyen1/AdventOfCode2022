import sys

test = '''
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k'''

fs_max = 70000000
data = test.rstrip().lstrip().split('\n$')
data = open('7.input.txt', 'r').read().split('\n$')
data_store = dict()

class node():
    def __init__(self, dirname):
        self.dirname = dirname
        self.prev = None
        self.dirs = []       # More nodes
        self.dirnames = []   # Strs for membership testing
        self.files = []

    def add_files(self, val):
        self.files.append(val)

    def add_dir(self, newdirnode):
        self.dirs.append(newdirnode)

    def add_dirname(self, dirname):
        self.dirnames.append(dirname)

    def get_node(self, nodename):
        for d in self.dirs:
            if d.dirname == nodename:
                return d

    def contains(self, dirname):
        if dirname in self.dirnames:
            return True

    def traverse(self):
        visited = list()

        nodes = list()
        nodes.append(self)

        while len(nodes) > 0:
            current = nodes.pop()
            data_store[current] = current.get_dir_size()     # store mappings for faster lookups
            #print(current, current.get_dir_size())
            #print(current.dirname)
            #print(current.dirs)
            #print(current.files)

            for c in current.dirs:
                nodes.append(c)

            #print(nodes)

    def get_dir_size(self):
        file_sizes = sum([int(f.split('.')[0]) for f in self.files])

        for c in self.dirs:
            file_sizes += c.get_dir_size()

        return file_sizes

    def __repr__(self):
        return self.dirname

# Init
root = node('/')
current_node = root

for t in data[1:]:
    cmd = t.lstrip().rstrip().split('\n')

    if len(cmd) == 1:
        cmd = cmd[0].split(' ')
    #print(cmd)

    match cmd[0]:
        case 'ls':
            for c in cmd[1:]:
                listings = c.split(' ')
                if listings[0] == 'dir':
                    if current_node.contains(listings[1]):
                        continue
                    new_node = node(listings[1])
                    new_node.prev = current_node
                    current_node.add_dir(new_node)
                    current_node.add_dirname(listings[1])
                else:
                    # File
                    fn = listings[0] + '.' + listings[1]
                    if fn in current_node.files:
                        continue
                    current_node.add_files(fn)
        case 'cd':
            target = cmd[1]

            if target == '..':
                nn = current_node.prev
                current_node = nn
            else:
                nn = current_node.get_node(cmd[1])
                current_node = nn

root.traverse()   # Traverse and store all dir sizes
#print(root.get_dir_size())

total_sum = 0
for k in data_store:
    #print(k, data_store[k])
    if data_store[k] <= 100000:
        total_sum += data_store[k]

print('Part 1 Total Dir Size <= 100000', total_sum)

free_space = fs_max - root.get_dir_size()
needed = 30000000 - free_space
print('Needed Free Space', needed)

sizes = sorted([data_store[k] for k in data_store])
sizes = filter(lambda x: x >= needed, sizes)
print('Part 2 Smallest Dir size to delete', list(sizes)[0])