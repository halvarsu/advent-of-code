import sys, os, re


class Day13(object):

    """Solves day13 of adventofcode.com """

    def __init__(self, inp=1350, test =False):
        """

        :inp: input num
        :test: overwrites filename and loads file 'test' instead

        """
        if test:
            self._input = 10
        else:
            self._input = inp


    def solve(self, part=1, w= 90,  h=45):
        import numpy as np
        self.height = h
        self.width = w
        self.board = np.zeros((w,h))
        for x in range(w):
            for y in range(h):
                self.board[x,y] = self.is_wall(x,y)
        return self.board

    
    def game(self):
        board = self.solve(part=1)



    def is_wall(self, x,y):
        if x <0 or y <0 :
            return True
        num = x*x + 3*x + 2*x*y + y + y*y + self._input
        return reduce(lambda x,y: x + int(y), bin(num)[2:],0)%2

    def __str__(self):
        board = self.board
        shape = board.shape
        ws = " " * len(str(board.shape[1]))
        s = ws
        s+= "".join([str(x//10) if x//10 else ' ' for x in range(shape[0]) ])+'\n'
        s+= ws + "".join([str(x %10) for x in range(shape[0])])+'\n'

        for y in range(self.height):
            s+= str(y)+'_'  if not y//10 else str(y)
            for x in range(self.width):
                if x == 1 and y == 1:
                    s+="X"
                elif x == 31 and y == 39:
                    s+='O'
                else:
                    s+="#" if board[x,y] else " "
            s+="\n"
        return s
def get_args():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-t','--test',help='run testfile',
                        action ='store_true',default=False)
    parser.add_argument('-p','--part',help='select part',
                        default=1, type=int)
    parser.add_argument('-i','--input',help='select input num',
                        default=10, type=int)
    return parser.parse_args()

if __name__ == "__main__":
    args = get_args()

    day13 = Day13(inp=10, test = args.test)
    board = day13.solve(part = args.part)
    print day13

