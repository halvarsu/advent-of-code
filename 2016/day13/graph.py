from node import Node
class Graph(object):

    """Uses the Node class to traverse the maze from problem 13 of Advent
    Of Code"""

    def __init__(self, inp, target, part):
        """ 
        :inp: the puzzle input, used in node.is_node to find node spaces
        :target: the target node position
        :part: part 1 or 2 of the puzzle
        """
        
        self._input = inp
        self._target = target
        self._part = part
        self.nodes = [Node((1,1), value=0, inp = self._input)]
        self.target_node = Node(self._target, inp = self._input)


    def __str__(self):
        for node in self.nodes:
            print node
        return ''

    def build(self):
        try:
            self.dejkstras(self.nodes)
        except ValueError:
            pass
        if self._part == 1:
            return self.target_node.get_value()
        elif self._part == 2:
            return len(self.nodes)

    def dejkstras(self,prev_nodes):
        '''Recursively searches through nodes to find neighboring nodes'''
        self.next_nodes = []

        for node in prev_nodes:
            links = node.get_links()
            current_val = node.get_value() +1
            if self._part == 2:
                if current_val > 50:
                    break
            self.neighbors = [Node(ID, value= current_val, 
                                inp=self._input
                             ) for ID in links]
            self.next_nodes += [n for n in self.neighbors if n not in self.next_nodes]

        for i in range(len(self.next_nodes)-1,-1,-1):
            new = self.next_nodes[i]
            current_val = new.get_value() +1

            if self._part == 1:
                if new == self.target_node:
                    # Breaks out of all the recursiveness when target 
                    # is found
                    self.target_node.set_value(current_val)
                    raise ValueError
            if new not in self.nodes:
                self.nodes.append(new)
            else:
                old = self.nodes.index(new)
                old_val = self.nodes[old].get_value()
                if current_val < old_val:
                    self.nodes[old].set_value(current_val)
                self.next_nodes.pop(self.next_nodes.index(new))

        if self.next_nodes:
            self.dejkstras(self.next_nodes) 
        return 




    def print_labyrinth(self):
        from day13 import Day13
        import numpy as np

        IDs = [node.get_ID() for node in self.nodes]
        x_vals = [ID[0] for ID in IDs]
        y_vals = [ID[1] for ID in IDs]
        max_x = max(x_vals) +2
        max_y = max(y_vals) +2
        d13 = Day13(inp = self._input)
    
        board = d13.solve(w = max_x , h = max_y)
        shape = board.shape
        sc =  len(str(board.shape[1]))
        s = " "*sc
        s+= "".join([str(x//10) if x//10 else ' ' for x in range(shape[0]) ])+'\n'
        s+= sc*" " + "".join([str(x %10) for x in range(shape[0])])+'\n'

        for y in range(max_y):
            s+= str(y)+'_'*(sc-1) if not y//10 else str(y)
            for x in range(max_x):
                if x == 1 and y == 1:
                    s+="X"
                elif (x,y) == self._target:
                    s+='O'
                elif (x,y) in IDs:
                    s+= '.'
                else:
                    s+="#" if board[x,y] else " "
            s+="\n"
        return s[:-1]
def get_args():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-t','--test',help='run testvalue',
                        action ='store_true',default=False)
    parser.add_argument('-p','--part',help='select part',
                        choices=[1,2],type=int,default=1)
    return parser.parse_args()

if __name__ == "__main__":
    args = get_args()
    if args.test:
        g = Graph(inp=10, target = (7,4), part = args.part)
    else:
        g = Graph(inp=1350, target = (31,39), part = args.part)
    num = g.build()
    s1 = g.print_labyrinth()
    print s1
    print num
