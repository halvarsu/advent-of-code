import numpy as np
from collections import defaultdict

# filename = "test_input3"
filename = "input"
with open(filename) as infile:
    connections = []
    nodes = defaultdict(list)
    for line in infile.readlines():
        a, b = line.strip().split("-")
        connections.append((a, b))
        nodes[a].append(b)
        nodes[b].append(a)


print(connections)
print(nodes)
print(nodes['start'])

def get_paths(node, nodes, prev = (), all_paths=[]):
    """Recursively explores a node-tree"""
    # print("HEI", node, nodes[node], prev)
    prev = prev + (node,)

    paths = []
    for other in nodes[node]:
        # print(node, other, prev, other in prev, other.lower() == other)
        if (other in prev) and (other.lower() == other):
            # print("!@#!@#")
            continue
        elif other == 'end':
            all_paths.append(prev + ('end',))
        else:
            get_paths(other, nodes, prev=prev, all_paths=all_paths)
    return all_paths

for path in (all_paths := get_paths('start', nodes, prev=())):
    print(path)
print(len(all_paths))
