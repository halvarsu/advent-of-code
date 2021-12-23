import numpy as np
from collections import defaultdict

# filename = "test_input3"
def get_data(filename):
    with open(filename) as infile:
        nodes = defaultdict(list)
        for line in infile.readlines():
            a, b = line.strip().split("-")
            nodes[a].append(b)
            nodes[b].append(a)
    return nodes


def get_paths(node, nodes, prev = (), all_paths=[], has_double=False):
    """Recursively explores a node-tree"""
    # print("HEI", node, nodes[node], prev)
    prev = prev + (node,)

    paths = []
    for other in nodes[node]:
        # print(node, other, prev, other in prev, other.lower() == other)
        if other == 'end':
            all_paths.append(prev + ('end',))
        elif (other in prev) and (other.lower() == other):
            if has_double or other == "start":
                continue
            else:
                get_paths(other, nodes, prev=prev, all_paths=all_paths,
                    has_double=True)
        else:
            get_paths(other, nodes, prev=prev, all_paths=all_paths,
                    has_double=has_double)
    return all_paths

def run(filename = "test_input1"):
    nodes = get_data(filename)
    for path in (all_paths := get_paths('start', nodes, prev=())):
        print(path)
    print(len(all_paths))
    return all_paths


if __name__ == "__main__":
    run(filename = "input")
