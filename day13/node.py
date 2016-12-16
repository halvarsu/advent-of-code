def is_node(x, y, inp = 10):
    if x < 0 or y < 0:
        return False
    num = x*x + 3*x + 2*x*y + y + y*y + inp
    tot = 0
    while num: tot+=num%2; num //= 2
    return not tot%2

def is_node2(x,y, inp=10):
    if x <0 or y <0 :
        return False
    num = x*x + 3*x + 2*x*y + y + y*y + inp
    return reduce(lambda x,y: x + int(y), bin(num)[2:],1)%2

class Node(object):

    """Represents a point on the board of problem 13 in adventofcode"""

    def __init__(self, ID, value = float('Inf'), inp=10):
        """

        :ID: tuple of two ints, x and y
        :value: number of steps from the start
        :inp: the puzzle input, used in is_node.

        """
        self._ID = ID
        self._value = value
        self._inp = inp

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._ID == other._ID
        else:
            return False

    def __ne__(self,other):
        return not self.__eq__(other)

    def __hash__(self):
        """Override default hash"""
        return self._ID

    def __str__(self):
        return str(self._ID)

    def connect(self, to):
        self.links.append(to)

    def find_links(self):
        links = []
        x,y = self._ID
        neighbors = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
        for x2,y2 in neighbors:
            if is_node(x2,y2, inp = self._inp):
                links.append((x2,y2))
        return links

    def get_links(self):
        if not hasattr(self, 'links'):
            self.links = self.find_links()
        return self.links

    def get_ID(self):
        return self._ID

    def get_value(self):
        return self._value

    def set_value(self,value):
        self._value = value
