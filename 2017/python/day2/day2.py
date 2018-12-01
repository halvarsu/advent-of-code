import sys
from os import path
import os
sys.path.append( path.dirname( path.dirname( path.abspath(__file__)  )  )  )
from AdventOfCode import AdventOfCode, partition, representsint, sign
import re
import numpy as np

class Day2(AdventOfCode):

    """Solves day 2 from adventOfCode.com. """

    def __init__(self, filename='input', test_file = False):
        """

        :filename: name of the input-file
        :test: overwrites filename and loads file 'test' instead

        """
        if test_file:
            self._filename = 'test'
        else:
            self._filename = filename
        AdventOfCode.__init__(self, filename = self._filename, day=2)
        self.registries = {}

    def input_prosessor(self, infile):
        return [self.line_prosessor(line) for line in infile]

    def line_prosessor(self, line):
        return [float(val) for val in line.split()]

    def solve(self,part = 0):
        data = np.array(self.get_input())
        if part == 0:
            print("Part 1 answer: {}".format(self.part1(data)))
            print("Part 2 answer: {}".format(self.part2(data)))
        elif part == 1:
            print("Part 1 answer: {}".format(self.part1(data)))
        elif part == 2:
            print("Part 2 answer: {}".format(self.part2(data)))


    def part1(self, data):
        return int(np.sum((np.max(data,axis=1)-np.min(data,axis=1))))

    def part2(self, data):
        s = 0
        for i in range(1,data.shape[0]):
            rolled = np.roll(data,i,axis=1)
            indices = np.where(~np.array( data % rolled ,dtype=bool))
            # could probably remove this for loop
            for index in np.array(indices).T:
                s+= data[index[0], index[1]] / rolled[index[0], index[1]]
        return int(s)

        
        



if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-t','--test',help='run testfile',
            action ='store_true',default=False)
    parser.add_argument('-p','--part',help='select part. 0 runs all',
            choices =[0,1,2],default=0, type=int)
    args = parser.parse_args()

    day2 = Day2(test_file = args.test)
    day2.solve(part = args.part)

